# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**35872 pair(s)** as of 2026-11-28.

## `area_die` (37 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0050` = 0.81 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=TSMC 16nm FinFET technology, component=core area | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0110` = 0.0003 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | component=Address Translation Module, location=RCD, process=TSMC 90nm, frequency=2.4GHz | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0110` = 0.0003 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=Address Translation Module, location=RCD, process=TSMC 90nm, frequency=2.4GHz | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0111` = 0.151 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=Rank Chunk List, location=RCD, process=TSMC 90nm, frequency=2.4GHz | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=PIM Chunk List, location=DRAM chip | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=Row Migration Table, location=DRAM chip | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0146` = 3.43 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=FIGFLEX, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0147` = 3.97 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=AxCore, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0148` = 4.68 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | component=FIGLUT, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0158` = 0.008701 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0281` = 0.000382 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Counter Logic | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0281` = 0.000382 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Counter Logic | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0282` = 0.000233 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=LFSR + Comparator | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0282` = 0.000233 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=LFSR + Comparator | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0283` = 0.00085 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Sobol + Comparator [13] | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0284` = 0.000281 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Sobol (FSM-based) [37] | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0284` = 0.000281 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Sobol (FSM-based) [37] | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-DEV-0071` = 8 mm^2 | `CLM-MAT-0418` = 4.841e-13 mm^2 | 100% | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) | grain_boundary_plane=Σ5(310)[001], material=SrTiO3 |
| `CLM-ARCH-0283` = 0.00085 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45nm FreePDK, precision=8-bit, converter_type=Sobol + Comparator [13] | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0158` = 0.008701 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0282` = 0.000233 mm^2 | 100% | component=Row Migration Table, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=LFSR + Comparator |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0284` = 0.000281 mm^2 | 100% | component=Row Migration Table, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Sobol (FSM-based) [37] |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0281` = 0.000382 mm^2 | 100% | component=Row Migration Table, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Counter Logic |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 100% | component=PIM Chunk List, location=DRAM chip | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0283` = 0.00085 mm^2 | 99% | component=Row Migration Table, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Sobol + Comparator [13] |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0282` = 0.000233 mm^2 | 99% | component=PIM Chunk List, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=LFSR + Comparator |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0284` = 0.000281 mm^2 | 99% | component=PIM Chunk List, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Sobol (FSM-based) [37] |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0281` = 0.000382 mm^2 | 99% | component=PIM Chunk List, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Counter Logic |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 98% | component=Row Migration Table, location=DRAM chip | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0111` = 0.151 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 98% | component=Rank Chunk List, location=RCD, process=TSMC 90nm, frequency=2.4GHz | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0283` = 0.00085 mm^2 | 97% | component=PIM Chunk List, location=DRAM chip | process=45nm FreePDK, precision=8-bit, converter_type=Sobol + Comparator [13] |
| `CLM-ARCH-0113` = 0.134 mm^2 | `CLM-ARCH-0158` = 0.008701 mm^2 | 94% | component=Row Migration Table, location=DRAM chip | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 |
| `CLM-ARCH-0050` = 0.81 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 90% | process=TSMC 16nm FinFET technology, component=core area | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0112` = 0.032 mm^2 | `CLM-ARCH-0158` = 0.008701 mm^2 | 73% | component=PIM Chunk List, location=DRAM chip | process=45 nm, fclk=100 MHz, lanes=784-lane, precision=INT8 |
| `CLM-ARCH-0146` = 3.43 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 57% | component=FIGFLEX, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0147` = 3.97 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 50% | component=AxCore, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |
| `CLM-ARCH-0148` = 4.68 mm^2 | `CLM-DEV-0071` = 8 mm^2 | 42% | component=FIGLUT, process=NanGate 15 nm technology, fclk=1 GHz, activation_format=FP16 | device_stack=ITO (150 nm) / ZnMgO (300 nm) / Se (500 nm) / MoO 3 (20 nm) / Au (80 nm) |

## `current` (57 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0028` = 0.6 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | process_step=current ramp-down | temperature=10 mK |
| `CLM-DEV-0028` = 0.6 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | process_step=current ramp-down | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0036` = 0.558 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | temperature=2 K, state=after light irradiation | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0057` = 30 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=small switching current | temperature=10 mK |
| `CLM-DEV-0057` = 30 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | switching_regime=small switching current | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0058` = 40 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | switching_regime=large switching current | temperature=10 mK |
| `CLM-DEV-0058` = 40 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | switching_regime=large switching current | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0075` = 1.5 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0077` = 4 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-EDA-0018` = 0.02 mA | `CLM-PROC-0077` = 1400 mA | 100% | circuit=BMR, corner=tt | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-MAT-0069` = 2e-06 mA | `CLM-PHOT-0149` = 90 mA | 100% | temperature=10 mK | device_variant=original LD |
| `CLM-MAT-0069` = 2e-06 mA | `CLM-PHOT-0150` = 118 mA | 100% | temperature=10 mK | device_variant=RLD |
| `CLM-MAT-0069` = 2e-06 mA | `CLM-PROC-0077` = 1400 mA | 100% | temperature=10 mK | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-PHOT-0149` = 90 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | device_variant=original LD | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-PHOT-0150` = 118 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | device_variant=RLD | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-PHOT-0210` = 1e-05 mA | `CLM-PROC-0077` = 1400 mA | 100% | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-EDA-0018` = 0.02 mA | `CLM-MAT-0069` = 2e-06 mA | 100% | circuit=BMR, corner=tt | temperature=10 mK |
| `CLM-EDA-0018` = 0.02 mA | `CLM-PHOT-0149` = 90 mA | 100% | circuit=BMR, corner=tt | device_variant=original LD |
| `CLM-EDA-0018` = 0.02 mA | `CLM-PHOT-0150` = 118 mA | 100% | circuit=BMR, corner=tt | device_variant=RLD |
| `CLM-DEV-0028` = 0.6 mA | `CLM-PROC-0077` = 1400 mA | 100% | process_step=current ramp-down | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-DEV-0036` = 0.558 mA | `CLM-PROC-0077` = 1400 mA | 100% | temperature=2 K, state=after light irradiation | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-DEV-0058` = 40 mA | `CLM-EDA-0018` = 0.02 mA | 100% | switching_regime=large switching current | circuit=BMR, corner=tt |
| `CLM-EDA-0018` = 0.02 mA | `CLM-PHOT-0210` = 1e-05 mA | 100% | circuit=BMR, corner=tt | incident_laser_fluence=0.1 µJ/cm2, mode=radial and azimuthal modes |
| `CLM-DEV-0057` = 30 mA | `CLM-EDA-0018` = 0.02 mA | 100% | switching_regime=small switching current | circuit=BMR, corner=tt |
| `CLM-DEV-0075` = 1.5 mA | `CLM-PROC-0077` = 1400 mA | 100% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-DEV-0077` = 4 mA | `CLM-PROC-0077` = 1400 mA | 100% | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-DEV-0036` = 0.558 mA | `CLM-PHOT-0150` = 118 mA | 100% | temperature=2 K, state=after light irradiation | device_variant=RLD |
| `CLM-DEV-0077` = 4 mA | `CLM-EDA-0018` = 0.02 mA | 100% | sample=NbN/AlN/FePt, temperature=4.5 K, stripe_orientation=θ = 90° | circuit=BMR, corner=tt |
| `CLM-DEV-0028` = 0.6 mA | `CLM-PHOT-0150` = 118 mA | 99% | process_step=current ramp-down | device_variant=RLD |
| `CLM-DEV-0036` = 0.558 mA | `CLM-PHOT-0149` = 90 mA | 99% | temperature=2 K, state=after light irradiation | device_variant=original LD |
| `CLM-DEV-0028` = 0.6 mA | `CLM-PHOT-0149` = 90 mA | 99% | process_step=current ramp-down | device_variant=original LD |
| `CLM-DEV-0075` = 1.5 mA | `CLM-PHOT-0150` = 118 mA | 99% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | device_variant=RLD |
| `CLM-DEV-0075` = 1.5 mA | `CLM-EDA-0018` = 0.02 mA | 99% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | circuit=BMR, corner=tt |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0058` = 40 mA | 99% | temperature=2 K, state=after light irradiation | switching_regime=large switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0058` = 40 mA | 98% | process_step=current ramp-down | switching_regime=large switching current |
| `CLM-DEV-0075` = 1.5 mA | `CLM-PHOT-0149` = 90 mA | 98% | sample=NbN/FePt, temperature=4.5 K, stripe_orientation_angle=90° | device_variant=original LD |
| `CLM-DEV-0036` = 0.558 mA | `CLM-DEV-0057` = 30 mA | 98% | temperature=2 K, state=after light irradiation | switching_regime=small switching current |
| `CLM-DEV-0028` = 0.6 mA | `CLM-DEV-0057` = 30 mA | 98% | process_step=current ramp-down | switching_regime=small switching current |
| `CLM-DEV-0057` = 30 mA | `CLM-PROC-0077` = 1400 mA | 98% | switching_regime=small switching current | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |
| `CLM-DEV-0058` = 40 mA | `CLM-PROC-0077` = 1400 mA | 97% | switching_regime=large switching current | material=Ta₂O₅, chamber_temperature=160 °C, acceleration_voltage=250 V |

_and 17 more_

## `energy` (3464 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0328` = 1000 meV | `CLM-MAT-0413` = -1000 meV | 200% | kekule_distortion_strength=0.2 | system=square lattice |
| `CLM-MAT-0275` = 995 meV | `CLM-MAT-0413` = -1000 meV | 200% | desorption_state=molecular | system=square lattice |
| `CLM-MAT-0409` = -91.5 meV | `CLM-PROC-0031` = 91 meV | 199% | direction=In-plane | error_metric=root-mean-square deviation per formula unit |
| `CLM-MAT-0086` = 52.4 meV | `CLM-MAT-0405` = -51.9 meV | 199% | material=CrGeCN4, method=PBE+SOC | direction=In-plane |
| `CLM-MAT-0113` = 15.9 meV | `CLM-MAT-0408` = -15.65 meV | 198% | method=three-band nearest-neighbor exciton-geometric calculation | direction=Out-of-plane |
| `CLM-MAT-0306` = 89.9 meV | `CLM-MAT-0409` = -91.5 meV | 198% | polarization_state=P↑ | direction=In-plane |
| `CLM-MAT-0085` = 53.3 meV | `CLM-MAT-0405` = -51.9 meV | 197% | material=CrSiCN4, method=PBE+SOC | direction=In-plane |
| `CLM-MAT-0048` = 185 meV | `CLM-MEM-0040` = -180 meV | 197% | material=LiFePO4 | method=DFT |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0460` = 5240 meV | 197% | material=MLBP | contact_metal=Pd |
| `CLM-MAT-0277` = 2789 meV | `CLM-MAT-0414` = -2700 meV | 197% | desorption_state=molecular | system=graphene |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MAT-0406` = -61.8 meV | 197% | mechanism=surface polar phonon, substrate=SiO2 | direction=In-plane |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0453` = -4640 meV | 196% | defect_complex=VAl(ON)3, model=DFT | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0291` = 2800 meV | `CLM-MAT-0414` = -2700 meV | 196% | trap_type=isolated bi-Ed | system=graphene |
| `CLM-MAT-0408` = -15.65 meV | `CLM-MAT-0471` = 15 meV | 196% | direction=Out-of-plane | orbital=Nb p orbitals |
| `CLM-MAT-0078` = 4810 meV | `CLM-MAT-0172` = -5090 meV | 194% | defect_complex=VAl(ON)3, model=DFT | material=MLBP |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0453` = -4640 meV | 193% | defect_complex=VAl(ON)3 | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0456` = 195 meV | `CLM-MEM-0040` = -180 meV | 192% | ligand_class=halogen-free phosphonate ligands, transition=alkyl to alkenyl, evaluation_method=MLIP-calculated | method=DFT |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MAT-0407` = -65.9 meV | 191% | mechanism=surface polar phonon, substrate=SiO2 | direction=In-plane |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0331` = 5630 meV | 190% | material=MLBP | phase=m-phase, temperature=300 K |
| `CLM-MAT-0276` = 2994 meV | `CLM-MAT-0414` = -2700 meV | 190% | desorption_state=molecular | system=graphene |
| `CLM-MAT-0002` = 200 meV | `CLM-MEM-0040` = -180 meV | 190% | mechanism=optical phonon | method=DFT |
| `CLM-MAT-0200` = 200 meV | `CLM-MEM-0040` = -180 meV | 190% | band=2.3 eV emission, impurity_content=<0.1 ppm | method=DFT |
| `CLM-MAT-0290` = 3000 meV | `CLM-MAT-0414` = -2700 meV | 190% | trap_type=isolated bi-Si3 | system=graphene |
| `CLM-MAT-0409` = -91.5 meV | `CLM-MAT-0444` = 101.9 meV | 190% | direction=In-plane | parameter=intrinsic (bare) ZO-phonon energy E0 |
| `CLM-MAT-0050` = 102 meV | `CLM-MAT-0409` = -91.5 meV | 190% | material=Li6PS5Cl | direction=In-plane |
| `CLM-MAT-0294` = 1120 meV | `CLM-MAT-0413` = -1000 meV | 189% | fit_function=Eq. ( 13), experimental_data_source=Ref. [ 6] | system=square lattice |
| `CLM-MAT-0410` = -20.27 meV | `CLM-PHOT-0171` = 18 meV | 189% | direction=Out-of-plane | doping_duration=1.5 min |
| `CLM-MAT-0453` = -4640 meV | `CLM-MAT-0460` = 5240 meV | 189% | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections | contact_metal=Pd |
| `CLM-MAT-0408` = -15.65 meV | `CLM-PHOT-0171` = 18 meV | 187% | direction=Out-of-plane | doping_duration=1.5 min |
| `CLM-MAT-0001` = 59.8 meV | `CLM-MAT-0405` = -51.9 meV | 187% | mechanism=surface polar phonon, substrate=SiO2 | direction=In-plane |
| `CLM-MAT-0290` = 3000 meV | `CLM-MAT-0455` = -3460 meV | 187% | trap_type=isolated bi-Si3 | modification=Opening the cyclohexane ring of cyclohexanesulfonic acid, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0276` = 2994 meV | `CLM-MAT-0455` = -3460 meV | 187% | desorption_state=molecular | modification=Opening the cyclohexane ring of cyclohexanesulfonic acid, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0085` = 53.3 meV | `CLM-MAT-0406` = -61.8 meV | 186% | material=CrSiCN4, method=PBE+SOC | direction=In-plane |
| `CLM-MAT-0394` = 1160 meV | `CLM-MAT-0413` = -1000 meV | 186% | functional=PBE | system=square lattice |
| `CLM-MAT-0172` = -5090 meV | `CLM-MAT-0274` = 5922 meV | 186% | material=MLBP | desorption_state=atomic |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0172` = -5090 meV | 185% | defect_complex=VAl(ON)3 | material=MLBP |
| `CLM-MAT-0086` = 52.4 meV | `CLM-MAT-0406` = -61.8 meV | 185% | material=CrGeCN4, method=PBE+SOC | direction=In-plane |
| `CLM-MAT-0290` = 3000 meV | `CLM-MAT-0452` = -3590 meV | 184% | trap_type=isolated bi-Si3 | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0276` = 2994 meV | `CLM-MAT-0452` = -3590 meV | 183% | desorption_state=molecular | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections |
| `CLM-MAT-0077` = 4330 meV | `CLM-MAT-0452` = -3590 meV | 183% | defect_complex=VAl(ON)3 | metric=mean campaign-best binding energy, evaluation_method=pretrained MLIP with dispersion corrections |

_and 3424 more_

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

## `frequency` (1343 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0299` = -7240 GHz | `CLM-MAT-0349` = 3600 GHz | 150% | material=NbOI2, cell_type=4-atoms cell, mode=Peierls mode δ | energy_range=~45.9 – 46.3 eV, edge=Re O2 edge |
| `CLM-MAT-0298` = -1630 GHz | `CLM-MAT-0349` = 3600 GHz | 145% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | energy_range=~45.9 – 46.3 eV, edge=Re O2 edge |
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
| `CLM-MAT-0298` = -1630 GHz | `CLM-PHOT-0152` = 5 GHz | 100% | material=NbOI2, cell_type=4-atoms cell, mode=polar mode P | regime=microwave regime |
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

_and 1303 more_

## `length_device` (7767 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0053` = 1.61 nm | 100% | component=fiber delay line | parameter=ts |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0068` = 100 nm | 100% | component=fiber delay line | material=PEDOT:PSS |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0084` = 22.17 nm | 100% | component=fiber delay line | rkky_coupling=-0.2 mJ/m² |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0085` = 22.21 nm | 100% | component=fiber delay line | rkky_coupling=-0.2 mJ/m² |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0092` = 280.6 nm | 100% | component=fiber delay line | cell_size=1 µm |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0093` = 502.3 nm | 100% | component=fiber delay line | cell_size=1 µm |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0112` = 0.3158 nm | 100% | component=fiber delay line | stacking_configuration=vdWH-IV |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-DEV-0113` = 0.6427 nm | 100% | component=fiber delay line | stacking_configuration=vdWH-IV |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-LITHO-0001` = 500 nm | 100% | component=fiber delay line | material=crystalline silicon membrane |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-LITHO-0005` = 3e+06 nm | 100% | component=fiber delay line | beam_profile=Gaussian |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0017` = 0.284 nm | 100% | component=fiber delay line | material=Sb monolayer on SiC(0001) |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0018` = 0.327 nm | 100% | component=fiber delay line | material=Sb monolayer on SiC(0001) |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0020` = 6.4 nm | 100% | component=fiber delay line | regime=partially-reconstructed |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0023` = 3.5 nm | 100% | component=fiber delay line | state=X2sA |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0024` = 6.4 nm | 100% | component=fiber delay line | state=X2sA |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0029` = 0.5291 nm | 100% | component=fiber delay line | material=bulk CeN |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0037` = 14.6 nm | 100% | component=fiber delay line | material=TiN, property=GL coherence length |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0039` = 42.9 nm | 100% | component=fiber delay line | measurement=neutron reflectivity, material=TiN |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0040` = 0.5 nm | 100% | component=fiber delay line | fermi_velocity=7×105 ms−1, model=Drude model |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0052` = 23 nm | 100% | component=fiber delay line | characterization_method=AFM |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0060` = 101.7 nm | 100% | component=fiber delay line | sample=Sample A |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0063` = 10.7 nm | 100% | component=fiber delay line | device=D1 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0068` = 14.5 nm | 100% | component=fiber delay line | method=estimated from the carrier density at the SDP |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0076` = 3.4e+05 nm | 100% | component=fiber delay line | material=GaN, growth_method=ammonothermal |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0081` = 0.98 nm | 100% | component=fiber delay line | material=CrSb |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0097` = 1.915 nm | 100% | component=fiber delay line | feature=alternating stacking of PEDOT and PSS |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0098` = 2.172 nm | 100% | component=fiber delay line | feature=alternating stacking of PEDOT and PSS |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0118` = 8.5 nm | 100% | component=fiber delay line | region=separated by a single hBN spacer layer |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0132` = 800 nm | 100% | component=fiber delay line | sample_alias=CoB/Pt, imaging_mode=Fresnel imaging, sample_tilt=25 o |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0133` = 41 nm | 100% | component=fiber delay line | sample_alias=CoB/Pt, imaging_mode=DPC |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0134` = 0.558 nm | 100% | component=fiber delay line | method=LDA-relaxed |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0135` = 0.013 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0136` = 0.006 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0137` = 0.011 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0138` = 0.005 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0139` = 0.007 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0140` = 0.005 nm | 100% | component=fiber delay line | superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0141` = 0.3947 nm | 100% | component=fiber delay line | layer_type=SrTiO3 layers, superlattice_layer_n=3, superlattice_layer_m=5 |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0143` = 1.136 nm | 100% | component=fiber delay line | structure=hydrogen-passivated zigzag graphene nanoribbon with six zigzag chains |
| `CLM-ARCH-0291` = 5e+12 nm | `CLM-MAT-0151` = 2200 nm | 100% | component=fiber delay line | laser_fluence=5 mJ/cm2, location=center of the laser track, direction=Y-direction |

_and 7727 more_

## `power` (570 pair(s))

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
| `CLM-ARCH-0114` = 3.55 mW | `CLM-ARCH-0227` = 2.425e+05 mW | 100% | component=PIM Chunk List, location=DRAM chip | process=16 nm, frequency=1 GHz |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-EDA-0002` = 0.000106 mW | 100% | component=PIM Chunk List, location=DRAM chip | benchmark_circuit=BGR, framework=AgenticSizing |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0189` = 2e-10 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4, vds=5 V |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0190` = 5.6e-09 mW | 100% | component=PIM Chunk List, location=DRAM chip | channel_material=(PEA)2PbI4 |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0191` = 5e-08 mW | 100% | component=PIM Chunk List, location=DRAM chip | device_type=drop-cast control devices |
| `CLM-ARCH-0114` = 3.55 mW | `CLM-MAT-0403` = 3e+05 mW | 100% | component=PIM Chunk List, location=DRAM chip | laser=fiber laser (AFS Jena) |

_and 530 more_

## `power_density` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0079` = 3.1e-05 W/mm^2 | `CLM-MAT-0026` = 4.8e-07 W/mm^2 | 98% | structure=long-base p+-n device, n_base_width=300 𝜇𝜇m, framework=extended theory | environment=ambient |

## `pressure` (2 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0064` = 6e-06 torr | `CLM-MAT-0296` = 3.75e+04 torr | 100% | temperature=room temperature | measurement=Tensile testing |
| `CLM-DEV-0064` = 6e-06 torr | `CLM-MAT-0465` = 1.5e+07 torr | 100% | temperature=room temperature | material=PbSe, functional=r2SCAN |

## `relative_deviation` (16265 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-EDA-0003` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | benchmark_circuit=LDO benchmark, framework=proposed method | sample=B1-1 |
| `CLM-EDA-0004` = 60 percent | `CLM-MAT-0111` = -60 percent | 200% | circuit=most complex circuit, framework=proposed framework | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-PHOT-0192` = 60 percent | 200% | sample=B1-1 | frequency_range=1.1-1.8 THz |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0044` = 59.9 percent | 200% | sample=B1-1 | voltage=8 VAg/AgCl, material=1 μm n-type GaN |
| `CLM-ARCH-0198` = 60.3 percent | `CLM-MAT-0111` = -60 percent | 200% | baseline_utilization=42.4% | sample=B1-1 |
| `CLM-EDA-0036` = 16.9 percent | `CLM-MAT-0481` = -17 percent | 199% | framework=Dr. RTL, design_count=20 human-written RTL designs | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0223` = 58 percent | `CLM-MAT-0111` = -60 percent | 197% | mode=greedy | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0425` = 58 percent | 197% | sample=B1-1 | compound=ZrHfRh2Bi2, temperature=300 K |
| `CLM-ARCH-0170` = 62.3 percent | `CLM-MAT-0111` = -60 percent | 196% | frequency=80 MHz, model=ConvSNN | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0426` = 63 percent | 195% | sample=B1-1 | compound=Zr2RhIrBi2, temperature=300 K |
| `CLM-ARCH-0083` = 18 percent | `CLM-MAT-0481` = -17 percent | 194% | platform=Arrow, application=OpenVINO GenAI | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0136` = 18 percent | `CLM-MAT-0481` = -17 percent | 194% | baseline=Adam5000 | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0081` = 16 percent | `CLM-MAT-0481` = -17 percent | 194% | platform=Orin, workload=L2-optimized GEMM, cache_policy=UC | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0082` = 16 percent | `CLM-MAT-0481` = -17 percent | 194% | platform=Arrow, application=OpenCV, variant=Cv+Opt | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0089` = 64.2 percent | `CLM-MAT-0111` = -60 percent | 193% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-MAT-0481` = -17 percent | `CLM-PROC-0043` = 15.5 percent | 191% | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG | voltage=8 VAg/AgCl, material=1 μm n-type GaN |
| `CLM-EDA-0040` = 18.7 percent | `CLM-MAT-0481` = -17 percent | 191% | method=open-source algorithm discovery | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0112` = 66.8 percent | 190% | sample=B1-1 | baseline=pure two-dimensional Coulomb reference, benchmark_protocol=high-field-calibrated |
| `CLM-MAT-0111` = -60 percent | `CLM-PROC-0080` = 53.66 percent | 189% | sample=B1-1 | method=Joint-endpoint watershed selection (WS / joint), test_set=confirmation set of 25 images from 9 additional source papers |
| `CLM-MAT-0481` = -17 percent | `CLM-MEM-0027` = 15.2 percent | 189% | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG | placement=TileDRAM |
| `CLM-ARCH-0090` = 67.5 percent | `CLM-MAT-0111` = -60 percent | 189% | baseline=naive MX implementation baseline, technique=OBSR | sample=B1-1 |
| `CLM-ARCH-0224` = 53 percent | `CLM-MAT-0111` = -60 percent | 188% | mode=greedy | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0252` = 53 percent | 188% | sample=B1-1 | band=NNN, coupling=Λ A, correlation_length=ξ ¯kF = 4 |
| `CLM-MAT-0481` = -17 percent | `CLM-PHOT-0101` = 14.7 percent | 186% | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG | circuit_design=Design B |
| `CLM-ARCH-0187` = 70 percent | `CLM-MAT-0111` = -60 percent | 186% | workload=elementwise graph, technique=Symbolic dynamic compilation | sample=B1-1 |
| `CLM-ARCH-0174` = 71.3 percent | `CLM-MAT-0111` = -60 percent | 184% | system=ARM2GC, benchmark_set=nine benchmarks | sample=B1-1 |
| `CLM-ARCH-0044` = 14.3 percent | `CLM-MAT-0481` = -17 percent | 184% | process=IHP 130 nm, channel_count=8 | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0097` = 72 percent | `CLM-MAT-0111` = -60 percent | 183% | training_dataset=CloudLab, evaluation_dataset=Lambda | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0039` = 49.85 percent | 183% | sample=B1-1 | platform=Jetson Orin Nano, threshold=550, verification_stage=Single function verification |
| `CLM-ARCH-0275` = 49.8 percent | `CLM-MAT-0111` = -60 percent | 183% | model=Kimi-Audio | sample=B1-1 |
| `CLM-ARCH-0086` = 14 percent | `CLM-MAT-0481` = -17 percent | 182% | platform=Orin, application=Demand Layering, variant=DL+Opt | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0210` = 48.24 percent | `CLM-MAT-0111` = -60 percent | 180% | metric=matrix-input storage | sample=B1-1 |
| `CLM-EDA-0035` = 21.3 percent | `CLM-MAT-0481` = -17 percent | 180% | framework=Dr. RTL, design_count=20 human-written RTL designs | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-ARCH-0229` = 75.23 percent | `CLM-MAT-0111` = -60 percent | 180% | model=Qwen MoE | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MEM-0026` = 75.7 percent | 179% | sample=B1-1 | placement=conventional |
| `CLM-EDA-0007` = 76 percent | `CLM-MAT-0111` = -60 percent | 179% | model=Non-cyclic + Node prediction model | sample=B1-1 |
| `CLM-MAT-0111` = -60 percent | `CLM-MAT-0251` = 47 percent | 178% | sample=B1-1 | band=NN, coupling=Λ A, correlation_length=ξ ¯kF = 4 |
| `CLM-MAT-0248` = 13.3 percent | `CLM-MAT-0481` = -17 percent | 178% | band=NN, coupling=Λ A, correlation_length=ξ ¯kF = 4 | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG |
| `CLM-EDA-0052` = 76.7 percent | `CLM-MAT-0111` = -60 percent | 178% | optimizer_variant=PVTSizing 2.0, baseline=RobustAnalog | sample=B1-1 |
| `CLM-MAT-0481` = -17 percent | `CLM-PROC-0026` = 13.2 percent | 178% | excitation_energy=2.33 eV, phonon_mode=G, material_stack=t(2+1)LG | material=WS2 |

_and 16225 more_

## `resistance` (5 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0119` = 8604 ohm | `CLM-MAT-0282` = 0.0039 ohm | 100% | device=experimental device | temperature=10 K, dc_current=0.1 mA |
| `CLM-MAT-0282` = 0.0039 ohm | `CLM-MEM-0001` = 900 ohm | 100% | temperature=10 K, dc_current=0.1 mA | resistance_state=high-resistance state |
| `CLM-DEV-0119` = 8604 ohm | `CLM-MAT-0281` = 6.59 ohm | 100% | device=experimental device | interface=IrMn3/Pt, temperature=10 K, dc_current=0.1 mA |
| `CLM-MAT-0281` = 6.59 ohm | `CLM-MEM-0001` = 900 ohm | 99% | interface=IrMn3/Pt, temperature=10 K, dc_current=0.1 mA | resistance_state=high-resistance state |
| `CLM-DEV-0119` = 8604 ohm | `CLM-MEM-0001` = 900 ohm | 90% | device=experimental device | resistance_state=high-resistance state |

## `sensitivity_advantage_ratio` (6 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0214` = 1.68 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 88% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0214` = 1.68 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 86% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0213` = 2.57 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 81% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0213` = 2.57 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 79% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0212` = 4.95 dimensionless | `CLM-PHOT-0017` = 13.5 dimensionless | 63% | scope=across all three attention mechanisms and batch sizes | target_gas=NO2, comparison=dual-narrowband thermal emitter vs conventional blackbody source |
| `CLM-ARCH-0212` = 4.95 dimensionless | `CLM-PHOT-0016` = 12.2 dimensionless | 59% | scope=across all three attention mechanisms and batch sizes | target_gas=CH4, comparison=dual-narrowband thermal emitter vs conventional blackbody source |

## `temperature` (608 pair(s))

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
| `CLM-DEV-0117` = -271.6 degC | `CLM-MAT-0053` = 230 degC | 185% | device=QHARS device | synthesis_approach=phosphine-free colloidal approach |
| `CLM-DEV-0035` = -204.1 degC | `CLM-PROC-0075` = 160 degC | 178% | relaxation_temperature=TLIESST | material=Ta₂O₅, acceleration_voltage=250 V |
| `CLM-DEV-0017` = 25.35 degC | `CLM-MAT-0356` = -33.15 degC | 176% | temperature_control_system=VAHEAT system | material=Pr1−xCaxMnO3 (PCMO) |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0091` = -113.1 degC | 175% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-MAT-0102` = -81 K | `CLM-MAT-0342` = 60 K | 174% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | measurement_method=angle resolved photoemission spectroscopy (ARPES) |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0307` = 186.9 degC | 173% | sample=NbN/I/FePt | property=T N |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0091` = -113.1 degC | 172% | time_after_cooling_onset=10 s | pressure=ambient pressure, magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0003` = -123.1 degC | 169% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0117` = -271.6 degC | `CLM-MAT-0307` = 186.9 degC | 169% | device=QHARS device | property=T N |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0003` = -123.1 degC | 166% | time_after_cooling_onset=10 s | calculation=acoustic phonon scattering |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0292` = -133.1 degC | 164% | time_after_cooling_onset=10 s | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-DEV-0076` = -257.6 degC | `CLM-PROC-0075` = 160 degC | 162% | sample=NbN/I/FePt | material=Ta₂O₅, acceleration_voltage=250 V |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0292` = -133.1 degC | 161% | time_after_cooling_onset=10 s | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-DEV-0117` = -271.6 degC | `CLM-PROC-0075` = 160 degC | 159% | device=QHARS device | material=Ta₂O₅, acceleration_voltage=250 V |
| `CLM-MAT-0102` = -81 K | `CLM-MAT-0292` = 140 K | 158% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | mn_content=0.03, acceptor_binding_energy_e0=96.9 meV |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0101` = -155.1 degC | 155% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-MAT-0003` = 150 K | `CLM-MAT-0102` = -81 K | 154% | calculation=acoustic phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0101` = -155.1 degC | 153% | time_after_cooling_onset=10 s | material=bulk FePS3 crystal, magnetic_field=0.5 T |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0279` = 106.9 degC | 152% | relaxation_temperature=TLIESST | sample_layer=IrMn3(10 nm)/Py bilayer |
| `CLM-MAT-0091` = 160 K | `CLM-MAT-0102` = -81 K | 151% | pressure=ambient pressure, magnetic_field=0.05 T | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-DEV-0033` = 84.85 degC | `CLM-DEV-0035` = -204.1 degC | 142% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-DEV-0076` = -257.6 degC | `CLM-MAT-0279` = 106.9 degC | 141% | sample=NbN/I/FePt | sample_layer=IrMn3(10 nm)/Py bilayer |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0356` = -33.15 degC | 140% | time_after_cooling_onset=10 s | material=Pr1−xCaxMnO3 (PCMO) |
| `CLM-MAT-0004` = 200 K | `CLM-MAT-0102` = -81 K | 140% | calculation=optical phonon and surface polar phonon scattering | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region |
| `CLM-MAT-0102` = -81 K | `CLM-MAT-0293` = 200 K | 140% | material=bulk FePS3 crystal, paramagnetic_region=paramagnetic region | mn_content=0.1, compensation_degree=Kmax |
| `CLM-DEV-0032` = 81.85 degC | `CLM-DEV-0035` = -204.1 degC | 140% | time_after_cooling_onset=10 s | relaxation_temperature=TLIESST |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0342` = -213.1 degC | 140% | time_after_cooling_onset=10 s | measurement_method=angle resolved photoemission spectroscopy (ARPES) |
| `CLM-DEV-0117` = -271.6 degC | `CLM-MAT-0279` = 106.9 degC | 139% | device=QHARS device | sample_layer=IrMn3(10 nm)/Py bilayer |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0356` = -33.15 degC | 139% | time_after_cooling_onset=10 s | material=Pr1−xCaxMnO3 (PCMO) |
| `CLM-DEV-0032` = 81.85 degC | `CLM-MAT-0342` = -213.1 degC | 138% | time_after_cooling_onset=10 s | measurement_method=angle resolved photoemission spectroscopy (ARPES) |
| `CLM-DEV-0035` = -204.1 degC | `CLM-MAT-0093` = 76.85 degC | 138% | relaxation_temperature=TLIESST | magnetic_field=0.05 T |
| `CLM-DEV-0033` = 84.85 degC | `CLM-MAT-0325` = -233.1 degC | 136% | time_after_cooling_onset=10 s | material=GdN |

_and 568 more_

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

## `thermal_conductivity` (7 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |
| `CLM-MAT-0007` = 3100 W/(m*K) | `CLM-MAT-0438` = 93 W/(m*K) | 97% | temperature=room-temperature, sample_13c_concentration=~0.00024% | structure=Al (70 nm)/Si structure |
| `CLM-MAT-0007` = 3100 W/(m*K) | `CLM-MAT-0439` = 140 W/(m*K) | 95% | temperature=room-temperature, sample_13c_concentration=~0.00024% | structure=Al (70 nm)/Si structure |
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0440` = 360 W/(m*K) | 94% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | structure=Al (70 nm)/Si structure |
| `CLM-MAT-0007` = 3100 W/(m*K) | `CLM-MAT-0440` = 360 W/(m*K) | 88% | temperature=room-temperature, sample_13c_concentration=~0.00024% | structure=Al (70 nm)/Si structure |
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0439` = 140 W/(m*K) | 84% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | structure=Al (70 nm)/Si structure |
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0438` = 93 W/(m*K) | 76% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | structure=Al (70 nm)/Si structure |

## `throughput_tool` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0280` = 6.48e+10 wph | `CLM-PHOT-0027` = 8.64e+15 wph | 100% | data_type=metric packets | modulation_format=60-Gbaud PAM4, link_type=single-link WDM transmission |

## `time` (4980 pair(s))

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
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0221` = 1.15e+10 ns | 100% | device_type=FTJ, architecture=Naive | prover=VeriLoRA, input_length_range=64–2048, operation=opening the weights |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0222` = 1.24e+10 ns | 100% | device_type=FTJ, architecture=Naive | prover=VeriLoRA, input_length_range=64–2048, operation=opening the weights |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0245` = 6.65e+07 ns | 100% | device_type=FTJ, architecture=Naive | engine=PL GEMV engines |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0254` = 4.24e+09 ns | 100% | device_type=FTJ, architecture=Naive | target_design=4-SM GPU, workload=1024 × 1024 GEMM, simulator=FoldSim |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0255` = 9.36e+13 ns | 100% | device_type=FTJ, architecture=Naive | target_design=4-SM GPU, workload=1024 × 1024 GEMM, simulator_type=software RTL simulation |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0266` = 7.04e+06 ns | 100% | device_type=FTJ, architecture=Naive | workload=two-layer N-MNIST network, lowering=spike-gated, baseline_lowering=dense |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0267` = 4.42e+06 ns | 100% | device_type=FTJ, architecture=Naive | weight_layout=spike-major, l2_cache_capacity=4 MiB |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0276` = 2.97e+09 ns | 100% | device_type=FTJ, architecture=Naive | platform=EdgeALM, model=Freeze-Omni, mode=Full-duplex |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-ARCH-0277` = 2.21e+09 ns | 100% | device_type=FTJ, architecture=Naive | model=Mini-Omni, mode=Half-duplex |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0066` = 6e+10 ns | 100% | device_type=FTJ, architecture=Naive | software=MATLAB Deep Learning Toolbox |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0089` = 0.007 ns | 100% | device_type=FTJ, architecture=Naive | sample=SESAM |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0111` = 4.16e+12 ns | 100% | device_type=FTJ, architecture=Naive | atom_count=10648 atoms, gpu=NVIDIA RTX 3090 Ti GPU (24 GB), system=Hg0.5Cd0.5Te cubic supercells |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-DEV-0116` = 1.2e+10 ns | 100% | device_type=FTJ, architecture=Naive | method=AI surrogate to perform 5000 MC fittings, parallelization=without any parallelization |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0011` = 1.35e+08 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=cache coherence module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0012` = 1.273e+09 ns | 100% | device_type=FTJ, architecture=Naive | tool=JasperGold, module=L1 Bus Interface module |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0059` = 1.423e+11 ns | 100% | device_type=FTJ, architecture=Naive | agent_model=Claude Opus 5.5, method=CRAFT |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0070` = 1.53e+11 ns | 100% | device_type=FTJ, architecture=Naive | benchmark_case=mgc des perf 1 |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0071` = 9.52e+11 ns | 100% | device_type=FTJ, architecture=Naive | benchmark_case=mgc des perf 1 |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0075` = 1.709e+10 ns | 100% | device_type=FTJ, architecture=Naive | method=CycleWalker |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0076` = 4.363e+10 ns | 100% | device_type=FTJ, architecture=Naive | method=CycleWalker |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0077` = 1.752e+10 ns | 100% | device_type=FTJ, architecture=Naive | method=CycleWalker |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0078` = 4.576e+11 ns | 100% | device_type=FTJ, architecture=Naive | method=CycleWalker |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-EDA-0079` = 3.79e+08 ns | 100% | device_type=FTJ, architecture=Naive | path_budget=64 |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-LITHO-0007` = 2.17e+08 ns | 100% | device_type=FTJ, architecture=Naive | benchmark_solves=144 solves, layer_matrix_size=578 × 578, hardware=RTX 5090, precision=single precision |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-LITHO-0008` = 2.04e+11 ns | 100% | device_type=FTJ, architecture=Naive | iterations=440 iterations, hardware=desktop processor, precision=double precision |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0119` = 0.00029 ns | 100% | device_type=FTJ, architecture=Naive | material=MAPbBr3, measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0120` = 0.0007 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Time-resolved optical Kerr-effect measurements |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0123` = 0.00015 ns | 100% | device_type=FTJ, architecture=Naive | measurement_method=Multidimensional coherent spectroscopy |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0127` = 0.0003 ns | 100% | device_type=FTJ, architecture=Naive | feature=XA |
| `CLM-ARCH-0012` = 153.5 ns | `CLM-MAT-0170` = 0.002 ns | 100% | device_type=FTJ, architecture=Naive | state=bright exciton |

_and 4940 more_

## `voltage` (134 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0247` = -1.96 V | `CLM-MEM-0011` = 2.32 V | 184% | substituent=−H | device=Ag/TiOx/NiOx/p++-Si device, operation=SET voltage (V SET) |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0247` = -1.96 V | 178% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | substituent=−H |
| `CLM-MAT-0099` = 0.53 V | `CLM-MAT-0247` = -1.96 V | 127% | charging_voltage=0.6 V versus Ag/AgCl | substituent=−H |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0247` = -1.96 V | 124% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | substituent=−H |
| `CLM-MAT-0100` = 0.38 V | `CLM-MAT-0247` = -1.96 V | 119% | charging_voltage=0.6 V versus Ag/AgCl | substituent=−H |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0247` = -1.96 V | 115% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | substituent=−H |
| `CLM-DEV-0120` = 0.069 V | `CLM-MAT-0247` = -1.96 V | 104% | interlayer_distance=0.6 nm | substituent=−H |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0247` = -1.96 V | 102% | incident_peak_electric_field=150 kV/cm | substituent=−H |
| `CLM-MAT-0247` = -1.96 V | `CLM-PROC-0076` = 250 V | 101% | substituent=−H | material=Ta₂O₅, chamber_temperature=160 °C |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | incident_peak_electric_field=150 kV/cm | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0006` = 85 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | incident_peak_electric_field=150 kV/cm | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0026` = 12.65 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_type=VO2 thin film device, temperature=330 K, transition_type=set | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0027` = 1.53 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_type=VO2 thin film device, temperature=330 K, transition_type=reset | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0067` = 0.47 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | device_architecture=Gr/n-Si, illumination=AM 1.5G, 100 mW cm⁻² | operating_condition=transverse open-circuit conditions |
| `CLM-DEV-0120` = 0.069 V | `CLM-MAT-0064` = 1.5e-07 V | 100% | interlayer_distance=0.6 nm | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 |
| `CLM-DEV-0120` = 0.069 V | `CLM-MAT-0270` = 2.94e-06 V | 100% | interlayer_distance=0.6 nm | operating_condition=transverse open-circuit conditions |
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
| `CLM-MAT-0064` = 1.5e-07 V | `CLM-PROC-0076` = 250 V | 100% | temperature=250 K, vtg=6 V, vbg=8.5 V, device=D1 | material=Ta₂O₅, chamber_temperature=160 °C |
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
| `CLM-MAT-0270` = 2.94e-06 V | `CLM-PROC-0076` = 250 V | 100% | operating_condition=transverse open-circuit conditions | material=Ta₂O₅, chamber_temperature=160 °C |

_and 94 more_

## `wavelength` (554 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-DEV-0074` = 0.488 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | power=2 mW | mo_coupling_coefficient=0 |
| `CLM-DEV-0126` = 0.167 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | frequency=5.2 GHz | mo_coupling_coefficient=0 |
| `CLM-DEV-0127` = 0.1 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | frequency=7.845 GHz | mo_coupling_coefficient=0 |
| `CLM-LITHO-0003` = 1.035 um | `CLM-PHOT-0157` = 5e-05 um | 100% | component=near-infrared laser pulse | device=fabricated chip |
| `CLM-MAT-0152` = 0.4 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | repetition_rate=1 kHz, pulse_duration=100 fs | mo_coupling_coefficient=0 |
| `CLM-MAT-0166` = 0.679 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=MoS₂, excitation_wavelength=532 nm | mo_coupling_coefficient=0 |
| `CLM-MAT-0167` = 0.318 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=MoS₂, substrate=sapphire, thickness=1.05 nm, angle=63.9° | mo_coupling_coefficient=0 |
| `CLM-MAT-0195` = 0.0035 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=(PEA)2PbI4 | mo_coupling_coefficient=0 |
| `CLM-MAT-0357` = 0.0001541 um | `CLM-PHOT-0011` = 3.26 um | 100% | source=Cu-Anode, equipment=Bruker D8 equipped with a monochromator | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) |
| `CLM-MAT-0357` = 0.0001541 um | `CLM-PHOT-0012` = 6.3 um | 100% | source=Cu-Anode, equipment=Bruker D8 equipped with a monochromator | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) |
| `CLM-MAT-0357` = 0.0001541 um | `CLM-PHOT-0013` = 3.26 um | 100% | source=Cu-Anode, equipment=Bruker D8 equipped with a monochromator | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter |
| `CLM-MAT-0357` = 0.0001541 um | `CLM-PHOT-0014` = 6.3 um | 100% | source=Cu-Anode, equipment=Bruker D8 equipped with a monochromator | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter |
| `CLM-MAT-0357` = 0.0001541 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | source=Cu-Anode, equipment=Bruker D8 equipped with a monochromator | mo_coupling_coefficient=0 |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0157` = 5e-05 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | device=fabricated chip |
| `CLM-PHOT-0011` = 3.26 um | `CLM-PHOT-0173` = 0.0001 um | 100% | target_gas=CH4, method=TMM/FDTD inverse design (MOPSO) | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0157` = 5e-05 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | device=fabricated chip |
| `CLM-PHOT-0012` = 6.3 um | `CLM-PHOT-0173` = 0.0001 um | 100% | target_gas=NO2, method=TMM/FDTD inverse design (MOPSO) | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0157` = 5e-05 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | device=fabricated chip |
| `CLM-PHOT-0013` = 3.26 um | `CLM-PHOT-0173` = 0.0001 um | 100% | target_gas=CH4, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0157` = 5e-05 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | device=fabricated chip |
| `CLM-PHOT-0014` = 6.3 um | `CLM-PHOT-0173` = 0.0001 um | 100% | target_gas=NO2, structure=fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0028` = 0.0167 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | component=integrated microheater | mo_coupling_coefficient=0 |
| `CLM-PHOT-0033` = 0.00315 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | excitation_wavelength=532 nm, cumulative_exposure_time=5 h | mo_coupling_coefficient=0 |
| `CLM-PHOT-0040` = 0.785 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | source=diode laser | mo_coupling_coefficient=0 |
| `CLM-PHOT-0055` = 2.062 um | `CLM-PHOT-0173` = 0.0001 um | 100% | device=Ho3+-doped fluoride glass waveguide laser | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0071` = 1.24 um | `CLM-PHOT-0157` = 5e-05 um | 100% | material=ITO | device=fabricated chip |
| `CLM-PHOT-0072` = 1.22 um | `CLM-PHOT-0157` = 5e-05 um | 100% | polarization=x-polarization, incident_angle=normal incidence | device=fabricated chip |
| `CLM-PHOT-0082` = 0.3621 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | process=Difference-frequency generation (DFG), input_signal_wavelength=637 nm | mo_coupling_coefficient=0 |
| `CLM-PHOT-0083` = 1.55 um | `CLM-PHOT-0157` = 5e-05 um | 100% | permittivity_diagonal_term=4.75, material=Bi-substituted yttrium iron garnet (Bi:YIG) | device=fabricated chip |
| `CLM-PHOT-0087` = 0.7757 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | fundamental_pump_wavelength=1551.42 nm | mo_coupling_coefficient=0 |
| `CLM-PHOT-0090` = 0.5191 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | device=microdisk, pump_wavelength=1559.40 nm, pump_power=12.4 mW | mo_coupling_coefficient=0 |
| `CLM-PHOT-0098` = 0.298 um | `CLM-PHOT-0099` = 2.03e+04 um | 100% | material=silicon nitride, radial_periodicity=229 nm, mode=out-of-plane mode | mo_coupling_coefficient=0 |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PHOT-0157` = 5e-05 um | 100% | mo_coupling_coefficient=0 | device=fabricated chip |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PHOT-0170` = 0.5413 um | 100% | mo_coupling_coefficient=0 | doping_duration=1.5 min, doping_gas=HCl |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PHOT-0172` = 0.0076 um | 100% | mo_coupling_coefficient=0 | doping_duration=3 min |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PHOT-0173` = 0.0001 um | 100% | mo_coupling_coefficient=0 | footprint=250-μm, configuration=serpentine configuration |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PHOT-0209` = 0.8 um | 100% | mo_coupling_coefficient=0 | excitation_mode=resonant continuous-wave excitation |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PKG-0003` = 0.001 um | 100% | mo_coupling_coefficient=0 | injection_current=9 mA, sample_type=D-DLAT sample |
| `CLM-PHOT-0099` = 2.03e+04 um | `CLM-PROC-0039` = 0.000388 um | 100% | mo_coupling_coefficient=0 | landing_energy=10 eV |
| `CLM-PHOT-0155` = 1.643 um | `CLM-PHOT-0157` = 5e-05 um | 100% | in_plane_asymmetry_parameter=0.75 | device=fabricated chip |

_and 514 more_
