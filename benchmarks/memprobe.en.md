# MEMPROBE: auditing what the memory artifact actually contains

[中文](memprobe.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.24595) · [Code](https://github.com/sora1998/MemProbe)

## What it actually measures

MEMPROBE evaluates the **memory artifact itself**. After an agent performs ordinary assistance for a simulated user, the benchmark asks how much of the user's hidden structured state can be reconstructed from the memory left behind. The target is therefore representation coverage, not whether the final assistant happened to answer one downstream question correctly.

## What changed relative to prior evaluation

End-task success can hide weak memory: a strong model may solve an immediate task from the current context even if its persistent memory is incomplete. MEMPROBE separates these two axes by evaluating assistance performance and then probing the stored artifact against hidden user-state dimensions.

## Decisive evidence

The benchmark uses 50 simulated users with 31 hidden dimensions each, yielding 1,550 recovery targets, and compares five representative memory conditions/systems. Assistance performance is close to saturation even for a memoryless condition, while category-balanced recovery from memory remains around 0.6 and falls further under top-k access. The central finding is that successful assistance and recoverable persistent memory are not equivalent.

## What the score supports

Recovery score is evidence about **what information survives into a queryable memory representation**. It is especially useful for diagnosing write/compression loss. It does not establish that retaining every recoverable attribute is desirable: privacy, minimization, and task relevance can make deliberate non-retention the correct behavior.

## Fair comparison contract

Fix the interaction history, hidden-state schema, write budget, memory access policy, and reconstruction model. Report full-artifact and top-k recovery separately; otherwise a representation-quality failure and a retrieval-interface failure are conflated. Memory size/cost should accompany coverage.

## What remains unmeasured

The benchmark does not directly score whether recovered memory improves future actions, nor whether stored attributes should legally or normatively be retained. Conflict resolution, temporal supersession, provenance, and deletion correctness require separate evaluation.

## Next discriminating validation

Pair each hidden-state dimension with downstream tasks and privacy labels. Then measure a Pareto frontier among recoverability, future utility, storage cost, and minimization instead of maximizing raw retention alone.

## Genealogy

`task success → persistent-memory artifact → representation coverage audit`

MEMPROBE exposes a hidden variable in memory research: the agent can look competent while leaving behind a poor long-term state.