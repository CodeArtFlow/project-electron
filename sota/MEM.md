# Memory — state of the art

Topic code `MEM`. Last reviewed 2026-10-12.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

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

### resistance

- **≈900 ohm** — In reference devices without AgNPs, electroformed devices show a high-resistance state of approximately 900 Ω.
  - `CLM-MEM-0001` · resistance_state high-resistance state · grade B · credibility unknown · measured · as of 2026-09-29
  - sources: SRC-00052
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

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

## Evidence base

- claims: 14
- grades: {'B': 14}
- distinct sources: 5
