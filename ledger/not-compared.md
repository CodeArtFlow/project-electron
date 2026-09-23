# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**56 pair(s)** as of 2026-09-23.

## `frequency` (3 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0001` = 18.98 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=single ring cavity, parameter=FSR | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0003` = 15.41 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=photonic molecule, mode_spacing=Ω2 | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0002` = 3.57 GHz | `CLM-PHOT-0024` = 0.03 GHz | 99% | component=photonic molecule, mode_spacing=Ω1 | angle_of_incidence=0° to 30°, rotation_angle=90° |

## `length_device` (14 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0007` = 0.00023 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0008` = 0.00033 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0003` = 6.8e-05 um | 100% | parameter=signal-ground electrode spacing | defocus=30 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0004` = 7.7e-05 um | 100% | parameter=signal-ground electrode spacing | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0009` = 0.0017 um | 100% | parameter=signal-ground electrode spacing | roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0010` = 0.0021 um | 100% | parameter=signal-ground electrode spacing | roughness_type=root mean square roughness (Sq) |
| `CLM-PHOT-0010` = 0.0021 um | `CLM-PROC-0003` = 6.8e-05 um | 97% | roughness_type=root mean square roughness (Sq) | defocus=30 nm |
| `CLM-PHOT-0010` = 0.0021 um | `CLM-PROC-0004` = 7.7e-05 um | 96% | roughness_type=root mean square roughness (Sq) | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PROC-0003` = 6.8e-05 um | 96% | roughness_type=arithmetic average roughness (Sa) | defocus=30 nm |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PROC-0004` = 7.7e-05 um | 95% | roughness_type=arithmetic average roughness (Sa) | material=HEA-NP, defocus=0 nm |
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

## `time` (19 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, design=our design with tiering |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, design=our design with tiering |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, memory_tier=HBF | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, design=our design with tiering | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=128, design=our design with tiering | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-MAT-0005` = 6.1 ps | `CLM-PROC-0002` = 2.7e+08 ps | 100% | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Naive | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0013` = 162 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Merged | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PROC-0002` = 2.7e+05 ns | 100% | device_type=FTJ, architecture=Symmetry | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, memory_tier=HBF |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, memory_tier=HBF |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0019` = 8.4e+04 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, memory_tier=HBF |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-PROC-0002` = 2.7e+05 ns | 99% | concurrency_n_a=128, design=our design with tiering | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-PROC-0002` = 2.7e+05 ns | 98% | concurrency_n_a=48, design=our design with tiering | hardware=NVIDIA Tesla T4 GPU |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PROC-0002` = 2.7e+05 ns | 69% | concurrency_n_a=48, memory_tier=HBF | hardware=NVIDIA Tesla T4 GPU |
