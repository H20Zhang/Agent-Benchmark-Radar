# MemTrapBench: when relevant history interferes with current reasoning

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-20<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.20202)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memtrapbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Main 1–5 and entire substantive Appendices A–D read. HTML omits prompt bodies; all construction/evaluation/AdaptiveMem prompts and four long case histories read in 33-page PDF. No code audit/rerun. Medical content is a constructed benchmark example, not independently validated clinical advice; no such advice reproduced in note.

[arXiv 2608.20202v1 (2026-08-20)](https://arxiv.org/html/2608.20202v1)

[Supplementary source 2608.20202v1, inspected 2026-09-30](https://arxiv.org/pdf/2608.20202v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Authors design a prior, final query and gold answer; GPT-5.4 expands these into repeated conditioning, noise and a related query under changed conditions. Final queries must be independently answerable without explicit reset instructions. Bias, feedback-induced avoidance and task-boundary cases test overextension of past experience; Safety deliberately introduces false sandbox beliefs. Not all memories are objectively true. AdaptiveMem is a system-prompt intervention targeting these risks, not a new storage algorithm.

Editorial placement: Where LongMemEval mainly asks for useful historical information, MemTrapBench retains history that may interfere with current reasoning and measures misuse. It adds a when-not-to-use-memory axis; deliberately false premises in the safety subset differ from facts that were once true but became stale. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

1050 instances: 350 Task Boundary, 350 Cognitive Bias, 200 Safety and 150 Trauma/feedback avoidance; main text histories span 18–40 turns. Answer models are Gemini-3-Flash-Preview and Qwen3-30B-A3B-Instruct-2507. Compare FullText, LightMem, MemOS, SimpleMem, EverMemOS and no history. GPT-5.2 is primary judge; Claude-Sonnet-4.6 is the alternative. Numeric default decoding values, embeddings and adapter retrieval budgets are unspecified. Prompts score dimensions 0–5; Safety and 24-game variants list two dimensions rather than the usual four.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 1, Gemini-3-Flash-Preview selected rows

Paper percentage-scaled quality scores, not binary success. Fixed Gemini answerer; Average numerically matches four-scenario equal weighting, not pooled 1050-case accuracy. Memory budgets are not explicitly matched.

350/350/150/200 instances per displayed scenario; 1050 total

| Strategy | Task Boundary | Cognitive Bias | Trauma | Safety | Average |
|---|---|---|---|---|---|
| wo/Mem | 87.08 | 70.95 | 86.73 | 95.9 | 85.16 |
| FullText | 47.01 | 44.36 | 69.43 | 81.9 | 60.68 |
| EverMemOS | 74.7 | 54.23 | 86.07 | 69.7 | 71.17 |

Locator: Table 1, Gemini-3-Flash-Preview selected rows · [Source](https://arxiv.org/html/2608.20202v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 3, TaskBoundary dedicated diagnostic

0–100 scores; exact subset count/model label not explicit in this table, so not a fully specified main-board configuration. Do not pool with Table 1.

Dedicated TaskBoundary subset; exact sample count not reported

| History condition | Correctness score | Composite score |
|---|---|---|
| No history | 96.87 | 92.29 |
| Related history, trap removed | 97.7 | 94.39 |
| Trap-inducing history | 45.33 | 31.05 |

Locator: Table 3, TaskBoundary dedicated diagnostic · [Source](https://arxiv.org/html/2608.20202v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## §3.6/Figure 4, explicit AdaptiveMem gains

Absolute change from adding AdaptiveMem to the same framework, not gain over no-memory or a result on all 1050 cases.

200 randomly sampled MemTrapBench instances; separate 200 LongMemEval samples for utility checks

| Memory strategy | Gemini gain (points) | Qwen gain (points) |
|---|---|---|
| FullText | 11.8 | 4.2 |
| LightMem | 14.9 | 2.5 |
| EverMemOS | 11.3 | 2.6 |

Locator: §3.6/Figure 4, explicit AdaptiveMem gains · [Source](https://arxiv.org/html/2608.20202v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 5, dedicated subset judge sensitivity

0–100 scale, SD in points; judges agree directionally but differ in absolute score, without a human-judge comparison.

Three independently generated responses/settings on dedicated subset; sample count not stated

| Judge | No-memory composite | Memory composite | Memory SD |
|---|---|---|---|
| GPT-5.2 | 92.29 | 31.05 | 5.68 |
| Claude-Sonnet-4.6 | 95.57 | 40.07 | 2.69 |

Locator: Table 5, dedicated subset judge sensitivity · [Source](https://arxiv.org/html/2608.20202v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

This designed negative-transfer stress test does not estimate average utility or harm prevalence in ordinary workloads. Overall decline does not imply every scenario declines: Qwen FullText Trauma 90.27 exceeds no-memory 87.17. Existing no-trap controls support a content effect but leave exact length/prompt matching to audit. Alternative-judge directional agreement is not human validation; absolute scores differ. The 24-game variant permits factorial and other higher operations, motivating explicit matched operator rules to separate rule inference from fixation.

Main §3.2 calls LightMem strongest Qwen memory strategy at 70.13 while FullText scores 70.99; this claim holds only among four external frameworks, not all five history strategies. Table 3 Task Boundary no-memory 92.29 differs main Table 1’s 87.08; a dedicated subset, never pool. Exact subset count and model label for Table 3–5 not fully specified. Table 5’s ± values are standard deviations over three independently generated responses, not confidence intervals or human agreement. Table 1 Average matches equal weighting of four scenario scores, not instance-count weighting; precise normalization/heterogeneous rubric aggregation not fully specified. Appendix construction variants request 30–40 or 20–30 turns versus observed 18–40 main summary; use dataset summary rather than asserting every generated item follows one prompt length. Some Case D 24-game histories say no solution without explicit operator scope, while gold allows extra operations. No-memory solvability alone does not completely remove convention ambiguity.



Next: Match query and context budget across valid memory, irrelevant memory, trap-removed same-topic history and no history. Measure positive and negative transfer. Compare AdaptiveMem with an equal-length generic reminder and unseen memory-dependent tasks; report correctness separately from format/conciseness.
<!-- EVIDENCE:limitations:END -->
