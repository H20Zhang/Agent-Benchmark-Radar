# DAS-Bench / DAS-Eval: RAG / academic-survey artifact

[中文](das-bench.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.18034) · [Benchmark and evaluator](https://github.com/ZhikaiXu24/DAS) · [Data](https://huggingface.co/datasets/ZhikaiXu24/DAS-Bench)

Extends retrieval/drafting into a revisable protocol for literature, taxonomy, claims, citations, discourse, and rendered artifacts.

## Genealogy: What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can a system assemble literature evidence into an auditable, readable, publication-oriented survey?

**Measurement object:** Academic-survey benchmark and evaluator that score literature coverage, taxonomy, claims, citations, discourse, and rendered artifact quality.

**Scale and protocol:** 30 topics across computer science and non-CS fields, with a matched 21-topic comparison subset. The protocol includes sixteen-criterion-evaluator, semantic-and-deterministic-checks, blinded-expert-comparison.

## What a Score Can Support

Thirty topics and 16 criteria combine deterministic citation checks with blinded expert comparison across evidence, taxonomy, claims, discourse, and artifact quality. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Generation-backbone and main-judge coupling plus closed-system native configurations keep cross-system gaps at the system level. The load-bearing confounders are generator-judge-coupling, closed-system-native-configurations, judge-sensitivity.

## Remaining Gap: What It Still Does Not Measure

The generation method is not yet public, and the shared generation backbone is also the main automatic judge.

## Genealogy: Where It Fits in the Map

`map_delta=early_signal`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DAS-Bench and DAS-Eval for academic surveys as complete artifacts, including literature organization, claims, citations, and presentation. Multiple criteria are richer than stylistic preference, but shared or related generation and grading models require independent bias checks.

### What a concrete task looks like

Illustrative task: from a topic and paper pool, a system builds a taxonomy, organizes arguments, and produces a readable survey. Broad coverage with a poor taxonomy and polished presentation with unsupported claims are different artifact failures.

### Most discriminating experiment

Fix the paper pool and generation budget, obtain blinded human pairwise judgments, and test whether automatic metrics preserve the ranking. Score rendering and argument quality separately and repeat across evaluators to distinguish style preference from research quality.

### Pair with

[litreview-arena](litreview-arena.en.md) · [claimprobe](claimprobe.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
