# DeepResearch Bench: evaluating research artifacts, evidence, and citations

[中文](deepresearch-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2506.11763) · [Project](https://deepresearch-bench.github.io/) · [Code](https://github.com/Ayanami0730/deep_research_bench)

## What it actually measures

DeepResearch Bench evaluates agents that perform multi-step web exploration and produce **long-form, citation-rich research reports**. Its 100 expert-authored tasks span 22 fields and are paired with evaluation of both report quality and citation/retrieval effectiveness.

## What changed relative to prior evaluation

BrowseComp deliberately compresses output to a short factual answer. DeepResearch Bench changes the artifact: the system must select evidence, synthesize it into a coherent analysis, and ground claims with citations. The benchmark therefore measures information sufficiency and reporting quality together.

## Decisive evidence

Tasks are written by domain experts, with the topic distribution informed by a large sample of real web-search-enabled chatbot queries. RACE evaluates report quality with adaptive reference-based criteria, while FACT measures effective citation quantity and citation accuracy. This explicitly prevents polished prose from standing in for grounded research.

## What the score supports

The benchmark supports end-to-end deep-research quality under its report evaluators. It is difficult to attribute differences to retrieval, planning, or writing because all three affect the final report and the evaluation itself contains model/judge assumptions.

## Fair comparison contract

Fix search access, model/version, time/call/token budget, language, report length constraints, and evaluator version. Report citation metrics separately from holistic report quality. Web drift and search-provider differences should be treated as experimental variables.

## What remains unmeasured

One hundred high-cost tasks limit statistical resolution. Long-form reference/judge scoring can miss subtle factual or methodological errors, and real research often requires clarification, private corpora, computation, or iterative review with users.

## Next discriminating validation

Add claim-level evidence graphs and controlled retrieval-budget sweeps. Then measure whether report quality improves because the agent found better evidence or simply generated better prose from the same evidence set.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DeepResearch Bench for citation-rich long-form research deliverables rather than single-fact lookup. Report quality, citation correctness, and coverage can diverge. Length and fluency can obscure weak evidence, making holistic preference alone insufficient.

### What a concrete task looks like

Illustrative task: an agent decomposes a research question, gathers sources, and writes a structured report with claims and citations. It may miss sources, misread evidence, or overstate conclusions during writing. Final report quality alone cannot localize these causes.

### Most discriminating experiment

First compare writers over fixed evidence, then compare retrieval policies with a fixed writer, controlling report length and research budget. Add claim-level support review to test whether holistic-score gains reflect evidence rather than formatting, style, or evaluator preferences.

### Pair with

[claimprobe](claimprobe.en.md) · [litreview-arena](litreview-arena.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`hard web answer finding → citation-grounded report generation → auditable research workflow`

The benchmark moves search evaluation from answer discovery to research-artifact quality.