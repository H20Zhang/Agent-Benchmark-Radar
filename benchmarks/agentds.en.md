# AgentDS: AI-allowed teams versus later autonomous baselines

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-10-18<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2603.19005)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agentds.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 21-page v3, including the disclosure and Appendices A.1–A.3 and B: full prompts, data previews, manual repair policy, inference settings and agent deployment. The June revision follows the October 2025 competition.

[arXiv 2603.19005v3 · 2026-06-03](https://arxiv.org/pdf/2603.19005v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

AgentDS compares AI-allowed competition teams with later AI baselines on 17 synthetic multimodal challenges. It has no controlled human-only arm. Scores are participant-relative quantiles, averaged within domains and then equally across six domains; they are not success rates.

<!-- EDITORIAL-METHOD:START -->
Seventeen synthetic challenges span six application domains and modalities including tables, text and images, with difficulty calibrated against generic pipelines. Teams may use AI, choose tools and submit repeatedly; autonomous agents and direct-prompt baselines are evaluated afterward. An illustrative team workflow interprets multimodal inputs, chooses features/models and revises submissions using feedback, while agent baselines deliver under much shorter deadlines. Scores become participant-relative quantiles, so changing the comparison population can change the relative score of an unchanged solution.

Editorial placement: unlike MLE-bench’s autonomous agents and historical medal thresholds, AgentDS includes AI-allowed competition teams in the outcome distribution. It describes a collaborative ecosystem but lacks budget-/population-matched human-only controls needed for causal collaboration claims.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Teams had ten days and up to 100 submissions per challenge. Agentic tools share Claude Opus 4.7, receive ten minutes and report their best submitted score. Direct prompting uses one call, later code execution and limited manual repairs; its default execution timeout is one hour.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V3; all 17 challenges, six equally weighted domain scores. Quantiles use each challenge’s successful-submitter pool; non-submissions score zero. Human and AI conditions are deliberately shown separately.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Opus 4.7 + MorphMind | 17 challenges / 6 domains | Overall quantile (0–1) | 0.510 | 10 min; best submitted result | §2.6.2/Figure 2, p. 6 |
| Claude Opus 4.7 + Claude Code | 17 challenges / 6 domains | Overall quantile (0–1) | 0.458 | 10 min; CLI 2.1.30; best submitted result | §2.6.2, p. 6; Appendix B, p. 21 |
| GPT-5.5 · direct prompting | 17 challenges / 6 domains | Overall quantile (0–1) | 0.415 | One call; limited manual code repair | §2.6.2, p. 6; Appendix A.2, p. 20 |
| Best human–AI team | 17 challenges / 6 domains; 29-team competition | Overall quantile (0–1) | 0.860 | 10 days; up to 100 submissions/challenge | Figure 5, p. 9; §2.5, p. 5 |

Fact source: [§2.6.2/Figure 2, p. 6; §2.6.2, p. 6; Appendix B, p. 21; §2.6.2, p. 6; Appendix A.2, p. 20; Figure 5, p. 9; §2.5, p. 5](https://arxiv.org/pdf/2603.19005v3)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Time, retries, compute and participant selection are unmatched, so the gap cannot establish a causal collaboration benefit or replacement claim. Domains are equally weighted, not individual challenges. Synthetic difficulty is deliberately calibrated against generic pipelines. The authors disclose affiliations with MorphMind’s developer.

<!-- EDITORIAL-NEXT:START -->
Next, randomize similarly experienced teams to no-AI, standardized-AI and unrestricted-tool conditions with matched time, submissions and compute; give autonomous agents the same resources. Normalize against fixed external references to avoid participant-composition score drift.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
