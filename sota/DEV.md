# Devices — state of the art

Topic code `DEV`. Last reviewed 2026-10-06.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### current

- **≈0.6 mA** — Below a critical holding current of approximately 0.6 mA, the metallic channel abruptly pinches off, triggering a reset.
  - `CLM-DEV-0028` · process_step current ramp-down · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00061
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### frequency

- **370 GHz** — For square patch arrays, a minimum mode separation of 0.37 THz for Ω R/π is measured at the anti-crossing point.
  - `CLM-DEV-0012` · magnetic_field 8.1 T, frequency 1.9 THz · grade B · credibility unknown · measured · as of 2026-09-23
  - sources: SRC-00033
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **180 GHz** — For rectangular patch arrays, a Rabi frequency Ω R/π of 0.18 THz is measured at the anti-crossing point.
  - `CLM-DEV-0013` · magnetic_field 7.5 T, frequency 2.2 THz · grade B · credibility unknown · measured · as of 2026-09-23
  - sources: SRC-00033
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### power

- **1 W** — For a gate drive EMF of 1.50 V, the simulated output power is 30.0 dBm.
  - `CLM-DEV-0025` · gate_bias_vgs -2.7 V · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00054
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **7.76 W** — In DC-AC conversion, the peak output power reaches 7.76 W.
  - `CLM-DEV-0030` · mode DC-AC conversion, vin 24-V DC input · grade B · credibility unknown · measured · as of 2026-10-02
  - sources: SRC-00077
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### qualitative

- An N-polar GaN/AlGaN MOSHEMT was fabricated on a Si(100) substrate by transferring Ga-polar epilayers using surface activated bonding.
  - `CLM-DEV-0001` · grade B · credibility unknown · measured · as of 2026-09-16
  - sources: SRC-00003
- Data transfer over the signatureless thermoradiative channel achieved a rate of up to 92.16 kbps with an error rate below 10^-6.
  - `CLM-DEV-0005` · channel_type signatureless thermoradiative channel · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00008
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- In a 6.7-nm-wide ribbon, the edge spectral suppression is approximately 19 meV.
  - `CLM-DEV-0007` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00024
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- In a 23-nm-wide ribbon, the edge spectral suppression is approximately 10 meV.
  - `CLM-DEV-0008` · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00024
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- In a ribbon model without periodic spin-orbit coupling modulation, the calculated central gap decreases from approximately 19.5 meV at a ribbon width of 5.52 nm.
  - `CLM-DEV-0009` · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00024
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- In a ribbon model without periodic spin-orbit coupling modulation, the calculated central gap decreases to approximately 0.3 meV at a ribbon width of 17.94 nm.
  - `CLM-DEV-0010` · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00024
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- With periodic spin-orbit coupling modulation, the calculated central spectral scale remains approximately 9.4 meV for ribbon widths above approximately 11 nm.
  - `CLM-DEV-0011` · model periodic SOC modulation, ribbon_width above approximately 11 nm · grade B · credibility unknown · simulated · as of 2026-09-22
  - sources: SRC-00024
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The phase-only SIM-D 2NN with phase uncertainty standard deviation sigma_p = 0.05 rad achieves a simulated accuracy of 87.58% +/- 0.7% in the binary task.
  - `CLM-DEV-0014` · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00041
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The phase-only SIM-D 2NN with phase uncertainty standard deviation sigma_p = 0.1 rad achieves a simulated accuracy of 86.32% +/- 1.2% in the binary task.
  - `CLM-DEV-0015` · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00041
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- A phase and amplitude SIM-D 2NN variant achieves 90.70% accuracy on the binary terrain classification task.
  - `CLM-DEV-0016` · model SIM-D2NN(Phase & Amplitude) · grade B · credibility unknown · simulated · as of 2026-09-28
  - sources: SRC-00041
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- For devices containing 320 to 480 atoms, HamGNN-NEGF achieves speedups of approximately 1,000-fold to 2,000-fold over conventional Full-NEGF.
  - `CLM-DEV-0018` · framework HamGNN-NEGF, baseline Full-NEGF · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00049
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Relative to the Full-NEGF baseline, DFTH-NEGF reduces total computational time by 18.3% for the Au-benzenedithiol-Au junction.
  - `CLM-DEV-0019` · method DFTH-NEGF, baseline Full-NEGF, device Au–benzenedithiol–Au junction · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00049
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- Relative to the Full-NEGF baseline, DFTH-NEGF reduces total computational time by 27.4% for the carbon nanotube.
  - `CLM-DEV-0020` · method DFTH-NEGF, baseline Full-NEGF, device carbon nanotube · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00049
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- The photoluminescence intensity asymmetry ratio reaches 27.
  - `CLM-DEV-0029` · detection_wavelength 819 nm, temperature 10 K · grade B · credibility unknown · measured · as of 2026-09-30
  - sources: SRC-00072
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### temperature

- **25.35 degC** — All experiments were performed at a temperature of 298.5 K.
  - `CLM-DEV-0017` · temperature_control_system VAHEAT system · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00046
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### temperature delta

- **30.4 K** — At a gate drive EMF of 1.50 V, the memory-on ASM-HEMT simulation yields a junction temperature rise of 30.4 K.
  - `CLM-DEV-0024` · gate_bias_vgs -2.7 V · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00054
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### time

- **1.504e+06 ns** — Under the memory-on ASM-HEMT simulation, mode 1 has a time constant of 1504 µs.
  - `CLM-DEV-0021` · mode 1, character thermal (mount), operating_point Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00054
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **14600 ns** — In the memory-on ASM-HEMT model simulation at gate drive 1.5 V, mode 3 (the linearized trap mode) has a time constant of 14.6 µs.
  - `CLM-DEV-0022` · mode 3, character trap, linearized, operating_point Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00054
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **6010 ns** — For the memory-on ASM-HEMT simulation, the channel thermal mode (mode 4) has a time constant of 6.01 µs.
  - `CLM-DEV-0023` · mode 4, character thermal (channel), operating_point Memory-on ASM-HEMT at A2 = 0.3 + 0.1j , gate drive 1.5 V · grade B · credibility unknown · simulated · as of 2026-09-30
  - sources: SRC-00054
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### voltage

- **≈85 V** — In the flat state of the nanogap metasurface, the peak gap voltage reaches approximately 85 V at an incident peak electric field of 150 kV/cm.
  - `CLM-DEV-0006` · incident_peak_electric_field 150 kV/cm · grade B · credibility unknown · measured · as of 2026-09-18
  - sources: SRC-00010
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **12.65 V** — The two-probe VO2 thin film device at 330 K undergoes an abrupt insulator-metal transition (set) at a threshold voltage of 12.65 V.
  - `CLM-DEV-0026` · device_type VO2 thin film device, temperature 330 K, transition_type set · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00061
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **1.53 V** — The VO2 thin film device resets back to a homogeneous insulator at a voltage of 1.53 V.
  - `CLM-DEV-0027` · device_type VO2 thin film device, temperature 330 K, transition_type reset · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00061
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 27
- grades: {'B': 27}
- distinct sources: 12
