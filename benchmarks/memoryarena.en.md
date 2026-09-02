# MemoryArena: directly testing whether memory improves future action

[中文](memoryarena.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.16313) · [Code](https://github.com/ZexueHe/MemoryArena)

## What it measures

MemoryArena decomposes tasks into interdependent multi-session subtasks. Earlier actions and feedback must be distilled into memory and later used to guide shopping, search, travel, mathematics, and physics tasks. The endpoint is future task success rather than answering what happened previously.

## Compared with what

Traditional memory benchmarks often separate memorization from acting. MemoryArena closes a `Memory-Agent-Environment` loop so experience distillation, preference planning, and progressive search matter only when later behavior improves.

## Score boundary

Higher task success supports the claim that remembered experience improves later performance under the named agent/environment/harness. It does not isolate writing, retrieval, or planning as the causal mechanism. Retry budget, tool versions, and the agent model remain system-level confounders.

## Fair comparison conditions

Align backbone, environment snapshot, tool interface, session dependencies, and memory integration. A baseline with fewer tools or retries cannot support a memory-component attribution.

## Next evaluation coordinate

The next step needs longer-lived state, irreversible actions, permissions, and recovery so the downstream cost of stale or incorrect memory is measurable too.
