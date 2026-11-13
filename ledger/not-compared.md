# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**19393 pair(s)** as of 2026-11-13.

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

## `current` (20 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0028` = 0.6 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | process_step=current ramp-down | temperature=10 mK |
| `CLM-DEV-0057` = 30 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=small switching current | temperature=10 mK |
| `CLM-DEV-0058` = 40 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=large switching current | temperature=10 mK |
| `CLM-EDA-0018` = 0.02 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | circuit=BMR, corner=tt | temperature=10 mK |
| `CLM-DEV-0058` = 40 mA | `CLM-EDA-0018` = 0.02 mA | 100% | switching_regime=large switching current | circuit=BMR, corner=tt |
| `CLM-DEV-0057` = 30 mA | `CLM-EDA-0018` = 0.02 mA | 100% | switching_regime=small switching current | circuit=BMR, corner=tt |
| `CLM-DEV-0077` = 4 mA | `CLM-EDA-0018` = 0.02 mA | 100% | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° | circuit=BMR, corner=tt |
| `CLM-DEV-0075` = 1.5 mA | `CLM-EDA-0018` = 0.02 mA | 99% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | circuit=BMR, corner=tt |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0058` = 40 mA | 99% | temperature=2 K, state=after light irradiation | switching_regime=large switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0058` = 40 mA | 98% | process_step=current ramp-down | switching_regime=large switching current |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0057` = 30 mA | 98% | temperature=2 K, state=after light irradiation | switching_regime=small switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0057` = 30 mA | 98% | process_step=current ramp-down | switching_regime=small switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-EDA-0018` = 0.02 mA | 97% | process_step=current ramp-down | circuit=BMR, corner=tt |
| `CLM-DEV-0036` = 0.558 mA | `CLM-EDA-0018` = 0.02 mA | 96% | temperature=2 K, state=after light irradiation | circuit=BMR, corner=tt |
| `CLM-DEV-0058` = 40 mA | `CLM-DEV-0075` = 1.5 mA | 96% | switching_regime=large switching current | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |
| `CLM-DEV-0057` = 30 mA | `CLM-DEV-0075` = 1.5 mA | 95% | switching_regime=small switching current | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |
| `CLM-DEV-0058` = 40 mA | `CLM-DEV-0077` = 4 mA | 90% | switching_regime=large switching current | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0057` = 30 mA | `CLM-DEV-0077` = 4 mA | 87% | switching_regime=small switching current | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0077` = 4 mA | 85% | process_step=current ramp-down | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0075` = 1.5 mA | 60% | process_step=current ramp-down | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° |

## `energy` (1088 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0048` = 185 meV | `CLM-MEM-0040` = -180 meV | 197% | material=LiFePO4 | method=DFT |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0172` = -5090 meV | 194% | defect_complex=VAl(ON)3, model=DFT | material=MLBP |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0331` = 5630 meV | 190% | material=MLBP | phase=m-phase, temperature=300 K |
| `CLM-MAT-0002` = 200 meV | `CLM-MEM-0040` = -180 meV | 190% | mechanism=optical phonon | method=DFT |
| `CLM-MAT-0200` = 200 meV | `CLM-MEM-0040` = -180 meV | 190% | band=2.3 eV emission, impurity_content=<0.1 ppm | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0274` = 5922 meV | 186% | material=MLBP | desorption_state=atomic |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0172` = -5090 meV | 185% | defect_complex=VAl(ON)3 | material=MLBP |
| `CLM-MAT-0104` = 220 meV | `CLM-MEM-0040` = -180 meV | 182% | measurement=RIXS, absorption_edge=Fe L3 edge | method=DFT |
| `CLM-MAT-0313` = 130 meV | `CLM-MEM-0040` = -180 meV | 172% | material=SmNiO3 | method=DFT |
| `CLM-MAT-0316` = 290 meV | `CLM-MEM-0040` = -180 meV | 162% | material=Ge, k_point=Γ point | method=DFT |
| `CLM-MAT-0049` = 296 meV | `CLM-MEM-0040` = -180 meV | 161% | material=LiFePO4 | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0290` = 3000 meV | 159% | material=MLBP | trap_type=isolated bi-Si3 |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0276` = 2994 meV | 159% | material=MLBP | desorption_state=molecular |
| `CLM-MAT-0050` = 102 meV | `CLM-MEM-0040` = -180 meV | 157% | material=Li6PS5Cl | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0291` = 2800 meV | 155% | material=MLBP | trap_type=isolated bi-Ed |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0277` = 2789 meV | 155% | material=MLBP | desorption_state=molecular |
| `CLM-MEM-0040` = -2.884e-05 fJ | `CLM-PROC-0031` = 1.458e-05 fJ | 151% | method=DFT | error_metric=root-mean-square deviation per formula unit |
| `CLM-MAT-0306` = 89.9 meV | `CLM-MEM-0040` = -180 meV | 150% | polarization_state=P↑ | method=DFT |
| `CLM-MAT-0201` = 370 meV | `CLM-MEM-0040` = -180 meV | 149% | band=2.3 eV emission, impurity_content=<0.1 ppm | method=DFT |
| `CLM-MAT-0016` = 2020 meV | `CLM-MAT-0172` = -5090 meV | 140% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0015` = 1980 meV | `CLM-MAT-0172` = -5090 meV | 139% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0014` = 1940 meV | `CLM-MAT-0172` = -5090 meV | 138% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0295` = 490 meV | `CLM-MEM-0040` = -180 meV | 137% | fit_function=Eq. ( 13), experimental_data_source=Ref. [ 6] | method=DFT |
| `CLM-MEM-0018` = 8.011e-05 fJ | `CLM-MEM-0040` = -2.884e-05 fJ | 136% | temperature=100 K, measurement_method=ARPES | method=DFT |
| `CLM-MAT-0051` = 1801 meV | `CLM-MAT-0172` = -5090 meV | 135% | axis=c | material=MLBP |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MEM-0040` = -180 meV | 133% | mechanism=surface polar phonon, substrate=SiO2 | method=DFT |
| `CLM-MAT-0013` = 1340 meV | `CLM-MAT-0172` = -5090 meV | 126% | synthesis_condition=Nitrogen-rich | material=MLBP |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0329` = 1310 meV | 126% | material=MLBP | kekule_distortion_strength=0.3 |
| `CLM-MAT-0327` = 740 meV | `CLM-MEM-0040` = -180 meV | 124% | kekule_distortion_strength=0.1 | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0294` = 1120 meV | 122% | material=MLBP | fit_function=Eq. ( 13), experimental_data_source=Ref. [ 6] |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0328` = 1000 meV | 120% | material=MLBP | kekule_distortion_strength=0.2 |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0275` = 995 meV | 120% | material=MLBP | desorption_state=molecular |
| `CLM-MAT-0275` = 995 meV | `CLM-MEM-0040` = -180 meV | 118% | desorption_state=molecular | method=DFT |
| `CLM-MAT-0328` = 1000 meV | `CLM-MEM-0040` = -180 meV | 118% | kekule_distortion_strength=0.2 | method=DFT |
| `CLM-MAT-0294` = 1120 meV | `CLM-MEM-0040` = -180 meV | 116% | fit_function=Eq. ( 13), experimental_data_source=Ref. [ 6] | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0327` = 740 meV | 115% | material=MLBP | kekule_distortion_strength=0.1 |
| `CLM-MAT-0329` = 1310 meV | `CLM-MEM-0040` = -180 meV | 114% | kekule_distortion_strength=0.3 | method=DFT |
| `CLM-MAT-0013` = 1340 meV | `CLM-MEM-0040` = -180 meV | 113% | synthesis_condition=Nitrogen-rich | method=DFT |
| `CLM-MAT-0051` = 1801 meV | `CLM-MEM-0040` = -180 meV | 110% | axis=c | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MEM-0018` = 500 meV | 110% | material=MLBP | temperature=100 K, measurement_method=ARPES |

_and 1048 more_

## `energy_advantage_ratio` (19 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0016` = 1.22 x | `CLM-PROC-0062` = 417 x | 100% | device=B200, benchmark=GroupGEMM | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0005` = 1.32 x | `CLM-PROC-0062` = 417 x | 100% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0016` = 1.22 x | `CLM-ARCH-0022` = 169.1 x | 99% | device=B200, benchmark=GroupGEMM | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0005` = 1.32 x | `CLM-ARCH-0022` = 169.1 x | 99% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0004` = 3.83 x | `CLM-PROC-0062` = 417 x | 99% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0002` = 5 x | `CLM-PROC-0062` = 417 x | 99% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0006` = 5.3 x | `CLM-PROC-0062` = 417 x | 99% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0016` = 1.22 x | `CLM-PROC-0058` = 73 x | 98% | device=B200, benchmark=GroupGEMM | surrogate_model=VP-DDBM, baseline_model=phase-field solver |
| `CLM-ARCH-0005` = 1.32 x | `CLM-PROC-0058` = 73 x | 98% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | surrogate_model=VP-DDBM, baseline_model=phase-field solver |
| `CLM-ARCH-0004` = 3.83 x | `CLM-ARCH-0022` = 169.1 x | 98% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0002` = 5 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0006` = 5.3 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0004` = 3.83 x | `CLM-PROC-0058` = 73 x | 95% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | surrogate_model=VP-DDBM, baseline_model=phase-field solver |
| `CLM-ARCH-0002` = 5 x | `CLM-PROC-0058` = 73 x | 93% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | surrogate_model=VP-DDBM, baseline_model=phase-field solver |
| `CLM-ARCH-0006` = 5.3 x | `CLM-PROC-0058` = 73 x | 93% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | surrogate_model=VP-DDBM, baseline_model=phase-field solver |
| `CLM-ARCH-0016` = 1.22 x | `CLM-MEM-0025` = 3.7 x | 67% | device=B200, benchmark=GroupGEMM | baseline=SoA mappings |
| `CLM-ARCH-0005` = 1.32 x | `CLM-MEM-0025` = 3.7 x | 64% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | baseline=SoA mappings |
| `CLM-ARCH-0022` = 169.1 x | `CLM-PROC-0062` = 417 x | 59% | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch | surrogate_model=deterministic U-Net |
| `CLM-ARCH-0022` = 169.1 x | `CLM-PROC-0058` = 73 x | 57% | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch | surrogate_model=VP-DDBM, baseline_model=phase-field solver |

## `frequency` (689 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0012` = 370 GHz | `CLM-MAT-0298` = -1630 GHz | 123% | magnetic_field=8.1 T, frequency=1.9 THz | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0052` = 320 GHz | 120% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-MAT-0299` = -7240 GHz | 117% | component=FIGFLEX, activation_format=FP16 | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0049` = 267 GHz | 116% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | signal_type=measured phase noise |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0051` = 230 GHz | 114% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-MAT-0299` = -7240 GHz | 111% | component=FIGFLEX, activation_format=FP16 | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-DEV-0013` = 180 GHz | `CLM-MAT-0298` = -1630 GHz | 111% | magnetic_field=7.5 T, frequency=2.2 THz | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0036` = 121 GHz | 107% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | sample_size=22 measured devices |
| `CLM-DEV-0012` = 370 GHz | `CLM-MAT-0299` = -7240 GHz | 105% | magnetic_field=8.1 T, frequency=1.9 THz | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0052` = 320 GHz | 104% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0151` = 4.34e+04 GHz | `CLM-MAT-0298` = -1630 GHz | 104% | component=FIGFLEX, activation_format=FP16 | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 104% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0049` = 267 GHz | 104% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | signal_type=measured phase noise |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0051` = 230 GHz | 103% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0152` = 6.49e+04 GHz | `CLM-MAT-0298` = -1630 GHz | 103% | component=FIGFLEX, activation_format=FP16 | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-DEV-0013` = 180 GHz | `CLM-MAT-0299` = -7240 GHz | 102% | magnetic_field=7.5 T, frequency=2.2 THz | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0036` = 121 GHz | 102% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | sample_size=22 measured devices |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-MAT-0298` = -1630 GHz | 102% | platform=optical PPLN module | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0001` = 18.98 GHz | 101% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | component=single ring cavity, parameter=FSR |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0003` = 15.41 GHz | 101% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 101% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0136` = 8.234 GHz | 101% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | structure=coupled SSPP waveguides |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PROC-0032` = 7.9 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | holder_type=two-channel holder, chip_type=Si/Si3N4 chip, metric=-3 dB bandwidth |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0061` = 7.48 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | corner_radius=1.4 mm |
| `CLM-DEV-0072` = 7 GHz | `CLM-MAT-0298` = -1630 GHz | 100% | measurement_method=BLS spectra | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0125` = 6 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | pump_detuning=27 MHz |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-MAT-0299` = -7240 GHz | 100% | platform=optical PPLN module | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PROC-0033` = 4.5 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | holder_type=four-channel configuration, metric=-3 dB bandwidth |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0001` = 18.98 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | component=single ring cavity, parameter=FSR |
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0002` = 3.57 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | component=photonic molecule, mode_spacing=Ω1 |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0003` = 15.41 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-MAT-0228` = 2.5 GHz | `CLM-MAT-0298` = -1630 GHz | 100% | component=α-Fe2O3 microdisk | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0136` = 8.234 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | structure=coupled SSPP waveguides |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PROC-0032` = 7.9 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | holder_type=two-channel holder, chip_type=Si/Si3N4 chip, metric=-3 dB bandwidth |
| `CLM-DEV-0072` = 7 GHz | `CLM-MAT-0299` = -7240 GHz | 100% | measurement_method=BLS spectra | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0061` = 7.48 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | corner_radius=1.4 mm |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0125` = 6 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | pump_detuning=27 MHz |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PROC-0033` = 4.5 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | holder_type=four-channel configuration, metric=-3 dB bandwidth |
| `CLM-MAT-0299` = -7240 GHz | `CLM-PHOT-0002` = 3.57 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | component=photonic molecule, mode_spacing=Ω1 |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-MAT-0298` = -1630 GHz | 100% | process_node=TSMC 28 nm | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P |

_and 649 more_

## `length_device` (5481 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0053` = 1.61 nm | `CLM-LITHO-0005` = 3e+06 nm | 100% | parameter=ts | beam_profile=Gaussian |
| `CLM-DEV-0053` = 1.61 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | parameter=ts | component=lens |
| `CLM-DEV-0053` = 1.61 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | parameter=ts | material=GaN, growth_method=ammonothermal |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | parameter=ts | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0065` = 4e+05 nm | 100% | parameter=ts | chip_thickness=4-mm |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0115` = 3.3e+04 nm | 100% | parameter=ts | dimension=width |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0116` = 1.47e+05 nm | 100% | parameter=ts | dimension=length |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0131` = 5e+05 nm | 100% | parameter=ts | channel_type=elementary channel |
| `CLM-DEV-0068` = 100 nm | `CLM-LITHO-0005` = 3e+06 nm | 100% | material=PEDOT:PSS | beam_profile=Gaussian |
| `CLM-DEV-0068` = 100 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | material=PEDOT:PSS | component=lens |
| `CLM-DEV-0068` = 100 nm | `CLM-MAT-0138` = 0.005 nm | 100% | material=PEDOT:PSS | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0068` = 100 nm | `CLM-MAT-0140` = 0.005 nm | 100% | material=PEDOT:PSS | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0084` = 22.17 nm | `CLM-LITHO-0005` = 3e+06 nm | 100% | rkky_coupling=-0.2 mJ/m² | beam_profile=Gaussian |
| `CLM-DEV-0084` = 22.17 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | rkky_coupling=-0.2 mJ/m² | component=lens |
| `CLM-DEV-0084` = 22.17 nm | `CLM-PHOT-0131` = 5e+05 nm | 100% | rkky_coupling=-0.2 mJ/m² | channel_type=elementary channel |
| `CLM-DEV-0085` = 22.21 nm | `CLM-LITHO-0005` = 3e+06 nm | 100% | rkky_coupling=-0.2 mJ/m² | beam_profile=Gaussian |
| `CLM-DEV-0085` = 22.21 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | rkky_coupling=-0.2 mJ/m² | component=lens |
| `CLM-DEV-0085` = 22.21 nm | `CLM-PHOT-0131` = 5e+05 nm | 100% | rkky_coupling=-0.2 mJ/m² | channel_type=elementary channel |
| `CLM-DEV-0092` = 280.6 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | cell_size=1 µm | component=lens |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0135` = 0.013 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0136` = 0.006 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0137` = 0.011 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0138` = 0.005 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0139` = 0.007 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0092` = 280.6 nm | `CLM-MAT-0140` = 0.005 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | cell_size=1 µm | component=lens |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0135` = 0.013 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0136` = 0.006 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0137` = 0.011 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0138` = 0.005 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0139` = 0.007 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-MAT-0140` = 0.005 nm | 100% | cell_size=1 µm | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-DEV-0093` = 502.3 nm | `CLM-PHOT-0057` = 0.024 nm | 100% | cell_size=1 µm | measurement_duration=exceeding 15.5 hours |
| `CLM-DEV-0093` = 502.3 nm | `CLM-PROC-0049` = 0.0229 nm | 100% | cell_size=1 µm | sample=twisted bilayer graphene-hBN |
| `CLM-DEV-0093` = 502.3 nm | `CLM-PROC-0050` = 0.0244 nm | 100% | cell_size=1 µm | sample=twisted bilayer graphene-hBN |
| `CLM-LITHO-0001` = 500 nm | `CLM-LITHO-0006` = 2e+08 nm | 100% | material=crystalline silicon membrane | component=lens |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0135` = 0.013 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0136` = 0.006 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0137` = 0.011 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-LITHO-0001` = 500 nm | `CLM-MAT-0138` = 0.005 nm | 100% | material=crystalline silicon membrane | superlattice_layer_n=3, superlattice_layer_m=5 |

_and 5441 more_

## `power` (312 pair(s))

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
| `CLM-ARCH-0037` = 787 mW | `CLM-ARCH-0166` = 0.027 mW | 100% | component=synthesized SRAM-PIM subsystem | processor=TEXEL |
| `CLM-ARCH-0037` = 787 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=synthesized SRAM-PIM subsystem | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=synthesized SRAM-PIM subsystem | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=synthesized SRAM-PIM subsystem | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=synthesized SRAM-PIM subsystem | device_type=drop-cast control devices |
| `CLM-ARCH-0037` = 787 mW | `CLM-PHOT-0068` = 0.00024 mW | 100% | component=synthesized SRAM-PIM subsystem | operating_point=3 mW total trapping-beam power |
| `CLM-ARCH-0038` = 9599 mW | `CLM-ARCH-0166` = 0.027 mW | 100% | component=added compute and buffer logic in HBM-PIM | processor=TEXEL |
| `CLM-ARCH-0038` = 9599 mW | `CLM-ARCH-0209` = 0.3 mW | 100% | component=added compute and buffer logic in HBM-PIM | process=28 nm |
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
| `CLM-ARCH-0114` = 3.55 mW | `CLM-ARCH-0190` = 2.838e+05 mW | 100% | component=PIM Chunk List, location=DRAM chip | benchmark=DiT-256 workload, process=28nm |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=PIM Chunk List, location=DRAM chip | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=PIM Chunk List, location=DRAM chip | device_type=drop-cast control devices |
| `CLM-ARCH-0149` = 4020 mW | `CLM-ARCH-0166` = 0.027 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | processor=TEXEL |
| `CLM-ARCH-0149` = 4020 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=FIGFLEX, toggle_rate=0.2, activation_format=FP16, precision=INT4 | benchmark_circuit=BGR, framework=AgenticSizing |

_and 272 more_

## `power_density` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0079` = 3.1e-05 W/mm^2 | `CLM-MAT-0026` = 4.8e-07 W/mm^2 | 98% | structure=long-base p+-n device, n_base_width=300 𝜇𝜇m, framework=extended theory | environment=ambient |

## `pressure` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0064` = 6e-06 torr | `CLM-MAT-0296` = 3.75e+04 torr | 100% | temperature=room temperature | measurement=Tensile testing |

## `relative_deviation` (8976 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-EDA-0003` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | benchmark_circuit=LDO benchmark, framework=proposed method | sample=B1-1 |
| `CLM-EDA-0004` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | circuit=most complex circuit, framework=proposed framework | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0044` = 59.9 percent | 200% | sample=B1-1 | voltage=8 VAg/AgCl, material=1 μm n-type GaN |
| `CLM-ARCH-0198` = 60.3 percent | `CLM-MAT-0111` = -60 percent | 200% | baseline_utilization=42.4% | sample=B1-1 |
| `CLM-ARCH-0170` = 62.3 percent | `CLM-MAT-0111` = -60 percent | 196% | frequency=80 MHz, model=ConvSNN | sample=B1-1 |
| `CLM-ARCH-0089` = 64.2 percent | `CLM-MAT-0111` = -60 percent | 193% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0112` = 66.8 percent | 190% | sample=B1-1 | baseline=pure two-dimensional Coulomb reference, benchmark_protocol=high-field-calibrated |
| `CLM-ARCH-0090` = 67.5 percent | `CLM-MAT-0111` = -60 percent | 189% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0252` = 53 percent | 188% | sample=B1-1 | band=NNN, coupling=Λ A, correlation_length=ξ ¯kF = 4 |
| `CLM-ARCH-0187` = 70 percent | `CLM-MAT-0111` = -60 percent | 186% | workload=elementwise graph, technique=Symbolic dynamic compilation | sample=B1-1 |
| `CLM-ARCH-0174` = 71.3 percent | `CLM-MAT-0111` = -60 percent | 184% | system=ARM2GC, benchmark_set=nine benchmarks | sample=B1-1 |
| `CLM-ARCH-0097` = 72 percent | `CLM-MAT-0111` = -60 percent | 183% | training_dataset=CloudLab, evaluation_dataset=Lambda | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0039` = 49.85 percent | 183% | sample=B1-1 | platform=Jetson Orin Nano, threshold=550, verification_stage=Single function verification |
| `CLM-ARCH-0210` = 48.24 percent | `CLM-MAT-0111` = -60 percent | 180% | metric=matrix-input storage | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0026` = 75.7 percent | 179% | sample=B1-1 | placement=conventional |
| `CLM-EDA-0007` = 76 percent | `CLM-MAT-0111` = -60 percent | 179% | model=Non-cyclic + Node prediction model | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0251` = 47 percent | 178% | sample=B1-1 | band=NN, coupling=Λ A, correlation_length=ξ ¯kF = 4 |
| `CLM-ARCH-0049` = 46 percent | `CLM-MAT-0111` = -60 percent | 177% | mechanism=uniform iteration offsets | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0186` = 46 percent | 177% | sample=B1-1 | indium_composition=13.5%, geometry=fixed pristine-GaN geometry |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0188` = 46 percent | 177% | sample=B1-1 | indium_composition=22%, baseline=pristine GaN |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0031` = 79.2 percent | 176% | sample=B1-1 | workload=six full-trace streams, hardware_configuration=six 3D DRAM organizations, method=TileDRAM |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0032` = 84.9 percent | 171% | sample=B1-1 | memory_technology=filamentary memristor |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0005` = 85 percent | 171% | sample=B1-1 | dataset=Iris test set |
| `CLM-EDA-0005` = 86.4 percent | `CLM-MAT-0111` = -60 percent | 169% | model=Cyclic Edge prediction model | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0021` = 87.5 percent | 169% | sample=B1-1 | device_technology=printed Ag/ZnO/Au ECM memristors |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0006` = 88 percent | 168% | sample=B1-1 | dataset=MNIST, setup=experimental system |
| `CLM-EDA-0043` = 88.1 percent | `CLM-MAT-0111` = -60 percent | 168% | design=AES | sample=B1-1 |
| `CLM-ARCH-0101` = 89.4 percent | `CLM-MAT-0111` = -60 percent | 167% | correction_type=uncorrected | sample=B1-1 |
| `CLM-EDA-0006` = 89.6 percent | `CLM-MAT-0111` = -60 percent | 167% | model=Non-cyclic Edge prediction model | sample=B1-1 |
| `CLM-EDA-0044` = 40 percent | `CLM-MAT-0111` = -60 percent | 167% | design=AES | sample=B1-1 |
| `CLM-ARCH-0099` = 91.8 percent | `CLM-MAT-0111` = -60 percent | 165% | training_method=CSI-based training | sample=B1-1 |
| `CLM-ARCH-0041` = 93.08 percent | `CLM-MAT-0111` = -60 percent | 164% | frequency=7 GHz | sample=B1-1 |
| `CLM-EDA-0045` = 93.3 percent | `CLM-MAT-0111` = -60 percent | 164% | design=AES | sample=B1-1 |
| `CLM-ARCH-0096` = 93.6 percent | `CLM-MAT-0111` = -60 percent | 164% | classifier=XGBoost, evaluation_method=five-fold cross-validation | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0059` = 94.4 percent | 164% | sample=B1-1 | route=Fourier route |
| `CLM-DEV-0069` = 38 percent | `CLM-MAT-0111` = -60 percent | 163% | wavelength=365 nm, batch=batch A, operating_voltage=0 V | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0012` = 95 percent | 163% | sample=B1-1 | encoding_scheme=differential encoding, benchmark=MNIST |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0023` = 95 percent | 163% | sample=B1-1 | device_technology=printed Ag/ZnO/Au ECM memristors |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0044` = 95.33 percent | 163% | sample=B1-1 | dataset=Fisher’s Iris flower dataset, architecture=SNN architecture, device=Pr0.7Ca0.3MnO3 (PCMO) RRAM |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0045` = 96 percent | 162% | sample=B1-1 | model=ideal LIF neuron, dataset=Fisher’s Iris flower dataset |

_and 8936 more_

## `resistance` (2 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0282` = 0.0039 ohm | `CLM-MEM-0001` = 900 ohm | 100% | temperature=10 K, dc_current=0.1 mA | resistance_state=high-resistance state |
| `CLM-MAT-0281` = 6.59 ohm | `CLM-MEM-0001` = 900 ohm | 99% | interface=IrMn3/Pt, temperature=10 K, dc_current=0.1 mA | resistance_state=high-resistance state |

## `sensitivity_advantage_ratio` (6 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0214` = 1.68 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 88% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0214` = 1.68 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 86% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0213` = 2.57 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 81% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0213` = 2.57 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 79% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0212` = 4.95 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 63% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0212` = 4.95 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 59% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |

## `temperature` (367 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0307` = 186.9 degC | 192% | relaxation_temperature=TLIESST | property=T N |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0092` = -23.15 degC | 191% | temperature_control_system=VAHEAT system | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0004` = -73.15 degC | 189% | time_after_cooling_onset=10 s | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0293` = -73.15 degC | 189% | time_after_cooling_onset=10 s | mn_content=0.1, compensation_degree=Kmax |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0053` = 230 degC | 189% | sample=NbN/I/FePt | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0053` = 230 degC | 189% | relaxation_temperature=TLIESST | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0004` = -73.15 degC | 186% | time_after_cooling_onset=10 s | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0293` = -73.15 degC | 186% | time_after_cooling_onset=10 s | mn_content=0.1, compensation_degree=Kmax |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0091` = -113.1 degC | 175% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0307` = 186.9 degC | 173% | sample=NbN/I/FePt | property=T N |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0091` = -113.1 degC | 172% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0003` = -123.1 degC | 169% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0003` = -123.1 degC | 166% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0292` = -133.1 degC | 164% | time_after_cooling_onset=10 s | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0292` = -133.1 degC | 161% | time_after_cooling_onset=10 s | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-MAT-0102` = -81 K | `CLM-MAT-0292` = 140 K | 158% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0101` = -155.1 degC | 155% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0003` = 150 K | `CLM-MAT-0102` = -81 K | 154% | calculation=acoustic phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0101` = -155.1 degC | 153% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0279` = 106.9 degC | 152% | relaxation_temperature=TLIESST | sample_layer=IrMn3(10 nm)/Py bilayer |
| `CLM-MAT-0091` = 160 K | `CLM-MAT-0102` = -81 K | 151% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0033` = 84.85 degC | `CLM-DEV-0035` = -204.1 degC | 142% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0279` = 106.9 degC | 141% | sample=NbN/I/FePt | sample_layer=IrMn3(10 nm)/Py bilayer |
| `CLM-MAT-0004` = 200 K | `CLM-MAT-0102` = -81 K | 140% | calculation=optical phonon and surface polar phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-MAT-0102` = -81 K | `CLM-MAT-0293` = 200 K | 140% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | mn_content=0.1, compensation_degree=Kmax |
| `CLM-DEV-0032` = 81.85 degC | `CLM-DEV-0035` = -204.1 degC | 140% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0093` = 76.85 degC | 138% | relaxation_temperature=TLIESST | magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0325` = -233.1 degC | 136% | time_after_cooling_onset=10 s | material=GdN |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0325` = -233.1 degC | 135% | time_after_cooling_onset=10 s | material=GdN |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0004` = -73.15 degC | 135% | temperature_control_system=VAHEAT system | calculation=optical phonon and surface polar phonon scattering |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0293` = -73.15 degC | 135% | temperature_control_system=VAHEAT system | mn_content=0.1, compensation_degree=Kmax |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0263` = 750 degC | 134% | sample=NbN/I/FePt | atmosphere=oxygen atmosphere (oxygen pressure regulated to 0.4 MPa) |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MEM-0019` = 768.9 degC | 134% | sample=NbN/I/FePt | model=realistic multi-orbital model of YCl, onsite_hubbard_parameter=0.9 eV |
| `CLM-DEV-0033` = 84.85 degC | `CLM-DEV-0076` = -257.6 degC | 133% | time_after_cooling_onset=10 s | sample=NbN/I/FePt |
| `CLM-MAT-0092` = 250 K | `CLM-MAT-0102` = -81 K | 132% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MEM-0020` = 801.9 degC | 132% | sample=NbN/I/FePt | method=Hartree-Fock approximation |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0142` = -264.1 degC | 132% | time_after_cooling_onset=10 s | measurement_setup=STM measurements |
| `CLM-DEV-0032` = 81.85 degC | `CLM-DEV-0076` = -257.6 degC | 132% | time_after_cooling_onset=10 s | sample=NbN/I/FePt |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0210` = -269.9 degC | 131% | time_after_cooling_onset=10 s | strain=+2%, method=anisotropic Migdal-Eliashberg equations |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0209` = -270.5 degC | 131% | time_after_cooling_onset=10 s | equation=Allen-Dynes modified McMillan equation |

_and 327 more_

## `temperature_delta` (52 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0324` = -0.008 K | `CLM-PHOT-0037` = 0.11 K | 107% | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0098` = 0.71 K | `CLM-MAT-0324` = -0.008 K | 101% | component=Pt injector | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-DEV-0097` = 0.75 K | `CLM-MAT-0324` = -0.008 K | 101% | component=Pt injector | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-DEV-0096` = 0.96 K | `CLM-MAT-0324` = -0.008 K | 101% | component=Pt injector | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-DEV-0095` = 1.35 K | `CLM-MAT-0324` = -0.008 K | 101% | component=Pt injector | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-DEV-0034` = 3 K | `CLM-MAT-0324` = -0.008 K | 100% | time_after_cooling_onset=10 s | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-DEV-0024` = 30.4 K | `CLM-MAT-0324` = -0.008 K | 100% | gate_bias_vgs=-2.7 V | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-MAT-0297` = 50 K | `CLM-MAT-0324` = -0.008 K | 100% | dissipated_power=4 W mm-1 | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] |
| `CLM-MAT-0324` = -0.008 K | `CLM-PHOT-0086` = 275.2 K | 100% | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] | external_pump_power=300 μW |
| `CLM-MAT-0324` = -0.008 K | `CLM-PHOT-0091` = 281.6 K | 100% | field_cooling_field=+9 T, current_density=5.38  108 A/m2, current_direction=[001] | device=microdisk, pump_power=12.4 mW |
| `CLM-PHOT-0037` = 0.11 K | `CLM-PHOT-0086` = 275.2 K | 100% | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW | external_pump_power=300 μW |
| `CLM-PHOT-0037` = 0.11 K | `CLM-PHOT-0091` = 281.6 K | 100% | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW | device=microdisk, pump_power=12.4 mW |
| `CLM-MAT-0297` = 50 K | `CLM-PHOT-0037` = 0.11 K | 100% | dissipated_power=4 W mm-1 | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0098` = 0.71 K | `CLM-PHOT-0091` = 281.6 K | 100% | component=Pt injector | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0098` = 0.71 K | `CLM-PHOT-0086` = 275.2 K | 100% | component=Pt injector | external_pump_power=300 μW |
| `CLM-DEV-0097` = 0.75 K | `CLM-PHOT-0086` = 275.2 K | 100% | component=Pt injector | external_pump_power=300 μW |
| `CLM-DEV-0097` = 0.75 K | `CLM-PHOT-0091` = 281.6 K | 100% | component=Pt injector | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0096` = 0.96 K | `CLM-PHOT-0091` = 281.6 K | 100% | component=Pt injector | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0096` = 0.96 K | `CLM-PHOT-0086` = 275.2 K | 100% | component=Pt injector | external_pump_power=300 μW |
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0037` = 0.11 K | 100% | gate_bias_vgs=-2.7 V | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0095` = 1.35 K | `CLM-PHOT-0091` = 281.6 K | 100% | component=Pt injector | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0095` = 1.35 K | `CLM-PHOT-0086` = 275.2 K | 100% | component=Pt injector | external_pump_power=300 μW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0091` = 281.6 K | 99% | time_after_cooling_onset=10 s | device=microdisk, pump_power=12.4 mW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0086` = 275.2 K | 99% | time_after_cooling_onset=10 s | external_pump_power=300 μW |
| `CLM-DEV-0098` = 0.71 K | `CLM-MAT-0297` = 50 K | 99% | component=Pt injector | dissipated_power=4 W mm-1 |
| `CLM-DEV-0097` = 0.75 K | `CLM-MAT-0297` = 50 K | 98% | component=Pt injector | dissipated_power=4 W mm-1 |
| `CLM-MAT-0229` = 5 K | `CLM-PHOT-0091` = 281.6 K | 98% | p_mw=128 mW, simulation_type=finite-element simulations | device=microdisk, pump_power=12.4 mW |
| `CLM-MAT-0229` = 5 K | `CLM-PHOT-0086` = 275.2 K | 98% | p_mw=128 mW, simulation_type=finite-element simulations | external_pump_power=300 μW |
| `CLM-DEV-0096` = 0.96 K | `CLM-MAT-0297` = 50 K | 98% | component=Pt injector | dissipated_power=4 W mm-1 |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0098` = 0.71 K | 98% | gate_bias_vgs=-2.7 V | component=Pt injector |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0097` = 0.75 K | 98% | gate_bias_vgs=-2.7 V | component=Pt injector |
| `CLM-DEV-0095` = 1.35 K | `CLM-MAT-0297` = 50 K | 97% | component=Pt injector | dissipated_power=4 W mm-1 |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0096` = 0.96 K | 97% | gate_bias_vgs=-2.7 V | component=Pt injector |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0037` = 0.11 K | 96% | time_after_cooling_onset=10 s | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0095` = 1.35 K | 96% | gate_bias_vgs=-2.7 V | component=Pt injector |
| `CLM-DEV-0034` = 3 K | `CLM-MAT-0297` = 50 K | 94% | time_after_cooling_onset=10 s | dissipated_power=4 W mm-1 |
| `CLM-DEV-0095` = 1.35 K | `CLM-PHOT-0037` = 0.11 K | 92% | component=Pt injector | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0034` = 3 K | 90% | gate_bias_vgs=-2.7 V | time_after_cooling_onset=10 s |
| `CLM-MAT-0229` = 5 K | `CLM-MAT-0297` = 50 K | 90% | p_mw=128 mW, simulation_type=finite-element simulations | dissipated_power=4 W mm-1 |
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0091` = 281.6 K | 89% | gate_bias_vgs=-2.7 V | device=microdisk, pump_power=12.4 mW |

_and 12 more_

## `thermal_conductivity` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |

## `time` (2015 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0130` = 1.036e+07 ns | 100% | device_type=FTJ, architecture=Naive | device=NVIDIA GeForce RTX 5080, form=direct, decode=ALU |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0131` = 1.115e+07 ns | 100% | device_type=FTJ, architecture=Naive | device=NVIDIA GeForce RTX 5080, form=hoisted, decode=LUT |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0153` = 3.72e+09 ns | 100% | device_type=FTJ, architecture=Naive | component=FIGFLEX, benchmark=Llama-3.1-8B |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0172` = 8.04e+10 ns | 100% | device_type=FTJ, architecture=Naive | program=Mini-Transformer, dynamic_instructions=3,411,714 |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0173` = 1.78e+11 ns | 100% | device_type=FTJ, architecture=Naive | program=Mini-ResNet, dynamic_instructions=11,022,541 |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0188` = 3.24e+10 ns | 100% | device_type=FTJ, architecture=Naive | benchmark=matmul_single_core, simulator=Wolfpine |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0189` = 7.2e+09 ns | 100% | device_type=FTJ, architecture=Naive | benchmark=matmul_single_core, simulator=ttsim |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0217` = 2.6e+10 ns | 100% | device_type=FTJ, architecture=Naive | model=ForeSight |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0066` = 6e+10 ns | 100% | device_type=FTJ, architecture=Naive | software=MATLAB Deep Learning Toolbox |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0089` = 0.007 ns | 100% | device_type=FTJ, architecture=Naive | sample=SESAM |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0011` = 1.35e+08 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=cache coherence module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0012` = 1.273e+09 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=L1 Bus Interface module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0119` = 0.00029 ns | 100% | device_type=FTJ, architecture=Naive | material=MAPbBr3, measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0120` = 0.0007 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0123` = 0.00015 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Multidimensional coherent spectroscopy |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0127` = 0.0003 ns | 100% | device_type=FTJ, architecture=Naive | feature=XA |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0170` = 0.002 ns | 100% | device_type=FTJ, architecture=Naive | state=bright exciton |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0197` = 0.000603 ns | 100% | device_type=FTJ, architecture=Naive | material=SnSe, excitation_helicity=σ+ |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0230` = 0.00015 ns | 100% | device_type=FTJ, architecture=Naive | parameter=overall temporal resolution |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0237` = 8.5e+09 ns | 100% | device_type=FTJ, architecture=Naive | spacer_cation=FPEA |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0238` = 3.5e+09 ns | 100% | device_type=FTJ, architecture=Naive | spacer_cation=FBZA |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0318` = 1.116e+14 ns | 100% | device_type=FTJ, architecture=Naive | method=Random sampling, dataset=600,000-sample Moir´e dataset |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0321` = 4.14e+12 ns | 100% | device_type=FTJ, architecture=Naive | method=FruBO with CatBoost, dataset=600,000-sample Moir´e dataset |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0323` = 2.592e+14 ns | 100% | device_type=FTJ, architecture=Naive | demagnetization_protocol=AC demagnetization |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Naive | illumination=random speckle illumination |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Naive | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0073` = 0.0004 ns | 100% | device_type=FTJ, architecture=Naive | material=ITO film |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Naive | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0059` = 4.629e+10 ns | 100% | device_type=FTJ, architecture=Naive | step_interval=750 phase-field Euler steps |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0060` = 1.11e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=deterministic U-Net, step_interval=750 phase-field Euler steps, hardware=single AMD MI250X Graphics Compute Die (GCD) of LUMI |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0061` = 6.34e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=VP-DDBM using five DBIM network evaluations, step_interval=750 phase-field Euler steps, hardware=single AMD MI250X Graphics Compute Die (GCD) of LUMI |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0069` = 9.166e+10 ns | 100% | device_type=FTJ, architecture=Naive | image_size=2000*2000 pixels, layers=160, algorithm=iterative SFF algorithm, cpu=AMD Ryzen 5 3600X CPU |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0130` = 1.036e+07 ns | 100% | device_type=FTJ, architecture=Merged | device=NVIDIA GeForce RTX 5080, form=direct, decode=ALU |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0131` = 1.115e+07 ns | 100% | device_type=FTJ, architecture=Merged | device=NVIDIA GeForce RTX 5080, form=hoisted, decode=LUT |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0153` = 3.72e+09 ns | 100% | device_type=FTJ, architecture=Merged | component=FIGFLEX, benchmark=Llama-3.1-8B |

_and 1975 more_

## `voltage` (99 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0247` = -1.96 V | `CLM-MEM-0011` = 2.32 V | 184% | substituent=−H | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0247` = -1.96 V | 178% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | substituent=−H |
| `CLM-MAT-0099` = 0.53 V | `CLM-MAT-0247` = -1.96 V | 127% | charging_voltage=0.6 V versus Ag/AgCl | substituent=−H |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0247` = -1.96 V | 124% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | substituent=−H |
| `CLM-MAT-0100` = 0.38 V | `CLM-MAT-0247` = -1.96 V | 119% | charging_voltage=0.6 V versus Ag/AgCl | substituent=−H |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0247` = -1.96 V | 115% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | substituent=−H |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0247` = -1.96 V | 102% | incident_peak_electric_field=150 kV/cm | substituent=−H |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | incident_peak_electric_field=150 kV/cm | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | incident_peak_electric_field=150 kV/cm | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0099` = 0.53 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0100` = 0.38 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0240` = 0.9 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−F |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0241` = 1.4 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−I |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0242` = 1.95 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−Cl |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0243` = 1.1 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−ONO2 |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0244` = 1.4 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−ONO |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0245` = 1.63 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−OSO2CF3 |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0246` = 1.99 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−O (BA) |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0247` = -1.96 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | substituent=−H |
| `CLM-MAT-0099` = 0.53 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | charging_voltage=0.6 V versus Ag/AgCl | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0100` = 0.38 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | charging_voltage=0.6 V versus Ag/AgCl | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0240` = 0.9 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−F | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0241` = 1.4 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−I | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0242` = 1.95 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−Cl | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0243` = 1.1 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−ONO2 | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0244` = 1.4 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−ONO | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0245` = 1.63 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−OSO2CF3 | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0246` = 1.99 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−O (BA) | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0247` = -1.96 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | substituent=−H | operating_condition=transverse open-circuit conditions |
| `CLM-MAT-0270` = 2.94e-06 V | `CLM-MEM-0011` = 2.32 V | 100% | operating_condition=transverse open-circuit conditions | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0100` = 0.38 V | 100% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0067` = 0.47 V | 99% | incident_peak_electric_field=150 kV/cm | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0099` = 0.53 V | 99% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0240` = 0.9 V | 99% | incident_peak_electric_field=150 kV/cm | substituent=−F |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0243` = 1.1 V | 99% | incident_peak_electric_field=150 kV/cm | substituent=−ONO2 |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0241` = 1.4 V | 98% | incident_peak_electric_field=150 kV/cm | substituent=−I |

_and 59 more_

## `wavelength` (253 pair(s))

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

_and 213 more_
