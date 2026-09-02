# MemGUI-Bench: testing experience reuse through repeated GUI execution

[中文](memgui-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.06075) · [Code](https://github.com/lgy0404/MemGUI-Bench)

## What it measures

MemGUI-Bench contains 128 tasks in 64 mirror pairs across 26 mobile applications and 68 scenarios; 89.8% require cross-temporal or cross-spatial retention. Pass@k, trajectories, and progressive scrutiny measure short-term retention, cross-session learning, cross-application transfer, and failure recovery.

## Compared with what

MemoryArena already makes memory affect future action. MemGUI-Bench places that action in executable mobile UI, asking whether steps, failures, and visual state from an earlier attempt help later execution rather than only reusing experience in text environments.

## Score boundary

Higher pass@k supports experience reuse under the named mobile snapshot, agent, and retry budget. It does not isolate the memory module because UI perception, runtime behavior, and retries are load-bearing confounders.

## Fair comparison conditions

Align app/runtime snapshot, backbone, perception model, judge, and retry budget. Cross-version comparisons can reflect UI drift rather than memory progress.

## Next evaluation coordinate

The next step is long-lived real-device state, permissions, and irreversible actions, where memory-induced mistakes and recovery become first-class outcomes.
