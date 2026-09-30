# Mem2ActBench: grounding arguments when the correct tool is supplied

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.acl-long.370/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mem2actbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Entire substantive main 1–6, limitations/ethics, Appendix A–D including algorithm and prompt templates read. Official repository README/root inspected for evaluator clarification; visible code is construction pipeline, evaluator not verified. No reruns.

[ACL 2026 final proceedings (2026-07)](https://aclanthology.org/2026.acl-long.370.pdf)

[Official source observed 2026-09-30 (mutable page)](https://github.com/Cantaloupe-M/Mem2ActBench)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Merge tool-use dialogue and conversational noise, extract entity-bound facts, resolve local conflicts and topologically order memory updates. Generate gold calls first, then hide memory-derived arguments in the final query; lexical and model filters reject obvious leakage.

Editorial placement: Compared with historical-fact QA such as LoCoMo, Mem2ActBench requires history-grounded tool arguments. Because the main setting supplies the correct tool, its added coordinate is argument grounding rather than tool selection or full execution success. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

400 generated tasks; evaluation uses 429 evidence-containing sessions in original order. Seven memory frameworks share Qwen2.5-Instruct backbones at 7B/32B/72B, temperature 0; BGE-M3 embeddings for retrieval. Main table supplies the target tool. History-chain construction uses Qwen3-Next-80B-A3B-Instruct; reverse queries use Kimi-K2-Thinking.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Main results compare arguments, not successful execution

Reported parameter F1,0–100; not successful execution rate. Gold tool supplied; same backbone within each column. Indexing and retrieval implementations differ.

Main 400 tasks; selected 429-session history; precise F1 micro/macro implementation not supplied in inspected paper

| System | Qwen2.5-7B argument F1 | Qwen2.5-32B argument F1 | Qwen2.5-72B argument F1 |
|---|---|---|---|
| A-mem | 30.99 | 33.72 | 35.93 |
| LTMemory | 26.71 | 33.87 | 35.32 |
| Mem0 | 14.21 | 24.52 | 28.95 |

Locator: ACL final Table 3, selected parameter metric · [Source](https://aclanthology.org/2026.acl-long.370.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Clarification supplies more evidence and extra turns

Parameter F1 and unigram overlap, 0–100. Qwen2.5-72B-Instruct. Oracle user reveals historical fragments during clarification; this changes turns/information access and is not directly comparable or a hard ceiling.

200-task subset

| Strategy | Argument F1 | BLEU-1 |
|---|---|---|
| LTMemory baseline | 29.24 | 50.64 |
| Query expansion | 32.42 | 53.07 |
| Self-refine | 29.68 | 51.73 |
| Interactive clarification | 48.68 | 61.89 |

Locator: ACL final Table 6, §5.6 · [Source](https://aclanthology.org/2026.acl-long.370.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 91.3% validates data quality, not agent success

Five experts, at least two per reviewed item; sample validation, not agent outcomes. 91.3% does not identify an integer pass count out of 200; aggregation details unclear.

The subset and protocol are specified above; exact per-cell sample counts are not supplied.

| Validation stage | Sampled items | Validated (%) |
|---|---|---|
| Fact extraction | 200 | 96.5 |
| Conflict resolution | 150 | 86.7 |
| Memory dependency | 200 | 91.3 |

Locator: ACL final Table 2 · [Source](https://aclanthology.org/2026.acl-long.370.pdf)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

The argument metric and selected diagnostics show headroom in evidence use. Main results cannot establish autonomous tool choice or execution quality. Synthetic conflict removal, model-dependent leakage screening, unreported F1 aggregation and unresolved TA semantics limit stronger conclusions.

§4.1 defines TA as correct tool plus exact all-argument match; Table 3 reports TA 87–97% with parameter F1 of 14–36, while §5.4 separately names TSA(tool only) and EM(tool plus all arguments). Do not silently relabel or certify TA; unresolved evaluator gap. Table 4 column Recall@k contains 1/5/10 retrieval depths, not measured recall. Table 4 and Table 5 do not clearly name backbone/configuration; omit from fully conditioned primary comparison until verified. Abstract/Table 1 average 12 turns versus §3.4 average 13. Report approximately 12–13 or avoid precise average. Table 1 session/token definitions mix corpus totals and per-session statistics; do not claim each query sees 2029 sessions/3238 total tokens.

Next: First verify the released evaluator against hand-scored calls. Then fix backbone/schema/budget and compare gold versus retrieved evidence with hidden versus supplied tool identity. Track exact argument match and real execution separately; pair with MemoryArena for closed-loop utility.
The construction corpus contains 2029 sessions, while evaluation uses 429 evidence-containing sessions. Queries may explicitly mention earlier preferences; they hide parameter values rather than every cue to memory use.
<!-- EVIDENCE:limitations:END -->
