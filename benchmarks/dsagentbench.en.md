# DSAgentBench: end-to-end data science through graphical desktops

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.10366)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dsagentbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read the complete 23-page main text, limitations and Appendices A–D, covering tasks, environments, grading, every prompt template, results and error analysis; visually checked Tables 3/4/11 and failure screenshots in Figures 6–9.

[arXiv 2608.10366v1 · 2026-08-11](https://arxiv.org/pdf/2608.10366v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DSAgentBench contains 275 human-authored tasks on an OSWorld-based Ubuntu desktop, covering acquisition, exploration, features, modeling, evaluation and visualization. Agents use 1920×1080 screenshots or screenshots plus accessibility trees and operate editors, notebooks, terminals and browsers through PyAutoGUI. Command-line work is reached through desktop interaction. Only 56.7% of tasks are multi-stage; not every task spans the full lifecycle.

[Source](https://arxiv.org/pdf/2608.10366v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DA-Code exposes executable data-science tools; DSAgentBench reaches editors, terminals and browsers through a graphical desktop. It adds UI grounding and interaction recovery to analytical quality. GUI success is not pure analysis capability, and only some tasks span multiple lifecycle stages.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Main runs permit fifteen interaction steps and 1,800 seconds, with temperature 0.1, top-p 0.9, at most 2,000 output tokens per call and a two-second post-action delay. Task evaluators check artifacts, execution and numeric/visual requirements to produce 0–1 scores; scores ≥0.95 count as success, while average score is separate. Approximately 10% of tasks add a visual judge after deterministic checks: usually GPT-4o, replaced by Gemini-2.5-Pro for GPT-4o outputs. Open models are evaluated only on screenshots, without accessibility-tree support.

[Source](https://arxiv.org/pdf/2608.10366v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected within-model success rates across observation interfaces

275-task benchmark; success requires task score≥0.95; fifteen interaction steps and 1,800 seconds; temperature 0.1, top-p 0.9, 2,000 output tokens/call; percentages reproduced as reported without inferring unpublished raw counts.

| Model | Screenshot success (%) | Screenshot + A11y success (%) |
| --- | --- | --- |
| Claude-4.6-Sonnet | 50.55 | 56.70 |
| GPT-5 | 23.63 | 29.81 |
| GPT-4o | 19.34 | 24.54 |

Source location: Table 3, p. 7; section 5.2; Appendix B.5–B.6, pp. 15–16 · [Source](https://arxiv.org/pdf/2608.10366v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## GPT-4o budget ablation: selected endpoints

GPT-4o with screenshot+A11y; Table 11; success threshold 0.95, with mean score a separate metric; not a budget curve for other models.

| Interaction budget | Task success (%) | Mean score (0–1) |
| --- | --- | --- |
| 15 steps | 24.54 | 0.55 |
| 50 steps | 25.81 | 0.57 |

Source location: Section 5.4 and Table 11, pp. 8, 15 · [Source](https://arxiv.org/pdf/2608.10366v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

Accessibility metadata helps systems differently, so UI grounding and analytical reasoning should not be collapsed into general data-science ability. GPT-4o gains little from fifteen to fifty steps, but that single-model ablation does not establish budget independence for all agents. Error analysis samples 604 closed-source and 150 open-source runs; limited reruns do not provide variance estimates for every configuration.

The abstract calls evaluation deterministic, but the main text says roughly 10% of tasks use visual LLM judging after deterministic gates. Appendix Table 15 labels average score as percent although its cells use 0–1. The example JEDI prompt still says 100 steps, unlike the main 15-step experiment; actual budgets require runtime configuration, not template inference. The paper’s characterization of DA-Code/MLAgentBench as only static execution is too broad and is not adopted.

Hold data tasks fixed while comparing GUI, terminal API and typed data-tool interfaces under matched wall-clock and model-call budgets. Inject interaction errors at identical intermediate states and separately measure grounding, analysis and recovery.

[Source](https://arxiv.org/pdf/2608.10366v1)
<!-- EVIDENCE:limitations:END -->
