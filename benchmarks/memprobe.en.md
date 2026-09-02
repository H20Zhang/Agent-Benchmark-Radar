# MEMPROBE: auditing what the memory store actually retained

[中文](memprobe.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.24595) · [Code](https://github.com/sora1998/MemProbe)

## What it measures

MEMPROBE reconstructs hidden user state from final memory artifacts for 50 simulated users, covering 31 dimensions and 1,550 recovery targets. Full-store and top-k conditions separate information that was never written from information that exists but is hard to retrieve.

## Compared with what

Benchmarks that only score final answers mix write-side loss with retrieval and reader failure. MEMPROBE makes the memory artifact itself auditable and separates retention from accessibility.

## Score boundary

Recoverability supports how much structured user state survived in the artifact. It does not mean the information should have been stored or that it improves downstream behavior. Very high recovery can even reflect unnecessary profiling, so privacy and consent are independent evaluation objectives.

## Fair comparison conditions

Align synthetic personas, serialization, memory budget, slot filler/judge, and retrieval-query formulation; full-store and top-k belong in separate tracks.

## Next evaluation coordinate

The next step couples recoverability to consent, deletion, usefulness, and future action so “remember more” is not treated as the sole optimization target.
