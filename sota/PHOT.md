# Photonics — state of the art

Topic code `PHOT`. Last reviewed 2026-10-09.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### frequency

- **18.98 GHz** — The single ring cavity has a free spectral range of 18.98 GHz.
  - `CLM-PHOT-0001` · component single ring cavity, parameter FSR · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00009
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **3.57 GHz** — The photonic molecule spectrum exhibits a super-mode spacing Ω1 of 3.57 GHz.
  - `CLM-PHOT-0002` · component photonic molecule, mode_spacing Ω1 · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00009
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **15.41 GHz** — The photonic molecule spectrum exhibits a spacing Ω2 of 15.41 GHz.
  - `CLM-PHOT-0003` · component photonic molecule, mode_spacing Ω2 · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00009
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **≈0.03 GHz** — The measured maximum resonance shift is approximately 0.03 GHz across the entire oblique incidence range from 0° to 30°.
  - `CLM-PHOT-0024` · angle_of_incidence 0° to 30°, rotation_angle 90° · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00028
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **121 GHz** — Across 22 measured devices, the mean linewidth ∆ν was 121 ± 58 GHz.
  - `CLM-PHOT-0036` · sample_size 22 measured devices · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **267 GHz** — At 267 GHz, the generated THz signal achieves a measured single-sideband phase noise of -95.7 dBc/Hz at a 10-kHz offset frequency.
  - `CLM-PHOT-0049` · signal_type measured phase noise · grade B · credibility unknown · measured · as of 2026-10-05
  - sources: SRC-00083
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≈194000 GHz** — The stabilized optical reference CW laser demonstrates an SSB phase noise of -83.6 dBc/Hz at a 10 kHz offset frequency at an optical carrier frequency of approximately 194 THz.
  - `CLM-PHOT-0050` · component stabilized CW laser, frequency_offset 10 kHz · grade B · credibility unknown · measured · as of 2026-10-05
  - sources: SRC-00083
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0023, CFL-0024 — see the open register
- **230 GHz** — The THz signal generated at 230 GHz achieves a measured phase noise of -96.8 dBc/Hz at a 10-kHz offset frequency.
  - `CLM-PHOT-0051` · frequency_offset 10 kHz, signal_type measured phase-noise levels · grade B · credibility unknown · measured · as of 2026-10-05
  - sources: SRC-00083
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0023, CFL-0025 — see the open register
- **320 GHz** — The THz signal generated at 320 GHz achieves a measured phase noise of -96.8 dBc/Hz at a 10-kHz offset frequency.
  - `CLM-PHOT-0052` · frequency_offset 10 kHz, signal_type measured phase-noise levels · grade B · credibility unknown · measured · as of 2026-10-05
  - sources: SRC-00083
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0024, CFL-0025 — see the open register
- **≤ ≈0.0048 GHz** — The Ho3+-doped fluoride glass waveguide laser exhibits a linewidth of approximately 4.8 MHz.
  - `CLM-PHOT-0056` · device Ho3+-doped fluoride glass waveguide laser · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00098
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### length device

- **7000 nm** — The coplanar waveguide has a signal-ground electrode spacing of 7 μm.
  - `CLM-PHOT-0004` · parameter signal-ground electrode spacing · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00009
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **0.23 nm** — The bare silicon substrate exhibited an arithmetic average roughness Sa of 0.23 nm.
  - `CLM-PHOT-0007` · sample bare silicon substrate, roughness_type arithmetic average roughness (Sa) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.33 nm** — The bare silicon substrate exhibited a root mean square roughness Sq of 0.33 nm.
  - `CLM-PHOT-0008` · sample bare silicon substrate, roughness_type root mean square roughness (Sq) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **1.7 nm** — After deposition of the MoSx film, the surface arithmetic average roughness Sa increased to 1.7 nm.
  - `CLM-PHOT-0009` · roughness_type arithmetic average roughness (Sa), sample after MoSx film deposition · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **2.1 nm** — After deposition of the MoSx film, the root mean square roughness Sq increased to 2.1 nm.
  - `CLM-PHOT-0010` · roughness_type root mean square roughness (Sq), sample after MoSx film deposition · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **850 nm** — In the MO-PhC slab simulation, the periodicity is 850 nm.
  - `CLM-PHOT-0026` · component MO-PhC slab · grade B · credibility unknown · simulated · as of 2026-09-23
  - sources: SRC-00031
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **60 nm** — The gold layer of the flat surface sample was sputtered to a thickness of 60 nm.
  - `CLM-PHOT-0041` · layer_material gold, sample_type flat surface · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0022 — see the open register
- **160000 nm** — The glass cover slip substrate for the flat surface sample had a thickness of 160 µm.
  - `CLM-PHOT-0042` · substrate_material glass cover slip, sample_type flat surface · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0022 — see the open register
- **765 nm** — The hole array structure fabricated in a square lattice has a period of 765 nm.
  - `CLM-PHOT-0043` · structure hole array (HA) in a square lattice · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **576 nm** — The radially periodic true-chiral array of apertures has a radial period of 576 nm.
  - `CLM-PHOT-0044` · structure_type true-chiral metasurface · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **603 nm** — The radially periodic true-chiral array of apertures has an azimuthal period of 603 nm.
  - `CLM-PHOT-0045` · period_direction azimuthal period (arc length), structure_type true-chiral metasurface · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **0.024 nm** — The lasing wavelength exhibited a drift of 24 pm over a period exceeding 15.5 hours.
  - `CLM-PHOT-0057` · measurement_duration exceeding 15.5 hours · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00098
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### power

- **0.0217 W** — The Ho3+-doped fluoride glass waveguide laser achieves an output power of 21.7 mW at an incident pump power of 825 mW.
  - `CLM-PHOT-0053` · pump_power 825 mW, device Ho3+-doped fluoride glass waveguide laser · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00098
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0028 — see the open register
- **≈0.1325 W** — The Ho3+-doped fluoride glass waveguide laser exhibits a threshold pump power of approximately 132.5 mW.
  - `CLM-PHOT-0054` · device Ho3+-doped fluoride glass waveguide laser · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00098
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0028 — see the open register

### qualitative

- The dual-harmonic acousto-optic modulator demonstrates 50% conversion efficiency to one sideband at 730 nm wavelength.
  - `CLM-PHOT-0018` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00020
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The hybrid optical-digital Meta-DLM system experimentally achieves a classification accuracy of 95.3% on the full-scale CIFAR-10 dataset using 7,680 trainable digital parameters.
  - `CLM-PHOT-0019` · dataset standard full-scale CIFAR-10 dataset, digital_parameters 7,680 · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00026
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The Meta-DLM system achieves an experimental MNIST classification accuracy of 98.5% across 11 parallel task channels.
  - `CLM-PHOT-0020` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00026
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- Under multi-task operation, Meta-DLM experimentally achieves a facial keypoint detection root mean square error of 2.64.
  - `CLM-PHOT-0021` · operation_mode parallel multi-task · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00026
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The maximum incident-angle range theta_i,max supported by the Meta-DLM experimental setup is measured to be 60 degrees.
  - `CLM-PHOT-0022` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00026
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The minimum incident angle difference delta_theta_min between adjacent channels in Meta-DLM is measured to be 2.3 degrees.
  - `CLM-PHOT-0023` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00026
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The average measured propagation loss on a processed lithium niobate wafer is 0.27 dB/cm.
  - `CLM-PHOT-0030` · material LN · grade B · credibility unknown · measured · as of 2026-09-25
  - sources: SRC-00035
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The lowest measured optical propagation loss on micro-ring resonators near the center of the wafer is 0.21 dB/cm.
  - `CLM-PHOT-0031` · device_type micro-ring resonators, intrinsic_quality_factor 1.8 million · grade B · credibility unknown · measured · as of 2026-09-25
  - sources: SRC-00035
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- With 10 mW of 20 kHz-modulated green light, an infrared modulation depth of approximately 45% of the available reflection contrast is achieved.
  - `CLM-PHOT-0032` · excitation_wavelength 532 nm, modulation_frequency 20 kHz, excitation_power 10 mW · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- The manufactured diamond used for device fabrication features an NV concentration of 4 ppm.
  - `CLM-PHOT-0034` · material single-crystal diamond · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- Across 22 measured cavity devices, the mean finesse was F = 12.2 ± 3.6.
  - `CLM-PHOT-0035` · sample_size 22 measured devices · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- Waveguide-coupled excitation of the device cavity resonance yields a peak modulation depth Mpeak of approximately 45% at an incident power of 9.6 mW.
  - `CLM-PHOT-0038` · excitation_type waveguide-coupled excitation · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- An all-dielectric metasurface demonstrated fifth-harmonic generation enhancement in argon with a reported enhancement factor of up to 45.
  - `CLM-PHOT-0039` · harmonic_order fifth-harmonic generation, platform all-dielectric metasurface · grade B · credibility unknown · measured · as of 2026-09-30
  - sources: SRC-00053
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The narrowest emission linewidth for InAs/GaAs quantum dots with a 10nm GaAs capping layer is 0.13nm under non-resonant laser excitation at cryogenic temperatures.
  - `CLM-PHOT-0046` · excitation 880nm laser · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00071
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The narrowest emission linewidth for reference InAs/GaAs quantum dots with a 95nm GaAs capping layer is 0.04nm under non-resonant laser excitation at cryogenic temperatures.
  - `CLM-PHOT-0047` · excitation 880nm laser · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00071
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### relative deviation

- **85 percent** — The optical hyperdimensional computing system achieved 85% classification accuracy on the Iris test set.
  - `CLM-PHOT-0005` · dataset Iris test set · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00014
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **88 percent** — The experimental optical HDC classification on the MNIST dataset achieved 88% accuracy.
  - `CLM-PHOT-0006` · dataset MNIST, setup experimental system · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00014
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### sensitivity advantage ratio

- **≈12.2** — The fabricated dual-narrowband thermal emitter achieves an approximate 12.2-fold improvement in relative sensitivity for CH4 gas detection compared with a conventional blackbody source.
  - `CLM-PHOT-0016` · target_gas CH4, comparison dual-narrowband thermal emitter vs conventional blackbody source · grade A · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00019
- **13.5** — The fabricated dual-narrowband thermal emitter achieves a 13.5-fold improvement in relative sensitivity for NO2 gas detection compared with a conventional blackbody source.
  - `CLM-PHOT-0017` · target_gas NO2, comparison dual-narrowband thermal emitter vs conventional blackbody source · grade A · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00019

### temperature

- **≤ 419.85 degC** — The fabricated dual-narrowband thermal emitter maintains its dual-narrowband spectral response for temperatures up to 693 K.
  - `CLM-PHOT-0015` · structure fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter · grade A · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00019

### temperature delta

- **≈0.11 K** — Under a circular green-beam excitation of 1.09 mW incident power, the mode-averaged temperature increase in a 20 µm cavity is approximately 0.11 K.
  - `CLM-PHOT-0037` · cavity_length 20 µm, beam_shape circular, incident_power 1.09 mW · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### throughput tool

- **8.64e+15 wph** — The single-link WDM transmission fabric achieves a aggregate data rate of 2.4 Tbps.
  - `CLM-PHOT-0027` · modulation_format 60-Gbaud PAM4, link_type single-link WDM transmission · grade B · credibility unknown · measured · as of 2026-09-23
  - sources: SRC-00032
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### time

- **≈4e+06 ns** — For a randomly generated trilayer DNN under H-polarized random speckle illumination at a wavelength of 1550 nm, the prediction by DNNsolver takes about 4 ms.
  - `CLM-PHOT-0025` · illumination random speckle illumination · grade B · credibility unknown · simulated · as of 2026-09-23
  - sources: SRC-00029
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **8.29e+10 ns** — The DBS optimization of the broadband directional coupler using PNGF takes 82.9 seconds on 128 cores.
  - `CLM-PHOT-0048` · algorithm DBS, cores 128 cores · grade B · credibility unknown · simulated · as of 2026-10-02
  - sources: SRC-00078
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### wavelength

- **3.26 um** — A multi-objective-optimized aperiodic dielectric-multilayer-on-TiN thermal emitter design has a calculated emission peak at 3.26 micrometers for CH4 gas sensing.
  - `CLM-PHOT-0011` · target_gas CH4, method TMM/FDTD inverse design (MOPSO) · grade A · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00019
- **6.3 um** — A multi-objective-optimized aperiodic dielectric-multilayer-on-TiN thermal emitter design has a calculated emission peak at 6.30 micrometers for NO2 gas sensing.
  - `CLM-PHOT-0012` · target_gas NO2, method TMM/FDTD inverse design (MOPSO) · grade A · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00019
- **3.26 um** — The fabricated aperiodic Si/SiO2-on-TiN thermal emitter sample has a measured emission peak at 3.26 micrometers for CH4 gas sensing.
  - `CLM-PHOT-0013` · target_gas CH4, structure fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter · grade A · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00019
- **6.3 um** — The fabricated aperiodic Si/SiO2-on-TiN thermal emitter sample has a measured emission peak at 6.30 micrometers for NO2 gas sensing.
  - `CLM-PHOT-0014` · target_gas NO2, structure fabricated aperiodic Si/SiO2 multilayer on 100 nm TiN, 10 cm diameter · grade A · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00019
- **0.0167 um** — Continuous wavelength tuning of 16.7 nm is demonstrated using the integrated microheater.
  - `CLM-PHOT-0028` · component integrated microheater · grade B · credibility unknown · measured · as of 2026-09-23
  - sources: SRC-00032
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≥ 0.3 um** — The 9-channel ultra-broadband WDM DETRX achieves total spectral coverage exceeding 300 nm.
  - `CLM-PHOT-0029` · component 9-channel ultra-broadband WDM DETRX, spectral_range O-to-C band · grade B · credibility unknown · measured · as of 2026-09-23
  - sources: SRC-00032
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **≤ 0.00315 um** — Green illumination produces photo-refractive resonance blue-shifts with a maximum observed tuning of 3.15 nm (0.87 THz).
  - `CLM-PHOT-0033` · excitation_wavelength 532 nm, cumulative_exposure_time 5 h · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00051
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **0.785 um** — A diode laser operating at a wavelength of 785 nm was used in the experimental setup.
  - `CLM-PHOT-0040` · source diode laser · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00065
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **2.06221 um** — The Ho3+-doped fluoride glass waveguide laser operates at a lasing wavelength of 2062.21 nm.
  - `CLM-PHOT-0055` · device Ho3+-doped fluoride glass waveguide laser · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00098
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0022` — length_device: _unexamined; classification pending_
  - claims: CLM-PHOT-0041, CLM-PHOT-0042
  - missing data: `not yet named`
- `CFL-0023` — frequency: _unexamined; classification pending_
  - claims: CLM-PHOT-0050, CLM-PHOT-0051
  - missing data: `not yet named`
- `CFL-0024` — frequency: _unexamined; classification pending_
  - claims: CLM-PHOT-0050, CLM-PHOT-0052
  - missing data: `not yet named`
- `CFL-0025` — frequency: _unexamined; classification pending_
  - claims: CLM-PHOT-0051, CLM-PHOT-0052
  - missing data: `not yet named`
- `CFL-0028` — power: _unexamined; classification pending_
  - claims: CLM-PHOT-0053, CLM-PHOT-0054
  - missing data: `not yet named`

## Evidence base

- claims: 57
- grades: {'B': 50, 'A': 7}
- distinct sources: 18
