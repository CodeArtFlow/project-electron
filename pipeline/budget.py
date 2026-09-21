"""The reader's spending limit: a monthly cap, enforced before every call, that fails closed.

The policy (cap, model, prices) is the committed file reference/reader_budget.yaml. The record of
what has been spent is corpus/candidates/_reader_spend.json, committed with every run so that it
survives between runs.

What makes this a cap and not a report:

  * CHECK BEFORE SPENDING. Before each call the worst case (all the input, plus the whole
    max_output_tokens, which for Gemini covers thinking and answer together) must fit in what is
    left today. If it does not, BudgetExhausted is raised and the call is never made.
  * PACED. A day may spend an even share of what is left of the month (left / days remaining), so
    the month cannot be burned on its first day and a single bad run is bounded to about a
    thirtieth of the cap.
  * PRICED OR REFUSED. A model that is not in the price table cannot be budgeted, so it cannot be
    used. Prices are dated: they step up on 2027-01-01 and the ledger must not under-count then.
  * UNKNOWN MEANS BILLED. A call whose outcome is not known (timeout: the server may have finished
    and billed us) is charged at its worst case, never at zero.
  * FAILS CLOSED. A policy or ledger that cannot be read is an error, never a fresh start. A run
    that cannot tell what it has spent does not spend.

It is a second line of defence: it is only as right as our copy of the prices. The cap that cannot
be wrong is Google's own (AI Studio > Spend > Monthly spend cap). See AGENTS.md, "Reader budget".

Usage:  python pipeline/budget.py           # policy, spend so far this month, what today may spend
        python pipeline/budget.py --check   # validate the policy file; exit 1 if it is malformed
"""

import calendar
import json
import math
import os
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
POLICY_PATH = ROOT / "reference" / "reader_budget.yaml"
LEDGER_PATH = ROOT / "corpus" / "candidates" / "_reader_spend.json"
STALE_PRICES_DAYS = 180


class BudgetError(Exception):
    """The policy or the ledger is unusable. The reader must not spend."""


class BudgetExhausted(Exception):
    """The next call might spend more than is left. Not an error: the run simply stops."""


def today_utc():
    return datetime.now(timezone.utc).date().isoformat()


def _d(value, what):
    """A YAML date (PyYAML parses 2027-01-01 to a date) or an ISO string -> date."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError as e:
        raise BudgetError(f"{what}: {value!r} is not an ISO date") from e


def _up(usd):
    """Round a cost UP to a millionth of a dollar. The ledger may over-count; it must never under-count."""
    return math.ceil(usd * 1e6 - 1e-9) / 1e6


def _num(value, what):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise BudgetError(f"{what} must be a positive number, got {value!r}")
    return float(value)


def load_policy(path=POLICY_PATH):
    """Read and validate the committed policy. Raises BudgetError; never returns a partial policy."""
    try:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        raise BudgetError(f"cannot read the reader budget policy {path}: {e}") from e
    if not isinstance(raw, dict):
        raise BudgetError("the reader budget policy is not a mapping")
    cap = _num(raw.get("monthly_cap_usd"), "monthly_cap_usd")
    model = raw.get("model")
    prices = (raw.get("prices") or {})
    schedules = {}
    for name, entries in (prices.get("models") or {}).items():
        if not isinstance(entries, list) or not entries:
            raise BudgetError(f"prices for {name} must be a non-empty list")
        parsed = sorted(({"from": _d(e.get("from"), f"{name}.from"),
                          "input": _num(e.get("input"), f"{name}.input"),
                          "output": _num(e.get("output"), f"{name}.output")} for e in entries),
                        key=lambda e: e["from"])
        if len({e["from"] for e in parsed}) != len(parsed):
            raise BudgetError(f"prices for {name} have two entries with the same date")
        schedules[name] = parsed
    if not schedules:
        raise BudgetError("the policy prices no model, so nothing can be budgeted")
    if model not in schedules:
        raise BudgetError(f"the default model {model!r} has no price in the policy")
    generation = _generation(raw.get("generation"), schedules)
    return {"monthly_cap_usd": cap, "model": model, "schedules": schedules, "generation": generation,
            "prices_retrieved": _d(prices.get("retrieved"), "prices.retrieved"),
            "prices_source": prices.get("source")}


GENERATION_KEYS = {"thinking_budget", "thinking_level", "temperature"}
THINKING_LEVELS = ("minimal", "low", "medium", "high")


def _generation(raw, schedules):
    """How each priced model is called. A priced model with no entry is refused: never run unconfigured."""
    raw = raw or {}
    out = {}
    for name in schedules:
        g = raw.get(name)
        if not isinstance(g, dict) or not g:
            raise BudgetError(f"{name} is priced but has no generation settings")
        extra = set(g) - GENERATION_KEYS
        if extra:
            raise BudgetError(f"{name}: unknown generation setting(s) {sorted(extra)}")
        if "thinking_budget" in g and "thinking_level" in g:
            raise BudgetError(f"{name}: thinking_budget and thinking_level cannot both be set (the API rejects it)")
        if "thinking_budget" in g and (isinstance(g["thinking_budget"], bool) or not isinstance(g["thinking_budget"], int)
                                       or g["thinking_budget"] < 0):
            raise BudgetError(f"{name}.thinking_budget must be a whole number of tokens, 0 or more")
        if "thinking_level" in g and g["thinking_level"] not in THINKING_LEVELS:
            raise BudgetError(f"{name}.thinking_level must be one of {THINKING_LEVELS}")
        if "temperature" in g and (isinstance(g["temperature"], bool) or not isinstance(g["temperature"], (int, float))
                                   or not 0 <= g["temperature"] <= 2):
            raise BudgetError(f"{name}.temperature must be a number from 0 to 2")
        out[name] = dict(g)
    return out


def _empty_ledger():
    return {"schema_version": 1, "months": {}}


def load_ledger(path=LEDGER_PATH):
    """A missing ledger is a first run. One that exists but cannot be read is an error."""
    path = Path(path)
    if not path.exists():
        return _empty_ledger()
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
        months = doc["months"]
        assert doc.get("schema_version") == 1 and isinstance(months, dict)
        for key, m in months.items():
            date.fromisoformat(key + "-01")
            assert m["usd"] >= 0 and all(v >= 0 for v in m["days"].values())
    except (OSError, ValueError, KeyError, TypeError, AssertionError, AttributeError) as e:
        raise BudgetError(f"the spend ledger {path} is unreadable ({type(e).__name__}); refusing to "
                          f"spend without knowing what has been spent. Repair it from git history.") from e
    return doc


class Budget:
    def __init__(self, policy, ledger_path=LEDGER_PATH, today=None, cap_usd=None, persist=True):
        self.policy = policy
        self.path = Path(ledger_path)
        self.today = _d(today or today_utc(), "today")
        cap = policy["monthly_cap_usd"]
        if cap_usd is not None:
            # A run may ask for LESS than the committed cap. It can never ask for more.
            cap = min(cap, _num(cap_usd, "cap_usd"))
        self.cap = cap
        self.persist = persist
        self.ledger = load_ledger(self.path)
        self.run = {"usd": 0.0, "calls": 0, "input_tokens": 0, "output_tokens": 0, "unknown_calls": 0}

    @classmethod
    def load(cls, root=ROOT, today=None, cap_usd=None, persist=True):
        return cls(load_policy(Path(root) / "reference" / "reader_budget.yaml"),
                   Path(root) / "corpus" / "candidates" / "_reader_spend.json", today, cap_usd, persist)

    # ---- prices
    def price(self, model, on=None):
        """(input, output) USD per 1M tokens for this model on this date. Refuses an unpriced model."""
        schedule = self.policy["schedules"].get(model)
        if not schedule:
            raise BudgetError(f"model {model!r} has no price in reference/reader_budget.yaml, so it "
                              f"cannot be budgeted and will not be used. Priced: "
                              f"{sorted(self.policy['schedules'])}")
        on = on or self.today
        current = [e for e in schedule if e["from"] <= on]
        if not current:
            raise BudgetError(f"{model} has no price effective on {on}")
        e = current[-1]
        return e["input"], e["output"]

    def cost(self, model, input_tokens, output_tokens):
        p_in, p_out = self.price(model)
        return (input_tokens * p_in + output_tokens * p_out) / 1e6

    def price_age_days(self):
        return (self.today - self.policy["prices_retrieved"]).days

    # ---- what has been spent
    @property
    def _month(self):
        return self.today.strftime("%Y-%m")

    def _m(self):
        return self.ledger["months"].get(self._month) or {"usd": 0.0, "days": {}}

    def spent_month(self):
        return self._m()["usd"]

    def spent_today(self):
        return self._m()["days"].get(self.today.isoformat(), 0.0)

    def remaining_month(self):
        return max(0.0, self.cap - self.spent_month())

    def allowance_today(self):
        """What today may spend in total: an even share of what the month had left when it began."""
        days_left = calendar.monthrange(self.today.year, self.today.month)[1] - self.today.day + 1
        before_today = self.spent_month() - self.spent_today()
        return max(0.0, self.cap - before_today) / days_left

    def remaining_today(self):
        return max(0.0, min(self.allowance_today() - self.spent_today(), self.remaining_month()))

    # ---- the gate
    def worst_case(self, model, input_tokens, max_output_tokens):
        return self.cost(model, input_tokens, max_output_tokens)

    def check(self, model, input_tokens, max_output_tokens):
        """Raise BudgetExhausted unless the worst case of this call fits in what is left today."""
        worst = self.worst_case(model, input_tokens, max_output_tokens)
        left = self.remaining_today()
        if worst > left + 1e-12:
            raise BudgetExhausted(
                f"the next call could cost up to ${worst:.4f} but only ${left:.4f} is left for today "
                f"(${self.spent_month():.4f} of the ${self.cap:.2f} monthly cap is spent; today's "
                f"even share is ${self.allowance_today():.4f})")
        return worst

    # ---- recording
    def record(self, model, input_tokens, output_tokens, unknown=False):
        usd = _up(self.cost(model, input_tokens, output_tokens))
        m = self.ledger["months"].setdefault(self._month, {"usd": 0.0, "calls": 0, "input_tokens": 0,
                                                            "output_tokens": 0, "days": {}})
        day = self.today.isoformat()
        m["usd"] = round(m["usd"] + usd, 6)
        m["days"][day] = round(m["days"].get(day, 0.0) + usd, 6)
        m["calls"] += 1
        m["input_tokens"] += int(input_tokens)
        m["output_tokens"] += int(output_tokens)
        self.run["usd"] = round(self.run["usd"] + usd, 6)
        self.run["calls"] += 1
        self.run["input_tokens"] += int(input_tokens)
        self.run["output_tokens"] += int(output_tokens)
        self.run["unknown_calls"] += 1 if unknown else 0
        self._save()
        return usd

    def _save(self):
        if not self.persist:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # Written after EVERY call, atomically: a crash between two papers must not lose a payment.
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, prefix=".spend-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(self.ledger, f, indent=2, sort_keys=True)
                f.write("\n")
            os.replace(tmp, self.path)
        except BaseException:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise

    def summary(self):
        return {"monthly_cap_usd": self.cap, "spent_month_usd": round(self.spent_month(), 6),
                "spent_today_usd": round(self.spent_today(), 6),
                "allowance_today_usd": round(self.allowance_today(), 6),
                "remaining_today_usd": round(self.remaining_today(), 6),
                "run_usd": self.run["usd"], "run_calls": self.run["calls"],
                "run_unknown_calls": self.run["unknown_calls"],
                "price_table_retrieved": self.policy["prices_retrieved"].isoformat(),
                "price_table_age_days": self.price_age_days()}


def main(argv):
    try:
        b = Budget.load(persist=False)
        model = b.policy["model"]
        p_in, p_out = b.price(model)
    except BudgetError as e:
        print("BUDGET POLICY ERROR:", e)
        return 1
    if "--check" in argv:
        print(f"OK - reader budget policy is valid: ${b.cap:.2f}/month, model {model}")
        return 0
    s = b.summary()
    print(f"reader budget - {b.today.isoformat()} (UTC)")
    print(f"  model        {model}  (${p_in:.2f} in / ${p_out:.2f} out per 1M tokens today)")
    print(f"  monthly cap  ${b.cap:.2f}   spent this month ${s['spent_month_usd']:.4f}   "
          f"remaining ${b.remaining_month():.4f}")
    print(f"  today        may spend ${s['allowance_today_usd']:.4f} in total, "
          f"${s['spent_today_usd']:.4f} spent, ${s['remaining_today_usd']:.4f} left")
    print(f"  prices       retrieved {s['price_table_retrieved']} ({s['price_table_age_days']} days ago)"
          f" from {b.policy['prices_source']}")
    if s["price_table_age_days"] > STALE_PRICES_DAYS:
        print(f"  WARNING: the price table is over {STALE_PRICES_DAYS} days old; re-check it against the source.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
