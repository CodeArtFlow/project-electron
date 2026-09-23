# Architecture — state of the art

Topic code `ARCH`. Last reviewed 2026-09-23.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy advantage ratio

- **≤ ≈5 ×** — Across the functional region of its simulated PFAL gate library, PFAL shows an energy advantage over static CMOS of up to approximately 5x at the most favorable operating point.
  - `CLM-ARCH-0002` · process TSMC 16nm FinFET, comparison PFAL vs static CMOS, operating_point most favorable operating point, vclk 1 V, fclk 100 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001
- **≤ 3.83 ×** — Optimized single-gate PFAL cells achieve up to 3.83x lower energy than equivalent static CMOS gates in simulation.
  - `CLM-ARCH-0004` · process TSMC 16nm FinFET, comparison single-gate PFAL vs static CMOS, power_clock trapezoidal, operating_point minimum-energy points of the parameter sweep (Table 2) · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **≤ 1.32 ×** — Sinusoidal power-clock excitation improves PFAL gate energy by up to 1.32x over trapezoidal excitation in simulation.
  - `CLM-ARCH-0005` · process TSMC 16nm FinFET, comparison sinusoidal vs trapezoidal power-clock, gate_at_maximum XOR/XNOR, vclk_at_maximum 0.5 V, fclk_at_maximum 384 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **≤ 5.3 ×** — A 4-bit Brent-Kung carry look-ahead adder in PFAL reaches up to 5.3x energy gain over a static CMOS estimate in simulation.
  - `CLM-ARCH-0006` · process TSMC 16nm FinFET, comparison 4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock triangular · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **≤ 1.22 ×** — GroupGEMM on B200 achieves up to 1.22x speedup with NUMA-aware execution.
  - `CLM-ARCH-0016` · device B200, benchmark GroupGEMM · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00016
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### energy delay product

- **1.23e-26 J*s** — Low-threshold PFAL Buffer/NOT cell reaches a minimum energy-delay product of 1.23e-26 J*s in simulation.
  - `CLM-ARCH-0001` · process TSMC 16nm FinFET, cell low-threshold Buffer/NOT, vclk 0.6 V, fclk 7.94 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001

### power

- **0.0404 W** — The 1024-MAC Systolic Array component in the MiX-INT4g16 accelerator consumes 40.4 mW of power in 28nm at 500 MHz.
  - `CLM-ARCH-0007` · component 1024-MAC Systolic Array, architecture MiX-INT4g16, array_size 1024-MAC, process 28nm, frequency 500 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00005
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.0318 W** — The 512-MAC systolic array for MiX-INT4g16 consumes 31.8 mW of power in 28nm at 500 MHz.
  - `CLM-ARCH-0008` · architecture MiX-INT4g16, array_size 512-MAC, process 28nm, frequency 500 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00005
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.0268 W** — The 512-MAC systolic array for MiX-INT4 consumes 26.8 mW of power in 28nm at 500 MHz.
  - `CLM-ARCH-0009` · architecture MiX-INT4, array_size 512-MAC, process 28nm, frequency 500 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00005
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### qualitative

- The proposed mapping scheme reduces energy consumption per computation by 53% compared to conventional mapping techniques.
  - `CLM-ARCH-0010` · device_type RRAM, architecture_baseline Naive architecture · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00011
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The Symmetry architecture reduces energy consumption by 29% compared with the Merged architecture for the FTJ device.
  - `CLM-ARCH-0011` · device_type FTJ, architecture_baseline Merged architecture · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00011
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The proposed solution runs 1.17 to 3.1x faster end-to-end than the state-of-the-art solution.
  - `CLM-ARCH-0017` · comparison_baseline state-of-the-art solution · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00021
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### relative deviation

- **≤ 2 percent** — With a quadrature-VCO power-clock, PFAL Buffer/NOT energy stays within 2% of the ideal sinusoidal power-clock case at 3 GHz.
  - `CLM-ARCH-0003` · process TSMC 16nm FinFET, comparison quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell Buffer/NOT, fclk 3 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001
- **≤ 14.3 percent** — Adaptive-NUMA Overlap improves decode throughput over Cluster-Aware Overlap by up to 14.3% on H200.
  - `CLM-ARCH-0015` · device H200, baseline CA Overlap, variant AN Overlap · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00016
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **≈98 percent** — At Na = 48, the hot set draws 98% of read traffic while occupying 3% of resident capacity.
  - `CLM-ARCH-0018` · concurrency_n_a 48, set_type hot set · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### time

- **153.53 ns** — The total latency for the FTJ device using the Naive architecture is 153.53 ns.
  - `CLM-ARCH-0012` · device_type FTJ, architecture Naive · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00011
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **161.99 ns** — The total latency for the FTJ device using the Merged architecture is 161.99 ns.
  - `CLM-ARCH-0013` · device_type FTJ, architecture Merged · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00011
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **153.53 ns** — The total latency for the FTJ device using the Symmetry architecture is 153.53 ns.
  - `CLM-ARCH-0014` · device_type FTJ, architecture Symmetry · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00011
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **84000 ns** — At Na = 48, the proposed hot-cold tiering design adds 0.084 ms of resume latency overhead.
  - `CLM-ARCH-0019` · concurrency_n_a 48, memory_tier HBF · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0014 — see the open register
- **1.4e+07 ns** — At Na = 48, the proposed design achieves a time-between-tokens (TBT) of 14 ms per token.
  - `CLM-ARCH-0020` · concurrency_n_a 48, design our design with tiering · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0014 — see the open register
- **2.7e+07 ns** — At Na = 128, the proposed design achieves a time-between-tokens (TBT) of 27 ms per token.
  - `CLM-ARCH-0021` · concurrency_n_a 128, design our design with tiering · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0014` — time: _unexamined; classification pending_
  - claims: CLM-ARCH-0019, CLM-ARCH-0020
  - missing data: `not yet named`

## Evidence base

- claims: 21
- grades: {'B': 21}
- distinct sources: 7
