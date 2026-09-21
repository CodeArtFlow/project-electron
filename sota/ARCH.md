# Architecture — state of the art

Topic code `ARCH`. Last reviewed 2026-09-20.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy advantage ratio

- **≤ ≈5 ×** — Across the functional region of its simulated PFAL gate library, PFAL shows an energy advantage over static CMOS of up to approximately 5x at the most favorable operating point.
  - `CLM-ARCH-0002` · process TSMC 16nm FinFET, comparison PFAL vs static CMOS, operating_point most favorable operating point, vclk 1 V, fclk 100 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001
- **≤ 3.83 ×** — Optimized single-gate PFAL cells achieve up to 3.83x lower energy than equivalent static CMOS gates in simulation.
  - `CLM-ARCH-0004` · process TSMC 16nm FinFET, comparison single-gate PFAL vs static CMOS, power_clock trapezoidal, operating_point minimum-energy points of the parameter sweep (Table 2) · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **≤ 1.32 ×** — Sinusoidal power-clock excitation improves PFAL gate energy by up to 1.32x over trapezoidal excitation in simulation.
  - `CLM-ARCH-0005` · process TSMC 16nm FinFET, comparison sinusoidal vs trapezoidal power-clock, gate_at_maximum XOR/XNOR, vclk_at_maximum 0.5 V, fclk_at_maximum 384 MHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002
- **≤ 5.3 ×** — A 4-bit Brent-Kung carry look-ahead adder in PFAL reaches up to 5.3x energy gain over a static CMOS estimate in simulation.
  - `CLM-ARCH-0006` · process TSMC 16nm FinFET, comparison 4-bit Brent-Kung CLA adder vs architecture-matched static CMOS estimate, power_clock triangular · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00002

### energy delay product

- **1.23e-26 J*s** — Low-threshold PFAL Buffer/NOT cell reaches a minimum energy-delay product of 1.23e-26 J*s in simulation.
  - `CLM-ARCH-0001` · process TSMC 16nm FinFET, cell low-threshold Buffer/NOT, vclk 0.6 V, fclk 7.94 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001

### relative deviation

- **≤ 2 percent** — With a quadrature-VCO power-clock, PFAL Buffer/NOT energy stays within 2% of the ideal sinusoidal power-clock case at 3 GHz.
  - `CLM-ARCH-0003` · process TSMC 16nm FinFET, comparison quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell Buffer/NOT, fclk 3 GHz · grade B · credibility unknown · simulated · as of 2026-09-17
  - sources: SRC-00001

## Live contradictions in this layer

_None._

## Evidence base

- claims: 6
- grades: {'B': 6}
- distinct sources: 2
