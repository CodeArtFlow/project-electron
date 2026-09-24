# Process — state of the art

Topic code `PROC`. Last reviewed 2026-09-24.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### length device

- **0.068 nm** — FRC analysis between AI inference and the ePIE reference in the held-out AuPd representative region yields a cutoff of 0.68 Å.
  - `CLM-PROC-0003` · defocus 30 nm · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00023
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **0.077 nm** — At 0 nm defocus on HEA-NP, FRC analysis relative to the ePIE reference yields a cutoff of 0.77 Å.
  - `CLM-PROC-0004` · material HEA-NP, defocus 0 nm · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00023
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### temperature

- **26.85 degC** — The silicon foil in the transmission simulations was thermalized to 300 K.
  - `CLM-PROC-0001` · thermal_model Debye model · grade B · credibility unknown · simulated · as of 2026-09-18
  - sources: SRC-00012
  - ⚙ automated extraction (gemini-3.6-flash; 2 quote(s) verified verbatim against the paper)

### time

- **≈270000 ns** — The workflow achieves an online latency of approximately 0.27 ms per probe position.
  - `CLM-PROC-0002` · hardware NVIDIA Tesla T4 GPU · grade B · credibility unknown · measured · as of 2026-09-22
  - sources: SRC-00023
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 4
- grades: {'B': 4}
- distinct sources: 2
