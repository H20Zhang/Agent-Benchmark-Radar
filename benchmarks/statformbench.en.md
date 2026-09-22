# StatFormBench: testing whether the analysis problem is formulated before code execution

[中文](statformbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.01982) · [Code](https://github.com/THU-CongLab/StatFormBench) · [Data](https://huggingface.co/datasets/THU-CongLab/StatFormBench)

## What it measures

StatFormBench decomposes the upstream analysis step into statistical problem classification, variable identification, and role assignment. It contains 1,013 samples from five statistics textbooks and a data-science case library, covering 20 coarse and 85 fine categories. The target is how to formulate the analysis, not whether an already specified program returns the expected result. [Paper](https://arxiv.org/abs/2609.01982)

## Compared with what

Compared with DS-1000 code implementation or Spider query generation, it relaxes the assumption that the user has already supplied the right analysis target. It complements end-to-end DataSciBench: a wrong final result can first be checked for a wrong method category, variable set, or role assignment before execution begins.

## Evaluation protocol

The official runner sends samples and prompts to named models, then evaluation modules compare parsed outputs with references. Metrics include coarse/fine classification accuracy, variable-set Jaccard, precision, recall, and role consistency. The reviewed variable_metrics.py computes Jaccard from set intersection and union. These variable metrics are not functional correctness after executing code. [Runner and scoring guide](https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md) · [Variable metrics](https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py)

## Decisive evidence and score boundary

Across 14 models, the paper reports best zero-shot fine classification accuracy of 72.0 and variable-set overlap of 63.2, with no model consistently best across both subtasks. These are source-reported best values for different metrics, not a fabricated single-model result and not an analysis-execution success rate. [Result source](https://arxiv.org/abs/2609.01982)

## Confounders and remaining coverage gaps

Textbooks may have appeared in model training, and a fixed taxonomy can compress multiple reasonable analyses into one label. Variable aliases, output parsing, and role rubrics affect the measurement. Statistical assumptions in actual data, numerical implementation, and clarification of ambiguous business goals remain unmeasured.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it as a pre-execution diagnostic to distinguish task-understanding failures from implementation failures in a data agent.

### What a concrete task looks like

Illustrative task: a user asks whether a redesign improved retention. The model must identify comparison groups, outcome variables, and possible confounders before choosing an analysis; an executable mean query may still answer the wrong question.

### Most discriminating experiment

Feed model-generated versus expert-supplied formulations to the same executor. Report formulation metrics and final numerical correctness separately, then blind-review cases with multiple valid formulations. If expert formulations remove most failures, prioritize problem definition rather than adding execution tools.

### Pair with

[ds-1000](ds-1000.en.md) · [datascibench](datascibench.en.md) · [data-agent-benchmark](data-agent-benchmark.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
