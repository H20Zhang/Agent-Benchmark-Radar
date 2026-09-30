# StatFormBench: statistical formulation and variable roles before execution

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-02<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.01982)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](statformbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 20-page v2 and Appendices A–E, including processing, all taxonomy entries and prompts, exact-match validation, source breakdowns and all supplementary result figures. This is the September 5 revision.

[arXiv 2609.01982v2 · 2026-09-05](https://arxiv.org/pdf/2609.01982v2)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

StatFormBench predicts problem categories and required variables/roles before execution. Variables match only when serialized values are identical, without semantic normalization. JCV averages per-sample set overlap; VRI averages the fraction of reference variables both recovered and correctly assigned a role.

<!-- EDITORIAL-METHOD:START -->
Inputs are statistical problem narratives and relevant data summaries; outputs specify categories, variables and roles before code is written. Labels derive from solved textbook/case-library material mapped into a common hierarchy. An illustrative group-comparison case requires selecting an analysis class, identifying variables and distinguishing the outcome from grouping roles. Runnable downstream code cannot repair a wrongly formulated target. This makes formulation visible, while dependence on solved-source taxonomies limits coverage of ambiguous consultations.

Editorial placement: StatABench covers statistical tools and reports; StatFormBench isolates their prerequisite. Compared with final-answer analysis tasks, it adds diagnosis of the chosen problem and variables without replacing estimation, execution or scientific interpretation.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The full zero-shot evaluation uses 1,013 samples: 629 textbook and 384 case-library items. Case inputs are data summaries with simulated previews, not original complete datasets. Sampling, context/token limits and repeat counts are not pinned in the paper.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V2; main metrics are percentages or mean ratios ×100. Definition rows report percentage-point changes. The audit denominator is 60 selected cases, not 1,013.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Gemini 3.1 Pro · zero-shot | 1,013 samples | Fine ACC / JCV / VRI (%) | 72.0 / 61.5 / 63.1 | Shared formulation prompt | Table 1, p. 6 |
| Claude Opus 4.6 · zero-shot | 1,013 samples | Fine ACC / JCV / VRI (%) | 69.5 / 63.2 / 66.2 | Shared formulation prompt | Table 1, p. 6 |
| Gemini 3.1 Pro · category definitions | 1,013 samples; change from zero-shot | Δ Fine ACC / JCV / VRI (points) | +3.8 / -0.7 / -0.9 | Added taxonomy definitions | Table 3, p. 8 |
| Claude Opus 4.6 · matching audit | 60 sampled from 387 difficult textbook cases | Outputs with ≥1 matching-induced error (%) | 11.7% (7/60) | Human review; nonrepresentative subset | Table 6, p. 18 |

Fact source: [Table 1, p. 6; Table 3, p. 8; Table 6, p. 18](https://arxiv.org/pdf/2609.01982v2)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The highest fine-category accuracy and overlap belong to different models. Category definitions improve classification but not every variable metric. Matching-induced errors were audited on a targeted difficult subset, not the whole benchmark. Solved-source labels, category imbalance and translated cases limit real-consultation generalization.

<!-- EDITORIAL-NEXT:START -->
Next, add human-confirmed synonym matching on identical samples with fixed category definitions, comparing serialized equality and semantic matching. Connect a common statistical executor to test whether better formulation improves downstream outcomes.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
