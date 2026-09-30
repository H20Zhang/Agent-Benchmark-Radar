# TML-Bench: automated modeling and prediction under short deadlines

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-03-05<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2603.05764)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](tml-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 19-page v1 and Appendices A–F, including scoring, harness operation and competition dimensions; all result figures were visually inspected.

[arXiv 2603.05764v1 · 2026-03-05](https://arxiv.org/pdf/2603.05764v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

TML-bench measures prediction quality under short agent-stage deadlines. Kilo Code runs offline, validates the submitted predictions and scores a hidden holdout afterward. Its headline aggregate selects each model’s best normalized budget per competition.

<!-- EDITORIAL-METHOD:START -->
Each competition supplies training data and test inputs. The offline agent builds a model and writes a prediction file, scored on a hidden holdout only after the deadline. An illustrative workflow loads tables, creates a validation split, selects preprocessing/algorithms under time pressure and predicts every test row. Short deadlines combine modeling quality, execution speed and timely delivery. Reporting medians only over successful runs separates conditional solution quality from the reliability of producing a submission.

Editorial placement: MLE-bench’s longer competition workflow is a useful reference; TML-Bench makes a short wall-clock deadline central. The changed coordinate is deliverable modeling quality under time pressure, not general research ability inferred from a higher normalized aggregate.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Each score is the median of the earliest five successful runs, not five total attempts. Only models covering all 12 settings enter the main comparison. The 1,200-second condition adds XGBoost-focused instructions; budget and prompt therefore change together.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1 §3.6; native hidden-holdout metrics, each median over five successful runs. Deadlines apply to the agent, excluding later scoring.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| MiniMax-M2.1-TEE · 240 s | Foot traffic; 10,289 holdout rows | RMSE ↓ | 0.066846 | Kilo Code; 240 s | §3.6, p. 6; Table 2, p. 19 |
| MiniMax-M2.1-TEE · 600 s | Foot traffic; 10,289 holdout rows | RMSE ↓ | 0.065770 | Kilo Code; 600 s | §3.6, p. 6; Table 2, p. 19 |
| MiniMax-M2.1-TEE · 1200 s | Foot traffic; 10,289 holdout rows | RMSE ↓ | 0.065489 | Kilo Code; 1200 s; XGBoost prompt | §3.6, p. 6; Table 2, p. 19 |
| GPT OSS120B TEE · 1200 s | Bank customer churn; 3,000 holdout rows | AUC ↑ (0–1) | 0.928000 | Kilo Code; 1200 s; XGBoost prompt | §3.6, p. 6; Table 2, p. 19 |

Fact source: [§3.6, p. 6; Table 2, p. 19](https://arxiv.org/pdf/2603.05764v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

MiniMax-M2.1-TEE leads the relative best-budget aggregate; that is not accuracy or a fixed-budget win. Selection among successful runs omits reliability from the score median. Precise hardware and token usage are unavailable. Time-scaling claims cannot isolate additional compute from changed instructions.

<!-- EDITORIAL-NEXT:START -->
Next, hold prompts, hardware and network conditions fixed while changing only deadlines. Include timeouts and invalid submissions in the denominator and report conditional quality separately, disentangling XGBoost guidance, additional time and successful-run selection.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
