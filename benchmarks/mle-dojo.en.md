# MLE-Dojo: iterative ML with score feedback

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-05-12<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2505.07782)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mle-dojo.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 36-page v1 and Appendices A–I, including the complete task inventory, metric definitions, prompts, examples and both agent integrations.

[arXiv 2505.07782v1 · 2025-05-12](https://arxiv.org/pdf/2505.07782v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

MLE-Dojo exposes competition-score feedback in an iterative environment. HumanRank averages relative public/private leaderboard positions; it is not task success. AUP summarizes a cross-task performance profile, not improvement over successive actions.

<!-- EDITORIAL-METHOD:START -->
The environment organizes two hundred competitions into resettable tasks where agents submit predictions, receive score feedback and revise them, supporting evaluation and future policy training. An illustrative loop reads data, trains a baseline, submits, uses leaderboard-derived feedback to adjust features and selects a final version. This measures feedback-conditioned optimization, unlike a one-shot submission without final-test scores. HumanRank is relative historical leaderboard position, not a fraction of completed tasks or independently tested experts surpassed.

Editorial placement: MLE-bench is the direct competition-delivery reference; MLE-Dojo adds iterative rewards and a train/evaluation task split. Turning evaluation into a potential learning environment is meaningful, but an interface for training is not evidence of demonstrated trained-policy transfer.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Main results use MLE Agent, the better of two runs, at most 15 steps and 12 hours, with a 32 GB GPU-memory limit, 50k input tokens and 8,192 output tokens. The corpus has 150 training and 50 evaluation tasks.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1 Table 2; same MLE Agent and best-of-two feedback protocol. HumanRank is a mean leaderboard percentile, higher is better.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Gemini-2.5-Pro · Tabular | Tabular; 10 evaluation tasks | Mean HumanRank (%) | 42.64% | exp-3-25; shared harness | Table 2, p. 9; Table 4, pp. 25–26 |
| DeepSeek-r1 · Tabular | Tabular; 10 evaluation tasks | Mean HumanRank (%) | 38.13% | Shared harness | Table 2, p. 9; Table 4, pp. 25–26 |
| Gemini-2.5-Pro · CV | CV; 10 evaluation tasks | Mean HumanRank (%) | 42.83% | exp-3-25; shared harness | Table 2, p. 9; Table 4, p. 25 |
| o3-mini · CV | CV; 10 evaluation tasks | Mean HumanRank (%) | 35.02% | 2025-01-31; shared harness | Table 2, p. 9; Table 4, p. 25 |

Fact source: [Table 2, p. 9; Table 4, pp. 25–26; Table 2, p. 9; Table 4, p. 25](https://arxiv.org/pdf/2505.07782v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The split enables future training experiments; the paper does not demonstrate learned-policy transfer. Its MLE-Lite count is inconsistent: a footnote says 22, but the evaluation inventory lists 21. The selected Tabular/CV subsets each have ten tasks. AUP’s formula/reporting discrepancy makes exact AUP comparisons unsafe without clarification.

<!-- EDITORIAL-NEXT:START -->
Next, compare no-score, public-validation-only and full-feedback conditions on identical tasks with matched steps/hardware and an independent final holdout. Replace oracle best-of-two reporting with a prespecified selection rule to separate feedback overfitting from transferable improvement.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
