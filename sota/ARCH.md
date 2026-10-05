# Architecture — state of the art

Topic code `ARCH`. Last reviewed 2026-10-05.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### area die

- **0.81 mm^2** — STELLA's core area is 0.81 mm2 fabricated in TSMC 16nm FinFET technology.
  - `CLM-ARCH-0050` · process TSMC 16nm FinFET technology, component core area · grade B · credibility unknown · measured · as of 2026-09-30
  - sources: SRC-00075
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

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
- **169.1 ×** — The projected IMAX configuration achieves a 169.1x smaller modeled end-to-end energy per batch compared to the RTX 4090 baseline.
  - `CLM-ARCH-0022` · platform projected IMAX configuration, metric_scope modeled end-to-end energy per batch · grade B · credibility unknown · projected · as of 2026-09-23
  - sources: SRC-00030
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### energy delay product

- **1.23e-26 J*s** — Low-threshold PFAL Buffer/NOT cell reaches a minimum energy-delay product of 1.23e-26 J*s in simulation.
  - `CLM-ARCH-0001` · process TSMC 16nm FinFET, cell low-threshold Buffer/NOT, vclk 0.6 V, fclk 7.94 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001

### frequency

- **25.9 GHz** — The optical PPLN module exhibits a measured nonlinear conversion bandwidth of 25.9 GHz.
  - `CLM-ARCH-0042` · platform optical PPLN module · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00062
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.0006 GHz** — The integrated phononic device provides a measured nonlinear conversion bandwidth of 0.6 MHz.
  - `CLM-ARCH-0043` · platform integrated phononic device · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00062
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

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
- **0.787 W** — The synthesized SRAM-PIM subsystem consumes 0.787 W of power.
  - `CLM-ARCH-0037` · component synthesized SRAM-PIM subsystem · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00044
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **9.599 W** — The added compute and buffer logic in HBM-PIM consumes 9.599 W of power.
  - `CLM-ARCH-0038` · component added compute and buffer logic in HBM-PIM · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00044
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
- The 15-term DPD correction form improves test-set NMSE by 26.1 dB.
  - `CLM-ARCH-0023` · test_type synthetic PA-model validation · grade B · credibility unknown · simulated · as of 2026-09-23
  - sources: SRC-00030
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The 15-term DPD correction form improves test-set ACLR by 26.0 dB.
  - `CLM-ARCH-0024` · test_type synthetic PA-model validation · grade B · credibility unknown · simulated · as of 2026-09-23
  - sources: SRC-00030
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- On 15 CPython server workloads, replacing a 16 KBITTAGE baseline with a 14 KBITTAGE augmented with a 1.3 KB lookahead engine reduces bytecode jump MPKI by 73.7%.
  - `CLM-ARCH-0025` · benchmark_suite 15 CPython server workloads, baseline_predictor 16 KBITTAGE, proposed_predictor 14 KBITTAGE augmented with the engine, engine_size 1.3 KB · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 6 quote(s) verified verbatim against the paper)
- On 15 CPython server workloads, replacing a 16 KBITTAGE baseline with a 14 KBITTAGE augmented with a 1.3 KB lookahead engine yields a 3.2% harmonic-mean IPC speedup.
  - `CLM-ARCH-0026` · benchmark_suite 15 CPython server workloads, baseline_predictor 16 KBITTAGE, proposed_predictor 14 KBITTAGE augmented with the engine, engine_size 1.3 KB · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 6 quote(s) verified verbatim against the paper)
- In gem5, scaling a 16 KB ITTAGE to 64 KB yields a harmonic-mean IPC improvement of 5.1% for the CPython workloads.
  - `CLM-ARCH-0027` · simulator gem5, baseline_predictor 3,392-entry 16 KB ITTAGE · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- In gem5, scaling a 16 KB ITTAGE to 64 KB yields an IPC improvement of up to 11.2% for the CPython workloads.
  - `CLM-ARCH-0028` · simulator gem5, baseline_predictor 3,392-entry 16 KB ITTAGE · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Under an iso-storage comparison, replacing 2 KB of a 16 KB ITTAGE baseline with the lookahead engine improves harmonic-mean IPC by up to 7.8%.
  - `CLM-ARCH-0029` · baseline_predictor 16 KB ITTAGE, replaced_capacity 2 KB · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The proposed lookahead engine reduces overall branch MPKI by 23.3% relative to the baseline.
  - `CLM-ARCH-0030` · proposed_predictor 14 KBITTAGE + 1.3 KB lookahead engine · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00040
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- PolyCIM delivers up to 4x improvement in macro utilization.
  - `CLM-ARCH-0031` · framework PolyCIM · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- PolyCIM achieves up to 3.2x speedup.
  - `CLM-ARCH-0032` · framework PolyCIM · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- PolyCIM achieves an average speedup of 2.1x across three evaluated DNN models.
  - `CLM-ARCH-0033` · framework PolyCIM, evaluated_models three complete DNN models with modern operators, including ConvNeXt-Tiny (CT), EfficientNet-B0 (EF), and MobileNetV2 (MN) · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- PolyCIM achieves an average speedup of 4.9x across evaluated convolution operators.
  - `CLM-ARCH-0034` · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- Without affine scheduling, latency degrades by 9.7x on the C1 operator.
  - `CLM-ARCH-0035` · operator C1, ablation_setting Without affine scheduling · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Disabling pre-tiling causes a 6.2x slowdown on the C1 operator.
  - `CLM-ARCH-0036` · operator C1, ablation_setting Disabling pre-tiling · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00042
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The optimized two-phase TP+EP expert mapping strategy achieves a 1.89x speedup over the EP baseline.
  - `CLM-ARCH-0039` · mapping_strategy optimized two-phase TP+EP mapping, baseline EP baseline · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00044
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Functional correctness was verified in Verilator against a Python golden model over 4,379 checked cycles.
  - `CLM-ARCH-0045` · reference_model Python golden model · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00067
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- At Nyquist input and 13GS/s sampling rate, the prototype ADC achieves 45.8-dB SNDR.
  - `CLM-ARCH-0051` · grade B · credibility unknown · measured · as of 2026-10-02
  - sources: SRC-00079
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- At Nyquist input and 13GS/s sampling rate, the prototype ADC achieves 56.1-dB SFDR.
  - `CLM-ARCH-0052` · grade B · credibility unknown · measured · as of 2026-10-02
  - sources: SRC-00079
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)

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
- **≈97.93 percent** — The directional coupler with a graded magnetic spacer transfers approximately 97.93% of the normalized output power to the adjacent waveguide.
  - `CLM-ARCH-0040` · frequency 7 GHz, component graded magnetic spacer · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00058
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **93.08 percent** — In the air-gap structure without a magnetic spacer, 93.08% of the normalized output power remains in the input waveguide.
  - `CLM-ARCH-0041` · frequency 7 GHz · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00058
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≈14.3 percent** — The 8-channel pulser peripheral instance corresponds to approximately 14.3% of the 104 kGE RISC-V SoC area.
  - `CLM-ARCH-0044` · process IHP 130 nm, channel_count 8 · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00067
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **26.3 percent** — Compared to the baseline, ZTA-Q increases LUT resource overhead by 26.3%.
  - `CLM-ARCH-0046` · design ZTA-Q, resource_type LUT · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00069
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **12.6 percent** — Compared to the baseline, ZTA-Q increases register resource overhead by 12.6%.
  - `CLM-ARCH-0047` · design ZTA-Q, resource_type register · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00069
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **150 percent** — Compared to the baseline, ZTA-Q increases DSP resource overhead by 150%.
  - `CLM-ARCH-0048` · design ZTA-Q, resource_type DSP · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00069
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **46 percent** — CONFERM's uniform iteration offsets shorten the emitted initiation interval by 46%.
  - `CLM-ARCH-0049` · mechanism uniform iteration offsets · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00070
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **27.3 percent** — Building PEEK with four Rocket cores upon a BOOM core introduces a 27.3% area overhead versus an unsafe baseline.
  - `CLM-ARCH-0053` · architecture PEEK with four Rockets upon a BOOM, baseline unsafe baseline · grade B · credibility unknown · simulated · as of 2026-10-02
  - sources: SRC-00080
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
  - `CLM-ARCH-0019` · concurrency_n_a 48, memory_tier HBF, component HBF tiering resume/access latency overhead · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **1.4e+07 ns** — At Na = 48, the proposed design achieves a time-between-tokens (TBT) of 14 ms per token.
  - `CLM-ARCH-0020` · concurrency_n_a 48, design our design with tiering, component end-to-end time-between-tokens (TBT) · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **2.7e+07 ns** — At Na = 128, the proposed design achieves a time-between-tokens (TBT) of 27 ms per token.
  - `CLM-ARCH-0021` · concurrency_n_a 128, design our design with tiering · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00025
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **≤ 4000 ns** — PEEK maintains a detection latency below 4us in most cases.
  - `CLM-ARCH-0054` · architecture PEEK · grade B · credibility unknown · simulated · as of 2026-10-02
  - sources: SRC-00080
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 54
- grades: {'B': 54}
- distinct sources: 19
