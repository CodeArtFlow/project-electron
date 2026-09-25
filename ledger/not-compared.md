# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**97 pair(s)** as of 2026-09-25.

## `energy_advantage_ratio` (5 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0016` = 1.22 x | `CLM-ARCH-0022` = 169.1 x | 99% | device=B200, benchmark=GroupGEMM | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0005` = 1.32 x | `CLM-ARCH-0022` = 169.1 x | 99% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0004` = 3.83 x | `CLM-ARCH-0022` = 169.1 x | 98% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0002` = 5 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0006` = 5.3 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |

## `frequency` (11 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0001` = 18.98 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=single ring cavity, parameter=FSR | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0003` = 15.41 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=photonic molecule, mode_spacing=Ω2 | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0002` = 3.57 GHz | `CLM-PHOT-0024` = 0.03 GHz | 99% | component=photonic molecule, mode_spacing=Ω1 | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0002` = 3.57 GHz | 99% | magnetic_field=8.1 T, frequency=1.9 THz | component=photonic molecule, mode_spacing=Ω1 |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0002` = 3.57 GHz | 98% | magnetic_field=7.5 T, frequency=2.2 THz | component=photonic molecule, mode_spacing=Ω1 |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0003` = 15.41 GHz | 96% | magnetic_field=8.1 T, frequency=1.9 THz | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0001` = 18.98 GHz | 95% | magnetic_field=8.1 T, frequency=1.9 THz | component=single ring cavity, parameter=FSR |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0003` = 15.41 GHz | 91% | magnetic_field=7.5 T, frequency=2.2 THz | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0001` = 18.98 GHz | 89% | magnetic_field=7.5 T, frequency=2.2 THz | component=single ring cavity, parameter=FSR |

## `length_device` (21 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0007` = 0.00023 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0008` = 0.00033 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0003` = 6.8e-05 um | 100% | parameter=signal-ground electrode spacing | defocus=30 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0004` = 7.7e-05 um | 100% | parameter=signal-ground electrode spacing | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0026` = 0.85 um | `CLM-PROC-0003` = 6.8e-05 um | 100% | component=MO-PhC slab | defocus=30 nm |
| `CLM-PHOT-0026` = 0.85 um | `CLM-PROC-0004` = 7.7e-05 um | 100% | component=MO-PhC slab | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0009` = 0.0017 um | 100% | parameter=signal-ground electrode spacing | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0010` = 0.0021 um | 100% | parameter=signal-ground electrode spacing | roughness_type=root mean square roughness (Sq), sample=after MoSx film deposition |
| `CLM-PHOT-0007` = 0.00023 um | `CLM-PHOT-0026` = 0.85 um | 100% | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) | component=MO-PhC slab |
| `CLM-PHOT-0008` = 0.00033 um | `CLM-PHOT-0026` = 0.85 um | 100% | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) | component=MO-PhC slab |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PHOT-0026` = 0.85 um | 100% | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition | component=MO-PhC slab |
| `CLM-PHOT-0010` = 0.0021 um | `CLM-PHOT-0026` = 0.85 um | 100% | roughness_type=root mean square roughness (Sq), sample=after MoSx film deposition | component=MO-PhC slab |
| `CLM-PHOT-0010` = 0.0021 um | `CLM-PROC-0003` = 6.8e-05 um | 97% | roughness_type=root mean square roughness (Sq), sample=after MoSx film deposition | defocus=30 nm |
| `CLM-PHOT-0010` = 0.0021 um | `CLM-PROC-0004` = 7.7e-05 um | 96% | roughness_type=root mean square roughness (Sq), sample=after MoSx film deposition | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PROC-0003` = 6.8e-05 um | 96% | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition | defocus=30 nm |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PROC-0004` = 7.7e-05 um | 95% | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0026` = 0.85 um | 88% | parameter=signal-ground electrode spacing | component=MO-PhC slab |
| `CLM-PHOT-0008` = 0.00033 um | `CLM-PROC-0003` = 6.8e-05 um | 79% | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) | defocus=30 nm |
| `CLM-PHOT-0008` = 0.00033 um | `CLM-PROC-0004` = 7.7e-05 um | 77% | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0007` = 0.00023 um | `CLM-PROC-0003` = 6.8e-05 um | 70% | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) | defocus=30 nm |
| `CLM-PHOT-0007` = 0.00023 um | `CLM-PROC-0004` = 7.7e-05 um | 67% | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) | material=HEA-NP, defocus=0 nm |

## `power` (3 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0007` = 40.4 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |

## `relative_deviation` (16 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0003` = 2 percent | `CLM-ARCH-0018` = 98 percent | 98% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | concurrency_n_a=48, set_type=hot set |
| `CLM-ARCH-0003` = 2 percent | `CLM-PHOT-0006` = 88 percent | 98% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | dataset=MNIST, setup=experimental system |
| `CLM-ARCH-0003` = 2 percent | `CLM-PHOT-0005` = 85 percent | 98% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | dataset=Iris test set |
| `CLM-ARCH-0003` = 2 percent | `CLM-EDA-0003` = 60 percent | 97% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | benchmark_circuit=LDO benchmark, framework=proposed method |
| `CLM-ARCH-0003` = 2 percent | `CLM-EDA-0004` = 60 percent | 97% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | circuit=most complex circuit, framework=proposed framework |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-ARCH-0018` = 98 percent | 85% | device=H200, baseline=CA Overlap, variant=AN Overlap | concurrency_n_a=48, set_type=hot set |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-PHOT-0006` = 88 percent | 84% | device=H200, baseline=CA Overlap, variant=AN Overlap | dataset=MNIST, setup=experimental system |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-PHOT-0005` = 85 percent | 83% | device=H200, baseline=CA Overlap, variant=AN Overlap | dataset=Iris test set |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-EDA-0003` = 60 percent | 76% | device=H200, baseline=CA Overlap, variant=AN Overlap | benchmark_circuit=LDO benchmark, framework=proposed method |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-EDA-0004` = 60 percent | 76% | device=H200, baseline=CA Overlap, variant=AN Overlap | circuit=most complex circuit, framework=proposed framework |
| `CLM-ARCH-0018` = 98 percent | `CLM-EDA-0003` = 60 percent | 39% | concurrency_n_a=48, set_type=hot set | benchmark_circuit=LDO benchmark, framework=proposed method |
| `CLM-ARCH-0018` = 98 percent | `CLM-EDA-0004` = 60 percent | 39% | concurrency_n_a=48, set_type=hot set | circuit=most complex circuit, framework=proposed framework |
| `CLM-EDA-0003` = 60 percent | `CLM-PHOT-0006` = 88 percent | 32% | benchmark_circuit=LDO benchmark, framework=proposed method | dataset=MNIST, setup=experimental system |
| `CLM-EDA-0004` = 60 percent | `CLM-PHOT-0006` = 88 percent | 32% | circuit=most complex circuit, framework=proposed framework | dataset=MNIST, setup=experimental system |
| `CLM-EDA-0003` = 60 percent | `CLM-PHOT-0005` = 85 percent | 29% | benchmark_circuit=LDO benchmark, framework=proposed method | dataset=Iris test set |
| `CLM-EDA-0004` = 60 percent | `CLM-PHOT-0005` = 85 percent | 29% | circuit=most complex circuit, framework=proposed framework | dataset=Iris test set |

## `thermal_conductivity` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |

## `time` (36 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Naive | illumination=random speckle illumination |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Merged | illumination=random speckle illumination |
| `CLM-ARCH-0013` = 162 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Merged | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Symmetry | illumination=random speckle illumination |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Symmetry | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=128, design=our design with tiering | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-MAT-0005` = 6.1 ps | `CLM-PHOT-0025` = 4e+09 ps | 100% | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV | illumination=random speckle illumination |
| `CLM-MAT-0005` = 6.1 ps | `CLM-PKG-0002` = 2.5e+11 ps | 100% | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-MAT-0005` = 6.1 ps | `CLM-PROC-0002` = 2.7e+08 ps | 100% | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Naive | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0013` = 162 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Merged | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Symmetry | hardware=NVIDIA Tesla T4 GPU |
| `CLM-PKG-0002` = 2.499e+08 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-PROC-0002` = 2.7e+05 ns | 99% | concurrency_n_a=128, design=our design with tiering | hardware=NVIDIA Tesla T4 GPU |
| `CLM-PHOT-0025` = 4e+06 ns | `CLM-PKG-0002` = 2.499e+08 ns | 98% | illumination=random speckle illumination | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-PROC-0002` = 2.7e+05 ns | 98% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PHOT-0025` = 4e+06 ns | 98% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | illumination=random speckle illumination |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-PKG-0002` = 2.499e+08 ns | 94% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-PHOT-0025` = 4e+06 ns | `CLM-PROC-0002` = 2.7e+05 ns | 93% | illumination=random speckle illumination | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-PKG-0002` = 2.499e+08 ns | 89% | concurrency_n_a=128, design=our design with tiering | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-PHOT-0025` = 4e+06 ns | 85% | concurrency_n_a=128, design=our design with tiering | illumination=random speckle illumination |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-PHOT-0025` = 4e+06 ns | 71% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | illumination=random speckle illumination |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PROC-0002` = 2.7e+05 ns | 69% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | hardware=NVIDIA Tesla T4 GPU |

## `wavelength` (4 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0028` = 0.0167 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | component=integrated microheater |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0028` = 0.0167 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | component=integrated microheater |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0028` = 0.0167 um | 99% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | component=integrated microheater |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0028` = 0.0167 um | 99% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | component=integrated microheater |
