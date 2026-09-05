# GateMem: useful shared memory under access control and deletion

[中文](gatemem.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.18829) · [Code](https://github.com/rzhub/GateMem)

## What it actually measures

GateMem evaluates whether a shared-memory agent can remain useful while enforcing **who may access which memory and what must be forgotten**. It models multiple principals across medical, office, education, and household scenarios, with long-form episodes, incremental memory injection, hidden checkpoints, access boundaries, and deletion targets.

## What changed relative to prior evaluation

Most memory benchmarks reward remembering more. Privacy benchmarks often test leakage without measuring whether the system remains useful. GateMem makes the tension explicit: utility, access-control violations, and deletion leakage are scored together. A system cannot win by storing everything, and it cannot win by refusing to remember anything.

## Decisive evidence

The evaluation finds no tested approach simultaneously strong on utility, access control, and active forgetting. Long-context baselines can provide strong governance behavior but pay high token cost, while retrieval/external-memory approaches reduce cost yet can surface unauthorized or deleted information. The released evaluator tracks utility together with privacy and deletion leakage rather than collapsing them into one accuracy number.

## What the score supports

GateMem supports a claim about the **governed memory system** under a specific principal/policy model. It does not isolate whether a leak originates in storage, indexing, retrieval filtering, generation, or policy interpretation. A good aggregate score therefore should be accompanied by the separate utility/access/deletion axes.

## Fair comparison contract

Fix principals, policy rules, deletion requests, memory history, model, retrieval top-k, and query set. Measure latency/token/storage overhead because stricter governance may be achieved by expensive full-context inspection. Do not expose hidden leak-target annotations to the agent; they are evaluator metadata, not task input.

## What remains unmeasured

Real enterprise policies include nested groups, delegated authority, purpose limitation, retention schedules, auditability, and policy changes over time. Cryptographic deletion and physical data erasure are also outside a language-level benchmark.

## Next discriminating validation

Separate policy enforcement at write, index, retrieval, and generation time under the same tasks. The key systems question is where to enforce access/deletion constraints so that violations fall without paying full-context cost.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use GateMem for shared-memory utility, access boundaries, and deletion behavior. The goal is not simply to conceal everything sensitive but to retain authorized usefulness while preventing unauthorized access. Behavioral non-disclosure is not proof of physical erasure.

### What a concrete task looks like

Illustrative task: multiple participants contribute information under different access rules, a later request seeks content reserved for another role, and a deletion request follows. The agent must condition memory use on identity, purpose, and time rather than merely detect sensitive keywords.

### Most discriminating experiment

Pair authorized, unauthorized, and post-deletion queries under fixed storage and retrieval, then compare policy implementations. Report legitimate utility, unauthorized disclosure, and post-deletion recovery separately. Deployment claims additionally require authentication and storage-erasure checks.

### Pair with

[sp-mem](sp-mem.en.md) · [utility-under-attack](utility-under-attack.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`remember more → remember selectively → governed multi-principal memory`

GateMem turns privacy and forgetting from caveats into first-class memory-system objectives.