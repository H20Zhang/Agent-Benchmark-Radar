# WANDR: RAG / live wide-and-deep search

[中文](wandr.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.14747) · [Benchmark](https://github.com/perplexityai/wandr)

Extends answer search to open-set discovery, hierarchical enrichment, and record-level refetch verification.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can an agent discover, enrich, and verify live-web records without knowing the complete set?

**Measurement object:** Live-web benchmark for wide-and-deep record collection with hierarchical tasks and reference-free record verification.

**Scale and protocol:** 500 self-contained Harbor task packages for wide and deep live-web collection. The protocol includes required-volume-denominators, record-level-url-excerpt-refetch, soft-and-hard-f1.

## What a Score Can Support

Five hundred Harbor task packages use required-volume denominators and URL/excerpt refetch to expose losses in discovery, support, and enrichment. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Unmatched stacks, a shared fetch backend, web drift, and an LLM judge make the results system-level evidence only. The load-bearing confounders are unmatched-system-stacks, shared-fetch-backend, web-drift, llm-judge.

## What It Still Does Not Measure

Live pages drift, the grader uses an LLM and fetch backend, and system providers, models, search tools, and harnesses are unmatched.

## Where It Fits in the Map

`map_delta=reinforces`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use WANDR for open-web research requiring broad discovery and deep enrichment of each record. Record-level verification reduces dependence on exhaustive gold sets, but valid records do not establish completeness. Distinguish discovery volume, validity, and enrichment quality.

### What a concrete task looks like

Illustrative task: an agent finds qualifying objects and supplies fields, source pages, and supporting excerpts for each. Many names with unreliable fields and a few excellent records with poor coverage are different failures.

### Most discriminating experiment

Fix requested volume, search tools, and fetch budget. Report deduplicated discovery, record validity, and field enrichment separately. Cache grading-time source snapshots and inspect unavailable pages so web drift or grader-fetch failures are not attributed to the research agent.

### Pair with

[gisa](gisa.en.md) · [autoresearchbench](autoresearchbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->


## Remaining gap and next validation

What remains unmeasured is stability across settings and transfer to realistic workflows. The next experiment should hold model and budget fixed and add deployment-like tasks to test whether gains come from the target capability itself.

## What changed relative to precursors

Compared with precursors on the same research line, its value is the newly explicit task boundary described above. The meaningful comparison is the added measurement coordinate, not dataset size alone.