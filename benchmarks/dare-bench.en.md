# DARE-bench: separating instruction fidelity from predictive quality

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-27<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.24288)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dare-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the full substantive 34-page v1 and Appendices A–M, including curation prompts, reference code, tool schemas, RL settings and rejection sampling. Checked the official released-subset counts and results.

[arXiv 2602.24288v1 · 2026-02-27](https://arxiv.org/pdf/2602.24288v1) · [Official repository documentation · 2026-09-30](https://github.com/Snowflake-Labs/dare-bench#task-types)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

DARE separates instruction fidelity, measured by exact reference predictions, from predictive modeling quality. Classification modeling uses macro-F1; regression and forecasting use clipped R². Exact outputs are a reproducibility proxy, not a direct audit of every intermediate operation.

<!-- EDITORIAL-METHOD:START -->
Tasks provide data and instructions, separating reproduction of prescribed outputs from building a good predictor. In an illustrative workflow, the agent must use specified preprocessing, a model and a seed to generate predictions. Another algorithm may predict better yet fail instruction fidelity; the modeling-quality track instead evaluates predictive metrics. The GRPO variant trains with computable rewards, but gains require checking both fidelity and quality rather than merely executable code.

Editorial placement: DS-1000 emphasizes tested code correctness and MLE-bench predictive outcomes. DARE separates following a prescribed analytical procedure from freely optimizing results. Better prediction therefore need not mean faithful execution of a request.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The paper evaluates 352 test tasks, versus 324 in the public subset. Main runs allow five turns, 200 seconds per execution and three repeats. RL uses a GRPO variant without group normalization or KL regularization, with eight rollouts per question.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Full-paper classification subsets: 74 tasks per variant × three repeats. IF is exact-output accuracy; MM is mean macro-F1 multiplied by 100.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| gpt-5 · Classification-IF | 74 tasks × 3 runs | IF accuracy (%) | 69.81% | Prescribed preprocessing/model/seed | Table 5, p. 7 |
| Claude-Sonnet-3.7 · Classification-MM | 74 tasks × 3 runs | MM macro-F1 × 100 | 61.03 | Open modeling against dataset labels | Table 5, p. 7 |
| Qwen3-4B Baseline | IF / MM: 74 tasks each × 3 runs | IF (%) / MM macro-F1 × 100 | 3.60% / 5.23 | Untuned model; main harness | Table 6, p. 8 |
| Qwen3-4B + RL | IF / MM: 74 tasks each × 3 runs | IF (%) / MM macro-F1 × 100 | 38.96% / 39.44 | Training T=1, top-p=0.95; main evaluation | Table 6, p. 8; Table 13, pp. 17–18 |

Fact source: [Table 5, p. 7; Table 6, p. 8; Table 6, p. 8; Table 13, pp. 17–18](https://arxiv.org/pdf/2602.24288v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Section 4.3 misattributes the 69.81% classification-fidelity value to Claude; Table 5 assigns it to GPT-5. Appendix limits also conflict: a task prompt says ten minutes and a tool schema says three calls. Keep full-paper and public-subset results separate. A single overall winner would conceal different metric families.

<!-- EDITORIAL-NEXT:START -->
Next, audit intermediate operations on the same tasks while pinning libraries, seeds and hardware. Compare outcome-equivalent implementations with different procedures to determine whether exact matching penalizes instruction violations or immaterial numerical variation.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
