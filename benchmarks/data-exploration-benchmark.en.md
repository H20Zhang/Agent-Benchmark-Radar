# Data Exploration Benchmark: how initial discovery affects downstream analysis

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-17<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.16045)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](data-exploration-benchmark.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read Sections 1–8, scoring formulas and case studies (9 pages including references; no appendix), with result heatmaps in Figures 3–6 visually checked.

[arXiv 2608.16045v1 · 2026-08-17](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

This evaluation makes pre-analysis understanding an explicit artifact: models convert raw Excel workbooks into schema-fixed JSON describing logical tables, field semantics, keys, relationships, provenance and lightweight profiles. Experiments use one real Vitamin D study workbook and 12 purposively selected DSBench tasks, divided into 4 simple, 5 middle and 3 difficult tasks. Main models are Gemini 3.1 Pro, Claude Opus 4.6 and GPT 5.4; GPT agent is tested only on the difficult group and the real workbook.

[Source](https://arxiv.org/pdf/2608.16045v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: unlike analysis tasks that supply schemas and field meanings, this suite examines how initial discovery affects downstream work. Relative to KramaBench’s broader data journey, it is a smaller exploration/guidance intervention. The coordinate is information formation before analysis, not proof of a general exploration policy or shared-memory benefit.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Structural evaluation aligns tables through maximum-weight matching and then aligns columns, scoring table/column/relation F1, types, semantics, provenance and numeric profiles. An LLM-judged summary can reduce the total by up to 30%. A separate downstream intervention holds questions and scoring fixed: Control receives raw files, Middle additionally receives self-generated exploration JSON, and Treatment receives oracle metadata without downstream answers. Total token cost is deliberately not held constant.

[Source](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Correct-answer counts on two downstream cases

Section 6.2 case studies; cells are correct answers divided by questions within the case, not overall benchmark scores; questions/scoring are fixed, but tokens and exploration effort are not; repeated-run variance is unreported.

| Model | Task | Control (correct/total) | Middle (correct/total) | Treatment (correct/total) |
| --- | --- | --- | --- | --- |
| GPT 5.4 | Financial model | 15/20 | 16/20 | 17/20 |
| Claude Opus 4.6 | Depot allocation | 6/9 | 7/9 | 9/9 |
| Gemini 3.1 Pro | Depot allocation | 6/9 | 9/9 | 7/9 |

Source location: Section 6.2, PDF pp. 7–8; intervention Table 1, p. 6 · [Source](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The selected cases demonstrate both gains and a counterexample. Explicit metadata can improve dependency recovery, yet Gemini answers two fewer depot-allocation questions with oracle metadata than with its own artifact. Providing a representation does not guarantee correct use. The small targeted sample and unreported repeated runs make these results evidence for a mechanism hypothesis and case study, not established production reliability or long-term shared-state benefits.

GPT agent does not cover all twelve tasks. Figure 6 includes DeepAnalyze on only one simple task and ai-analyst on two, unlike the four-task main-model group. The summary judge and repetition count are undisclosed.

Under matched total budgets, compare raw files, generated JSON, human-corrected JSON and equally long prose summaries. Across multiple subsequent questions and data changes, measure accuracy, repeated profiling cost and invalidation detection to test whether reusable representations improve amortized cost.

[Source](https://arxiv.org/pdf/2608.16045v1)
<!-- EVIDENCE:limitations:END -->
