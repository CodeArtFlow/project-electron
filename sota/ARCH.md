# Architecture — state of the art

Topic code `ARCH`. Last reviewed 2026-09-20.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy advantage ratio

- **5 dimensionless** — Single-gate PFAL cells show an energy advantage over static CMOS of approximately 5x in simulation.
  - `CLM-ARCH-0002` · process TSMC 16nm FinFET, comparison single-gate PFAL vs static CMOS, operating_point maximum over the sweep, at reduced frequency and elevated supply · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001
- **1.02 dimensionless** — With a quadrature-VCO power-clock, PFAL Buffer/NOT energy stays within 2% of the ideal sinusoidal case.
  - `CLM-ARCH-0003` · process TSMC 16nm FinFET, comparison QVCO power-clock vs ideal sinusoid, fclk 3 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001
- **3.83 dimensionless** — Optimized single-gate PFAL cells achieve up to 3.83x lower energy than equivalent static CMOS gates in simulation.
  - `CLM-ARCH-0004` · process TSMC 16nm FinFET, comparison single-gate PFAL vs static CMOS, operating_point EDP-optimal over power-clock amplitude, frequency and waveform · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **1.32 dimensionless** — Sinusoidal power-clock excitation improves PFAL energy by up to 1.32x over trapezoidal excitation.
  - `CLM-ARCH-0005` · process TSMC 16nm FinFET, comparison sinusoidal vs trapezoidal power-clock · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **5.3 dimensionless** — A 4-bit Brent-Kung carry look-ahead adder in PFAL reaches up to 5.3x energy gain over a static CMOS estimate.
  - `CLM-ARCH-0006` · process TSMC 16nm FinFET, comparison 4-bit Brent-Kung CLA adder vs static CMOS estimate, power_clock triangular · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002

### energy delay product

- **1.23e-26 J*s** — Low-threshold PFAL Buffer/NOT cell reaches a minimum energy-delay product of 1.23e-26 J*s in simulation.
  - `CLM-ARCH-0001` · process TSMC 16nm FinFET, cell low-threshold Buffer/NOT, vclk 0.6 V, fclk 7.94 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001

## Live contradictions in this layer

_None._

## Evidence base

- claims: 6
- grades: {'B': 6}
- distinct sources: 2
