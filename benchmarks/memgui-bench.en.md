# MemGUI-Bench: separating retries, experience and GUI memory

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-03<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.06075)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memgui-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive main 1–7 and Appendix A.1–A.11 read; all evaluator prompts checked in downloaded 59-page v3 PDF because HTML omits prompt bodies. Table 10 long task catalogue sampled across 1–4 app cases, not independently executed or exhaustively re-annotated; screenshot case text read, graphical curves not digitized. No code audit or rerun.

[arXiv2602.06075v3 (2026-08-27)](https://arxiv.org/html/2602.06075v3)

The frozen release reference is preserved. Newly reviewed versions and conditions do not replace initial-release results.
[Fixed-version PDF 2602.06075v3](https://arxiv.org/pdf/2602.06075v3)
[Official source observed 2026-09-30 (mutable page)](https://memgui-bench.github.io/)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Task construction and memory observation

Execute app tasks in snapshot-resettable Android emulators, retry failures up to three times while allowing persistent agent experience. Mirror pairs share app combinations but vary requirements. Evaluation starts with logs and final three screenshots, adds step descriptions, then requests selected historical screenshots. Information-unit scoring supplements binary success.

Editorial placement: Compared with dialogue QA such as LoCoMo, MemGUI-Bench embeds memory demands in app operations, retries and mirror tasks. It adds execution and experience reuse while introducing vision, control and judging into the score. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental conditions and scoring targets

128 tasks / 26 apps: 48 easy, 42 medium, 38 hard; 28/56/34/10 tasks involve 1/2/3/4 apps. Workflow agents share Gemini-2.5-Pro without thinking, but observations and calls differ; end-to-end agents use their own fine-tuned models. Main M2 evaluator uses Gemini-2.5-Flash descriptions and Gemini-2.5-Pro judgments. Step cap=floor(1.4×golden steps+1).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Cumulative success does not isolate learning

Gemini-2.5-Pro workflows with step limits; observations, memory and calls differ. SR@3 is cumulative any-success, not third-attempt accuracy.

SR: 128 tasks; FRR first-attempt failures per system

| System | SR@1 (%) | SR@3 (%) | FRR (%) |
|---|---|---|---|
| Agent-S2 | 27.3 | 49.2 | 21.5 |
| M3A | 32.8 | 47.7 | 16.3 |
| T3A | 22.7 | 42.2 | 20.7 |

Locator: Table 2 and 14, selected February snapshot systems · [Source](https://arxiv.org/html/2602.06075v3)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## The 40-task ablation tests LTM removal

Separate 40-task subset, same-backbone component ablation; no multi-seed intervals supplied.

40 tasks: 13 easy/19 medium/8 hard

| Agent-S2 configuration | SR@1 (%) | SR@3 (%) |
|---|---|---|
| STM and LTM | 27.5 | 45.0 |
| Remove LTM | 17.5 | 25.0 |
| Remove STM and LTM | 5 | 10 |

Locator: Table 3; Appendix A.9.4 · [Source](https://arxiv.org/html/2602.06075v3)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Validate the deployed judge on this suite

M1 all Gemini-2.5-Pro; deployed M2 substitutes Flash only for descriptions. Validation of success labels, not agent success.

256 trajectories: 128 M3A and 128 T3A; three human annotators/trajectory

| Evaluator | F1 (%) | Precision (%) | Recall (%) |
|---|---|---|---|
| M1 | 93.1 | 92.4 | 93.8 |
| M2 | 81.2 | 82.5 | 80.0 |

Locator: Table 1B and 12, judge validation · [Source](https://arxiv.org/html/2602.06075v3)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Token-budget results reclassify existing trajectories

Threshold=golden steps×9507 tokens; estimated usage=actual steps×agent mean tokens/step. Reclassifies over-budget trajectories; not adaptive-policy execution.

128 tasks

| System | Step-budget SR@3 (%) | Estimated token-budget SR@3 (%) |
|---|---|---|
| Agent-S2 | 49.2 | 0 |
| M3A | 47.7 | 21.9 |

Locator: Table 5, Appendix A.9.5 · [Source](https://arxiv.org/html/2602.06075v3)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Supported conclusions and unresolved questions

This executable GUI suite diagnoses memory-related behavior, not isolated memory-module quality. MTPR is confounded by difficulty and only 13 standard tasks. IRR averages 115 task-level ratios; FRR divides by first-attempt failures and weights first recovery on attempts 2/3 by 1/0.5. Judge prompts permit explaining an impossible task to count as success. The deployed evaluator has 81.2% F1 on this suite; 99% from another evaluator/dataset is not interchangeable.

Main prose gives M3A 5.3 seconds/step versus Table 13 14.7 and Table 14 14.5; do not reuse prose value. Table 1 M2 SPA cost 0.028 versus prose 0.031; use table with scope. Table 1 baseline G1 F1=88.2, prose 92.5 is single-app subset Table 11. Table 6/A.5 mention 12 agents, main/Table 7 show 11. Table 9 percentages are multi-label category instances, not percentages of 128 tasks. Token normalization 9507 described as 11-agent mean, but listed per-step numbers are not consistent with that simple mean; treat as authors’ chosen threshold. Failure-analysis percentages have changing denominators and inconsistent Agent-S2 partial hallucination rates 58.2 vs 66.7; omit causal prevalence claims.

Next experiment: Extend the existing 40-task ablation with actual fixed-token reruns; separate same-task retries from held-out mirror transfer, reset experience by group and disclose order. Human final-state checks and app-state validators can separate memory, vision, execution and judge errors. Pair with MemoryArena groups and Mem2ActBench argument grounding.
IRR does not directly measure internal memory: successful tasks are assigned 100%, while unsuccessful implicit-decision tasks are assigned 0%; other cases use correctly retained information units divided by required units.
<!-- EVIDENCE:limitations:END -->
