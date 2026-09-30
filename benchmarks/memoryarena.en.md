# MemoryArena: cross-session action dependencies and strict success

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-18<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.16313)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memoryarena.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Main 1–5 and substantive Appendix A–C methods/results read. PDF prompts 8–11 and case-study excerpts 12–19 inspected; long illustrative mathematical derivations not independently proof-checked or fully rederived. Figure curves not digitized.

[arXiv 2602.16313v2 (2026-09-17)](https://arxiv.org/html/2602.16313v2)

[Supplementary source 2602.16313v2, inspected 2026-09-30](https://arxiv.org/pdf/2602.16313v2)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Reset memory per task group. Execute interdependent subtasks in separate sessions, store completed interaction traces, retrieve for the next session and continue acting. Shopping enforces compatibility; travel accumulates cross-person constraints; search adds conditions; formal reasoning reuses intermediate derivations.

Editorial placement: Compared with LongMemEval’s historical QA, MemoryArena uses earlier subtask experience/state in later actions and evaluates dependent task groups. The new coordinate is cross-session action dependence; some search subquestions still need memory-off controls to verify that dependence. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

v2 contains 701 task groups and 4,850 subtasks: 150 shopping, 270 travel, 221 search, 40 math and 20 physics groups. Appendix B uses session-start retrieval, although general equations allow action-level retrieval. Shopping permits 20 rounds/item and 4,096 output tokens; travel 30 tool steps/person; formal reasoning 8,192 output tokens at temperature 0.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## External memory helps some tasks and hurts others

Fractions in [0,1]; PS averages passed-subtask fractions per group; sPS additionally averages satisfied constraints within each subtask. Same Claude-Sonnet-4.6 task agent. Memory representations/access differ; no universal winner. Search/formal SR scores final answers, while shopping/travel require globally valid output.

Shopping 150, travel 270, search 221, math 40, physics 20 groups, per v2 Table 2; reported rounded fractions

| System | Shopping SR | Shopping PS | Travel SR | Travel sPS | Search SR | Math SR | Physics SR |
|---|---|---|---|---|---|---|---|
| Claude-Sonnet-4.6 / Long context | 0.13 | 0.79 | 0.0 | 0.89 | 0.06 | 0.37 | 0.4 |
| Claude-Sonnet-4.6 / Text-Embedding-3-Small | 0.04 | 0.55 | 0.0 | 0.42 | 0.27 | 0.37 | 0.63 |
| Claude-Sonnet-4.6 / MemoRAG | 0.01 | 0.54 | 0.0 | 0.47 | 0.35 | 0.3 | 0.5 |

Locator: v2 Table 5, Appendix C.1 · [Source](https://arxiv.org/html/2602.16313v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Conditional constraint accuracy declines without reaching zero

Conditional constraint pass rate, [0,1]. Observed decline remains nonzero at L4. This is not unconditional whole-trip success or proof that only reasoning failed.

Group-travel constraints conditional on previous correct constraints; counts per level not supplied

| Condition | L0 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|
| Long-context memory | 0.48 | 0.29 | 0.21 | 0.18 | 0.15 |

Locator: v2 Table 7, Appendix C.3 · [Source](https://arxiv.org/html/2602.16313v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## An approximate oracle intervention is already reported

Long-context task score and delta on [0,1] scale. Inject gold prior outcomes plus LLM-distilled workflows. Approximate oracle changes evidence and presentation, so it is not a hard upper bound.

Exact intervention sample counts/model identifier not specified in Table 8

| Task | Original score | Reported absolute delta |
|---|---|---|
| Group travel | 0.0 | 0.05 |
| Progressive search | 0.06 | 0.05 |

Locator: v2 Table 8, Appendix C.3 · [Source](https://arxiv.org/html/2602.16313v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

External memory can help search while hurting shopping under the same task agent. Zero strict travel success coexists with substantial soft constraint satisfaction. End-to-end scores conflate memory with action/reasoning; approximate-oracle gains narrow the diagnosis without proving a single cause.

Table 3/caption GPT-5.1-mini versus §4.1 GPT-5-mini; exact identifier unresolved. Appendix C.3 prose says depth pass rate eventually zero; Table 7 L4=0.15. Use table. Table 8 math original 0.26 differs Table 3 long-context 0.21; do not merge. Main equations action-level retrieval versus Appendix B session-level actual setup. Progressive-search decomposition prompt asks self-contained independent subqueries despite cross-session dependence framing; final prompt includes original full question, so dependency necessity needs controlled no-history validation.

Next: Use identical task seeds for no-history, raw-history, learned memory and gold-outcome-plus-workflow conditions. Match action/retrieval budgets and log acquisition versus use failures. Pair with LoCoMo for recall and MemProbe for controlled preservation/update behavior.
Search and formal reasoning score the final subtask; shopping and travel require globally valid outputs. Approximate oracle memory is an existing diagnostic, not a substitute for a matched intervention.
<!-- EVIDENCE:limitations:END -->
