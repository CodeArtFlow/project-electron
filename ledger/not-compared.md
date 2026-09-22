# Not compared

**Generated artifact - do not edit by hand.** Produced by `pipeline/reconcile.py --detect`.

Pairs of claims that measure the same quantity in the same unit and disagree numerically, but share **no subject context**: no condition, named on both with an equal value, that says what was measured (operating points such as temperature do not count; see `reference/comparability.yaml`). They were not compared, so no conflict was opened. They are listed so that is visible. A pair here is a reason to look at the two claims' conditions, not a finding.

**9 pair(s)** as of 2026-09-22.

## `length_device` (4 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0007` = 0.00023 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0008` = 0.00033 um | 100% | parameter=signal-ground electrode spacing | sample=bare silicon substrate, roughness_type=root mean square roughness (Sq) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0009` = 0.0017 um | 100% | parameter=signal-ground electrode spacing | roughness_type=arithmetic average roughness (Sa) |
| `CLM-PHOT-0004` = 7 um | `CLM-PHOT-0010` = 0.0021 um | 100% | parameter=signal-ground electrode spacing | roughness_type=root mean square roughness (Sq) |

## `relative_deviation` (4 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-ARCH-0003` = 2 percent | `CLM-PHOT-0006` = 88 percent | 98% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | dataset=MNIST, setup=experimental system |
| `CLM-ARCH-0003` = 2 percent | `CLM-PHOT-0005` = 85 percent | 98% | process=TSMC 16nm FinFET, comparison=quadrature-VCO power-clock vs ideal sinusoidal power-clock, cell=Buffer/NOT, fclk=3 GHz | dataset=Iris test set |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-PHOT-0006` = 88 percent | 84% | device=H200, baseline=CA Overlap, variant=AN Overlap | dataset=MNIST, setup=experimental system |
| `CLM-ARCH-0015` = 14.3 percent | `CLM-PHOT-0005` = 85 percent | 83% | device=H200, baseline=CA Overlap, variant=AN Overlap | dataset=Iris test set |

## `thermal_conductivity` (1 pair(s))

| Claim A | Claim B | Gap | A's conditions | B's conditions |
|---|---|---|---|---|
| `CLM-MAT-0006` = 22 W/(m*K) | `CLM-MAT-0007` = 3100 W/(m*K) | 99% | material=𝛽-Ga2O3 substrate, orientation=(010), direction=cross-plane | temperature=room-temperature, sample_13c_concentration=~0.00024% |
