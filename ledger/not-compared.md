# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**10001 pair(s)** as of 2026-10-27.

## `area_die` (11 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0110` = 0.0003 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | component=Address Translation Module, location=RCD, process=TSMC 90nm, frequency=2.4GHz | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0158` = 0.008701 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | component=PIM Chunk List, location=DRAM chip | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 98% | component=Row Migration Table, location=DRAM chip | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0111` = 0.151 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 98% | component=Rank Chunk List, location=RCD, process=TSMC 90nm, frequency=2.4GHz | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0158` = 0.008701 mm^2 | 94% | component=Row Migration Table, location=DRAM chip | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 |
| `CLM-ARCH-0050` = 0.81 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 90% | process=TSMC 16nm FinFET technology, component=core area | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0158` = 0.008701 mm^2 | 73% | component=PIM Chunk List, location=DRAM chip | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 |
| `CLM-ARCH-0146` = 3.43 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 57% | component=FIGFLEX, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0147` = 3.97 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 50% | component=AxCore, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0148` = 4.68 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 42% | component=FIGLUT, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |

## `current` (13 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0028` = 0.6 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | process_step=current ramp-down | temperature=10 mK |
| `CLM-DEV-0057` = 30 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=small switching current | temperature=10 mK |
| `CLM-DEV-0058` = 40 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=large switching current | temperature=10 mK |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0058` = 40 mA | 99% | temperature=2 K, state=after light irradiation | switching_regime=large switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0058` = 40 mA | 98% | process_step=current ramp-down | switching_regime=large switching current |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0057` = 30 mA | 98% | temperature=2 K, state=after light irradiation | switching_regime=small switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0057` = 30 mA | 98% | process_step=current ramp-down | switching_regime=small switching current |
| `CLM-DEV-0058` = 40 mA | `CLM-DEV-0075` = 1.5 mA | 96% | switching_regime=large switching current | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |
| `CLM-DEV-0057` = 30 mA | `CLM-DEV-0075` = 1.5 mA | 95% | switching_regime=small switching current | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |
| `CLM-DEV-0058` = 40 mA | `CLM-DEV-0077` = 4 mA | 90% | switching_regime=large switching current | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0057` = 30 mA | `CLM-DEV-0077` = 4 mA | 87% | switching_regime=small switching current | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0077` = 4 mA | 85% | process_step=current ramp-down | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0075` = 1.5 mA | 60% | process_step=current ramp-down | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |

## `energy` (264 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0172` = -5090 meV | 194% | defect_complex=VAl(ON)3, model=DFT | material=MLBP |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0172` = -5090 meV | 185% | defect_complex=VAl(ON)3 | material=MLBP |
| `CLM-MAT-0016` = 2020 meV | `CLM-MAT-0172` = -5090 meV | 140% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0015` = 1980 meV | `CLM-MAT-0172` = -5090 meV | 139% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0014` = 1940 meV | `CLM-MAT-0172` = -5090 meV | 138% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0051` = 1801 meV | `CLM-MAT-0172` = -5090 meV | 135% | axis=c | material=MLBP |
| `CLM-MAT-0013` = 1340 meV | `CLM-MAT-0172` = -5090 meV | 126% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0172` = -5090 meV | `CLM-MEM-0018` = 500 meV | 110% | material=MLBP | temperature=100 K, measurement_method=ARPES |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0201` = 370 meV | 107% | material=MLBP | band=2.3 eV emission, impurity_content=<0.1 ppm |
| `CLM-MAT-0104` = 220 meV | `CLM-MAT-0172` = -5090 meV | 104% | measurement=RIXS, absorption_edge=Fe L3 edge | material=MLBP |
| `CLM-MAT-0002` = 200 meV | `CLM-MAT-0172` = -5090 meV | 104% | mechanism=optical phonon | material=MLBP |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0200` = 200 meV | 104% | material=MLBP | band=2.3 eV emission, impurity_content=<0.1 ppm |
| `CLM-MAT-0172` = -5090 meV | `CLM-PROC-0031` = 91 meV | 102% | material=MLBP | error_metric=root-mean-square deviation per formula unit |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MAT-0172` = -5090 meV | 101% | mechanism=surface polar phonon, substrate=SiO2 | material=MLBP |
| `CLM-MAT-0113` = 15.9 meV | `CLM-MAT-0172` = -5090 meV | 100% | method=three-band nearest-neighbor exciton-geometric calculation | material=MLBP |
| `CLM-MAT-0115` = 2.22 meV | `CLM-MAT-0172` = -5090 meV | 100% | state=3p | material=MLBP |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0001` = 9.581e-06 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | mechanism=surface polar phonon, substrate=SiO2 |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0002` = 3.204e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | mechanism=optical phonon |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0013` = 0.0002147 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | synthesis_condition=Nitrogen-rich |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0014` = 0.0003108 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | synthesis_condition=Nitrogen-rich |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0015` = 0.0003172 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | synthesis_condition=Nitrogen-rich |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0016` = 0.0003236 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | synthesis_condition=Nitrogen-rich |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0048` = 2.964e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=LiFePO4 |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0049` = 4.742e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=LiFePO4 |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0050` = 1.634e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=Li6PS5Cl |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0051` = 0.0002886 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | axis=c |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0077` = 0.0006937 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | defect_complex=VAl(ON)3 |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0078` = 0.0007706 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | defect_complex=VAl(ON)3, model=DFT |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0085` = 8.54e-06 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=CrSiCN4, method=PBE+SOC |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0086` = 8.395e-06 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=CrGeCN4, method=PBE+SOC |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0104` = 3.525e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | measurement=RIXS, absorption_edge=Fe L3 edge |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0113` = 2.547e-06 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | method=three-band nearest-neighbor exciton-geometric calculation |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0114` = 2.083e-08 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=WSe2 |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0115` = 3.557e-07 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | state=3p |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0172` = -0.0008155 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | material=MLBP |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0200` = 3.204e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | band=2.3 eV emission, impurity_content=<0.1 ppm |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MAT-0201` = 5.928e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | band=2.3 eV emission, impurity_content=<0.1 ppm |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-MEM-0018` = 8.011e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | temperature=100 K, measurement_method=ARPES |
| `CLM-ARCH-0075` = 1.67e+12 fJ | `CLM-PROC-0031` = 1.458e-05 fJ | 100% | architecture=eight-output accelerator with shared activation delivery | error_metric=root-mean-square deviation per formula unit |
| `CLM-LITHO-0002` = 1e+12 fJ | `CLM-MAT-0001` = 9.581e-06 fJ | 100% | component=near-infrared laser pulse | mechanism=surface polar phonon, substrate=SiO2 |

_and 224 more_

## `energy_advantage_ratio` (7 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0016` = 1.22 x | `CLM-ARCH-0022` = 169.1 x | 99% | device=B200, benchmark=GroupGEMM | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0005` = 1.32 x | `CLM-ARCH-0022` = 169.1 x | 99% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0004` = 3.83 x | `CLM-ARCH-0022` = 169.1 x | 98% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0002` = 5 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0006` = 5.3 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0016` = 1.22 x | `CLM-MEM-0025` = 3.7 x | 67% | device=B200, benchmark=GroupGEMM | baseline=SoA mappings |
| `CLM-ARCH-0005` = 1.32 x | `CLM-MEM-0025` = 3.7 x | 64% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | baseline=SoA mappings |

## `frequency` (360 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | platform=optical PPLN module | wavelength=400 nm |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-PROC-0038` = 0.00061 GHz | 100% | platform=optical PPLN module | component=laser system |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-ARCH-0151` = 4.34e+04 GHz | 100% | platform=integrated phononic device | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-ARCH-0152` = 6.49e+04 GHz | 100% | platform=integrated phononic device | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-DEV-0012` = 370 GHz | 100% | platform=integrated phononic device | magnetic_field=8.1 T, frequency=1.9 THz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-DEV-0013` = 180 GHz | 100% | platform=integrated phononic device | magnetic_field=7.5 T, frequency=2.2 THz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-MAT-0150` = 5000 GHz | 100% | platform=integrated phononic device | material=monolayer MoTe2, phonon_mode=A1g |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0001` = 18.98 GHz | 100% | platform=integrated phononic device | component=single ring cavity, parameter=FSR |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0003` = 15.41 GHz | 100% | platform=integrated phononic device | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0036` = 121 GHz | 100% | platform=integrated phononic device | sample_size=22 measured devices |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0049` = 267 GHz | 100% | platform=integrated phononic device | signal_type=measured phase noise |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | platform=integrated phononic device | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0051` = 230 GHz | 100% | platform=integrated phononic device | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0052` = 320 GHz | 100% | platform=integrated phononic device | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PROC-0040` = 18 GHz | 100% | platform=integrated phononic device | material=1T-TaS2 flake, flake_thickness=70 nm, wavefront_type=fast wavefronts |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-ARCH-0151` = 4.34e+04 GHz | 100% | process_node=TSMC 28 nm | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-ARCH-0152` = 6.49e+04 GHz | 100% | process_node=TSMC 28 nm | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | process_node=TSMC 28 nm | wavelength=400 nm |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | process_node=TSMC 28 nm | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0073` = 0.5 GHz | `CLM-ARCH-0151` = 4.34e+04 GHz | 100% | process=45 nm | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0073` = 0.5 GHz | `CLM-ARCH-0152` = 6.49e+04 GHz | 100% | process=45 nm | component=FIGFLEX, activation_format=FP16 |
| `CLM-ARCH-0073` = 0.5 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | process=45 nm | wavelength=400 nm |
| `CLM-ARCH-0073` = 0.5 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | process=45 nm | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-MAT-0148` = 0.001756 GHz | 100% | component=FIGFLEX, activation_format=FP16 | transition=f-g |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | component=FIGFLEX, activation_format=FP16 | wavelength=400 nm |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=FIGFLEX, activation_format=FP16 | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | component=FIGFLEX, activation_format=FP16 | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-MAT-0148` = 0.001756 GHz | 100% | component=FIGFLEX, activation_format=FP16 | transition=f-g |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | component=FIGFLEX, activation_format=FP16 | wavelength=400 nm |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | component=FIGFLEX, activation_format=FP16 | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | component=FIGFLEX, activation_format=FP16 | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0012` = 370 GHz | `CLM-MAT-0148` = 0.001756 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | transition=f-g |
| `CLM-DEV-0012` = 370 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | wavelength=400 nm |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0012` = 370 GHz | `CLM-PROC-0038` = 0.00061 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | component=laser system |
| `CLM-DEV-0013` = 180 GHz | `CLM-MAT-0148` = 0.001756 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | transition=f-g |
| `CLM-DEV-0013` = 180 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | wavelength=400 nm |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0013` = 180 GHz | `CLM-PROC-0038` = 0.00061 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | component=laser system |
| `CLM-DEV-0072` = 7 GHz | `CLM-MAT-0153` = 1e-06 GHz | 100% | measurement_method=BLS spectra | wavelength=400 nm |

_and 320 more_

## `length_device` (3117 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0053` = 1.61 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | parameter=ts | material=GaN, growth_method=ammonothermal |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | parameter=ts | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | parameter=ts | chip_thickness=4-mm |
| `CLM-DEV-0068` = 100 nm | `CLM-MAT-0138` = 0.005 nm | 100% | material=PEDOT:PSS | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0068` = 100 nm | `CLM-MAT-0140` = 0.005 nm | 100% | material=PEDOT:PSS | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0135` = 0.013 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0136` = 0.006 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0137` = 0.011 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0138` = 0.005 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0139` = 0.007 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0140` = 0.005 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-PHOT-0057` = 0.024 nm | 100% | material=crystalline silicon membrane | measurement_duration=exceeding 15.5 hours |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0004` = 7000 nm | 100% | material=Sb monolayer on SiC(0001) | parameter=signal-ground electrode spacing |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=Sb monolayer on SiC(0001) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | material=Sb monolayer on SiC(0001) | chip_thickness=4-mm |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0097` = 2e+04 nm | 100% | material=Sb monolayer on SiC(0001) | spiral_arms=20 |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0004` = 7000 nm | 100% | material=Sb monolayer on SiC(0001) | parameter=signal-ground electrode spacing |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=Sb monolayer on SiC(0001) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | material=Sb monolayer on SiC(0001) | chip_thickness=4-mm |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0097` = 2e+04 nm | 100% | material=Sb monolayer on SiC(0001) | spiral_arms=20 |
| `CLM-MAT-0020` = 6.4 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | regime=partially-reconstructed | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0020` = 6.4 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | regime=partially-reconstructed | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0020` = 6.4 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | regime=partially-reconstructed | chip_thickness=4-mm |
| `CLM-MAT-0023` = 3.5 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | state=X2sA | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0023` = 3.5 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | state=X2sA | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0023` = 3.5 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | state=X2sA | chip_thickness=4-mm |
| `CLM-MAT-0024` = 6.4 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | state=X2sA | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0024` = 6.4 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | state=X2sA | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0024` = 6.4 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | state=X2sA | chip_thickness=4-mm |
| `CLM-MAT-0029` = 0.5291 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=bulk CeN | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0029` = 0.5291 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | material=bulk CeN | chip_thickness=4-mm |
| `CLM-MAT-0029` = 0.5291 nm | `CLM-PHOT-0097` = 2e+04 nm | 100% | material=bulk CeN | spiral_arms=20 |
| `CLM-MAT-0037` = 14.6 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | material=TiN, property=GL coherence length | chip_thickness=4-mm |
| `CLM-MAT-0040` = 0.5 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0040` = 0.5 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0040` = 0.5 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | chip_thickness=4-mm |
| `CLM-MAT-0040` = 0.5 nm | `CLM-PHOT-0097` = 2e+04 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | spiral_arms=20 |
| `CLM-MAT-0059` = 1000 nm | `CLM-MAT-0135` = 0.013 nm | 100% | region=pristine zone, temperature=1.5 K | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-MAT-0059` = 1000 nm | `CLM-MAT-0136` = 0.006 nm | 100% | region=pristine zone, temperature=1.5 K | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-MAT-0059` = 1000 nm | `CLM-MAT-0137` = 0.011 nm | 100% | region=pristine zone, temperature=1.5 K | superlattice_layer_n=3, superlattice_layer_m=5 |

_and 3077 more_

## `power` (204 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0007` = 40.4 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | device_type=drop-cast control devices |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | device_type=drop-cast control devices |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | device_type=drop-cast control devices |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0037` = 787 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=synthesized SRAM-PIM subsystem | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=synthesized SRAM-PIM subsystem | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=synthesized SRAM-PIM subsystem | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=synthesized SRAM-PIM subsystem | device_type=drop-cast control devices |
| `CLM-ARCH-0037` = 787 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | component=synthesized SRAM-PIM subsystem | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0038` = 9599 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=added compute and buffer logic in HBM-PIM | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0038` = 9599 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=added compute and buffer logic in HBM-PIM | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0038` = 9599 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=added compute and buffer logic in HBM-PIM | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0038` = 9599 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=added compute and buffer logic in HBM-PIM | device_type=drop-cast control devices |
| `CLM-ARCH-0038` = 9599 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | component=added compute and buffer logic in HBM-PIM | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | process_node=TSMC 28 nm | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | process_node=TSMC 28 nm | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | process_node=TSMC 28 nm | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | process_node=TSMC 28 nm | device_type=drop-cast control devices |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | process_node=TSMC 28 nm | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=PIM Chunk List, location=DRAM chip | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=PIM Chunk List, location=DRAM chip | device_type=drop-cast control devices |
| `CLM-ARCH-0149` = 4020 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0149` = 4020 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0149` = 4020 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0149` = 4020 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | device_type=drop-cast control devices |
| `CLM-ARCH-0149` = 4020 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0150` = 6670 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=FIGFLEX, benchmark=Llama-3.1-8B, activation_format=FP16, interface=HBM3E | benchmark_circuit=BGR, framework=AgenticSizing |

_and 164 more_

## `power_density` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0079` = 3.1e-05 W/mm^2 | `CLM-MAT-0026` = 4.8e-07 W/mm^2 | 98% | structure=long-base p+-n device, n_base_width=300 𝜇𝜇m, framework=extended theory | environment=ambient |

## `relative_deviation` (4683 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-EDA-0003` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | benchmark_circuit=LDO benchmark, framework=proposed method | sample=B1-1 |
| `CLM-EDA-0004` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | circuit=most complex circuit, framework=proposed framework | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0044` = 59.9 percent | 200% | sample=B1-1 | voltage=8 VAg/AgCl, material=1 μm n-type GaN |
| `CLM-ARCH-0089` = 64.2 percent | `CLM-MAT-0111` = -60 percent | 193% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0112` = 66.8 percent | 190% | sample=B1-1 | baseline=pure two-dimensional Coulomb reference, benchmark_protocol=high-field-calibrated |
| `CLM-ARCH-0090` = 67.5 percent | `CLM-MAT-0111` = -60 percent | 189% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-ARCH-0097` = 72 percent | `CLM-MAT-0111` = -60 percent | 183% | training_dataset=CloudLab, evaluation_dataset=Lambda | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0039` = 49.85 percent | 183% | sample=B1-1 | platform=Jetson Orin Nano, threshold=550, verification_stage=Single function verification |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0026` = 75.7 percent | 179% | sample=B1-1 | placement=conventional |
| `CLM-EDA-0007` = 76 percent | `CLM-MAT-0111` = -60 percent | 179% | model=Non-cyclic + Node prediction model | sample=B1-1 |
| `CLM-ARCH-0049` = 46 percent | `CLM-MAT-0111` = -60 percent | 177% | mechanism=uniform iteration offsets | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0186` = 46 percent | 177% | sample=B1-1 | indium_composition=13.5%, geometry=fixed pristine-GaN geometry |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0188` = 46 percent | 177% | sample=B1-1 | indium_composition=22%, baseline=pristine GaN |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0031` = 79.2 percent | 176% | sample=B1-1 | workload=six full-trace streams, hardware_configuration=six 3D DRAM organizations, method=TileDRAM |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0032` = 84.9 percent | 171% | sample=B1-1 | memory_technology=filamentary memristor |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0005` = 85 percent | 171% | sample=B1-1 | dataset=Iris test set |
| `CLM-EDA-0005` = 86.4 percent | `CLM-MAT-0111` = -60 percent | 169% | model=Cyclic Edge prediction model | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0021` = 87.5 percent | 169% | sample=B1-1 | device_technology=printed Ag/ZnO/Au ECM memristors |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0006` = 88 percent | 168% | sample=B1-1 | dataset=MNIST, setup=experimental system |
| `CLM-ARCH-0101` = 89.4 percent | `CLM-MAT-0111` = -60 percent | 167% | correction_type=uncorrected | sample=B1-1 |
| `CLM-EDA-0006` = 89.6 percent | `CLM-MAT-0111` = -60 percent | 167% | model=Non-cyclic Edge prediction model | sample=B1-1 |
| `CLM-ARCH-0099` = 91.8 percent | `CLM-MAT-0111` = -60 percent | 165% | training_method=CSI-based training | sample=B1-1 |
| `CLM-ARCH-0041` = 93.08 percent | `CLM-MAT-0111` = -60 percent | 164% | frequency=7 GHz | sample=B1-1 |
| `CLM-ARCH-0096` = 93.6 percent | `CLM-MAT-0111` = -60 percent | 164% | classifier=XGBoost, evaluation_method=five-fold cross-validation | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0059` = 94.4 percent | 164% | sample=B1-1 | route=Fourier route |
| `CLM-DEV-0069` = 38 percent | `CLM-MAT-0111` = -60 percent | 163% | wavelength=365 nm, batch=batch A, operating_voltage=0 V | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0012` = 95 percent | 163% | sample=B1-1 | encoding_scheme=differential encoding, benchmark=MNIST |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0023` = 95 percent | 163% | sample=B1-1 | device_technology=printed Ag/ZnO/Au ECM memristors |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0063` = 37 percent | 162% | sample=B1-1 | disorder_type=radius disorder |
| `CLM-ARCH-0077` = 36.86 percent | `CLM-MAT-0111` = -60 percent | 161% | framework=RAPID-DNN, fault_configuration=mixed random fault configuration, baseline=fault-agnostic baseline | sample=B1-1 |
| `CLM-ARCH-0040` = 97.93 percent | `CLM-MAT-0111` = -60 percent | 161% | frequency=7 GHz, component=graded magnetic spacer | sample=B1-1 |
| `CLM-ARCH-0018` = 98 percent | `CLM-MAT-0111` = -60 percent | 161% | concurrency_n_a=48, set_type=hot set | sample=B1-1 |
| `CLM-ARCH-0100` = 36.2 percent | `CLM-MAT-0111` = -60 percent | 160% | correction_type=uncorrected | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0038` = 99.69 percent | 160% | sample=B1-1 | platform=Jetson Orin Nano, threshold=550, verification_stage=Group verification |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0116` = 100 percent | 160% | sample=B1-1 | system=2D square-lattice tight-binding model |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0124` = 36 percent | 160% | sample=B1-1 | elastic_constant=C22, rotation_direction=from y to x |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0022` = 100 percent | 160% | sample=B1-1 | device_technology=printed Ag/ZnO/Au ECM memristors |
| `CLM-ARCH-0084` = 34 percent | `CLM-MAT-0111` = -60 percent | 157% | platform=Arrow, application=Sparse point cloud processing | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0198` = 34 percent | 157% | sample=B1-1 | method=DFT calculations, location=X valleys |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0064` = 31 percent | 152% | sample=B1-1 | disorder_type=radius disorder |

_and 4643 more_

## `temperature` (211 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0092` = -23.15 degC | 191% | temperature_control_system=VAHEAT system | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0004` = -73.15 degC | 189% | time_after_cooling_onset=10 s | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0053` = 230 degC | 189% | sample=NbN/I/FePt | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0053` = 230 degC | 189% | relaxation_temperature=TLIESST | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0004` = -73.15 degC | 186% | time_after_cooling_onset=10 s | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0091` = -113.1 degC | 175% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0091` = -113.1 degC | 172% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0003` = -123.1 degC | 169% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0003` = -123.1 degC | 166% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0101` = -155.1 degC | 155% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0003` = 150 K | `CLM-MAT-0102` = -81 K | 154% | calculation=acoustic phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0101` = -155.1 degC | 153% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0091` = 160 K | `CLM-MAT-0102` = -81 K | 151% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0033` = 84.85 degC | `CLM-DEV-0035` = -204.1 degC | 142% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-MAT-0004` = 200 K | `CLM-MAT-0102` = -81 K | 140% | calculation=optical phonon and surface polar phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-DEV-0035` = -204.1 degC | 140% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0093` = 76.85 degC | 138% | relaxation_temperature=TLIESST | magnetic_field=0.05 T |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0004` = -73.15 degC | 135% | temperature_control_system=VAHEAT system | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MEM-0019` = 768.9 degC | 134% | sample=NbN/I/FePt | model=realistic multi-orbital model of YCl, onsite_hubbard_parameter=0.9 eV |
| `CLM-DEV-0033` = 84.85 degC | `CLM-DEV-0076` = -257.6 degC | 133% | time_after_cooling_onset=10 s | sample=NbN/I/FePt |
| `CLM-MAT-0092` = 250 K | `CLM-MAT-0102` = -81 K | 132% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MEM-0020` = 801.9 degC | 132% | sample=NbN/I/FePt | method=Hartree-Fock approximation |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0142` = -264.1 degC | 132% | time_after_cooling_onset=10 s | measurement_setup=STM measurements |
| `CLM-DEV-0032` = 81.85 degC | `CLM-DEV-0076` = -257.6 degC | 132% | time_after_cooling_onset=10 s | sample=NbN/I/FePt |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0210` = -269.9 degC | 131% | time_after_cooling_onset=10 s | strain=+2%, method=anisotropic Migdal-Eliashberg equations |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0209` = -270.5 degC | 131% | time_after_cooling_onset=10 s | equation=Allen-Dynes modified McMillan equation |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0142` = -264.1 degC | 131% | time_after_cooling_onset=10 s | measurement_setup=STM measurements |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0210` = -269.9 degC | 130% | time_after_cooling_onset=10 s | strain=+2%, method=anisotropic Migdal-Eliashberg equations |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0209` = -270.5 degC | 130% | time_after_cooling_onset=10 s | equation=Allen-Dynes modified McMillan equation |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0093` = 76.85 degC | 130% | sample=NbN/I/FePt | magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0092` = -23.15 degC | 128% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0092` = -23.15 degC | 127% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-MAT-0102` = -81 K | `CLM-PROC-0001` = 300 K | 127% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | thermal_model=Debye model |
| `CLM-MAT-0102` = -81 K | `CLM-PHOT-0085` = 302.1 K | 127% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | external_pump_power=300 μW |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MEM-0019` = 768.9 degC | 127% | relaxation_temperature=TLIESST | model=realistic multi-orbital model of YCl, onsite_hubbard_parameter=0.9 eV |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MEM-0020` = 801.9 degC | 125% | relaxation_temperature=TLIESST | method=Hartree-Fock approximation |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0102` = -354.1 degC | 124% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-MAT-0093` = 350 K | `CLM-MAT-0102` = -81 K | 123% | magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0102` = -354.1 degC | 123% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0091` = -113.1 degC | 122% | temperature_control_system=VAHEAT system | pressure=ambient pressure, magnetic_field=0.05 T |

_and 171 more_

## `temperature_delta` (9 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0037` = 0.11 K | `CLM-PHOT-0086` = 275.2 K | 100% | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW | external_pump_power=300 μW |
| `CLM-PHOT-0037` = 0.11 K | `CLM-PHOT-0091` = 281.6 K | 100% | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0037` = 0.11 K | 100% | gate_bias_vgs=-2.7 V | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0091` = 281.6 K | 99% | time_after_cooling_onset=10 s | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0086` = 275.2 K | 99% | time_after_cooling_onset=10 s | external_pump_power=300 μW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0037` = 0.11 K | 96% | time_after_cooling_onset=10 s | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0034` = 3 K | 90% | gate_bias_vgs=-2.7 V | time_after_cooling_onset=10 s |
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0091` = 281.6 K | 89% | gate_bias_vgs=-2.7 V | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0086` = 275.2 K | 89% | gate_bias_vgs=-2.7 V | external_pump_power=300 μW |

## `thermal_conductivity` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |

## `time` (851 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0130` = 1.036e+07 ns | 100% | device_type=FTJ, architecture=Naive | device=NVIDIA GeForce RTX 5080, form=direct, decode=ALU |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0131` = 1.115e+07 ns | 100% | device_type=FTJ, architecture=Naive | device=NVIDIA GeForce RTX 5080, form=hoisted, decode=LUT |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0153` = 3.72e+09 ns | 100% | device_type=FTJ, architecture=Naive | component=FIGFLEX, benchmark=Llama-3.1-8B |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0066` = 6e+10 ns | 100% | device_type=FTJ, architecture=Naive | software=MATLAB Deep Learning Toolbox |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0011` = 1.35e+08 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=cache coherence module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0012` = 1.273e+09 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=L1 Bus Interface module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0119` = 0.00029 ns | 100% | device_type=FTJ, architecture=Naive | material=MAPbBr3, measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0120` = 0.0007 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0123` = 0.00015 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Multidimensional coherent spectroscopy |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0127` = 0.0003 ns | 100% | device_type=FTJ, architecture=Naive | feature=XA |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0170` = 0.002 ns | 100% | device_type=FTJ, architecture=Naive | state=bright exciton |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0197` = 0.000603 ns | 100% | device_type=FTJ, architecture=Naive | material=SnSe, excitation_helicity=σ+ |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Naive | illumination=random speckle illumination |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Naive | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0073` = 0.0004 ns | 100% | device_type=FTJ, architecture=Naive | material=ITO film |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Naive | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0130` = 1.036e+07 ns | 100% | device_type=FTJ, architecture=Merged | device=NVIDIA GeForce RTX 5080, form=direct, decode=ALU |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0131` = 1.115e+07 ns | 100% | device_type=FTJ, architecture=Merged | device=NVIDIA GeForce RTX 5080, form=hoisted, decode=LUT |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0153` = 3.72e+09 ns | 100% | device_type=FTJ, architecture=Merged | component=FIGFLEX, benchmark=Llama-3.1-8B |
| `CLM-ARCH-0013` = 162 ns | `CLM-DEV-0066` = 6e+10 ns | 100% | device_type=FTJ, architecture=Merged | software=MATLAB Deep Learning Toolbox |
| `CLM-ARCH-0013` = 162 ns | `CLM-EDA-0011` = 1.35e+08 ns | 100% | device_type=FTJ, architecture=Merged | tool=JasperGold, module=cache coherence module |
| `CLM-ARCH-0013` = 162 ns | `CLM-EDA-0012` = 1.273e+09 ns | 100% | device_type=FTJ, architecture=Merged | tool=JasperGold, module=L1 Bus Interface module |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0119` = 0.00029 ns | 100% | device_type=FTJ, architecture=Merged | material=MAPbBr3, measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0120` = 0.0007 ns | 100% | device_type=FTJ, architecture=Merged | measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0123` = 0.00015 ns | 100% | device_type=FTJ, architecture=Merged | measurement_method=Multidimensional coherent spectroscopy |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0127` = 0.0003 ns | 100% | device_type=FTJ, architecture=Merged | feature=XA |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0170` = 0.002 ns | 100% | device_type=FTJ, architecture=Merged | state=bright exciton |
| `CLM-ARCH-0013` = 162 ns | `CLM-MAT-0197` = 0.000603 ns | 100% | device_type=FTJ, architecture=Merged | material=SnSe, excitation_helicity=σ+ |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Merged | illumination=random speckle illumination |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Merged | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0073` = 0.0004 ns | 100% | device_type=FTJ, architecture=Merged | material=ITO film |
| `CLM-ARCH-0013` = 162 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Merged | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0013` = 162 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Merged | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=128, design=our design with tiering |

_and 811 more_

## `voltage` (21 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | incident_peak_electric_field=150 kV/cm | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0099` = 0.53 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0100` = 0.38 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0100` = 0.38 V | 100% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0067` = 0.47 V | 99% | incident_peak_electric_field=150 kV/cm | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0099` = 0.53 V | 99% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0027` = 1.53 V | 98% | incident_peak_electric_field=150 kV/cm | device_type=VO2 thin film device, temperature=330 K, transition_type=reset |
| `CLM-DEV-0006` = 85 V | `CLM-MEM-0011` = 2.32 V | 97% | incident_peak_electric_field=150 kV/cm | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0100` = 0.38 V | 97% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0026` = 12.65 V | `CLM-DEV-0067` = 0.47 V | 96% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0099` = 0.53 V | 96% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0026` = 12.65 V | 85% | incident_peak_electric_field=150 kV/cm | device_type=VO2 thin film device, temperature=330 K, transition_type=set |
| `CLM-MAT-0100` = 0.38 V | `CLM-MEM-0011` = 2.32 V | 84% | charging_voltage=0.6 V versus Ag/AgCl | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0026` = 12.65 V | `CLM-MEM-0011` = 2.32 V | 82% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0067` = 0.47 V | `CLM-MEM-0011` = 2.32 V | 80% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-MAT-0099` = 0.53 V | `CLM-MEM-0011` = 2.32 V | 77% | charging_voltage=0.6 V versus Ag/AgCl | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0100` = 0.38 V | 75% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0027` = 1.53 V | `CLM-DEV-0067` = 0.47 V | 69% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0099` = 0.53 V | 65% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0027` = 1.53 V | `CLM-MEM-0011` = 2.32 V | 34% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |

## `wavelength` (248 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0074` = 0.488 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | power=2 mW | mo_coupling_coefficient=0 |
| `CLM-MAT-0152` = 0.4 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | repetition_rate=1 kHz, pulse_duration=100 fs | mo_coupling_coefficient=0 |
| `CLM-MAT-0166` = 0.679 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=MoS₂, excitation_wavelength=532 nm | mo_coupling_coefficient=0 |
| `CLM-MAT-0167` = 0.318 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=MoS₂, substrate=sapphire, thickness=1.05 nm, angle=63.9° | mo_coupling_coefficient=0 |
| `CLM-MAT-0195` = 0.0035 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=(PEA)2PbI4 | mo_coupling_coefficient=0 |
| `CLM-PHOT-0028` = 0.0167 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | component=integrated microheater | mo_coupling_coefficient=0 |
| `CLM-PHOT-0033` = 0.00315 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | excitation_wavelength=532 nm, cumulative_exposure_time=5 h | mo_coupling_coefficient=0 |
| `CLM-PHOT-0040` = 0.785 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | source=diode laser | mo_coupling_coefficient=0 |
| `CLM-PHOT-0082` = 0.3621 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | process=Difference-frequency generation (DFG), input_signal_wavelength=637 nm | mo_coupling_coefficient=0 |
| `CLM-PHOT-0087` = 0.7757 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | fundamental_pump_wavelength=1551.42 nm | mo_coupling_coefficient=0 |
| `CLM-PHOT-0090` = 0.5191 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | device=microdisk, pump_wavelength=1559.40 nm, pump_power=12.4 mW | mo_coupling_coefficient=0 |
| `CLM-PHOT-0098` = 0.298 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=silicon nitride, radial_periodicity=229 nm, mode=out-of-plane mode | mo_coupling_coefficient=0 |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PKG-0003` = 0.001 um | 100% | mo_coupling_coefficient=0 | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PROC-0039` = 0.000388 um | 100% | mo_coupling_coefficient=0 | landing_energy=10 eV |
| `CLM-LITHO-0003` = 1.035 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | component=near-infrared laser pulse | mo_coupling_coefficient=0 |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PROC-0039` = 0.000388 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | landing_energy=10 eV |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PROC-0039` = 0.000388 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | landing_energy=10 eV |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PROC-0039` = 0.000388 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | landing_energy=10 eV |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PROC-0039` = 0.000388 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | landing_energy=10 eV |
| `CLM-PHOT-0055` = 2.062 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | device=Ho3+-doped fluoride glass waveguide laser | mo_coupling_coefficient=0 |
| `CLM-PHOT-0071` = 1.24 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=ITO | mo_coupling_coefficient=0 |
| `CLM-PHOT-0072` = 1.22 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | polarization=x-polarization, incident_angle=normal incidence | mo_coupling_coefficient=0 |
| `CLM-PHOT-0083` = 1.55 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | permittivity_diagonal_term=4.75, material=Bi-substituted yttrium iron garnet (Bi:YIG) | mo_coupling_coefficient=0 |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | mo_coupling_coefficient=0 |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PKG-0003` = 0.001 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | mo_coupling_coefficient=0 |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PKG-0003` = 0.001 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0055` = 2.062 um | `CLM-PROC-0039` = 0.000388 um | 100% | device=Ho3+-doped fluoride glass waveguide laser | landing_energy=10 eV |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PKG-0003` = 0.001 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | mo_coupling_coefficient=0 |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PKG-0003` = 0.001 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | mo_coupling_coefficient=0 |
| `CLM-PHOT-0071` = 1.24 um | `CLM-PROC-0039` = 0.000388 um | 100% | material=ITO | landing_energy=10 eV |
| `CLM-PHOT-0072` = 1.22 um | `CLM-PROC-0039` = 0.000388 um | 100% | polarization=x-polarization, incident_angle=normal incidence | landing_energy=10 eV |
| `CLM-PHOT-0083` = 1.55 um | `CLM-PROC-0039` = 0.000388 um | 100% | permittivity_diagonal_term=4.75, material=Bi-substituted yttrium iron garnet (Bi:YIG) | landing_energy=10 eV |
| `CLM-LITHO-0003` = 1.035 um | `CLM-PROC-0039` = 0.000388 um | 100% | component=near-infrared laser pulse | landing_energy=10 eV |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0040` = 0.785 um | `CLM-PROC-0039` = 0.000388 um | 100% | source=diode laser | landing_energy=10 eV |
| `CLM-PHOT-0055` = 2.062 um | `CLM-PKG-0003` = 0.001 um | 100% | device=Ho3+-doped fluoride glass waveguide laser | injection_current=9 mA, sample_type=D-DLAT sample |

_and 208 more_
