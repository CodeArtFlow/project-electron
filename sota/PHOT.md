# Photonics — state of the art

Topic code `PHOT`. Last reviewed 2026-09-23.

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

### length device

- **7000 nm** — The coplanar waveguide has a signal-ground electrode spacing of 7 μm.
  - `CLM-PHOT-0004` · parameter signal-ground electrode spacing · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00009
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **0.23 nm** — The bare silicon substrate exhibited an arithmetic average roughness Sa of 0.23 nm.
  - `CLM-PHOT-0007` · sample bare silicon substrate, roughness_type arithmetic average roughness (Sa) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0012 — see the open register
- **0.33 nm** — The bare silicon substrate exhibited a root mean square roughness Sq of 0.33 nm.
  - `CLM-PHOT-0008` · sample bare silicon substrate, roughness_type root mean square roughness (Sq) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0013 — see the open register
- **1.7 nm** — After deposition of the MoSx film, the surface arithmetic average roughness Sa increased to 1.7 nm.
  - `CLM-PHOT-0009` · roughness_type arithmetic average roughness (Sa) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0012 — see the open register
- **2.1 nm** — After deposition of the MoSx film, the root mean square roughness Sq increased to 2.1 nm.
  - `CLM-PHOT-0010` · roughness_type root mean square roughness (Sq) · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00018
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0013 — see the open register

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

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0012` — length_device: _unexamined; classification pending_
  - claims: CLM-PHOT-0007, CLM-PHOT-0009
  - missing data: `not yet named`
- `CFL-0013` — length_device: _unexamined; classification pending_
  - claims: CLM-PHOT-0008, CLM-PHOT-0010
  - missing data: `not yet named`

## Evidence base

- claims: 24
- grades: {'B': 17, 'A': 7}
- distinct sources: 7
