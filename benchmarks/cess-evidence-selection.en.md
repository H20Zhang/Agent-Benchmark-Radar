# CESS: auditing evidence selection in deep research

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-30<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.39026v1)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](cess-evidence-selection.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and release status

Full text and key results reviewed; no independent experimental reproduction.

Review on 2026-10-02 (Asia/Shanghai) covered arXiv:2609.39026v1 Sections 1–6 and Appendices A–G, with key results checked against the PDF. Public access to the authors' implementation, exact fixtures and trajectory logs remains unverified. This entry accepts a paper-defined diagnostic protocol, not a confirmed runnable package. [Paper](https://arxiv.org/html/2609.39026v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What becomes measurable

An agent may encounter supporting material first, pursue similar evidence and stop before finding counterevidence. Correct citations do not guarantee a representative sample.

CESS fixes a document pool and evidence-direction scores, then uses logged selection and continuation probabilities to correct a pool-average estimate. Shrinkage stabilizes short trajectories. The raw estimator's unbiasedness requires correct probabilities and positive support; practical shrinkage and clipping do not automatically retain it. Unreachable documents require interval treatment.

The target is the pool's encoded evidence direction, not report accuracy or objective truth. Policy effects require a separate paired intervention crossing uniform/agent selection with fixed/adaptive stopping; differences between corrected estimates cannot replace policy effects. [Sections 2–3, Equations 1–10; Appendix B](https://arxiv.org/html/2609.39026v1)
Before search, CESS predicts every candidate document’s evidence direction and averages those predictions. It corrects that average using observed prediction errors weighted by selection and continuation probabilities.

<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Labels, sampling and controls

MS2 supplies outcome-direction information; PERSPECTRUM supplies support/undermine labels. Both aggregate equally across documents, without establishing evidence quality or effect magnitude.

The public-agent experiment uses Qwen2.5-32B-Instruct and replaces Open Deep Research's search tool with a fixed pool. Ranking branches share initial state, first query and sampling randomness; later queries may diverge. Cached responses fix repeated model inputs. Every trajectory completes four searches, so this experiment does not test early-stopping correction. Comparisons must fix pools, labels, probability logging and clipping/shrinkage order, preserving repeated-run dependence at question level. [Appendices A.1–A.2, D and F](https://arxiv.org/html/2609.39026v1)
In both result tables, CESS uses the full-pool prediction mean as anchor and λ=0.5: clip the raw sequential estimate to [-1,1], then shrink toward that prediction. Direction categories use thresholds ±0.05 for positive, neutral and negative. The ten-round ordinary-shrinkage baseline moves toward the tuning-set mean with α=0.75, selected on separate five-round runs for 267 tuning questions and held fixed during ten-round evaluation.

<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Pool estimation after two selections

36 PERSPECTRUM tasks, two rankings and three paired seeds yield 216 four-search trajectories; this table evaluates their first two selections. MAE and sensitivity are dimensionless; direction error is a fraction. Lower is better for all columns.

| Method | MAE | Ranking sensitivity | Direction error |
|---|---:|---:|---:|
| Opened Mean | 0.5727 | 0.5849 | 0.4907 |
| CESS | 0.2287 | 0.0746 | 0.3102 |

These are controlled pool-estimation gains, not report-accuracy improvements. [Table 3; Appendix D](https://arxiv.org/html/2609.39026v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## A stronger baseline exposes the error–stability trade-off

A separate PERSPECTRUM experiment allows up to ten rounds: 267 tuning questions and 36 evaluation questions, aggregated across the paper's models, controllers and stopping conditions. Sensitivity S averages repetitions before contrasting rankings and cannot be compared directly with the preceding table. Lower is better for every column.

| Method | MAE | Ranking sensitivity S | Direction disagreement |
|---|---:|---:|---:|
| Opened Mean shrunk to Tuning Mean | 0.2427 | 0.2393 | 0.3893 |
| CESS | 0.3103 | 0.1608 | 0.5208 |

Ordinary shrinkage has lower error; CESS has lower sensitivity. Across Table 11's 28 matched-sensitivity settings, CESS has lower error in 3, no detected difference in 15 and higher error in 10. Correlated settings and unadjusted intervals prevent treating these as independent wins/losses. [Appendix F, Table 8 and Equation 16; Appendix G, Table 11](https://arxiv.org/html/2609.39026v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Genealogy, reproduction gaps and next test

Relative to DeepResearch Bench's report evaluation, this adds an upstream diagnostic of representation of a fixed pool. It complements ClaimProbe's writer-faithfulness audit without asserting direct derivation. `map_delta=early_signal`; one work does not revise a durable defining chain.

Known pools, correct probabilities and labels are required; prediction, shrinkage and clipping affect results. Appendix A.2 delegates split/tuning details to implementation, but implementation, exact tasks, prompts, predictor fitting and logs remain unverified. Token costs, latency and retries are incomplete. The formula-defined diagnostic is supported; an exactly reproducible experimental release is not confirmed.

Next, publish fixed pools, labels and per-round probability logs; match prediction/tuning budgets; separately validate pool-estimation error and selection/stopping interventions on the same questions, reporting zero-probability coverage. Stable estimates must not be equated with correct reports. [Section 3; Appendices A.2, D and F–G](https://arxiv.org/html/2609.39026v1)
<!-- EVIDENCE:limitations:END -->
