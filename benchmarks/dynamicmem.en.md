# DynamicMem: when profile reconstruction and personalized service diverge

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.22877)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dynamicmem.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Entire substantive main 1–6 and Appendices A–K read, including all construction, answer, scoring and failure-diagnosis prompts; author checklist statistical-significance disclosure checked. Figures read through captions and source-reported numeric changes, not digitized into invented point values. No code execution or reproduction.

[arXiv2606.22877v1 (2026-06-22)](https://arxiv.org/html/2606.22877v1)

The frozen release reference is preserved. Newly reviewed versions and conditions do not replace initial-release results.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Task construction and memory observation

Generate attributes, habits and preferences with externally motivated changes, turn these into cross-app event chains and state-consistent request/response logs, then retain only checkpoint-supported gold fields. State Completion names the state key; Personalized Service supplies a situation and task requiring a reminder, filter or configuration. Five quarterly checkpoints use only the available log prefix.

Editorial placement: Compared with LongMemEval’s long-history QA, DynamicMem centers changing user profiles and measures both state completion and situation-driven service. Checkpoints and different task demands expose the gap between recovering a fact and using it when needed. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental conditions and scoring targets

10 PersonaHub users; 1790 event chains/17715 logs, about 2.2M tokens per user. 1824 State Completion and 1810 Service problems, 4994 fine-grained scoring points in total. Gemini-3-Flash-preview constructs data; GPT-5-mini builds memory and answers, text-embedding-3-large retrieves, GPT-5.4 scores. Fixed authored queries/tasks. RAG/HippoRAG2 top 20; A-Mem: 5 plus 5 linked neighbors; MemoryOS/SimpleMem: 10; actual context budgets differ.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Named-habit recall differs from scenario-triggered service

0–100 score; per-field s=0.8 × Core+0.2 × Detail/2, Core binary/Detail 0, 1, 2. Same stored corpus, different queries, not necessarily identical retrieved context.

All five checkpoints; 1824 SC/1810 PS problems total; exact habit-family field count not separately supplied in table

| System | Habit State Completion score | Habit Service score | Preference Service score |
|---|---|---|---|
| Vanilla RAG | 53.5 | 5.3 | 65.0 |
| A-Mem | 56.9 | 7.4 | 64.4 |
| MemoryOS | 52.3 | 9.6 | 62.5 |

Locator: Table 2, selected systems; §4.3 scoring · [Source](https://arxiv.org/html/2606.22877v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Three to fifteen months affect the task families differently

Explicit source-reported deltas, not digitized absolute values; history length and current target states both change.

C1=first 3 months; C5=15 months; per-checkpoint eligible fields differ

| System | State Completion change (points) | Service change (points) |
|---|---|---|
| Vanilla RAG | -4.4 | 2.8 |
| A-Mem | -8.9 | 4.9 |
| SimpleMem | -16.7 | -1.5 |

Locator: §5.1 Finding 1, explicit reportedC 5−C1 changes · [Source](https://arxiv.org/html/2606.22877v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## The shared answerer receives unequal context budgets

Shared GPT-5-mini answerer, unequal context sizes; does not normalize ingestion cost.

Average retrieved-memory context per query

| System | SC context (thousand tokens) | Service context (thousand tokens) |
|---|---|---|
| Vanilla RAG | 12.6 | 14.6 |
| A-Mem | 15.6 | 17.0 |
| SimpleMem | 20.8 | 20.7 |

Locator: Appendix I, measured answer-context budget · [Source](https://arxiv.org/html/2606.22877v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Judge calibration covers one user and four configurations

189 items each from A-Mem/HippoRAG2/Oracle/RAG; does not validate all users/systems or the error-taxonomy classifier.

Sample sizes are shown in the table.

| Scope | Audited items | Unreasonable judgments | Agreement (%) |
|---|---|---|---|
| User001, four configurations | 756 | 28 | 96.3 |

Locator: Appendix I human judge audit · [Source](https://arxiv.org/html/2606.22877v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Supported conclusions and unresolved questions

Profile completion declines with history, but Service is not uniformly stable: SimpleMem drops slightly. Retention and updating should be separated; curves/cases alone cannot prove a compression/index mechanism caused a failure. Gold evidence marks first occurrence only, so valid later restatements can make exact citation recall understate evidence availability. Oracle logs provide a model-conditioned reference, not a hard ceiling. Ten synthetic users, observability filtering, no error bars and single-user judge calibration limit generalization.

Appendix K says cited evidence is everything the answerer saw; Appendix J generates a local concise citation list from a larger memory context. Treat attribution as conditional until code/artifacts reconcile. §5.1 says the habit Service gap is not a memory failure because corpus is shared; different queries/retrieved contexts still confound that inference. Update figure caption uses changes from most recent previous presence; nearby prose says both regimes anchoredC 1. Use caption definition for update, C1 anchor for stable retention. No statistical significance/error bars, explicitly acknowledged in checklist.

Next experiment: Freeze logs, queries and total budget; compare raw records, summaries and explicit updated state, separating stable/changed fields quarterly. Retain full retrieved context and answer citations, audit sufficiency separately, then run paired oracle-evidence and answerer-swap interventions. Add executed service tasks to measure stale-profile costs.
All app records are synthetic. Service tasks generate and score reminder, filter or configuration fields without executing tools or testing realized outcomes.
The reported “over 93%” failure attribution comes from 300 sampled non-perfect cases per system/task with nonempty citations; failures without citations are excluded. The answerer generates local evidence excerpts, while diagnosis treats those excerpts as all available evidence. Without verifying equivalence to the full retrieved context, this does not establish that changing the answerer cannot help.
<!-- EVIDENCE:limitations:END -->
