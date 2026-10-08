# Process — state of the art

Topic code `PROC`. Last reviewed 2026-10-08.

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
- **3.2 nm** — Multislice electron ptychography with joint Bayesian optimization yields an amorphous-layer thickness of 3.2 nm at a final FIB milling voltage of 2 kV.
  - `CLM-PROC-0011` · feature amorphous-layer thickness · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0029, CFL-0030, CFL-0031 — see the open register
- **5 nm** — Multislice electron ptychography with joint Bayesian optimization yields an amorphous-layer thickness of 5.0 nm at a final FIB milling voltage of 5 kV.
  - `CLM-PROC-0012` · feature amorphous-layer thickness · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0029, CFL-0032, CFL-0033 — see the open register
- **7 nm** — Multislice electron ptychography with joint Bayesian optimization yields an amorphous-layer thickness of 7.0 nm at a final FIB milling voltage of 8 kV.
  - `CLM-PROC-0013` · feature amorphous-layer thickness · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0030, CFL-0032, CFL-0034 — see the open register
- **26.4 nm** — Multislice electron ptychography with joint Bayesian optimization yields an amorphous-layer thickness of 26.4 nm at a final FIB milling voltage of 30 kV.
  - `CLM-PROC-0014` · milling_voltage 30 kV, feature amorphous-layer thickness · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0031, CFL-0033, CFL-0034 — see the open register
- **23.2 nm** — In the 2 kV region top subregion, joint Bayesian optimization yields a total specimen thickness of 23.2 nm.
  - `CLM-PROC-0015` · subregion top, milling_voltage 2 kV · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **24.5 nm** — In the 2 kV region middle subregion, joint Bayesian optimization yields a total specimen thickness of 24.5 nm.
  - `CLM-PROC-0016` · subregion middle, milling_voltage 2 kV · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **26.5 nm** — In the 2 kV region bottom subregion, joint Bayesian optimization yields a total specimen thickness of 26.5 nm.
  - `CLM-PROC-0017` · subregion bottom, milling_voltage 2 kV · grade B · credibility unknown · simulated · as of 2026-10-07
  - sources: SRC-00100
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### qualitative

- The scaling factor applied to SEM-EDS experimental results to account for detector efficiency and collection solid angle is 1.13.
  - `CLM-PROC-0010` · voltage 20 kV · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### relative deviation

- **≤ 1.1125 percent** — The maximum relative deviation between the third-order polynomial model fit and Monte Carlo simulations for characteristic X-ray yield is 1.1125%.
  - `CLM-PROC-0006` · voltage 20 kV, model third-order polynomial · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **≤ 0.5479 percent** — The maximum relative deviation between the fourth-order polynomial model fit and Monte Carlo simulations is 0.5479%.
  - `CLM-PROC-0007` · voltage 20 kV · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≤ 0.5461 percent** — The maximum relative deviation between the fifth-order polynomial model fit and Monte Carlo simulations is 0.5461%.
  - `CLM-PROC-0008` · voltage 20 kV · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≤ 0.3757 percent** — The maximum relative deviation between the sixth-order polynomial model fit and Monte Carlo simulations is 0.3757%.
  - `CLM-PROC-0009` · voltage 20 kV · grade B · credibility unknown · simulated · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

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
- **5.79e+09 ns** — The full-resolution GPU implementation of drift search took 5.79 s on an NVIDIA RTX PRO 6000 Blackwell GPU for a 2048 x 2048 silicon scan pair.
  - `CLM-PROC-0005` · hardware NVIDIA RTX PRO 6000 Blackwell GPU, implementation_type full-resolution implementation · grade B · credibility unknown · measured · as of 2026-09-25
  - sources: SRC-00037
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

Shown here, not in an appendix: a reader of this page must see the disagreement without navigating elsewhere.

- `CFL-0029` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0011, CLM-PROC-0012
  - missing data: `not yet named`
- `CFL-0030` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0011, CLM-PROC-0013
  - missing data: `not yet named`
- `CFL-0031` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0011, CLM-PROC-0014
  - missing data: `not yet named`
- `CFL-0032` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0012, CLM-PROC-0013
  - missing data: `not yet named`
- `CFL-0033` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0012, CLM-PROC-0014
  - missing data: `not yet named`
- `CFL-0034` — length_device: _unexamined; classification pending_
  - claims: CLM-PROC-0013, CLM-PROC-0014
  - missing data: `not yet named`

## Evidence base

- claims: 17
- grades: {'B': 17}
- distinct sources: 5
