# EDA — state of the art

Topic code `EDA`. Last reviewed 2026-11-12.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### current

- **0.02 mA** — The short-channel BMR bias circuit provides a reference current of 20.0 µA at the typical-typical corner.
  - `CLM-EDA-0018` · circuit BMR, corner tt · grade B · credibility unknown · simulated · as of 2026-10-29
  - sources: SRC-00254
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

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
- The post-layout simulation of the SAR ADC placed using Ours achieves an SNDR of 34.3717 dB.
  - `CLM-EDA-0019` · method Ours, input_frequency 117.1875 kHz · grade B · credibility unknown · simulated · as of 2026-10-29
  - sources: SRC-00267
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The post-layout simulation of the SAR ADC placed using Ours yields an ENOB of 5.4172 bit.
  - `CLM-EDA-0020` · method Ours · grade B · credibility unknown · simulated · as of 2026-10-29
  - sources: SRC-00267
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- For the SAR ADC, Ours reduces placement area by 16.77% relative to MAGICAL.
  - `CLM-EDA-0021` · grade B · credibility unknown · simulated · as of 2026-10-29
  - sources: SRC-00267
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- For the flat LDO, Ours reduces maximum output deviation by 9.36% relative to MAGICAL.
  - `CLM-EDA-0022` · method Ours · grade B · credibility unknown · simulated · as of 2026-10-29
  - sources: SRC-00267
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- On 73 introductory examples from Vitis HLS, all 73 examples pass C simulation, synthesis, and co-simulation in Silinx HLS.
  - `CLM-EDA-0023` · benchmark_suite 73 Vitis HLS introductory examples · grade B · credibility unknown · measured · as of 2026-11-09
  - sources: SRC-00324
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- When optimizing for area, the open flow uses 15% fewer slices compared to ISE across 45 open-source designs.
  - `CLM-EDA-0024` · benchmark_set 45 open-source designs · grade B · credibility unknown · measured · as of 2026-11-09
  - sources: SRC-00324
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- When optimizing for area, the open flow achieves 14% shorter critical paths compared to ISE across 45 open-source designs.
  - `CLM-EDA-0025` · benchmark_set 45 open-source designs · grade B · credibility unknown · measured · as of 2026-11-09
  - sources: SRC-00324
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- When optimizing for speed, the open flow uses 21% fewer slices compared to ISE across 45 open-source designs.
  - `CLM-EDA-0026` · benchmark_set 45 open-source designs · grade B · credibility unknown · measured · as of 2026-11-09
  - sources: SRC-00324
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- When optimizing for speed, the open flow achieves 8% shorter critical paths compared to ISE across 45 open-source designs.
  - `CLM-EDA-0027` · benchmark_set 45 open-source designs · grade B · credibility unknown · measured · as of 2026-11-09
  - sources: SRC-00324
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- Dr. RTL achieves an average improvement of 21.3% in worst negative slack (WNS) across 20 designs.
  - `CLM-EDA-0028` · tool Dr. RTL, dataset_size 20 designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Dr. RTL achieves an average improvement of 16.9% in total negative slack (TNS) across 20 designs.
  - `CLM-EDA-0029` · tool Dr. RTL, dataset_size 20 designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Dr. RTL achieves an average area reduction of 5.8% across 20 designs.
  - `CLM-EDA-0030` · tool Dr. RTL, dataset_size 20 designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- E-Layout reports an average improvement of 6.07% in total negative slack (TNS) across nine designs.
  - `CLM-EDA-0031` · tool E-Layout · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- E-Layout reports an average improvement of 2.29% in worst negative slack (WNS) across nine designs.
  - `CLM-EDA-0032` · tool E-Layout · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- E-Layout achieves an average area reduction of 1.07% across nine designs.
  - `CLM-EDA-0033` · tool E-Layout · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- CircuitProver reduces average proof rounds from 9.2 to 4.6.
  - `CLM-EDA-0034` · tool CircuitProver · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00333
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

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
- **21.3 percent** — Dr. RTL achieves an average WNS improvement of 21.3% over commercial synthesis on 20 human-written RTL designs.
  - `CLM-EDA-0035` · framework Dr. RTL, design_count 20 human-written RTL designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0127, CFL-0128 — see the open register
- **16.9 percent** — Dr. RTL achieves an average TNS improvement of 16.9% over commercial synthesis across 20 human-written RTL designs.
  - `CLM-EDA-0036` · framework Dr. RTL, design_count 20 human-written RTL designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0127, CFL-0129 — see the open register
- **5.8 percent** — Dr. RTL achieves an average area reduction of 5.8% over commercial synthesis across 20 human-written RTL designs.
  - `CLM-EDA-0037` · framework Dr. RTL, design_count 20 human-written RTL designs · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0128, CFL-0129 — see the open register
- **7.4 percent** — Commercial synthesis tuning improves average WNS by 7.4% across eight designs.
  - `CLM-EDA-0038` · method commercial synthesis tuning · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0130 — see the open register
- **11.1 percent** — Commercial synthesis tuning improves average TNS by 11.1% across eight designs.
  - `CLM-EDA-0039` · method commercial synthesis tuning · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0130 — see the open register
- **18.7 percent** — Open-source algorithm discovery reduces area-delay product by 18.7% across eight designs.
  - `CLM-EDA-0040` · method open-source algorithm discovery · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **10.6 percent** — Algorithm discovery achieves an average reduction of 10.6% in area relative to agent-tuned Yosys+ABC.
  - `CLM-EDA-0041` · method algorithm discovery, baseline agent-tuned Yosys+ABC · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0131 — see the open register
- **9.1 percent** — Algorithm discovery achieves an average delay reduction of 9.1% relative to agent-tuned Yosys+ABC.
  - `CLM-EDA-0042` · method algorithm discovery, baseline agent-tuned Yosys+ABC · grade B · credibility unknown · simulated · as of 2026-11-10
  - sources: SRC-00334
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0131 — see the open register
- **88.1 percent** — On the AES benchmark, TAPCO-G reduced standard-cell leakage power by 88.1%, lowering leakage from 96.3 uW to 11.5 uW.
  - `CLM-EDA-0043` · design AES · grade B · credibility unknown · measured · as of 2026-11-10
  - sources: SRC-00339
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0133, CFL-0134 — see the open register
- **40 percent** — On the AES benchmark, TAPCO-G reduced total power by 40.0%, from 432.0 mW to 259.0 mW.
  - `CLM-EDA-0044` · design AES · grade B · credibility unknown · measured · as of 2026-11-10
  - sources: SRC-00339
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0133, CFL-0135 — see the open register
- **93.3 percent** — Across 45 physical probes on AES, TAPCO-G's full graph model achieved a sign accuracy of 93.3%.
  - `CLM-EDA-0045` · design AES · grade B · credibility unknown · measured · as of 2026-11-10
  - sources: SRC-00339
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0134, CFL-0135 — see the open register

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

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0127` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0035, CLM-EDA-0036
  - missing data: `not yet named`
- `CFL-0128` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0035, CLM-EDA-0037
  - missing data: `not yet named`
- `CFL-0129` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0036, CLM-EDA-0037
  - missing data: `not yet named`
- `CFL-0130` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0038, CLM-EDA-0039
  - missing data: `not yet named`
- `CFL-0131` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0041, CLM-EDA-0042
  - missing data: `not yet named`
- `CFL-0133` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0043, CLM-EDA-0044
  - missing data: `not yet named`
- `CFL-0134` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0043, CLM-EDA-0045
  - missing data: `not yet named`
- `CFL-0135` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-EDA-0044, CLM-EDA-0045
  - missing data: `not yet named`

## Evidence base

- claims: 45
- grades: {'B': 45}
- distinct sources: 12
