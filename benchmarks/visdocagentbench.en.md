# VisDocAgentBench: RAG / agentic visual-document retrieval

[中文](visdocagentbench.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.17889) · [Code](https://github.com/hulx2002/VisDocAgentBench) · [Data](https://huggingface.co/datasets/hulx2002/VisDocAgentBench)

Compares static rankers with search/inspection agents under the same ranked-page output.

## Genealogy: What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can an agent use search, visual inspection, and OCR to place distributed evidence pages in the top 10?

**Measurement object:** Visual-document retrieval benchmark that compares static rankers and iterative visual/OCR agents under one ranked-page contract.

**Scale and protocol:** 2,375 pages from 100 documents and 120 queries, with 1,469 redistributable page images. The protocol includes shared-top-10-contract, twelve-action-agent-budget, support-provided-intervention.

## What a Score Can Support

Across 2,375 pages and 120 queries, a shared top-10 contract plus support interventions and ablations makes discovery and inspection visible. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

The 120 queries, six cross-document paths, and unmatched agent routes limit causal attribution to a planner or vision component. The load-bearing confounders are small-query-set, planner-model-tool-mismatch, few-cross-document-paths.

## Remaining Gap: What It Still Does Not Measure

Only 120 queries and six cross-document paths; planner, model, and tool routes are not capacity matched.

## Genealogy: Where It Fits in the Map

`map_delta=reinforces`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use VisDocAgentBench to compare static visual ranking with iterative page inspection under a common ranking contract and action budget. When iterative agents use stronger models or more tools, score differences first describe systems rather than the causal value of iteration.

### What a concrete task looks like

Illustrative task: a system ranks scientific-document pages using static representations or opens pages to inspect figures and OCR before reranking. Newly inspected evidence should affect selection rather than merely increase the number of calls.

### Most discriminating experiment

Share candidate sets, visual backbone, and final top-k between static and iterative methods, with a supplied-support-page control. Track ranking gains per inspection and report redistributable and complete page collections separately to control artifact availability.

### Pair with

[mc-search](mc-search.en.md) · [maple](maple.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
