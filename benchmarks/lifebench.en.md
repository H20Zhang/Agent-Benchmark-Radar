# LifeBench: evaluating declarative and habitual/procedural memory in one long life trajectory

[中文](lifebench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

LifeBench constructs long, densely connected multi-source life events and evaluates both declarative facts and habitual/procedural patterns. A memory system must recover individual events and infer repeated behaviors, routines, and cross-event structure.

## Compared with what

Most conversational-memory benchmarks center on explicit factual QA. LifeBench brings non-declarative memory into the evaluation object, so retrieving all factual statements is no longer sufficient evidence that an agent has learned a user's recurring behavioral patterns.

## Decisive evidence and score boundary

The paper reports that top-tier memory systems reach only about 55.2% accuracy, leaving the coordinate far from saturated. This supports the difficulty of long-horizon life-pattern modeling; it does not identify storage, retrieval, or reasoning as the causal bottleneck because the evaluation remains end-to-end.

## Fair comparison conditions

Align event generation, task family, backbone, memory budget, and evaluator, and report declarative versus habitual/procedural slices separately. One aggregate score cannot diagnose the representation mechanism.

## Next evaluation coordinate

A stronger benchmark should make habitual/procedural memory influence later actions directly and test whether those patterns update when preferences change rather than becoming stale stereotypes.
