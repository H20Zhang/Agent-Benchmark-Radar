# MemFuseBench: Agent Memory / cross-source fusion

[中文](memfusebench.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.18704) · [Data](https://github.com/Darwin-Agent/Mi-Memory/tree/master/MemFuse/MemFuseBench)

Moves from single-history recall to linking, causal fusion, conflict handling, and provenance across devices, users, and time.

## Genealogy: What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can a system select, fuse, and arbitrate source-tagged memories without losing provenance?

**Measurement object:** Cross-source memory benchmark for linking, causal fusion, conflict arbitration, and provenance over heterogeneous event streams.

**Scale and protocol:** 357 questions over 7,823 source-tagged events with six diagnostic categories. The protocol includes evidence-checklists, adversarial-distractors, six-diagnostic-categories.

## What a Score Can Support

The 357 questions, 7,823 events, and six diagnostics isolate linking, causal fusion, conflict handling, and provenance. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Synthetic generation and model-guided verification lack a human ceiling and do not establish external validity on real user histories. The load-bearing confounders are synthetic-generator-style, model-guided-verification, missing-human-ceiling.

## Remaining Gap: What It Still Does Not Measure

Synthetic construction and model-guided verification have no human ceiling or demonstrated real-world external validity.

## Genealogy: Where It Fits in the Map

`map_delta=early_signal`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MemFuseBench for linking, conflict resolution, and provenance across memory sources. A longer context alone is not a sufficient control. Compare whether the same evidence supports correct conclusions with source relationships retained or removed.

### What a concrete task looks like

Illustrative task: one source records an event, another explains its cause, and a third revises the information. The agent must align records and justify the operative version. Concatenation can conflate separate events or different authority levels.

### Most discriminating experiment

Compare identical events without source tags, with source tags, and with explicit cross-source links. Report linking, fusion, arbitration, and provenance separately. Add conflicting but textually similar sources to test use of source structure rather than generator style.

### Pair with

[lifebench](lifebench.en.md) · [gatemem](gatemem.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
