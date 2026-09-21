"""The reader's spending limit: prove the cap holds, and that it fails closed.

No network, no credentials. What is under test is arithmetic and refusal: the cap must refuse to
spend, not merely report having spent.

Usage:  python pipeline/test_budget.py
"""

import copy
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from budget import (Budget, BudgetError, BudgetExhausted, POLICY_PATH, load_ledger,  # noqa: E402
                    load_policy)

MODEL = "gemini-3.8-flash"


def policy(**over):
    p = {"monthly_cap_usd": 10.0, "model": MODEL, "prices_retrieved": date(2026, 9, 21),
         "prices_source": "test",
         "schedules": {MODEL: [{"from": date(2026, 1, 1), "input": 0.75, "output": 3.75},
                               {"from": date(2027, 1, 1), "input": 1.50, "output": 7.50}]}}
    p.update(over)
    return p


def budget(folder, today="2026-09-10", cap=None, **kw):
    return Budget(policy(), Path(folder) / "spend.json", today, cap_usd=cap, **kw)


class Prices(unittest.TestCase):
    def test_cost_is_tokens_times_price_per_million(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f)
            self.assertAlmostEqual(b.cost(MODEL, 1_000_000, 0), 0.75)
            self.assertAlmostEqual(b.cost(MODEL, 0, 1_000_000), 3.75)
            self.assertAlmostEqual(b.cost(MODEL, 20_000, 3_000), 0.015 + 0.01125)

    def test_the_price_steps_up_on_the_announced_date_and_not_before(self):
        with tempfile.TemporaryDirectory() as f:
            self.assertEqual(budget(f, "2026-12-31").price(MODEL), (0.75, 3.75))
            self.assertEqual(budget(f, "2027-01-01").price(MODEL), (1.50, 7.50))
            # Twice the price means the same run costs twice as much and is throttled accordingly.
            self.assertAlmostEqual(budget(f, "2027-01-02").cost(MODEL, 100_000, 5_000),
                                   2 * budget(f, "2026-12-30").cost(MODEL, 100_000, 5_000))

    def test_a_model_with_no_price_cannot_be_used(self):
        with tempfile.TemporaryDirectory() as f:
            with self.assertRaises(BudgetError) as ctx:
                budget(f).price("gemini-3.1-pro-preview")
            self.assertIn("cannot be budgeted", str(ctx.exception))

    def test_a_date_before_the_first_price_is_refused_not_guessed(self):
        with tempfile.TemporaryDirectory() as f:
            with self.assertRaises(BudgetError):
                budget(f, "2025-06-01").price(MODEL)


class TheCapRefuses(unittest.TestCase):
    def test_a_call_whose_worst_case_does_not_fit_is_refused_before_it_is_made(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-10", cap=0.50)            # 21 days left -> $0.0238 today
            self.assertAlmostEqual(b.allowance_today(), 0.50 / 21)
            with self.assertRaises(BudgetExhausted):
                b.check(MODEL, 48_000, 12_000)                # about $0.081 worst case
            self.assertEqual(b.spent_month(), 0.0)            # refusing costs nothing

    def test_a_call_that_fits_is_allowed_and_recording_uses_up_the_room(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-10")                       # $10 / 21 days = $0.476 today
            worst = b.check(MODEL, 48_000, 12_000)
            self.assertLess(worst, b.remaining_today())
            before = b.remaining_today()
            usd = b.record(MODEL, 48_000, 4_000)
            self.assertLessEqual(b.remaining_today(), before - usd + 1e-12)
            self.assertLess(before - usd - b.remaining_today(), 2e-6)
            self.assertGreaterEqual(b.spent_today(), usd - 1e-12)          # rounded UP, never down
            self.assertLess(b.spent_today() - usd, 2e-6)

    def test_the_cap_binds_however_many_small_calls_are_made(self):
        """The property that matters: keep calling until refused; the total never passes the cap."""
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-30", cap=1.00)             # last day: all of it is available
            calls = 0
            while True:
                try:
                    b.check(MODEL, 30_000, 8_000)
                except BudgetExhausted:
                    break
                b.record(MODEL, 30_000, 8_000)                # spend the worst case every time
                calls += 1
                self.assertLess(calls, 1000)
            self.assertLessEqual(b.spent_month(), 1.00 + 1e-9)
            self.assertGreater(calls, 0)

    def test_the_cli_can_lower_the_cap_but_never_raise_it(self):
        with tempfile.TemporaryDirectory() as f:
            self.assertEqual(budget(f, cap=0.25).cap, 0.25)
            self.assertEqual(budget(f, cap=1000.0).cap, 10.0)   # asking for more changes nothing
            with self.assertRaises(BudgetError):
                budget(f, cap=0)
            with self.assertRaises(BudgetError):
                budget(f, cap=-5)


class Pacing(unittest.TestCase):
    def test_a_day_gets_an_even_share_of_what_is_left(self):
        with tempfile.TemporaryDirectory() as f:
            self.assertAlmostEqual(budget(f, "2026-09-01").allowance_today(), 10 / 30)
            self.assertAlmostEqual(budget(f, "2026-09-30").allowance_today(), 10.0)
            self.assertAlmostEqual(budget(f, "2026-02-01").allowance_today(), 10 / 28)   # month length

    def test_unspent_days_roll_forward_and_a_heavy_day_leaves_less_for_the_rest(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-01")
            b.record(MODEL, 100_000, 5_000)                   # a light first day
            tomorrow = Budget(policy(), b.path, "2026-09-02")
            self.assertGreater(tomorrow.allowance_today(), 10 / 30)      # the saving carried over
            b2 = budget(f + "/x", "2026-09-01")
            b2.record(MODEL, 4_000_000, 400_000)              # a huge first day: $4.50
            nxt = Budget(policy(), b2.path, "2026-09-02")
            self.assertLess(nxt.allowance_today(), 10 / 30)

    def test_a_day_cannot_spend_more_than_its_share_even_if_the_month_has_room(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-01")
            with self.assertRaises(BudgetExhausted):
                b.check(MODEL, 400_000, 100_000)              # $0.675 worst case vs $0.333 share
            self.assertGreater(b.remaining_month(), 9.9)       # the month has plenty; the DAY does not

    def test_a_new_month_starts_a_new_allowance(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, "2026-09-30", cap=1.0)
            b.record(MODEL, 1_000_000, 100_000)               # spends $1.125 of a $1 month
            self.assertEqual(b.remaining_today(), 0.0)
            october = Budget(policy(), b.path, "2026-10-01", cap_usd=1.0)
            self.assertEqual(october.spent_month(), 0.0)
            self.assertGreater(october.remaining_today(), 0.0)
            self.assertIn("2026-09", october.ledger["months"])   # history is kept


class Recording(unittest.TestCase):
    def test_every_call_is_persisted_immediately(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f)
            b.record(MODEL, 10_000, 1_000)
            # A brand-new Budget, as the next run would be, sees it. No end-of-run step is needed.
            again = Budget(policy(), b.path, "2026-09-10")
            self.assertAlmostEqual(again.spent_month(), b.spent_month())
            self.assertEqual(json.loads(b.path.read_text())["months"]["2026-09"]["calls"], 1)

    def test_a_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f, persist=False)
            b.record(MODEL, 10_000, 1_000)
            self.assertFalse(b.path.exists())

    def test_unknown_outcomes_are_counted_and_charged(self):
        with tempfile.TemporaryDirectory() as f:
            b = budget(f)
            usd = b.record(MODEL, 48_000, 12_000, unknown=True)
            self.assertGreater(usd, 0.05)
            self.assertEqual(b.run["unknown_calls"], 1)
            self.assertEqual(b.summary()["run_unknown_calls"], 1)


class FailsClosed(unittest.TestCase):
    def test_a_corrupt_ledger_stops_the_reader_instead_of_restarting_at_zero(self):
        with tempfile.TemporaryDirectory() as f:
            path = Path(f) / "spend.json"
            for bad in ("{not json", "[]", '{"schema_version": 2, "months": {}}',
                        '{"schema_version": 1, "months": {"2026-09": {"usd": -1, "days": {}}}}',
                        '{"schema_version": 1, "months": {"nonsense": {"usd": 1, "days": {}}}}',
                        '{"schema_version": 1, "months": {"2026-09": {"days": {}}}}', ""):
                path.write_text(bad, encoding="utf-8")
                with self.assertRaises(BudgetError, msg=bad):
                    load_ledger(path)
                with self.assertRaises(BudgetError, msg=bad):
                    Budget(policy(), path, "2026-09-10")

    def test_a_missing_ledger_is_a_first_run_not_an_error(self):
        with tempfile.TemporaryDirectory() as f:
            self.assertEqual(load_ledger(Path(f) / "nope.json")["months"], {})

    def test_a_malformed_policy_stops_the_reader(self):
        real = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as f:
            path = Path(f) / "p.yaml"

            def write(doc):
                path.write_text(yaml.safe_dump(doc), encoding="utf-8")

            breakers = {
                "no cap": lambda d: d.pop("monthly_cap_usd"),
                "zero cap": lambda d: d.update(monthly_cap_usd=0),
                "text cap": lambda d: d.update(monthly_cap_usd="ten"),
                "no prices": lambda d: d.update(prices={"models": {}}),
                "unpriced default model": lambda d: d.update(model="gemini-not-priced"),
                "negative price": lambda d: d["prices"]["models"][real["model"]][0].update(input=-1),
                "bad date": lambda d: d["prices"]["models"][real["model"]][0].update(**{"from": "soon"}),
                "duplicate date": lambda d: d["prices"]["models"][real["model"]].append(
                    dict(d["prices"]["models"][real["model"]][0])),
                "empty schedule": lambda d: d["prices"]["models"].update({real["model"]: []}),
                "priced model with no generation settings": lambda d: d["generation"].pop(real["model"]),
                "unknown generation setting": lambda d: d["generation"][real["model"]].update(top_k=3),
                "thinking budget AND level": lambda d: d["generation"][real["model"]].update(
                    thinking_budget=0, thinking_level="low"),
                "negative thinking budget": lambda d: d["generation"][real["model"]].update(thinking_budget=-1),
                "bad thinking level": lambda d: d["generation"][real["model"]].update(thinking_level="extreme"),
                "temperature out of range": lambda d: d["generation"][real["model"]].update(temperature=5),
            }
            for name, breaker in breakers.items():
                doc = copy.deepcopy(real)
                breaker(doc)
                write(doc)
                with self.assertRaises(BudgetError, msg=name):
                    load_policy(path)
            path.write_text("not: [valid", encoding="utf-8")
            with self.assertRaises(BudgetError):
                load_policy(path)
            with self.assertRaises(BudgetError):
                load_policy(Path(f) / "missing.yaml")


class TheCommittedPolicy(unittest.TestCase):
    def test_the_real_policy_is_valid_and_is_what_the_user_decided(self):
        p = load_policy()
        # The user set $10 a month on 2026-09-21 and chose gemini-3.5-flash-lite the same day, after
        # the live API refused their first choice. Guard against either being changed by accident:
        # raising the cap or changing the model must be a deliberate edit of this test as well.
        self.assertEqual(p["monthly_cap_usd"], 10.0)
        self.assertEqual(p["model"], "gemini-3.5-flash-lite")

    def test_a_model_the_live_api_refused_is_not_a_candidate(self):
        # Google's docs listed gemini-2.5-flash as stable; the API said 404 "no longer available to
        # new users". A docs page is not evidence a model can be called, so it must not be priced.
        self.assertNotIn("gemini-2.5-flash", load_policy()["schedules"])

    def test_3_5_flash_lite_is_cheaper_and_has_no_announced_step_up_while_3_8_does(self):
        with tempfile.TemporaryDirectory() as f:
            now = Budget(load_policy(), Path(f) / "s.json", "2026-12-31")
            later = Budget(load_policy(), Path(f) / "s.json", "2027-06-01")
            self.assertEqual(now.price("gemini-3.5-flash-lite"), (0.30, 2.50))
            self.assertEqual(later.price("gemini-3.5-flash-lite"), (0.30, 2.50))    # unchanged in the new year
            self.assertEqual(later.price("gemini-3.8-flash"), (1.50, 7.50))         # doubled
            self.assertLess(now.cost("gemini-3.5-flash-lite", 20_000, 3_000), now.cost("gemini-3.8-flash", 20_000, 3_000))

    def test_the_real_generation_settings_buy_the_least_thinking_each_model_offers(self):
        g = load_policy()["generation"]
        self.assertEqual(g["gemini-3.5-flash-lite"], {"thinking_level": "minimal"})
        self.assertEqual(g["gemini-3.8-flash"], {"thinking_level": "low"})       # cannot go lower
        # Google: leave Gemini 3 temperature at its default of 1.0, so none is set.
        for settings in g.values():
            self.assertNotIn("temperature", settings)

    def test_the_real_price_table_carries_the_announced_2027_step_up(self):
        with tempfile.TemporaryDirectory() as f:
            b = Budget(load_policy(), Path(f) / "s.json", "2026-12-31")
            after = Budget(load_policy(), Path(f) / "s.json", "2027-01-01")
            self.assertEqual(b.price("gemini-3.8-flash"), (0.75, 3.75))
            self.assertEqual(after.price("gemini-3.8-flash"), (1.50, 7.50))

    def test_a_whole_maximum_size_paper_fits_in_one_days_share(self):
        # Otherwise the reader could never read a long paper at all. The WORST case of both calls
        # (a 120,000-character paper is over-estimated at 48,000 tokens), at the 2026 price.
        with tempfile.TemporaryDirectory() as f:
            b = Budget(load_policy(), Path(f) / "s.json", "2026-09-10")
            per_paper = b.worst_case("gemini-3.8-flash", 48_000, 12_000) + \
                b.worst_case("gemini-3.8-flash", 2_900, 2_048)
            self.assertLess(per_paper, b.allowance_today())


if __name__ == "__main__":
    unittest.main(verbosity=1)
