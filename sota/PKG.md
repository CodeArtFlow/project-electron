# Packaging — state of the art

Topic code `PKG`. Last reviewed 2026-10-07.

> Derived from the claim ledger. Every statement traces to a claim; nothing here is composed freehand.

## Current position

### qualitative

- HBF-Sim achieves 139.285 GB/s of array-service bandwidth when scaled to 16 channels.
  - `CLM-PKG-0001` · channel_count 16 channels, subarrays_per_channel 32 subarrays, read_latency 15 µs · grade B · credibility unknown · simulated · as of 2026-09-24
  - sources: SRC-00034
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

### time

- **2.4995e+08 ns** — The captured Qwen3-1.7B decode sequence completes in 249.95 ms during execution in HBF-Sim.
  - `CLM-PKG-0002` · model Qwen3-1.7B, channels 16 channels, erase_latency 2000 µs · grade B · credibility unknown · simulated · as of 2026-09-24
  - sources: SRC-00034
  - ⚙ automated extraction (gemini-3.6-flash; 5 quote(s) verified verbatim against the paper)

## Live contradictions in this layer

_None._

## Evidence base

- claims: 2
- grades: {'B': 2}
- distinct sources: 1
