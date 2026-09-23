# MemCalib: calibrating how strongly supplied memory influences a response

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.24259)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memcalib.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.24259) · [Project](https://quark-medical.github.io/MemCalib-Project/) · [Data](https://huggingface.co/datasets/ZiLaotou/MemCalib)

## What it measures

MemCalib evaluates propositions already supplied in context. For the current query, an atom should be ignored (A), provide bounded local support (B), or control a material conclusion or constraint (C). The official project specifies 15,000 examples and 234,220 atoms: 13,500 training and 1,500 held-out test examples, with a further 1,500 training examples reserved for validation in the paper. [Official data and protocol](https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html)

## Compared with what

Compared with relevance, recall, or aggregate answer correctness, the target is the degree of influence each proposition should have. Relative to negative-transfer diagnostics such as MemTrapBench, it keeps both over-use and under-use visible. Ignoring all history is not automatically a well-calibrated memory policy.

## Evaluation protocol

An example contains a query, composite memory blocks, extracted propositions, ideal use levels, and atom-specific rubrics across health, general assistance, and coding. The official page names Sample Calibration Score, Exact Calibration, and directional error metrics. This review checked the dataset card and detailed project description. The advertised code repository currently contains only a short README; no executable scorer was verified, so numerical score reproduction is not certified. [Dataset](https://huggingface.co/datasets/ZiLaotou/MemCalib) · [Code release status](https://github.com/Quark-Medical/memcalib)

## Decisive evidence and score boundary

The public data and annotation contract define a reusable memory-use task, which is the accepted contribution here; MemCalib-RL is not registered as a second benchmark. The paper reports that common training approaches can improve one error direction while worsening the other. This motivates inspecting both directions, not a claim that one optimization dominates under every setting. [Paper](https://arxiv.org/abs/2609.24259)

## Confounders and remaining coverage gaps

The key validity questions concern the stability of the B/C boundary, atom decomposition, and rubric interpretation. Providing the memories directly leaves retrieval, writing, source authority, and environment actions unmeasured. The health-heavy domain mixture also affects the aggregate; calibration scores are not evidence of clinical reliability.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it after retrieval to diagnose over-personalization, ignored constraints, or promotion of a locally relevant fact into a global decision rule.

### What a concrete task looks like

Illustrative task: the current project's implementation language is a binding constraint while a preference from an old project is background. The former should control the answer without mechanically adopting the latter.

### Most discriminating experiment

Keep the generator and supplied memories fixed; compare full memory, an oracle of relevant atoms, and removal of distractors. Report both error directions by A/B/C class and audit boundary cases with human and multiple-evaluator agreement. Until the scorer is released, clearly separate local rubric implementations from the paper's reported scores.

### Pair with

[memtrapbench](memtrapbench.en.md) · [memory-trust-gap](memory-trust-gap.en.md) · [locomo-conv](locomo-conv.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
