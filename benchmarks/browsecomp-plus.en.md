# BrowseComp-Plus: fixing the corpus to separate agent and retriever progress

[中文](browsecomp-plus.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2508.06600) · [Code](https://github.com/texttron/BrowseComp-Plus)

## What it measures

BrowseComp-Plus converts BrowseComp-style deep search into roughly 830 queries over about 100K fixed, human-verified documents with positives and hard negatives. It reports retrieval recall, answer accuracy, and controlled-retriever conditions so that retriever, agent, and environment factors can be separated more cleanly than in a live-web stack.

## Compared with what

BrowseComp is realistic but provider ranking and web drift make reproduction and attribution difficult. A fixed corpus enables stronger matched comparisons: change the retriever while holding the agent fixed, or vice versa.

## Decisive evidence and current results

The ACL 2026 version reports Search-R1+BM25 at 3.86%, the GPT-5 benchmark agent at 55.9%, and GPT-5 with Qwen3-Embedding-8B retrieval at 70.1% with fewer search calls. Radar stores these as a separate paper snapshot. They should not be ranked directly against live BrowseComp's 51.5% Deep Research result or other corpus variants because the evaluation object differs.

## Fair comparison conditions

Align corpus/qrels, the 830-query subset, context cap, judge, search budget, and retriever. Different query-conditioned corpus construction or corpus scale requires a separate track.

## Score boundary and next evaluation coordinate

Fixed corpora improve attribution but remove freshness and provider interfaces. BrowseComp-Plus_CM later shows that query-conditioned small corpora can underestimate evidence-discovery difficulty, making corpus construction itself a visible variable.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use BrowseComp-Plus to compare deep-search policies and retrieval infrastructure over a fixed corpus, improving attribution relative to live web search. That control removes some drift and interface complexity, so it complements rather than replaces live-search evaluation.

### What a concrete task looks like

Illustrative task: an agent searches a fixed document collection across several rounds, progressively satisfying indirect constraints. A common corpus and interface make it easier to distinguish finding key documents from choosing productive follow-up searches.

### Most discriminating experiment

Cross retrievers with agents under fixed documents, top-k, and total calls, reporting evidence recall, answers, and cost. Expand distractors or use an independently assembled corpus to test whether gains depend on the curated candidate collection.

### Pair with

[browsecomp](browsecomp.en.md) · [browsecomp-plus-cm](browsecomp-plus-cm.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
