# EDA — state of the art

Topic code `EDA`. Last reviewed 2026-10-09.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### power

- **1.06e-07 W** — On the bandgap reference (BGR) circuit benchmark, AgenticSizing achieved a power consumption of 0.106 µW in one of its successful runs.
  - `CLM-EDA-0002` · benchmark_circuit BGR, framework AgenticSizing · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00027
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### relative deviation

- **≤ ≈60300 percent** — SLED-IFV achieves approximately 603x solver-only speedup on the otbn_sec_add benchmark compared to the baseline.
  - `CLM-EDA-0001` · benchmark otbn_sec_add, form F, baseline_time 1224 s · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00022
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **60 percent** — For the LDO benchmark, AgenticSizing achieved a 60% success rate with an average of 83 iterations.
  - `CLM-EDA-0003` · benchmark_circuit LDO benchmark, framework proposed method · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00027
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **60 percent** — For the full LDO benchmark, AgenticSizing achieved a success rate of 60% with an average of 89.7 simulation evaluations.
  - `CLM-EDA-0004` · circuit most complex circuit, framework proposed framework · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00027
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **86.4 percent** — The cyclic edge prediction model generated 86.4% valid circuits.
  - `CLM-EDA-0005` · model Cyclic Edge prediction model · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00045
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **89.6 percent** — The non-cyclic edge prediction model generated 89.6% valid circuits.
  - `CLM-EDA-0006` · model Non-cyclic Edge prediction model · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00045
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **76 percent** — The combined non-cyclic and node prediction model generated 76.0% valid circuits.
  - `CLM-EDA-0007` · model Non-cyclic + Node prediction model · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00045
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 7
- grades: {'B': 7}
- distinct sources: 3
