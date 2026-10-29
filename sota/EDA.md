# EDA — state of the art

Topic code `EDA`. Last reviewed 2026-10-29.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### frequency

- **0.22 GHz** — The CPI-optimized configuration reaches a maximum operating frequency of 220 MHz.
  - `CLM-EDA-0014` · configuration CPI-optimized · grade B · credibility unknown · measured · as of 2026-10-27
  - sources: SRC-00240
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.25 GHz** — The area-optimized configuration achieves an operating frequency of 250 MHz.
  - `CLM-EDA-0015` · configuration area-optimized · grade B · credibility unknown · measured · as of 2026-10-27
  - sources: SRC-00240
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### power

- **1.06e-07 W** — On the bandgap reference (BGR) circuit benchmark, AgenticSizing achieved a power consumption of 0.106 µW in one of its successful runs.
  - `CLM-EDA-0002` · benchmark_circuit BGR, framework AgenticSizing · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00027
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### qualitative

- The base testbench for the Async FIFO design achieves a functional coverage of 91.7% by hitting 33 out of 36 bins.
  - `CLM-EDA-0008` · design Async FIFO · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00156
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The base testbench for the UART TX design achieves a functional coverage of 88.9% by hitting 16 out of 18 bins.
  - `CLM-EDA-0009` · design UART TX · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00156
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The base testbench for the AHB2APB design achieves a functional coverage of 67.4% by hitting 31 out of 46 bins.
  - `CLM-EDA-0010` · design AHB2APB · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00156
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The CPI-optimized configuration achieves 1.221 cycles per instruction on aggregate across eight benchmarks.
  - `CLM-EDA-0013` · configuration CPI-optimized · grade B · credibility unknown · measured · as of 2026-10-27
  - sources: SRC-00240
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The algorithmic HLS baseline achieves 4.000 cycles per instruction.
  - `CLM-EDA-0016` · configuration algorithmic HLS baseline · grade B · credibility unknown · measured · as of 2026-10-27
  - sources: SRC-00240
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The Ibex reference core achieves 1.575 cycles per instruction at 242 MHz on the aggregate benchmark suite.
  - `CLM-EDA-0017` · configuration Ibex reference, fclk 242 MHz · grade B · credibility unknown · measured · as of 2026-10-27
  - sources: SRC-00240
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

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

### time

- **1.35e+08 ns** — The JasperGold runtime was measured at 135 ms for the cache coherence module.
  - `CLM-EDA-0011` · tool JasperGold, module cache coherence module · grade B · credibility unknown · measured · as of 2026-10-23
  - sources: SRC-00235
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **1.273e+09 ns** — The JasperGold runtime was measured at 1273 ms for the L1 Bus Interface module.
  - `CLM-EDA-0012` · tool JasperGold, module L1 Bus Interface module · grade B · credibility unknown · measured · as of 2026-10-23
  - sources: SRC-00235
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 17
- grades: {'B': 17}
- distinct sources: 6
