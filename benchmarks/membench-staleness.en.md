# membench (staleness): ranking current facts ahead of stale facts

**English** | [中文](membench-staleness.md) · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, scenarios, and results](https://github.com/Ps23102004/membench)

## What it actually measures

This component benchmark measures **ranking correctness under memory updates and supersession**. When a store simultaneously contains an old fact, a newer replacement, negation, nearby entities, different validity windows, and distractors, can the system rank the currently valid state ahead of facts that must no longer be used and abstain when evidence is insufficient? Retrieval is not counted as successful merely because something relevant appears in top-k; stale-state leakage is a first-class failure.

## What changed relative to conventional recall benchmarks

Ordinary memory recall often asks only whether a gold fact appears somewhere in the retrieved set. If both stale and current versions are returned, recall can still look excellent. membench reports `staleness@1`, leakage, abstention, and contradiction resolution in addition to recall and precision, making **update semantics** separable from generic relevance. A public revision also replaced an invalid top-k staleness formulation and closed an abstention loophole that could inflate scores.

## Decisive evidence

The suite contains **60 executable probes** behind pluggable write/query/reset interfaces and reports recall, precision, `staleness@1`, leakage, abstention, contradiction resolution, and Wilson intervals. On **12 supersession probes, the embedding baseline returns a stale answer in 11 cases**; recency reranking reduces this to **0/12**. In this small controlled store, update-aware ranking therefore fixes a failure that semantic similarity alone handles poorly.

## What the score supports

The results support the claim that pure embedding retrieval is fragile to supersession in these hand-written probes and that recency-aware reranking sharply reduces stale top-1 results. They do not establish that recency is sufficient for large-scale long-term memory: real updates are not always monotonic, and an older fact can remain correct within a particular time interval or context.

## Fair comparison contract

Memory records, timestamp semantics, write/query API, embedding model, top-k, abstention policy, and exact-substring evaluator should be aligned. Methods should report both current-fact recall and stale leakage so aggressive filtering cannot appear better by suppressing both. Recency methods should also report sensitivity to k because candidate-set changes alter whether the current fact is visible at all.

## How to use it in research

The suite is useful as a **unit test for update mechanisms**, including timestamp-aware scoring, conflict resolution, versioned memory, forgetting policies, and consolidation. A full memory system can first demonstrate component correctness here and then move to a long-horizon agent benchmark to test whether improved ranking changes future actions rather than only retrieval output.

## Next discriminating validation

The main gaps are scale, natural data, complex validity intervals, and downstream action. A high-value next benchmark would include multi-step supersession chains, non-monotonic rollback, time-bounded facts, and entity conflicts and compare recency ranking, explicit version graphs, and learned conflict resolvers under the same retrieval budget, measuring both current-state accuracy and historical traceability.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use membench (staleness) as a quick regression test for stale-fact handling, not as the main evidence for general memory quality. It tests whether current facts outrank superseded ones. Passing small exact-match probes does not establish reliable state understanding in complex histories.

### What a concrete task looks like

Illustrative task: a fact about an entity is stored and later negated or superseded. A query should return the operative value rather than a forbidden old one. Returning nothing may reduce stale outputs without satisfying legitimate retrieval.

### Most discriminating experiment

Track operative-fact retrieval, stale-fact rank, and abstention together. Keep the metric definition stable while sweeping top-k. Add paraphrases and larger distractor stores to test whether success relies on exact substrings or tiny collections.

### Pair with

[statemembench](statemembench.en.md) · [longmemeval](longmemeval.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`map_delta=early_signal`, bound to `memory-update-and-staleness`. The corrected metrics make the suite useful as a component diagnostic, but **60 related hand-written probes, one author, and a small store** are not enough to establish a durable field shift. Broader evidence is needed before update-aware evaluation becomes a required coordinate of long-term-memory benchmarking.
