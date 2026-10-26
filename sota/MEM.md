# Memory — state of the art

Topic code `MEM`. Last reviewed 2026-10-26.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy

- **≈8.01088e-05 fJ** — ARPES measurement performed at a temperature of 100 K reveals a flat band splitting of approximately 0.5 eV in YCl.
  - `CLM-MEM-0018` · temperature 100 K, measurement_method ARPES · grade B · credibility unknown · measured · as of 2026-10-14
  - sources: SRC-00148
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### energy advantage ratio

- **≥ 3.7 ×** — The proposed pipelined mapping achieves a speedup of 3.7x to 16.4x over SoA mappings across the evaluated workloads.
  - `CLM-MEM-0025` · baseline SoA mappings · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00169
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### length device

- **37.5 nm** — For a CrSBr nanotube with a perimeter Nc corresponding to a nanotube diameter of 220 Å, the simulated equilibrium distance between two domain walls is 375 Å.
  - `CLM-MEM-0007` · diameter 220 ˚A · grade B · credibility unknown · simulated · as of 2026-10-05
  - sources: SRC-00084
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≈90 nm** — The Ag/TiOx/NiOx/p++-Si heterostructure cross-sectional TEM reveals a NiOx layer thickness of roughly 90 nm.
  - `CLM-MEM-0008` · layer NiOx, structure p++-Si/NiOx/TiOx heterostructure · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00118
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0050 — see the open register
- **≈30 nm** — The Ag/TiOx/NiOx/p++-Si heterostructure cross-sectional TEM reveals a TiOx layer thickness of roughly 30 nm.
  - `CLM-MEM-0009` · layer TiOx, structure p++-Si/NiOx/TiOx heterostructure · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00118
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0051 — see the open register
- **≈120 nm** — The Ag/TiOx/NiOx/p++-Si heterostructure cross-sectional TEM shows a total film thickness of approximately 120 nm.
  - `CLM-MEM-0010` · structure p++-Si/NiOx/TiOx heterostructure · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00118
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0050, CFL-0051 — see the open register

### qualitative

- In a neural-network simulation using synthetic depression trajectories, the abrupt response yields an MNIST classification accuracy of approximately 50%.
  - `CLM-MEM-0002` · dataset MNIST · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00052
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- In a neural-network simulation using synthetic depression trajectories, the sigmoidal response yields an MNIST classification accuracy of approximately 85%.
  - `CLM-MEM-0003` · dataset MNIST · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00052
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- In a neural-network simulation using synthetic depression trajectories, the slowly evolving response yields an MNIST classification accuracy of approximately 88%.
  - `CLM-MEM-0004` · dataset MNIST, depression_regime slowly evolving response · grade B · credibility unknown · simulated · as of 2026-09-29
  - sources: SRC-00052
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- The single-pulse switching threshold fluence for the continuous-film sample is 3.98 ± 0.29 mJ cm−2.
  - `CLM-MEM-0005` · pulse_duration 30 fs · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00066
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- Multidomain formation appears at the center of the switched region when the average fluence exceeds 7.96 ± 0.59 mJ cm−2.
  - `CLM-MEM-0006` · pulse_duration 30 fs · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00066
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- The normalized hardware cost of uniform Diff-W/Diff-A encoding is 3.06.
  - `CLM-MEM-0017` · encoding Diff-W/Diff-A · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00147
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- TileDRAM achieves a geometric mean speedup of 1.77x across 108 MoE FFN cases in full-trace replay.
  - `CLM-MEM-0029` · grade B · credibility unknown · simulated · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- Retargeting six full-trace streams to six 3D DRAM organizations with TileDRAM yields a 2.20x geometric mean speedup.
  - `CLM-MEM-0030` · grade B · credibility unknown · simulated · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The saturation magnetization of Cu-seeded gamma-FeMn films is approximately 0.06 to 0.07 muB/atom.
  - `CLM-MEM-0033` · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00203
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The effective perpendicular anisotropy energy density of gamma-FeMn films thicker than 40 nm is approximately 3 kJ/m3.
  - `CLM-MEM-0034` · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00203
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- The room-temperature anomalous Hall conductivity of the sample is approximately 12 to 14 S/cm.
  - `CLM-MEM-0035` · temperature room -temperature, material 𝛾-FeMn · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00203
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- Upon post-annealing at 430 degrees Celsius, the saturation magnetization of FeMn rises sharply to 0.65 muB/atom.
  - `CLM-MEM-0036` · annealing_temperature 430°C · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00203
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- From sum-rule analysis of XMCD spectra, the orbital moment in gamma-FeMn is approximately 0.003 muB/Fe atom.
  - `CLM-MEM-0037` · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00203
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)

### relative deviation

- **≈0.01 percent** — Next-Generation Sequencing (NGS) technologies have low error rates of approximately 0.01%.
  - `CLM-MEM-0013` · technology Next-Generation Sequencing (NGS) · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00125
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≤ 5 percent** — Third-Generation Sequencing (TGS) technologies have error rates up to 5%.
  - `CLM-MEM-0014` · technology Third-Generation Sequencing (TGS) · grade B · credibility unknown · measured · as of 2026-10-07
  - sources: SRC-00125
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **95 percent** — A differential encoding memristor-based artificial neural network achieves an MNIST handwritten digit recognition accuracy of 95%.
  - `CLM-MEM-0012` · encoding_scheme differential encoding, benchmark MNIST · grade B · credibility unknown · simulated · as of 2026-10-08
  - sources: SRC-00118
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **87.5 percent** — The experimental validation of MAGIC NOR logic primitive on printed Ag/ZnO/Au ECM memristors achieved an overall success rate of 87.5 %.
  - `CLM-MEM-0021` · device_technology printed Ag/ZnO/Au ECM memristors · grade B · credibility unknown · measured · as of 2026-10-14
  - sources: SRC-00169
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0081, CFL-0082 — see the open register
- **100 percent** — The experimental validation of MAGIC NOT logic primitive on printed Ag/ZnO/Au ECM memristors achieved an overall success rate of 100 %.
  - `CLM-MEM-0022` · device_technology printed Ag/ZnO/Au ECM memristors · grade B · credibility unknown · measured · as of 2026-10-14
  - sources: SRC-00169
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0081 — see the open register
- **95 percent** — The experimental validation of FELIX XOR logic primitive on printed Ag/ZnO/Au ECM memristors achieved an overall success rate of 95.0 %.
  - `CLM-MEM-0023` · device_technology printed Ag/ZnO/Au ECM memristors · grade B · credibility unknown · measured · as of 2026-10-14
  - sources: SRC-00169
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0082 — see the open register
- **1.25 percent** — Input switching was observed in 1.25 % of the tests for NOR and XOR operations on printed Ag/ZnO/Au ECM memristors.
  - `CLM-MEM-0024` · logic_primitives NOR and XOR · grade B · credibility unknown · measured · as of 2026-10-14
  - sources: SRC-00169
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **75.7 percent** — Under conventional placement in full-trace replay across 108 MoE FFN cases, the request-weighted row-conflict rate is 75.7%.
  - `CLM-MEM-0026` · placement conventional · grade B · credibility unknown · simulated · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **15.2 percent** — Under TileDRAM placement in full-trace replay across 108 MoE FFN cases, the request-weighted row-conflict rate is reduced to 15.2%.
  - `CLM-MEM-0027` · placement TileDRAM · grade B · credibility unknown · simulated · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.17 percent** — Address transformation in TileDRAM adds a geometric mean overhead of 0.17% over identity address generation across 108 measured kernel configurations on an RTX 3090.
  - `CLM-MEM-0028` · workload 108 measured kernel configurations · grade B · credibility unknown · measured · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **79.2 percent** — Retargeting six full-trace streams to six 3D DRAM organizations reduces row conflicts by 79.2% under TileDRAM.
  - `CLM-MEM-0031` · workload six full-trace streams, hardware_configuration six 3D DRAM organizations, method TileDRAM · grade B · credibility unknown · simulated · as of 2026-10-16
  - sources: SRC-00185
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **84.9 percent** — CwSG reaches 84.9% accuracy on SVHN in simulations using measured filamentary memristor trajectories.
  - `CLM-MEM-0032` · memory_technology filamentary memristor · grade B · credibility unknown · simulated · as of 2026-10-20
  - sources: SRC-00192
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **99.6907 percent** — The group verification pass rate at a threshold of 550 for Jetson Orin Nano is 0.996907.
  - `CLM-MEM-0038` · platform Jetson Orin Nano, threshold 550, verification_stage Group verification · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00218
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **49.8454 percent** — On Jetson Orin Nano, the expected pass rate after removing one correct bank mask in single function verification at a threshold of 550 is 0.498454.
  - `CLM-MEM-0039` · platform Jetson Orin Nano, threshold 550, verification_stage Single function verification · grade B · credibility unknown · measured · as of 2026-10-21
  - sources: SRC-00218
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### resistance

- **≈900 ohm** — In reference devices without AgNPs, electroformed devices show a high-resistance state of approximately 900 Ω.
  - `CLM-MEM-0001` · resistance_state high-resistance state · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00052
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### temperature

- **≈768.85 degC** — Random phase approximation analysis predicts a critical Curie temperature of approximately 1042 K for the 2D ferromagnetic order in realistic multi-orbital YCl model.
  - `CLM-MEM-0019` · model realistic multi-orbital model of YCl, onsite_hubbard_parameter 0.9 eV · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00148
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **≈801.85 degC** — Self-consistent Hartree-Fock calculation yields a critical Curie temperature of approximately 1075 K at filling number N = 3.8.
  - `CLM-MEM-0020` · method Hartree-Fock approximation · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00148
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### time

- **8079 ns** — For N=32 neurons, the single-array iteration time for the unenhanced Scan-select algorithm is 8079 ns.
  - `CLM-MEM-0015` · selection_algorithm unenhanced Scan-select · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00143
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0060 — see the open register
- **168423 ns** — For N=512 neurons, the single-array iteration time for the unenhanced Scan-select algorithm is 168423 ns.
  - `CLM-MEM-0016` · selection_algorithm unenhanced Scan-select · grade B · credibility unknown · simulated · as of 2026-10-14
  - sources: SRC-00143
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0060 — see the open register

### voltage

- **≈2.32 V** — The memristor device SET voltage occurs at approximately +2.32 V.
  - `CLM-MEM-0011` · device Ag/TiOx/NiOx/p++-Si device, operation SET voltage (V SET) · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00118
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0050` — length_device: _unexamined; classification pending_
  - claims: CLM-MEM-0008, CLM-MEM-0010
  - missing data: `not yet named`
- `CFL-0051` — length_device: _unexamined; classification pending_
  - claims: CLM-MEM-0009, CLM-MEM-0010
  - missing data: `not yet named`
- `CFL-0060` — time: _unexamined; classification pending_
  - claims: CLM-MEM-0015, CLM-MEM-0016
  - missing data: `not yet named`
- `CFL-0081` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-MEM-0021, CLM-MEM-0022
  - missing data: `not yet named`
- `CFL-0082` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-MEM-0021, CLM-MEM-0023
  - missing data: `not yet named`

## Evidence base

- claims: 39
- grades: {'B': 39}
- distinct sources: 13
