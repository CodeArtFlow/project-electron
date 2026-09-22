# Photonics — state of the art

Topic code `PHOT`. Last reviewed 2026-09-22.

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

### relative deviation

- **85 percent** — The optical hyperdimensional computing system achieved 85% classification accuracy on the Iris test set.
  - `CLM-PHOT-0005` · dataset Iris test set · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00014
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)
- **88 percent** — The experimental optical HDC classification on the MNIST dataset achieved 88% accuracy.
  - `CLM-PHOT-0006` · dataset MNIST, setup experimental system · grade B · credibility unknown · measured · as of 2026-09-21
  - sources: SRC-00014
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0012` — length_device: _unexamined; classification pending_
  - claims: CLM-PHOT-0007, CLM-PHOT-0009
  - missing data: `not yet named`
- `CFL-0013` — length_device: _unexamined; classification pending_
  - claims: CLM-PHOT-0008, CLM-PHOT-0010
  - missing data: `not yet named`

## Evidence base

- claims: 10
- grades: {'B': 10}
- distinct sources: 3
