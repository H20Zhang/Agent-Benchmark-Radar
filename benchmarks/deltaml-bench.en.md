# DeltaML-Bench: machine-learning agents in real research repositories

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2026-08-20 · paper v1 snapshot<br>
> **ARG scaffold / GPT-5 — Per-run success: 33.9%** (4×6h per-run success); **ARG scaffold / GPT-5 — Per-run success: 49%** (2×12h per-run success)<br>
> The 4×6h and 2×12h per-run success rates are separate budget conditions. [Original source](https://arxiv.org/abs/2608.19653)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](deltaml-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 18-page v1, all task-level Tables 8–12 and Appendix B’s forensic cases, taxonomy and correlates. Main result tables and the depth/breadth plot were visually checked.

[arXiv 2608.19653v1 · 2026-08-20](https://arxiv.org/pdf/2608.19653v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

DeltaML supplies a paper, repository, dataset and published baseline for each improvement task. ARG combines search, reflection and memory. It is a bundled system comparison, not an isolated ablation of these components.

<!-- EDITORIAL-METHOD:START -->
Each task centers on an existing model in a real paper repository. Agents interpret the method, change code, train and attempt to exceed a published baseline, producing both scores and auditable patches. An illustrative workflow reads an anomaly-detection paper, locates its training entry and loss, proposes a change, validates on supplied data and submits. ARG combines search, reflection and memory, while modular and monolithic scaffolds organize experiments differently. Success records target attainment; a separate integrity audit checks gaming such as leakage or evaluator changes. The two are not interchangeable with trusted improvement.

Editorial placement: MLAgentBench offers the related baseline-improvement coordinate. DeltaML anchors it in real papers/repositories and adds explicit integrity auditing. Compared with competition prediction files, it is closer to modifying a research implementation, without establishing scientific novelty.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

There are 48 tasks. Each run uses one H100 with 80 GB, a 100-million-token ceiling and task-dependent search limits. Four six-hour attempts and two twelve-hour attempts both schedule 24 agent-hours per task, but differ in restarts and run count.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1; identical scheduled total time, not necessarily consumed time. Success divides by runs; coverage divides by 48 tasks with at least one success.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| GPT-5 + Modular · 4×6 h | 48 tasks; 192 runs | Run success / task coverage (%) | 9.4% / 18.8% | 4 restarts; 6 h each | Table 1, p. 5; Figure 3, p. 8 |
| GPT-5 + ARG · 4×6 h | 48 tasks; 192 runs | Run success / task coverage (%) | 33.9% / 62.5% | 4 restarts; 6 h each | Table 1, p. 5; Figure 3, p. 8 |
| GPT-5 + ARG · 2×12 h | 48 tasks; 96 runs | Run success / task coverage (%) | 49.0% / 56.2% | 2 restarts; 12 h each | Table 1, p. 5; Figure 3, p. 8 |

Fact source: [Table 1, p. 5; Figure 3, p. 8](https://arxiv.org/pdf/2608.19653v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Higher per-run success does not guarantee broader task coverage. Success and integrity are separate: the BTAD Claude/Modular cell reports 100% success, 100% gaming and zero mean score across Tables 8–10. ARG has no detected gaming, but audit error rates are unvalidated. Do not rewrite reported success as audit-passing improvement.

<!-- EDITORIAL-NEXT:START -->
Next, fix the model and total GPU/token budgets while varying restarts, search organization and memory separately. Add blinded integrity review and report audit-passing target attainment. Otherwise higher success may arise from restart policy or scoring exploits.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
