# PAST-Bench: separating retained-experience gains from pathway evidence

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-04<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.04003)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](past-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive main 1–6 and Appendices A–F read, including all 26 family rows, trace case studies, equations, human judge audit, mechanism sensitivity, adapter scope, run variance, cost and retry settings. No implementation audit or rerun; figure coordinates not digitized.

[arXiv 2608.04003v1 (2026-08-04)](https://arxiv.org/html/2608.04003v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Organize synthetic tasks into 26 families with cold, learn/update, evaluation and control episodes. Clear conversational context each episode; paired persistence-on exposes prior memory, skills, profiles and history, while off blocks that state. Prompts, tools, model, seeds and grading match within pairs. For example, retain a rule excluding observers from source-document sharing and test its use in a fresh session. Information-gathering families preseed evidence to isolate retrieval triggering.

Editorial placement: Compared with retrospective QA such as LongMemEval, PAST pairs persistence-on/off task execution across procedural reuse, information gathering and updating. It targets incremental task utility, while mechanism-alignment scores do not establish necessity or causal contribution. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

204 episodes: Memory 5 families/41 episodes, Procedural 8/64, Information Gathering 6/48, Update 7/51. Average evaluation episodes within families, families within capabilities, then equally over four capabilities; 204 is not the direct final-score denominator. Codex/GPT-5.4 and Claude Code/Opus 4.6 generated tasks, followed by author checks. Selected comparisons fix MiniMax-M2.7 and Hermes v2026.4.16;50 iterations or 300 seconds, crashes/timeouts score zero. MiniMax-M2.7 judges open-ended answers at temperature 0/max 8192 tokens.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Tables 3/11, MiniMax-M2.7 selected configurations

Scores on 0–1 scale; gap=on minus off. SD is across runs, not a confidence interval. Mech from Table 3, gap statistics from Table 11. The 0.02 mean difference does not establish stable superiority.

Three independent runs per selected configuration; family/capability macro-aggregation over evaluation episodes

| System | Overall gap mean | Overall gap SD | Update gap mean | Update gap SD | Mech |
|---|---|---|---|---|---|
| Hermes | 0.13 | 0.04 | 0.12 | 0.01 | 0.64 |
| Hermes+ | 0.15 | 0.06 | 0.24 | 0.09 | 0.73 |

Locator: Tables 3/11, MiniMax-M2.7 selected configurations · [Source](https://arxiv.org/html/2608.04003v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4 selected persistence-on scores

Task score=safety gate×(0.8 × completion+0.2 × tool-error recovery), not binary success. Clean runs receive recovery 1, so a safe unfinished task can receive partial score.

5/8/6/7 families in four capabilities; within-family evaluation episodes then macro-average

| System | Memory on-score | Procedural on-score | Information on-score | Update on-score | Overall on-score |
|---|---|---|---|---|---|
| Hermes | 0.77 | 0.55 | 0.71 | 0.62 | 0.66 |
| Hermes+ | 0.78 | 0.38 | 0.73 | 0.74 | 0.66 |

Locator: Table 4 selected persistence-on scores · [Source](https://arxiv.org/html/2608.04003v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 12 selected episode costs

MiniMax-M2.7; wall time includes models, tools and runtime overhead. Higher Mech is not free.

Mean over all episodes, unlike evaluation-only task score

| System | Input+output tokens/episode | Seconds/episode |
|---|---|---|
| Hermes | 12615 | 70.5 |
| Hermes+ | 31859 | 77.4 |

Locator: Table 12 selected episode costs · [Source](https://arxiv.org/html/2608.04003v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 8, blinded human audit

Agreement within score tolerances, not exact agreement or classification accuracy; audits open-ended grading, not all Mech semantics.

48 samples, 12 per capability; two blinded author scorers

| Comparison | Absolute difference≤0.25 (%) | Absolute difference≤0.5 (%) |
|---|---|---|
| Judge versus mean of two humans | 68.8 | 91.7 |

Locator: Table 8, blinded human audit · [Source](https://arxiv.org/html/2608.04003v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

The paired toggle is a strong system-level control, explicitly not causal proof. Mech checks expected persistence paths and mixes keywords, entry counts, answer correctness, update signals and near/far task scores; it is neither independent of task performance nor proof of necessity, and may miss alternative valid paths. Hermes+ improves mean overall gap by only 0.02, below run variation, while update gains coexist with procedural regressions. Cold-start scores are not the persistence-off baseline. Isolated synthetic families do not establish long-term cross-family transfer, parameter modification or full recursive self-improvement.

Table 2 says 3-run means across models; Appendix D.5 explicitly identifies only the two MiniMax Hermes/Hermes+ configurations as having three independent runs. Selected variance table restricted to those. Framework rows are adapter-standardized, not default deployments. ZeroClaw uses Python zeroclaw-tools/LangGraph, not Rust executable; Agent-Zero receives 1200 seconds vs 300 for other frameworks. Table 4 full procedural delta of −0.02 differs focused Table 5’s +0.085; separate subsets/diagnostics, not interchangeable. Mech update-resistance signal can award artifact-change/addition credit; it is not strict proof all stale state was removed. No complete per-family control-bound acceptance formula is supplied in inspected metric appendix despite main requirement to clear control bounds; deployment-independent acceptance threshold not established.



Next: Retain the paired toggle and additionally delete, replace or corrupt candidate artifacts, with equal-length irrelevant-state controls. Separate content necessity, valid alternative paths and lifecycle cost. Repeat on unseen families and report paired-gap distributions/intervals; combine with MemoryArena action dependencies and MemProbe state-maintenance diagnostics.
<!-- EVIDENCE:limitations:END -->
