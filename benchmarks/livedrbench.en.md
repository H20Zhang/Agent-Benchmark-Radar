# LiveDRBench: separating broad claim discovery from report writing

[中文](livedrbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2508.04183) · [Code](https://github.com/microsoft/LiveDRBench) · [Data](https://huggingface.co/datasets/microsoft/LiveDRBench)

## What it measures

LiveDRBench treats deep research as discovery of structured claims and their support across many sources, rather than production of lengthy prose. The official v1-full release has 100 tasks in eight categories, collected in May-June 2025; the paper first appeared on 2025-08-06. This is historical backfill. Neither the name Live nor a plan for future refreshes establishes that this test snapshot is continuously changing. [Official dataset description](https://github.com/microsoft/LiveDRBench/blob/main/README.md)

## Compared with what

Compared with holistic report grading, the intermediate claim representation separates evidence coverage from writing quality. Compared with single-answer search, the target requires a broader discovery set. This missing predecessor helps contextualize later claim, citation, and dependency-checklist evaluations such as ClaimProbe and Mr.LHDR; adding one historical record does not establish a new field trend.

## Evaluation protocol

Tasks specify a query and output structure; reference claims support precision, recall, and F1 evaluation. Code dispatches category-specific graders with GPT-4o as the default judge. The reviewed evaluate.py assigns zero to missing predictions and computes overall metrics by averaging question-level results, not by equally averaging eight category means. The release is test-only; encrypting references should not be mistaken for complete contamination protection. [Scoring implementation](https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py)

## Decisive evidence and score boundary

The paper reports an overall F1 of 0.55 for the strongest system in its original experiment, with substantial variation across subcategories. This is a historical system-level result, not a current-best claim for 2026. The reusable contribution is exposing incomplete discovery, not proving that longer reports or more search calls necessarily help. [Paper](https://arxiv.org/abs/2508.04183)

## Confounders and remaining coverage gaps

Reference sets can omit alternative valid evidence, the web drifts, and judges and output parsing affect scores. Coverage is concentrated in selected scientific and event domains, not all research work. High claim F1 also does not establish good report structure, argumentation, or prose.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it to evaluate search breadth and evidence coverage alongside a separate report-quality assessment.

### What a concrete task looks like

Illustrative task: identify materials satisfying several experimental conditions, together with supporting evidence. Finding one familiar case or writing a fluent survey does not establish complete coverage.

### Most discriminating experiment

Fix the model, evidence snapshot, and search budget; compare single-chain search with branching exploration. Retain unfinished tasks, aggregate per question, and independently validate correct discoveries outside the references. Score the report separately so prose quality cannot hide missing evidence.

### Pair with

[deepresearch-bench](deepresearch-bench.en.md) · [claimprobe](claimprobe.en.md) · [mr-lhdr](mr-lhdr.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
