# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**3098 pair(s)** as of 2026-10-12.

## `current` (7 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0028` = 0.6 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | process_step=current ramp-down | temperature=10 mK |
| `CLM-DEV-0057` = 30 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=small switching current | temperature=10 mK |
| `CLM-DEV-0058` = 40 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=large switching current | temperature=10 mK |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0058` = 40 mA | 99% | temperature=2 K, state=after light irradiation | switching_regime=large switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0058` = 40 mA | 98% | process_step=current ramp-down | switching_regime=large switching current |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0057` = 30 mA | 98% | temperature=2 K, state=after light irradiation | switching_regime=small switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0057` = 30 mA | 98% | process_step=current ramp-down | switching_regime=small switching current |

## `energy` (144 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
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
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0114` = 0.13 meV | 100% | defect_complex=VAl(ON)3 | material=WSe2 |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0114` = 0.13 meV | 100% | defect_complex=VAl(ON)3, model=DFT | material=WSe2 |
| `CLM-MAT-0013` = 1340 meV | `CLM-MAT-0114` = 0.13 meV | 100% | synthesis_condition=Nitrogen-rich | material=WSe2 |
| `CLM-MAT-0014` = 1940 meV | `CLM-MAT-0114` = 0.13 meV | 100% | synthesis_condition=Nitrogen-rich | material=WSe2 |
| `CLM-MAT-0015` = 1980 meV | `CLM-MAT-0114` = 0.13 meV | 100% | synthesis_condition=Nitrogen-rich | material=WSe2 |
| `CLM-MAT-0016` = 2020 meV | `CLM-MAT-0114` = 0.13 meV | 100% | synthesis_condition=Nitrogen-rich | material=WSe2 |
| `CLM-MAT-0051` = 1801 meV | `CLM-MAT-0114` = 0.13 meV | 100% | axis=c | material=WSe2 |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0115` = 2.22 meV | 100% | defect_complex=VAl(ON)3 | state=3p |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0115` = 2.22 meV | 100% | defect_complex=VAl(ON)3, model=DFT | state=3p |
| `CLM-MAT-0002` = 200 meV | `CLM-MAT-0114` = 0.13 meV | 100% | mechanism=optical phonon | material=WSe2 |
| `CLM-MAT-0104` = 220 meV | `CLM-MAT-0114` = 0.13 meV | 100% | measurement=RIXS, absorption_edge=Fe L3 edge | material=WSe2 |
| `CLM-MAT-0014` = 1940 meV | `CLM-MAT-0115` = 2.22 meV | 100% | synthesis_condition=Nitrogen-rich | state=3p |
| `CLM-MAT-0015` = 1980 meV | `CLM-MAT-0115` = 2.22 meV | 100% | synthesis_condition=Nitrogen-rich | state=3p |
| `CLM-MAT-0016` = 2020 meV | `CLM-MAT-0115` = 2.22 meV | 100% | synthesis_condition=Nitrogen-rich | state=3p |
| `CLM-MAT-0051` = 1801 meV | `CLM-MAT-0115` = 2.22 meV | 100% | axis=c | state=3p |
| `CLM-MAT-0013` = 1340 meV | `CLM-MAT-0115` = 2.22 meV | 100% | synthesis_condition=Nitrogen-rich | state=3p |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MAT-0114` = 0.13 meV | 100% | mechanism=surface polar phonon, substrate=SiO2 | material=WSe2 |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0113` = 15.9 meV | 100% | defect_complex=VAl(ON)3, model=DFT | method=three-band nearest-neighbor exciton-geometric calculation |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0113` = 15.9 meV | 100% | defect_complex=VAl(ON)3 | method=three-band nearest-neighbor exciton-geometric calculation |
| `CLM-MAT-0049` = 296 meV | `CLM-MAT-0115` = 2.22 meV | 99% | material=LiFePO4 | state=3p |
| `CLM-MAT-0016` = 2020 meV | `CLM-MAT-0113` = 15.9 meV | 99% | synthesis_condition=Nitrogen-rich | method=three-band nearest-neighbor exciton-geometric calculation |
| `CLM-MAT-0015` = 1980 meV | `CLM-MAT-0113` = 15.9 meV | 99% | synthesis_condition=Nitrogen-rich | method=three-band nearest-neighbor exciton-geometric calculation |

_and 104 more_

## `energy_advantage_ratio` (5 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0016` = 1.22 x | `CLM-ARCH-0022` = 169.1 x | 99% | device=B200, benchmark=GroupGEMM | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0005` = 1.32 x | `CLM-ARCH-0022` = 169.1 x | 99% | process=TSMC 16nm FinFET, comparison=sinusoidal vs trapezoidal power-clock, gate_at_maximum=XOR/XNOR, vclk_at_maximum=0.5 V, fclk_at_maximum=384 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0004` = 3.83 x | `CLM-ARCH-0022` = 169.1 x | 98% | process=TSMC 16nm FinFET, comparison=single-gate PFAL vs static CMOS, power_clock=trapezoidal, operating_point=minimum-energy points of the parameter sweep (Table 2) | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0002` = 5 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=PFAL vs static CMOS, operating_point=most favorable operating point, vclk=1 V, fclk=100 MHz | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |
| `CLM-ARCH-0006` = 5.3 x | `CLM-ARCH-0022` = 169.1 x | 97% | process=TSMC 16nm FinFET, comparison=4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock=triangular | platform=projected IMAX configuration, metric_scope=modeled end-to-end energy per batch |

## `frequency` (139 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-DEV-0012` = 370 GHz | 100% | platform=integrated phononic device | magnetic_field=8.1 T, frequency=1.9 THz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-DEV-0013` = 180 GHz | 100% | platform=integrated phononic device | magnetic_field=7.5 T, frequency=2.2 THz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0001` = 18.98 GHz | 100% | platform=integrated phononic device | component=single ring cavity, parameter=FSR |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0003` = 15.41 GHz | 100% | platform=integrated phononic device | component=photonic molecule, mode_spacing=Ω2 |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0036` = 121 GHz | 100% | platform=integrated phononic device | sample_size=22 measured devices |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0049` = 267 GHz | 100% | platform=integrated phononic device | signal_type=measured phase noise |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | platform=integrated phononic device | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0051` = 230 GHz | 100% | platform=integrated phononic device | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0052` = 320 GHz | 100% | platform=integrated phononic device | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0070` = 0.556 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | process_node=TSMC 28 nm | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0073` = 0.5 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | process=45 nm | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0024` = 0.03 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | angle_of_incidence=0° to 30°, rotation_angle=90° | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-PHOT-0036` = 121 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | sample_size=22 measured devices | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0049` = 267 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | signal_type=measured phase noise | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0050` = 1.94e+05 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | component=stabilized CW laser, frequency_offset=10 kHz | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0050` = 1.94e+05 GHz | `CLM-PHOT-0060` = 6.89 GHz | 100% | component=stabilized CW laser, frequency_offset=10 kHz | lattice_constant=17 mm, material=YIG |
| `CLM-PHOT-0050` = 1.94e+05 GHz | `CLM-PHOT-0061` = 7.48 GHz | 100% | component=stabilized CW laser, frequency_offset=10 kHz | corner_radius=1.4 mm |
| `CLM-PHOT-0051` = 230 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | frequency_offset=10 kHz, signal_type=measured phase-noise levels | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0052` = 320 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | frequency_offset=10 kHz, signal_type=measured phase-noise levels | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | platform=optical PPLN module | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0060` = 6.89 GHz | 100% | platform=integrated phononic device | lattice_constant=17 mm, material=YIG |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0061` = 7.48 GHz | 100% | platform=integrated phononic device | corner_radius=1.4 mm |
| `CLM-DEV-0012` = 370 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | magnetic_field=8.1 T, frequency=1.9 THz | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0024` = 0.03 GHz | `CLM-PHOT-0049` = 267 GHz | 100% | angle_of_incidence=0° to 30°, rotation_angle=90° | signal_type=measured phase noise |
| `CLM-PHOT-0024` = 0.03 GHz | `CLM-PHOT-0051` = 230 GHz | 100% | angle_of_incidence=0° to 30°, rotation_angle=90° | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-PHOT-0024` = 0.03 GHz | `CLM-PHOT-0052` = 320 GHz | 100% | angle_of_incidence=0° to 30°, rotation_angle=90° | frequency_offset=10 kHz, signal_type=measured phase-noise levels |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | platform=optical PPLN module | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-PHOT-0002` = 3.57 GHz | 100% | platform=integrated phononic device | component=photonic molecule, mode_spacing=Ω1 |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | angle_of_incidence=0° to 30°, rotation_angle=90° |
| `CLM-PHOT-0024` = 0.03 GHz | `CLM-PHOT-0036` = 121 GHz | 100% | angle_of_incidence=0° to 30°, rotation_angle=90° | sample_size=22 measured devices |
| `CLM-PHOT-0001` = 18.98 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | component=single ring cavity, parameter=FSR | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0003` = 15.41 GHz | `CLM-PHOT-0056` = 0.0048 GHz | 100% | component=photonic molecule, mode_spacing=Ω2 | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0036` = 121 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | sample_size=22 measured devices | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-PHOT-0056` = 0.0048 GHz | `CLM-PHOT-0061` = 7.48 GHz | 100% | device=Ho3+-doped fluoride glass waveguide laser | corner_radius=1.4 mm |
| `CLM-PHOT-0056` = 0.0048 GHz | `CLM-PHOT-0060` = 6.89 GHz | 100% | device=Ho3+-doped fluoride glass waveguide laser | lattice_constant=17 mm, material=YIG |
| `CLM-DEV-0013` = 180 GHz | `CLM-PHOT-0050` = 1.94e+05 GHz | 100% | magnetic_field=7.5 T, frequency=2.2 THz | component=stabilized CW laser, frequency_offset=10 kHz |
| `CLM-ARCH-0043` = 0.0006 GHz | `CLM-ARCH-0070` = 0.556 GHz | 100% | platform=integrated phononic device | process_node=TSMC 28 nm |
| `CLM-ARCH-0042` = 25.9 GHz | `CLM-PHOT-0024` = 0.03 GHz | 100% | platform=optical PPLN module | angle_of_incidence=0° to 30°, rotation_angle=90° |

_and 99 more_

## `length_device` (896 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0053` = 1.61 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | parameter=ts | material=GaN, growth_method=ammonothermal |
| `CLM-DEV-0053` = 1.61 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | parameter=ts | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0004` = 7000 nm | 100% | material=Sb monolayer on SiC(0001) | parameter=signal-ground electrode spacing |
| `CLM-MAT-0017` = 0.284 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=Sb monolayer on SiC(0001) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0004` = 7000 nm | 100% | material=Sb monolayer on SiC(0001) | parameter=signal-ground electrode spacing |
| `CLM-MAT-0018` = 0.327 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=Sb monolayer on SiC(0001) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0020` = 6.4 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | regime=partially-reconstructed | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0020` = 6.4 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | regime=partially-reconstructed | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0023` = 3.5 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | state=X2sA | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0023` = 3.5 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | state=X2sA | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0024` = 6.4 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | state=X2sA | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0024` = 6.4 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | state=X2sA | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0029` = 0.5291 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=bulk CeN | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0040` = 0.5 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0040` = 0.5 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | fermi_velocity=7×105 ms−1, model=Drude model | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0059` = 1000 nm | `CLM-PHOT-0057` = 0.024 nm | 100% | region=pristine zone, temperature=1.5 K | measurement_duration=exceeding 15.5 hours |
| `CLM-MAT-0063` = 10.7 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | device=D1 | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0068` = 14.5 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | method=estimated from the carrier density at the SDP | material=GaN, growth_method=ammonothermal |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-MAT-0097` = 1.915 nm | 100% | material=GaN, growth_method=ammonothermal | feature=alternating stacking of PEDOT and PSS |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-MAT-0098` = 2.172 nm | 100% | material=GaN, growth_method=ammonothermal | feature=alternating stacking of PEDOT and PSS |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PHOT-0007` = 0.23 nm | 100% | material=GaN, growth_method=ammonothermal | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PHOT-0008` = 0.33 nm | 100% | material=GaN, growth_method=ammonothermal | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PHOT-0009` = 1.7 nm | 100% | material=GaN, growth_method=ammonothermal | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PHOT-0010` = 2.1 nm | 100% | material=GaN, growth_method=ammonothermal | roughness_type=root mean square roughness (Sq), sample=after MoSx film deposition |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PHOT-0057` = 0.024 nm | 100% | material=GaN, growth_method=ammonothermal | measurement_duration=exceeding 15.5 hours |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PROC-0003` = 0.068 nm | 100% | material=GaN, growth_method=ammonothermal | defocus=30 nm |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PROC-0011` = 3.2 nm | 100% | material=GaN, growth_method=ammonothermal | feature=amorphous-layer thickness |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PROC-0012` = 5 nm | 100% | material=GaN, growth_method=ammonothermal | feature=amorphous-layer thickness |
| `CLM-MAT-0076` = 3.4e+05 nm | `CLM-PROC-0013` = 7 nm | 100% | material=GaN, growth_method=ammonothermal | feature=amorphous-layer thickness |
| `CLM-MAT-0081` = 0.98 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | material=CrSb | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0097` = 1.915 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | feature=alternating stacking of PEDOT and PSS | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-MAT-0098` = 2.172 nm | `CLM-PHOT-0042` = 1.6e+05 nm | 100% | feature=alternating stacking of PEDOT and PSS | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0007` = 0.00023 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0008` = 0.00033 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0057` = 2.4e-05 um | 100% | parameter=signal-ground electrode spacing | measurement_duration=exceeding 15.5 hours |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0003` = 6.8e-05 um | 100% | parameter=signal-ground electrode spacing | defocus=30 nm |
| `CLM-PHOT-0004` = 7 um | `CLM-PROC-0004` = 7.7e-05 um | 100% | parameter=signal-ground electrode spacing | material=HEA-NP, defocus=0 nm |
| `CLM-PHOT-0007` = 0.00023 um | `CLM-PHOT-0042` = 160 um | 100% | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-PHOT-0008` = 0.00033 um | `CLM-PHOT-0042` = 160 um | 100% | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) | substrate_material=glass cover slip, sample_type=flat surface |
| `CLM-PHOT-0009` = 0.0017 um | `CLM-PHOT-0042` = 160 um | 100% | roughness_type=arithmetic average roughness (Sa), sample=after MoSx film deposition | substrate_material=glass cover slip, sample_type=flat surface |

_and 856 more_

## `power` (59 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0007` = 40.4 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0037` = 787 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=synthesized SRAM-PIM subsystem | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0038` = 9599 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=added compute and buffer logic in HBM-PIM | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | process_node=TSMC 28 nm | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-DEV-0025` = 1 W | `CLM-EDA-0002` = 1.06e-07 W | 100% | gate_bias_vgs=-2.7 V | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-DEV-0030` = 7.76 W | `CLM-EDA-0002` = 1.06e-07 W | 100% | mode=DC-AC conversion, vin=24-V DC input | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-EDA-0002` = 1.06e-07 W | `CLM-MAT-0106` = 0.002412 W | 100% | benchmark_circuit=BGR, framework=AgenticSizing | wavelength=405 nm |
| `CLM-EDA-0002` = 1.06e-07 W | `CLM-PHOT-0053` = 0.0217 W | 100% | benchmark_circuit=BGR, framework=AgenticSizing | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-EDA-0002` = 1.06e-07 W | `CLM-PHOT-0054` = 0.1325 W | 100% | benchmark_circuit=BGR, framework=AgenticSizing | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0038` = 9599 mW | `CLM-MAT-0106` = 2.412 mW | 100% | component=added compute and buffer logic in HBM-PIM | wavelength=405 nm |
| `CLM-DEV-0030` = 7.76 W | `CLM-MAT-0106` = 0.002412 W | 100% | mode=DC-AC conversion, vin=24-V DC input | wavelength=405 nm |
| `CLM-ARCH-0038` = 9599 mW | `CLM-PHOT-0053` = 21.7 mW | 100% | component=added compute and buffer logic in HBM-PIM | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0025` = 1 W | `CLM-MAT-0106` = 0.002412 W | 100% | gate_bias_vgs=-2.7 V | wavelength=405 nm |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-ARCH-0038` = 9599 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | component=added compute and buffer logic in HBM-PIM |
| `CLM-DEV-0030` = 7.76 W | `CLM-PHOT-0053` = 0.0217 W | 100% | mode=DC-AC conversion, vin=24-V DC input | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0037` = 787 mW | `CLM-MAT-0106` = 2.412 mW | 100% | component=synthesized SRAM-PIM subsystem | wavelength=405 nm |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-ARCH-0038` = 9599 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | component=added compute and buffer logic in HBM-PIM |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-DEV-0030` = 7760 mW | 100% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | mode=DC-AC conversion, vin=24-V DC input |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-DEV-0030` = 7760 mW | 100% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | mode=DC-AC conversion, vin=24-V DC input |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-DEV-0030` = 7760 mW | 99% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | mode=DC-AC conversion, vin=24-V DC input |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-MAT-0106` = 2.412 mW | 99% | process_node=TSMC 28 nm | wavelength=405 nm |
| `CLM-ARCH-0038` = 9599 mW | `CLM-PHOT-0054` = 132.5 mW | 99% | component=added compute and buffer logic in HBM-PIM | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0030` = 7.76 W | `CLM-PHOT-0054` = 0.1325 W | 98% | mode=DC-AC conversion, vin=24-V DC input | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-MAT-0106` = 0.002412 W | `CLM-PHOT-0054` = 0.1325 W | 98% | wavelength=405 nm | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-DEV-0025` = 1 W | `CLM-PHOT-0053` = 0.0217 W | 98% | gate_bias_vgs=-2.7 V | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-DEV-0025` = 1000 mW | 97% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | gate_bias_vgs=-2.7 V |
| `CLM-ARCH-0037` = 787 mW | `CLM-PHOT-0053` = 21.7 mW | 97% | component=synthesized SRAM-PIM subsystem | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-DEV-0025` = 1000 mW | 97% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | gate_bias_vgs=-2.7 V |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-ARCH-0037` = 787 mW | 97% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | component=synthesized SRAM-PIM subsystem |
| `CLM-ARCH-0038` = 9599 mW | `CLM-ARCH-0071` = 370.1 mW | 96% | component=added compute and buffer logic in HBM-PIM | process_node=TSMC 28 nm |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-DEV-0025` = 1000 mW | 96% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | gate_bias_vgs=-2.7 V |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-ARCH-0037` = 787 mW | 96% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | component=synthesized SRAM-PIM subsystem |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-DEV-0030` = 7760 mW | 95% | process_node=TSMC 28 nm | mode=DC-AC conversion, vin=24-V DC input |
| `CLM-ARCH-0071` = 370.1 mW | `CLM-PHOT-0053` = 21.7 mW | 94% | process_node=TSMC 28 nm | pump_power=825 mW, device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-ARCH-0007` = 40.4 mW | `CLM-MAT-0106` = 2.412 mW | 94% | component=1024-MAC Systolic Array, architecture=MiX-INT4g16, array_size=1024-MAC, process=28nm, frequency=500 MHz | wavelength=405 nm |
| `CLM-ARCH-0009` = 26.8 mW | `CLM-ARCH-0071` = 370.1 mW | 93% | architecture=MiX-INT4, array_size=512-MAC, process=28nm, frequency=500 MHz | process_node=TSMC 28 nm |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-MAT-0106` = 2.412 mW | 92% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | wavelength=405 nm |
| `CLM-ARCH-0008` = 31.8 mW | `CLM-ARCH-0071` = 370.1 mW | 91% | architecture=MiX-INT4g16, array_size=512-MAC, process=28nm, frequency=500 MHz | process_node=TSMC 28 nm |

_and 19 more_

## `relative_deviation` (1569 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-EDA-0003` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | benchmark_circuit=LDO benchmark, framework=proposed method | sample=B1-1 |
| `CLM-EDA-0004` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | circuit=most complex circuit, framework=proposed framework | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0112` = 66.8 percent | 190% | sample=B1-1 | baseline=pure two-dimensional Coulomb reference, benchmark_protocol=high-field-calibrated |
| `CLM-EDA-0007` = 76 percent | `CLM-MAT-0111` = -60 percent | 179% | model=Non-cyclic + Node prediction model | sample=B1-1 |
| `CLM-ARCH-0049` = 46 percent | `CLM-MAT-0111` = -60 percent | 177% | mechanism=uniform iteration offsets | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0005` = 85 percent | 171% | sample=B1-1 | dataset=Iris test set |
| `CLM-EDA-0005` = 86.4 percent | `CLM-MAT-0111` = -60 percent | 169% | model=Cyclic Edge prediction model | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0006` = 88 percent | 168% | sample=B1-1 | dataset=MNIST, setup=experimental system |
| `CLM-EDA-0006` = 89.6 percent | `CLM-MAT-0111` = -60 percent | 167% | model=Non-cyclic Edge prediction model | sample=B1-1 |
| `CLM-ARCH-0041` = 93.08 percent | `CLM-MAT-0111` = -60 percent | 164% | frequency=7 GHz | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0059` = 94.4 percent | 164% | sample=B1-1 | route=Fourier route |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0012` = 95 percent | 163% | sample=B1-1 | encoding_scheme=differential encoding, benchmark=MNIST |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0063` = 37 percent | 162% | sample=B1-1 | disorder_type=radius disorder |
| `CLM-ARCH-0077` = 36.86 percent | `CLM-MAT-0111` = -60 percent | 161% | framework=RAPID-DNN, fault_configuration=mixed random fault configuration, baseline=fault-agnostic baseline | sample=B1-1 |
| `CLM-ARCH-0040` = 97.93 percent | `CLM-MAT-0111` = -60 percent | 161% | frequency=7 GHz, component=graded magnetic spacer | sample=B1-1 |
| `CLM-ARCH-0018` = 98 percent | `CLM-MAT-0111` = -60 percent | 161% | concurrency_n_a=48, set_type=hot set | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0116` = 100 percent | 160% | sample=B1-1 | system=2D square-lattice tight-binding model |
| `CLM-ARCH-0084` = 34 percent | `CLM-MAT-0111` = -60 percent | 157% | platform=Arrow, application=Sparse point cloud processing | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0064` = 31 percent | 152% | sample=B1-1 | disorder_type=radius disorder |
| `CLM-ARCH-0053` = 27.3 percent | `CLM-MAT-0111` = -60 percent | 146% | architecture=PEEK with four Rockets upon a BOOM, baseline=unsafe baseline | sample=B1-1 |
| `CLM-ARCH-0046` = 26.3 percent | `CLM-MAT-0111` = -60 percent | 144% | design=ZTA-Q, resource_type=LUT | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0062` = 25 percent | 142% | sample=B1-1 | disorder_type=position disorder, corner_radius_ratio=0.45r |
| `CLM-ARCH-0048` = 150 percent | `CLM-MAT-0111` = -60 percent | 140% | design=ZTA-Q, resource_type=DSP | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0021` = 162 percent | 137% | sample=B1-1 | material=polycrystalline rolled Au, measurement_type=10-times continuous measurement |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0024` = 184 percent | 133% | sample=B1-1 | material=polycrystalline rolled Au |
| `CLM-ARCH-0083` = 18 percent | `CLM-MAT-0111` = -60 percent | 130% | platform=Arrow, application=OpenVINO GenAI | sample=B1-1 |
| `CLM-ARCH-0080` = 207 percent | `CLM-MAT-0111` = -60 percent | 129% | platform=Arrow, coherence=CC | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0022` = 215 percent | 128% | sample=B1-1 | material=polycrystalline rolled Au, measurement_type=10-times continuous measurement |
| `CLM-ARCH-0081` = 16 percent | `CLM-MAT-0111` = -60 percent | 127% | platform=Orin, workload=L2-optimized GEMM, cache_policy=UC | sample=B1-1 |
| `CLM-ARCH-0082` = 16 percent | `CLM-MAT-0111` = -60 percent | 127% | platform=Arrow, application=OpenCV, variant=Cv+Opt | sample=B1-1 |
| `CLM-ARCH-0044` = 14.3 percent | `CLM-MAT-0111` = -60 percent | 124% | process=IHP 130 nm, channel_count=8 | sample=B1-1 |
| `CLM-ARCH-0086` = 14 percent | `CLM-MAT-0111` = -60 percent | 123% | platform=Orin, application=Demand Layering, variant=DL+Opt | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0026` = 13.2 percent | 122% | sample=B1-1 | material=WS2 |
| `CLM-ARCH-0047` = 12.6 percent | `CLM-MAT-0111` = -60 percent | 121% | design=ZTA-Q, resource_type=register | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0028` = 12.5 percent | 121% | sample=B1-1 | model=ttWS2 simulation model |
| `CLM-ARCH-0069` = 318 percent | `CLM-MAT-0111` = -60 percent | 119% | baseline=reference Cortex-M0 implementation | sample=B1-1 |
| `CLM-ARCH-0085` = 11 percent | `CLM-MAT-0111` = -60 percent | 118% | workload=10-token prefill | sample=B1-1 |
| `CLM-ARCH-0068` = 352 percent | `CLM-MAT-0111` = -60 percent | 117% | baseline=reference Cortex-M0 implementation | sample=B1-1 |
| `CLM-ARCH-0087` = 8 percent | `CLM-MAT-0111` = -60 percent | 113% | platform=NVIDIA DGX Spark, operation=GPU Read-Alone, cache_policy=WB, coherence=two-way CC | sample=B1-1 |
| `CLM-MAT-0083` = 530 percent | `CLM-MAT-0111` = -60 percent | 111% | n=40, method=spin-restricted TAO-LDA | sample=B1-1 |

_and 1529 more_

## `temperature` (63 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0092` = -23.15 degC | 191% | temperature_control_system=VAHEAT system | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0004` = -73.15 degC | 189% | time_after_cooling_onset=10 s | calculation=optical phonon and surface polar phonon scattering |
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
| `CLM-MAT-0092` = 250 K | `CLM-MAT-0102` = -81 K | 132% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0092` = -23.15 degC | 128% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0092` = -23.15 degC | 127% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-MAT-0102` = -81 K | `CLM-PROC-0001` = 300 K | 127% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | thermal_model=Debye model |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0102` = -354.1 degC | 124% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-MAT-0093` = 350 K | `CLM-MAT-0102` = -81 K | 123% | magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0102` = -354.1 degC | 123% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0091` = -113.1 degC | 122% | temperature_control_system=VAHEAT system | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0003` = -123.1 degC | 121% | temperature_control_system=VAHEAT system | calculation=acoustic phonon scattering |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0101` = -155.1 degC | 116% | temperature_control_system=VAHEAT system | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0053` = 503.1 K | `CLM-MAT-0102` = -81 K | 116% | synthesis_approach=phosphine-free colloidal approach | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0035` = -204.1 degC | `CLM-PROC-0001` = 26.85 degC | 113% | relaxation_temperature=TLIESST | thermal_model=Debye model |
| `CLM-DEV-0017` = 25.35 degC | `CLM-DEV-0035` = -204.1 degC | 112% | temperature_control_system=VAHEAT system | relaxation_temperature=TLIESST |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0102` = -354.1 degC | 107% | temperature_control_system=VAHEAT system | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0053` = 230 degC | 89% | temperature_control_system=VAHEAT system | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0092` = -23.15 degC | 89% | relaxation_temperature=TLIESST | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-MAT-0053` = 503.1 K | `CLM-MAT-0101` = 118 K | 77% | synthesis_approach=phosphine-free colloidal approach | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0003` = 150 K | `CLM-MAT-0053` = 503.1 K | 70% | calculation=acoustic phonon scattering | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0017` = 25.35 degC | `CLM-DEV-0033` = 84.85 degC | 70% | temperature_control_system=VAHEAT system | time_after_cooling_onset=10 s |
| `CLM-DEV-0017` = 25.35 degC | `CLM-DEV-0032` = 81.85 degC | 69% | temperature_control_system=VAHEAT system | time_after_cooling_onset=10 s |
| `CLM-DEV-0033` = 84.85 degC | `CLM-PROC-0001` = 26.85 degC | 68% | time_after_cooling_onset=10 s | thermal_model=Debye model |
| `CLM-MAT-0053` = 503.1 K | `CLM-MAT-0091` = 160 K | 68% | synthesis_approach=phosphine-free colloidal approach | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0032` = 81.85 degC | `CLM-PROC-0001` = 26.85 degC | 67% | time_after_cooling_onset=10 s | thermal_model=Debye model |

_and 23 more_

## `temperature_delta` (3 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0024` = 30.4 K | `CLM-PHOT-0037` = 0.11 K | 100% | gate_bias_vgs=-2.7 V | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0034` = 3 K | `CLM-PHOT-0037` = 0.11 K | 96% | time_after_cooling_onset=10 s | cavity_length=20 µm, beam_shape=circular, incident_power=1.09 mW |
| `CLM-DEV-0024` = 30.4 K | `CLM-DEV-0034` = 3 K | 90% | gate_bias_vgs=-2.7 V | time_after_cooling_onset=10 s |

## `thermal_conductivity` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |

## `time` (173 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Naive | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Naive | illumination=random speckle illumination |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Naive | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Naive | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Naive | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0013` = 162 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Merged | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Merged | illumination=random speckle illumination |
| `CLM-ARCH-0013` = 162 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Merged | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0013` = 162 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Merged | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0013` = 162 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Merged | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0020` = 1.4e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-ARCH-0021` = 2.7e+07 ns | 100% | device_type=FTJ, architecture=Symmetry | concurrency_n_a=128, design=our design with tiering |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PHOT-0025` = 4e+06 ns | 100% | device_type=FTJ, architecture=Symmetry | illumination=random speckle illumination |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | device_type=FTJ, architecture=Symmetry | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | device_type=FTJ, architecture=Symmetry | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0014` = 153.5 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | device_type=FTJ, architecture=Symmetry | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0019` = 8.4e+04 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | concurrency_n_a=48, memory_tier=HBF, component=HBF tiering resume/access latency overhead | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0020` = 1.4e+07 ns | `CLM-MAT-0035` = 200 ns | 100% | concurrency_n_a=48, design=our design with tiering, component=end-to-end time-between-tokens (TBT) | illumination=one sun |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-DEV-0051` = 1321 ns | 100% | concurrency_n_a=128, design=our design with tiering | frequency=146 MHz |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | concurrency_n_a=128, design=our design with tiering | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-MAT-0035` = 200 ns | 100% | concurrency_n_a=128, design=our design with tiering | illumination=one sun |
| `CLM-ARCH-0021` = 2.7e+07 ns | `CLM-MAT-0036` = 750 ns | 100% | concurrency_n_a=128, design=our design with tiering | illumination=one sun |
| `CLM-ARCH-0054` = 4000 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | architecture=PEEK | algorithm=DBS, cores=128 cores |
| `CLM-ARCH-0054` = 4000 ns | `CLM-PKG-0002` = 2.499e+08 ns | 100% | architecture=PEEK | model=Qwen3-1.7B, channels=16 channels, erase_latency=2000 µs |
| `CLM-ARCH-0054` = 4000 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | architecture=PEEK | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-ARCH-0074` = 1.66e+07 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | architecture=eight-output accelerator with shared activation delivery | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-ARCH-0074` = 1.66e+07 ns | `CLM-MAT-0035` = 200 ns | 100% | architecture=eight-output accelerator with shared activation delivery | illumination=one sun |
| `CLM-ARCH-0074` = 1.66e+07 ns | `CLM-MAT-0036` = 750 ns | 100% | architecture=eight-output accelerator with shared activation delivery | illumination=one sun |
| `CLM-DEV-0021` = 1.504e+06 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | mode=1, character=thermal (mount), operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-DEV-0021` = 1.504e+06 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | mode=1, character=thermal (mount), operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | algorithm=DBS, cores=128 cores |
| `CLM-DEV-0022` = 1.46e+04 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | mode=3, character=trap, linearized, operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-DEV-0022` = 1.46e+04 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | mode=3, character=trap, linearized, operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | algorithm=DBS, cores=128 cores |
| `CLM-DEV-0022` = 1.46e+04 ns | `CLM-PROC-0005` = 5.79e+09 ns | 100% | mode=3, character=trap, linearized, operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | hardware=NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type=full-resolution implementation |
| `CLM-DEV-0023` = 6010 ns | `CLM-MAT-0005` = 0.0061 ns | 100% | mode=4, character=thermal (channel), operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | material=monolayer MoS2, temperature=300 K, excitation_energy=1.7 eV |
| `CLM-DEV-0023` = 6010 ns | `CLM-PHOT-0048` = 8.29e+10 ns | 100% | mode=4, character=thermal (channel), operating_point=Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V | algorithm=DBS, cores=128 cores |

_and 133 more_

## `voltage` (16 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | incident_peak_electric_field=150 kV/cm | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0099` = 0.53 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-MAT-0100` = 0.38 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0100` = 0.38 V | 100% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0099` = 0.53 V | 99% | incident_peak_electric_field=150 kV/cm | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0027` = 1.53 V | 98% | incident_peak_electric_field=150 kV/cm | device_type=VO2 thin film device, temperature=330 K, transition_type=reset |
| `CLM-DEV-0006` = 85 V | `CLM-MEM-0011` = 2.32 V | 97% | incident_peak_electric_field=150 kV/cm | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0100` = 0.38 V | 97% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0099` = 0.53 V | 96% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0006` = 85 V | `CLM-DEV-0026` = 12.65 V | 85% | incident_peak_electric_field=150 kV/cm | device_type=VO2 thin film device, temperature=330 K, transition_type=set |
| `CLM-MAT-0100` = 0.38 V | `CLM-MEM-0011` = 2.32 V | 84% | charging_voltage=0.6 V versus Ag/AgCl | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0026` = 12.65 V | `CLM-MEM-0011` = 2.32 V | 82% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-MAT-0099` = 0.53 V | `CLM-MEM-0011` = 2.32 V | 77% | charging_voltage=0.6 V versus Ag/AgCl | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0100` = 0.38 V | 75% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0099` = 0.53 V | 65% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | charging_voltage=0.6 V versus Ag/AgCl |
| `CLM-DEV-0027` = 1.53 V | `CLM-MEM-0011` = 2.32 V | 34% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |

## `wavelength` (23 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0033` = 0.00315 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0033` = 0.00315 um | `CLM-PHOT-0055` = 2.062 um | 100% | excitation_wavelength=532 nm, cumulative_exposure_time=5 h | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0028` = 0.0167 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | component=integrated microheater |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0028` = 0.0167 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | component=integrated microheater |
| `CLM-PHOT-0033` = 0.00315 um | `CLM-PHOT-0040` = 0.785 um | 100% | excitation_wavelength=532 nm, cumulative_exposure_time=5 h | source=diode laser |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0028` = 0.0167 um | 99% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | component=integrated microheater |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0028` = 0.0167 um | 99% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | component=integrated microheater |
| `CLM-PHOT-0028` = 0.0167 um | `CLM-PHOT-0055` = 2.062 um | 99% | component=integrated microheater | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0029` = 0.3 um | `CLM-PHOT-0033` = 0.00315 um | 99% | component=9-channel ultra-broadband WDM DETRX, spectral_range=O-to-C band | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0028` = 0.0167 um | `CLM-PHOT-0040` = 0.785 um | 98% | component=integrated microheater | source=diode laser |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0040` = 0.785 um | 88% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | source=diode laser |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0040` = 0.785 um | 88% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | source=diode laser |
| `CLM-PHOT-0028` = 0.0167 um | `CLM-PHOT-0033` = 0.00315 um | 81% | component=integrated microheater | excitation_wavelength=532 nm, cumulative_exposure_time=5 h |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0040` = 0.785 um | 76% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | source=diode laser |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0040` = 0.785 um | 76% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | source=diode laser |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0055` = 2.062 um | 67% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0055` = 2.062 um | 67% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0040` = 0.785 um | `CLM-PHOT-0055` = 2.062 um | 62% | source=diode laser | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0055` = 2.062 um | 37% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | device=Ho3+-doped fluoride glass waveguide laser |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0055` = 2.062 um | 37% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | device=Ho3+-doped fluoride glass waveguide laser |
