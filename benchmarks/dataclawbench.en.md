# DataClawBench: evaluating final outcomes and milestone progress separately

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-04<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.02503)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dataclawbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all 25 pages of v3 and Appendices A–F, including configurations, category results, costs, anonymization, annotation, three complete prompts and four case studies; visually checked Tables 4–5.

[arXiv 2605.02503v3 · 2026-05-27](https://arxiv.org/pdf/2605.02503v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DataClawBench v3 provides approximately 2.06 million enterprise, industry and policy records in eighteen files, preserving missingness, naming and unit inconsistencies. Its 492 tasks comprise 131 easy, 286 medium and 75 hard tasks without task-specific source hints, complete schemas or noise descriptions. Experts and agents establish reference answers and milestones in a cleaned environment. Eight models use OpenClaw with read-only Docker workspaces and 1,200 seconds per task; only International Comparison tasks permit web search.

[Source](https://arxiv.org/pdf/2605.02503v3)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DA-Code/DataSciBench center final artifacts; DataClawBench additionally uses milestones and time discounting to describe progress. It diagnoses how far failed runs get, but process scores on separate correct/incorrect subsets cannot replace accuracy or be treated as paired comparisons across models.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

GLM-5 grades Acc against reference answers, averaging sub-question scores for multi-part tasks; it is not necessarily binary whole-task accuracy. EE, computed only on correct tasks, divides reference steps by agent steps. GPR, computed only on incorrect tasks, measures milestone achievement, including upstream achievements inferred from correct downstream results. TPE discounts first-achievement times with γ=0.9 over achieved milestones only, so it does not measure completeness alone. Provider defaults and maximum contexts vary; GPT-5.4 thinking is off while Claude and Gemini use high effort, preventing matched-compute interpretation.

[Source](https://arxiv.org/pdf/2605.02503v3)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected outcome and process measures with different populations

All 492 v3 tasks; Acc averages within-task parts; EE uses each model’s correct tasks, while GPR/TPE use its incorrect tasks, whose exact counts are not separately given; GLM-5 judge, γ=0.9, OpenClaw with 1,200 seconds per task; reasoning settings differ by model.

| Model | Acc (%) | EE (ratio) | GPR (%) | TPE (0–1) |
| --- | --- | --- | --- | --- |
| Claude Opus 4.6 | 63.4 | 0.42 | 45.1 | 0.59 |
| Gemini 3.1 Pro Preview | 45.8 | 0.32 | 33.6 | 0.41 |
| GPT-5.4 | 23.4 | 0.46 | 18.5 | 0.75 |

Source location: Tables 4–5, p. 6; equations 1–2, p. 3; Appendix A Table 7, p. 12; Appendix E, pp. 20–21 · [Source](https://arxiv.org/pdf/2605.02503v3)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

GPT-5.4 has high EE and TPE but low Acc and GPR, illustrating that quick termination or a few early achievements can appear efficient. Models have different failed-task subsets, so GPR is not a paired same-task comparison. The environment intervention reruns only thirty previously failed tasks and bundles noise removal with source pruning, leaving separate causal contributions unidentified.

Section 3.2 mentions deterministic evaluation, but actual outcomes and milestones are judged by GLM-5. Table 16 lists 3,934 total tasks although eight rows of 492 imply 3,936. Case 2 claims that changing a shared denominator changes rankings after per-indicator min-max normalization; a common positive scaling factor would cancel under standard min-max, so that causal explanation requires code inspection rather than repetition.

Match reasoning effort and budgets, independently intervene on noise, source selection and schema guidance over identical tasks, and repeat runs. Blind-review both correct and incorrect trajectories, measuring exact final outputs, milestone recall and falsely inferred progress.

[Source](https://arxiv.org/pdf/2605.02503v3)
<!-- EVIDENCE:limitations:END -->
