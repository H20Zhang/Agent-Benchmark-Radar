# CausalDS: identifiability in association, intervention and counterfactual tasks

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-09<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2607.08093)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](causalds.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete substantive 55-page v1 and Appendix A.1–A.16: generation/audits, composition, every scoring family, all breakdowns, restarts, matched ablations, failures, deployment and full prompts. Tables 3/4/24/25 were visually verified.

[arXiv 2607.08093v1 · 2026-07-09](https://arxiv.org/pdf/2607.08093v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

CausalDS combines narrated synthetic causal models, observational files and private ground truth. CausalDSScore is a lower-is-better loss combining binary errors, numeric losses and graph/set loss. Abstention changes scoring pools; missing numeric answers are excluded, so coverage must accompany loss.

<!-- EDITORIAL-METHOD:START -->
Each scene derives observational data, narrative and private ground truth from a controlled structural causal model, then poses associational, interventional or counterfactual questions. An illustrative workflow identifies relationships from the story, judges identifiability, inspects observations and estimates an intervention effect or abstains rather than merely predicting correlation. Tasks score identification decisions, numeric estimates or graph/set outputs. Synthetic mechanisms provide ground truth, but unintended causal claims in the narrative can still change the question.

Editorial placement: compared with generic analysis/prediction benchmarks, CausalDS explicitly asks whether the evidence identifies the target rather than assuming every task has a computable numeric answer. Like StatFormBench it requires problem formulation, adding structural causal semantics and abstention.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The exam samples 100 scene/tasks from 953 scenes. Mini-swe-agent runs offline with 100 steps and a $10 cap where priced, never reached. Closed models use high reasoning; open models use serving defaults. Qwen’s 32k context limits comparability.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Main: 100-task exam, but Pass Rate covers 34 binary tasks and continuous validity has 39 targets. Matched rows: one run per view; paired loss capped at 1, including missing/invalid/abstained answers.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Opus 4.8 · main | 100 tasks; 34 binary / 39 numeric targets | Score ↓ / Pass Rate (%) / valid count | 0.2780 / 82.4% / 38/39 | High reasoning; adaptive thinking | Table 3, p. 10; Table 4, p. 12 |
| GPT-5.5 · main | 100 tasks; 34 binary / 39 numeric targets | Score ↓ / Pass Rate (%) / valid count | 0.5610 / 82.4% / 37/39 | High reasoning | Table 3, p. 10; Table 4, p. 12 |
| Kimi K2.6 · hard minus clean | 10 matched scene/task pairs | Mean loss Δ ± SD; 95% CI | +0.20 ± 0.27; [+0.053, +0.373] | proxy_hard − clean; diagnostic loss | Table 24, p. 38 |
| Qwen 3.6-35B · hard minus clean | 10 matched scene/task pairs | Mean loss Δ ± SD; 95% CI | +0.33 ± 0.47; [+0.070, +0.626] | proxy_hard − clean; diagnostic loss | Table 24, p. 38 |

Fact source: [Table 3, p. 10; Table 4, p. 12; Table 24, p. 38](https://arxiv.org/pdf/2607.08093v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The matched observation ablation uses ten selected identifiable tasks and a different loss that assigns one to failures. It is not a population effect. Story audits treat extra causal claims as warnings; synthetic generation is not perfect semantic validation. Small interval-coverage samples and answer-dependent denominators limit broad capability rankings.

<!-- EDITORIAL-NEXT:START -->
Next, hold causal graphs/queries fixed while varying sample size, narrative wording and observational access. Report coverage, identification accuracy and answered-task loss together, distinguishing justified abstention from lower averages obtained through excluded missing answers.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
