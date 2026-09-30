# AI4AI-Bench: clean replay of learning-system source changes

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-20<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.20318)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ai4ai-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 19-page v1, Appendix A’s ten task protocols and Appendix B’s complete RAGEN contract. Also checked the official evaluation/replay documentation on the stated date.

[arXiv 2608.20318v1 · 2026-08-20](https://arxiv.org/pdf/2608.20318v1) · [Official repository documentation · 2026-09-30](https://github.com/Einsia/AI4AI-Bench#evaluation-and-replay)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

AI4AI separates exploration from formal replay: only source changes carry into a fresh run. Scores normalize the baseline to 0.1 and the target optimum to 1. Best configuration and averages across reasoning levels are different summaries.

<!-- EDITORIAL-METHOD:START -->
Agents inspect training code, try modifications and observe proxy evaluation during exploration. Formal evaluation applies only the source patch in a fresh environment and retrains or reevaluates, excluding exploration-generated weights and caches. An illustrative workflow changes an optimizer or learning algorithm, performs a short trial and relies on clean replay for validation. This separates source-level algorithm changes from state accumulated in one run, while remaining dependent on the supplied data, evaluator and compute.

Editorial placement: relative to DeltaML’s research-repository improvement, AI4AI more explicitly restricts the phase boundary to source patches. The coordinate is reproducibility in a fresh run rather than a high-scoring exploration checkpoint, not automatic certification of algorithmic novelty.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Exploration lasts four hours on one B300; formal replay allows up to twelve hours. Eight training tasks evaluate the best of up to three latest valid checkpoints. Proxy and final evaluation are not always sample-disjoint. The main grid has 29 configurations over ten tasks.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1; normalized σ is unitless, not accuracy. Each task/configuration has one scored cell; no repeated-seed confidence interval is supplied.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Opus 5 / Claude Code / medium | 10 tasks; 10 cells | Mean σ (0–1) | 0.288 | Best reported configuration | Table 3, p. 8 |
| Claude Opus 5 / Claude Code / all efforts | 10 tasks × 5 efforts; 50 cells | Mean σ (0–1) | 0.250 | Across-effort system average | §3.2, p. 6; Figure 2, p. 8 |
| GPT-5.6 Sol / Codex / max | 10 tasks; 10 cells | Mean σ (0–1) | 0.245 | Model and harness both differ | Table 3, p. 8 |
| Learning-side patch cohort | 122 of 263 changed submissions | Mean σ (0–1) | 0.226 | Five systems; Kimi K3 excluded | Table 4, p. 9 |
| Run-side-only patch cohort | 141 of 263 changed submissions | Mean σ (0–1) | 0.126 | Five systems; Kimi K3 excluded | Table 4, p. 9 |

Fact source: [Table 3, p. 8; §3.2, p. 6; Figure 2, p. 8; Table 4, p. 9](https://arxiv.org/pdf/2608.20318v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Learning-side patches average 0.226 versus 0.126 for run-side-only patches, but this is an observational classification of changed submissions, excluding Kimi K3; it is not causal evidence for editing strategy. Model and harness changes are also confounded. The official release currently supports self-hosted scoring, not a blind evaluation service.

<!-- EDITORIAL-NEXT:START -->
Next, replay identical patches across seeds with independently held-out final samples. Match models/scaffolds and separately permit run-configuration versus learning-algorithm edits. Observed correlations between patch type and score do not replace this intervention.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
