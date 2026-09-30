# KramaBench: discovery, cleaning and integration in noisy data lakes

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-06-06<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2506.06541)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](kramabench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all substantive main sections, ethics/reproducibility statements and Appendices A–H (30 pages), with Table 5 visually checked.

[arXiv 2506.06541v3 · 2026-03-05](https://arxiv.org/pdf/2506.06541v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

KramaBench v3 contains 104 end-to-end tasks and 633 subtasks over 1,764 files from 24 sources in six domains. It evaluates final answers, coverage of essential operations in generated code, and separately prompted subtasks given the gold files. DS-Guru samples each file before generating Python; its few-shot variant repairs execution failures. smolagents DR repeatedly inspects files, executes code and revises its plan, while Reflexion adds evaluator and reflection agents. Full exposes the entire lake, Oracle supplies gold files, and Trimmed limits uploads to ten files. Internet access is disabled for the open systems but cannot be reliably disabled for commercial web interfaces, preventing a strictly matched cross-system ranking.

[Source](https://arxiv.org/pdf/2506.06541v3)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DS-1000 supplies code and local context, while DA-Code adds interactive analysis. KramaBench centers discovery, cleaning and integration in a noisy data lake. Its additional coordinate is input preparation and source selection, not demonstrated cross-task memory reuse.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Each end-to-end answer receives a score between 0 and 1, averaged over tasks and displayed on a 0–100 scale. Exact strings and numbers use binary matching, approximate numbers use relative absolute error, lists use F1, and some semantic matches use an LLM. The reported score is therefore not a binary complete-task success rate. Unstarred results generally report the mean and standard deviation of three runs. Within-system Full/Oracle contrasts are more informative about retrieval than cross-framework leaderboards. A complete common agent action or token cap is not specified; DS-Guru iteration and sampling ablations are reported separately.

[Source](https://arxiv.org/pdf/2506.06541v3)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected input and framework comparisons with the same model

104 tasks; mean per-task answer score ×100, not binary completion rate; mean ± standard deviation over three runs; open systems have no internet; compare Full and Oracle within each row.

| System | Model | Full score (0–100) | Oracle score (0–100) |
| --- | --- | --- | --- |
| DS-Guru few-shot | GPT-o3 | 24.98 ± 1.25 | 43.71 ± 1.94 |
| smolagents DR | Claude-3.7 | 55.83 ± 3.41 | 60.67 ± 1.23 |
| smolagents Reflexion | Claude-3.7 | 55.37 ± 3.36 | 62.81 ± 3.10 |

Source location: Table 5, PDF p. 7; score definition Table 3 and Appendix G.1, pp. 4, 29 · [Source](https://arxiv.org/pdf/2506.06541v3)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The selected same-model comparisons show that gold-file selection helps by an amount that depends on the framework. Reflexion is close to single-agent DR under Full, which does not establish that all multi-agent designs are ineffective. Approximate-answer grading, method changes across revisions and conflicting prose/table values qualify the conclusions.

Source conflicts reRead Tables 5/11 give OpenAI DR 52.18 on Trimmed, while the prose incorrectly assigns it another system’s 58.12. The claimed 0–7-point Oracle benefit does not cover the 18.73-point DS-Guru/GPT-o3 gain, and one GPT-o3 row in Appendix Table 9 conflicts with the main table. Obscured-input coverage is inconsistently described as 20% versus all tasks. The human-study task denominator and judge model are incompletely specified.

Fix the model, action count and token budget, then compare iterative retrieval with a prebuilt catalog under Full, Oracle and gold-intermediate-table conditions. Track operation-level errors, incremental maintenance cost and reuse across repeated tasks.

[Source](https://arxiv.org/pdf/2506.06541v3)
<!-- EVIDENCE:limitations:END -->
