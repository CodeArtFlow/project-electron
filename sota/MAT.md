# Materials — state of the art

Topic code `MAT`. Last reviewed 2026-09-25.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy

- **9.58102e-06 fJ** — The surface polar phonon energy for a SiO2 substrate is 59.8 meV.
  - `CLM-MAT-0001` · mechanism surface polar phonon, substrate SiO2 · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00004
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- **3.20435e-05 fJ** — The optical phonon energy in BLG is 200 meV.
  - `CLM-MAT-0002` · mechanism optical phonon · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00004
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)

### qualitative

- For the GaN-V N system using Training-set I, the RMSD of the 255-atom test supercell is 0.037 Å.
  - `CLM-MAT-0008` · grade B · credibility unknown · simulated · as of 2026-09-21
  - sources: SRC-00017
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- For SiO2-V O, increasing the number of small-supercell defect configurations reduces the energy error in the 323-atom test supercell from 0.184 eV for Training-set I to 0.023 eV for Training-set III.
  - `CLM-MAT-0009` · grade B · credibility unknown · simulated · as of 2026-09-21
  - sources: SRC-00017
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- When training on 16-atom defect supercells in the Cu2ZnSnS4-Cu-Zn system under the Defect-Only Scheme, the total-energy prediction error for the 128-atom test supercell is 21.231 eV.
  - `CLM-MAT-0010` · grade B · credibility unknown · simulated · as of 2026-09-21
  - sources: SRC-00017
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- When training on 16-atom defect supercells in the Cu2ZnSnS4-Cu-Zn system under the Defect-Only Scheme, the total-energy prediction error for the 288-atom test supercell is 51.484 eV.
  - `CLM-MAT-0011` · grade B · credibility unknown · simulated · as of 2026-09-21
  - sources: SRC-00017
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- For the SiO2-V 2+ O system in the Defect-Only Scheme with 17-atom defect supercells, the total-energy prediction error for the 323-atom test supercell reaches 46.080 eV.
  - `CLM-MAT-0012` · grade B · credibility unknown · simulated · as of 2026-09-21
  - sources: SRC-00017
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)

### temperature

- **-123.15 degC** — The temperature used in the acoustic phonon scattering calculation is 150 K.
  - `CLM-MAT-0003` · calculation acoustic phonon scattering · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00004
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)
- **-73.15 degC** — The temperature used in the optical phonon and surface polar phonon scattering calculations is 200 K.
  - `CLM-MAT-0004` · calculation optical phonon and surface polar phonon scattering · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00004
  - ⚙ automated extraction (gemini-3.6-flash; 1 quote(s) verified verbatim against the paper)

### thermal conductivity

- **22 W/(m*K)** — The measured cross-plane thermal conductivity of the (010) 𝛽-Ga2O3 substrate is 22 ± 2 W m-1 K-1.
  - `CLM-MAT-0006` · material 𝛽-Ga2O3 substrate, orientation (010), direction cross-plane · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00013
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **≈3100 W/(m*K)** — The extracted room-temperature thermal conductivity of the isotopically purified single-crystal diamond sample is approximately 3100 W m-1 K-1.
  - `CLM-MAT-0007` · temperature room-temperature, sample_13c_concentration ~0.00024% · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00015
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### time

- **0.0061 ns** — In optically excited monolayer MoS2, spin and orbital polarization decay at long times with a lifetime of 6.1 ps at 300 K.
  - `CLM-MAT-0005` · material monolayer MoS2, temperature 300 K, excitation_energy 1.7 eV · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00007
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 12
- grades: {'B': 12}
- distinct sources: 5
