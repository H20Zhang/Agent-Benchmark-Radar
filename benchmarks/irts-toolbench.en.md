# IRTS-ToolBench: tool-assisted reasoning over irregular time series

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-13<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.15107)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](irts-toolbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read Sections 1–6 and Appendices A–E (15 pages), covering all task definitions, construction, tools, results and three illustrated examples; visually checked Table 2.

[arXiv 2606.15107v1 · 2026-06-13](https://arxiv.org/pdf/2606.15107v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

IRTS-ToolBench transforms regular sequences from two existing time-series QA resources using LLM-selected missingness mechanisms and executable parameters. It contains 1,700 irregular univariate questions across ten task types and thirteen domains, with multiple-choice or true/false outputs. GPT-5.1, Claude Sonnet 4.5 and Gemini 2.5 Flash support generation and quality filtering. The library contains seven irregularity operators and 23 analytical tools. Reference tool sets come from three-model voting, with a union fallback, making them conventional reference sets rather than proven minimal necessary sequences.

[Source](https://arxiv.org/pdf/2606.15107v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: general analysis suites often underemphasize sampling structure; IRTS-ToolBench specializes in irregular time series and suitable tools. It spans regularity, statistics and other reasoning targets beyond forecasting. The changed coordinate is temporal structure/tool fit, not an assumption that tool use always improves prediction.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Answer options are exactly matched, yielding sample-weighted overall and task-specific accuracy. Exact, partial and mismatched tool-set rates are separate and do not affect answer scores. The selected comparisons use two models with every task category reported, avoiding the missing categories in two no-tool Claude rows. Evaluation is zero-shot, but complete step, token, temperature and repetition settings are not provided.

[Source](https://arxiv.org/pdf/2606.15107v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected within-model comparisons with and without tools

Table 2 rows reporting all ten categories; overall denominator 1,700, category denominators shown in headers; exact option matching; zero-shot; tool availability is the reported contrast, but budgets, repeats and scaffold details are incomplete.

| Model | Overall accuracy (%) | Anomaly detection (%, 250 questions) | Irregularity severity (%, 150 questions) |
| --- | --- | --- | --- |
| Qwen3.6-27B / Without tools | 78.59 | 96.80 | 58.00 |
| Qwen3.6-27B / With tools | 74.41 | 99.60 | 81.33 |
| DeepSeek-V4-Flash / Without tools | 60.29 | 59.20 | 31.33 |
| DeepSeek-V4-Flash / With tools | 74.00 | 96.40 | 98.67 |

Source location: Appendix C Table 2, p. 11; task counts Appendix A Table 1, p. 7; metrics section 4, pp. 3–4 · [Source](https://arxiv.org/pdf/2606.15107v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

Tool effects depend on model and task. DeepSeek greatly improves missingness-density estimation and overall accuracy; Qwen improves anomaly detection but loses overall accuracy, especially on regularity discrimination. Generated mechanisms and contextual descriptions can make answers depend on construction rules; these results do not establish causal identification of missingness mechanisms in real sensors.

Two no-tool Claude rows omit forecasting and regularity-discrimination results, leaving their overall denominator unclear; they are excluded here. The claim that Qwen wins in every setting is too strong: its tool score 74.41 is below Claude’s tool score 76.00. Two human reviewers inspect approximately 2%, not the full benchmark.

Hold the model, prompt, total budget and tool-selection interface fixed and report numerical analysis, regularity detection and mechanism attribution separately. Add naturally irregular sequences and accept multiple equivalent correct tool paths to test whether the reference tool set penalizes valid solutions.

[Source](https://arxiv.org/pdf/2606.15107v1)
<!-- EVIDENCE:limitations:END -->
