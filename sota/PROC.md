# Process — state of the art

Topic code `PROC`. Last reviewed 2026-10-25.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### energy

- **1.45798e-05 fJ** — The root-mean-square deviation of the formation free energy per formula unit for fluorides is reduced to 0.091 eV.
  - `CLM-PROC-0031` · error_metric root-mean-square deviation per formula unit · grade B · credibility unknown · simulated · as of 2026-10-13
  - sources: SRC-00137
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### frequency

- **7.9 GHz** — The two-channel holder equipped with a representative Si/Si3N4 TEM chip exhibits a -3 dB bandwidth of 7.9 GHz.
  - `CLM-PROC-0032` · holder_type two-channel holder, chip_type Si/Si3N4 chip, metric -3 dB bandwidth · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00152
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)
- **≈4.5 GHz** — For the four-channel configuration, the -3 dB bandwidth reaches approximately 4.5 GHz.
  - `CLM-PROC-0033` · holder_type four-channel configuration, metric -3 dB bandwidth · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00152
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

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
- **50 nm** — Experimental vertically oriented wide-trench lines milled through a gold film achieved a linewidth of 50.0±2.7 nm.
  - `CLM-PROC-0030` · feature wide -trench line · grade B · credibility unknown · measured · as of 2026-10-09
  - sources: SRC-00133
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≤ 150 nm** — For slab-style parameterization training data generation, total layer thickness is restricted not to exceed 1500 Angstroms.
  - `CLM-PROC-0036` · parameterization_type slab-style · grade B · credibility unknown · simulated · as of 2026-10-21
  - sources: SRC-00195
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)

### qualitative

- The scaling factor applied to SEM-EDS experimental results to account for detector efficiency and collection solid angle is 1.13.
  - `CLM-PROC-0010` · voltage 20 kV · grade B · credibility unknown · measured · as of 2026-10-01
  - sources: SRC-00064
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- For a 330 µm-wide deflector, the FEM calculated deflection angle per unit applied voltage is 16 µrad·V-1.
  - `CLM-PROC-0034` · slit_width 330 µm, method finite-element modelling · grade B · credibility unknown · simulated · as of 2026-10-15
  - sources: SRC-00152
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

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
- **0.023 percent** — For the grade 1 no-target group of 34 public test images, training with all 244 images resulted in a false-positive area fraction of 0.023%.
  - `CLM-PROC-0018` · training_set_size full 244-image public training set, test_subset No target, grade 1 (including mapped −1) · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00107
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
- **0.624 percent** — On 10 confirmed negative internal test images, the mean-score ensemble yielded a false-positive area fraction of 0.624%.
  - `CLM-PROC-0019` · test_dataset 10 images confirmed negative by multiple observers · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00107
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **4.5 percent** — For the polycrystalline rolled Au reference sample, the mean normalized mean absolute error (NMAE) is 4.5% across 10 continuous measurements.
  - `CLM-PROC-0020` · material polycrystalline rolled Au, measurement_type 10-times continuous measurement · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0035, CFL-0036, CFL-0037, CFL-0038 — see the open register
- **162 percent** — For the polycrystalline rolled Au reference sample, the mean RMSE-to-MAE ratio (RMR) is 1.62 across 10 continuous measurements.
  - `CLM-PROC-0021` · material polycrystalline rolled Au, measurement_type 10-times continuous measurement · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0035, CFL-0039, CFL-0040, CFL-0041 — see the open register
- **215 percent** — For the polycrystalline rolled Au sample, the mean Durbin-Watson (DW) statistic is 2.15 across 10 continuous measurements.
  - `CLM-PROC-0022` · material polycrystalline rolled Au, measurement_type 10-times continuous measurement · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0036, CFL-0039, CFL-0042, CFL-0043 — see the open register
- **4.2 percent** — For the polycrystalline rolled Au sample, the mean difference of the coefficients of determination (∆R2) is 0.042 across 10 continuous measurements.
  - `CLM-PROC-0023` · material polycrystalline rolled Au, measurement_type 10-times continuous measurement · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0037, CFL-0040, CFL-0042, CFL-0044 — see the open register
- **184 percent** — For the polycrystalline rolled Au sample, the mean optimal exponent n is 1.84.
  - `CLM-PROC-0024` · material polycrystalline rolled Au · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0038, CFL-0041, CFL-0043, CFL-0044 — see the open register
- **≈5700 percent** — Applying a two-component model to the 30th PYS measurement of the heavily doped p-type Si (PL) sample improves the AIC by approximately 57 relative to the single-component model.
  - `CLM-PROC-0025` · measurement_number 30th measurement · grade B · credibility unknown · measured · as of 2026-10-08
  - sources: SRC-00109
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **≈13.2 percent** — The mean W-column phase increases by approximately 13.2% from the monolayer to the bilayer region.
  - `CLM-PROC-0026` · material WS2 · grade B · credibility unknown · measured · as of 2026-10-09
  - sources: SRC-00129
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0056 — see the open register
- **4.7 percent** — The mean W-column phase increases by 4.7% from the bilayer to the trilayer region.
  - `CLM-PROC-0027` · material WS2 · grade B · credibility unknown · measured · as of 2026-10-09
  - sources: SRC-00129
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0056 — see the open register
- **≈12.5 percent** — Simulations show an increase of about 12.5% in simulated mean phase value from monolayer to bilayer.
  - `CLM-PROC-0028` · model ttWS2 simulation model · grade B · credibility unknown · simulated · as of 2026-10-09
  - sources: SRC-00129
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0057 — see the open register
- **≈4.4 percent** — Simulations show an increase of about 4.4% in simulated mean phase value from bilayer to trilayer.
  - `CLM-PROC-0029` · model ttWS2 simulation model · grade B · credibility unknown · simulated · as of 2026-10-09
  - sources: SRC-00129
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
  - **live contradiction:** CFL-0057 — see the open register
- **5 percent** — The full spin-resolved PNR synthetic data emulation applies a magnetic field resolution smearing dq/q of 0.05.
  - `CLM-PROC-0035` · data_type synthetic full spin-resolved PNR data · grade B · credibility unknown · simulated · as of 2026-10-21
  - sources: SRC-00195
  - ⚙ automated extraction (gemini-3.6-flash; 3 quote(s) verified verbatim against the paper)
- **1000 percent** — For the polymer-brush example parameterization, the continuous brush profile is discretized into 10 slices of equal thickness.
  - `CLM-PROC-0037` · model polymer-brush · grade B · credibility unknown · simulated · as of 2026-10-21
  - sources: SRC-00195
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
- `CFL-0035` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0020, CLM-PROC-0021
  - missing data: `not yet named`
- `CFL-0036` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0020, CLM-PROC-0022
  - missing data: `not yet named`
- `CFL-0037` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0020, CLM-PROC-0023
  - missing data: `not yet named`
- `CFL-0038` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0020, CLM-PROC-0024
  - missing data: `not yet named`
- `CFL-0039` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0021, CLM-PROC-0022
  - missing data: `not yet named`
- `CFL-0040` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0021, CLM-PROC-0023
  - missing data: `not yet named`
- `CFL-0041` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0021, CLM-PROC-0024
  - missing data: `not yet named`
- `CFL-0042` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0022, CLM-PROC-0023
  - missing data: `not yet named`
- `CFL-0043` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0022, CLM-PROC-0024
  - missing data: `not yet named`
- `CFL-0044` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0023, CLM-PROC-0024
  - missing data: `not yet named`
- `CFL-0056` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0026, CLM-PROC-0027
  - missing data: `not yet named`
- `CFL-0057` — relative_deviation: _unexamined; classification pending_
  - claims: CLM-PROC-0028, CLM-PROC-0029
  - missing data: `not yet named`

## Evidence base

- claims: 37
- grades: {'B': 37}
- distinct sources: 12
