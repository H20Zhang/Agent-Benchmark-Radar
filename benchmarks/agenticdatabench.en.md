# AgenticDataBench: data-science tasks and fine-grained skill evaluation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2607.01647)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agenticdatabench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read Sections 1–7 and all method, setup, result, skill-diagnosis and budget discussions (14 pages including references; no appendix), checking Table 4 and Figures 7–9.

[arXiv 2607.01647v1 · 2026-07-02](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

AgenticDataBench extracts 29,602 step descriptions from 6,510 Stack Overflow solutions and uses embedding clustering, LLM splitting/merging and expert review to obtain 433 data-science skills. These guide the selection of 102 real business tasks and the generation and human validation of 242 additional tasks, yielding 344 tasks in 15 domains. Docker provides Bash, Python and database execution. Four harnesses are paired with Qwen3.5-397B-A17B, Kimi-K2.5 and Claude Sonnet 4.6, using default temperatures and different budgets: DA-Agent has 80 steps, a 15-step history and a one-minute action timeout; Smolagents has 40 coding steps and five minutes per action; Claude Code and CodeX receive 60 minutes per task with adaptive action timeouts.

[Source](https://arxiv.org/pdf/2607.01647v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DataSciBench and DA-Code emphasize task outputs; AgenticDataBench adds fine-grained skill labels to executing such tasks. The added coordinate is diagnostic resolution, not a universal success definition. Harness budgets and soft-score differences remain separate comparison constraints.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Task scores combine table, JSON, text and chart checks with normalized modeling metrics, mapped to 0–1 and reported on a 0–100 scale. A separate LLM diagnoses skill applications using reference solutions, skill annotations and scoring feedback; skills with fewer than three applications are excluded from skill comparisons. This diagnostic layer is not independent executable ground truth for each step.

[Source](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected harness and cost comparison with Kimi-K2.5 fixed

344 tasks; task scores include binary and continuous grading, with complete aggregation weights unspecified; tokens are trajectory means; successful-step ratio uses execution steps as its denominator, not questions; budgets differ by harness, preventing an equal-cost ablation.

| Harness | Overall task score (0–100) | Tokens per trajectory (thousands) | Successful-step ratio (%) |
| --- | --- | --- | --- |
| Smolagents | 43.8 | 379.4 | 88.1 |
| DA-Agent | 44.8 | 145.4 | 94.1 |
| CodeX | 48.8 | 1091.2 | 59.5 |

Source location: Tables 4–5, PDF pp. 9–10; sections 3.3 and 6.1 · [Source](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The same Kimi-K2.5 model has substantially different scores and token consumption across harnesses. CodeX scores higher while taking more steps and having a lower successful-step ratio, illustrating an exploration/efficiency tradeoff rather than a simple error-rate ranking. Budgets, context management and prompt adaptation vary together, so the advantage cannot be attributed solely to skill coverage or cross-step data reuse.

Table 4 gives Claude Code/Kimi-K2.5 a total of 44.3, while one paragraph says 43.3; the table is used. The skill-judge model, human agreement, repeats and full aggregation weights are unspecified. A budget intervention on at most ten failures cannot establish general budget insensitivity.

Within one harness, fix the model, wall-clock time and token budget, then separately add data profiles, cross-step caching and skill retrieval. Evaluate final task outputs, manually audit skill-diagnosis accuracy, and measure redundant large-file reads and stale-cache failures.

[Source](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:limitations:END -->
