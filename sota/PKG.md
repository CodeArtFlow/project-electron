# Packaging — state of the art

Topic code `PKG`. Last reviewed 2026-10-19.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### qualitative

- HBF-Sim achieves 139.285 GB/s of array-service bandwidth when scaled to 16 channels.
  - `CLM-PKG-0001` · channel_count 16 channels, subarrays_per_channel 32 subarrays, read_latency 15 µs · grade B · credibility unknown · simulated · as of 2026-09-24
  - sources: SRC-00034
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### relative deviation

- **≤ ≈35 percent** — The brightness and EQE of the transferred chips undergo a maximum decrease of approximately 35% after the D-DLAT process.
  - `CLM-PKG-0004` · process D-DLAT, device transferred chips · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00160
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

### time

- **2.4995e+08 ns** — The captured Qwen3-1.7B decode sequence completes in 249.95 ms during execution in HBF-Sim.
  - `CLM-PKG-0002` · model Qwen3-1.7B, channels 16 channels, erase_latency 2000 µs · grade B · credibility unknown · simulated · as of 2026-09-24
  - sources: SRC-00034
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### wavelength

- **0.001 um** — The EL emission peak of the D-DLAT sample is red-shifted by 1 nm under an injection current of 9 mA.
  - `CLM-PKG-0003` · injection_current 9 mA, sample_type D-DLAT sample · grade B · credibility unknown · measured · as of 2026-10-15
  - sources: SRC-00160
  - ⚙ automated extraction (gemini-3.6-flash; 4 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 4
- grades: {'B': 4}
- distinct sources: 2
