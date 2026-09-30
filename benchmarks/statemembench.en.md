# StateMemBench: From recalling facts to maintaining operative state

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · 2026-08-20 · paper v1 snapshot<br>
> **StateMem / DeepSeek — State score: 36.3%** (Same-backbone DeepSeek state-maintenance score)<br>
> A state-memory configuration under the specified model, not a full cross-model or cross-protocol winner. [Original source](https://arxiv.org/abs/2608.19652)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](statemembench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

Read Sections 1–7 and Appendices A–I: cross-benchmark error labeling and human audit, symbolic scenarios and validation, all StateMem prompts, the answer wrapper and matched control, costs and all supplemental results. Reviewed the August 20, 2026 first version without reproducing code. Conflicting tables remain unresolved.

[Full primary paper](https://arxiv.org/pdf/2608.19652v1) · 2608.19652v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

LongMemEval already includes knowledge updates, and MemoryAgentBench tests ordered fact edits. StateMemBench additionally scores selection of a stale value separately from generic errors. Compared with concurrent STALE, it explicitly states conflicts and dependencies, reducing the confound of discovering implicit relationships. Unlike conventional dialogue state tracking, it evaluates final decisions without imposing a fixed slot representation. Anti-traps require retaining an earlier value when it remains valid, defeating an always-pick-the-latest heuristic. This compares measurement coordinates: LongMemEval and LoCoMo are external generalization tests, not direct sources of StateMemBench questions.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

A symbolic program specifies rules, value updates, scoped exceptions, commitments and retractions; deterministic replay computes the operative answer. Traps arise when lazy policies such as trusting the latest mention, most frequent value or cached derivation disagree with replay. The five modes are status, salience, sequence, compound and anti-trap. Public research, shopping and personal-finance material supplies surface entities and vocabulary; state values and trap semantics are independently sampled. Sonnet-4.6 renders dialogues, followed by checks for load-bearing facts in assigned sessions and banned phrases. A strong reader with relevant sessions must answer correctly in at least two of three samples; a weak reader with full history must hit the drift target in at least three of five, or retain the gold answer for anti-traps. This deliberately selects model-trapping scenarios.

Short Set A has 190 scenarios, each with 18 sessions, a median 165 turns and roughly 3,000 tokens, with one probe. Long Set B has 44 scenarios, each merging three trap threads across roughly 38 sessions, a median 599 turns and 7,000–15,000 tokens, with three probes. Thus there are 234 scenarios but 322 graded probes. In a shopping example, ten packs weekly implies twenty for two weeks; after the weekly amount falls to seven, the correct two-week total is fourteen rather than the cached twenty. Hidden grading pools contain the current answer, targeted drift value and plausible distractors; answer models never see the choices.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

StateMem makes one encoder call per turn to create structured units with content, priority, provenance and dependencies. Superseded units remain for audit but are inactive; a deterministic dependency traversal flags downstream units for rechecking without extra model calls. One answer call receives active state and triggers, then recomputes from current inputs. Roughly 165–600 encoder calls per scenario make this substantially more expensive than a single long-context call.

Memory/retrieval comparisons use matched Qwen-3.5-9B or DeepSeek-V4-Flash backbones, thinking disabled and temperature zero, with one run per configuration and a fixed DeepSeek-V4-Pro judge. Retrieval uses k=10 on StateMemBench and k=20 on external LongMemEval/LoCoMo. Accuracy is current-state answers divided by scored probes; drift rate is targeted stale answers divided by all probes, not by errors. Off-pool responses must accompany drift rates because non-answers can appear deceptively resistant. Deterministic word-boundary matching covers about 28% of answers and agrees with the judge on 94.1% of that subset; remaining free-form mapping still relies on the model judge.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Full set: accuracy, drift and off-pool responses

DeepSeek-V4-Flash, thinking off, temperature zero, DeepSeek-V4-Pro judge; 190 short and 132 long probes, total 322. Accuracy is a 0–1 proportion; drift also uses 322 as denominator. Other in-pool distractor answers are omitted, so displayed counts need not sum to 322.

| Method | Correct /322 | Accuracy | Drift /322 | Off-pool count |
|---|---|---|---|---|
| Long-context | 48 | 0.149 | 206 | 64 |
| Dense | 66 | 0.205 | 177 | 66 |
| A-Mem | 64 | 0.199 | 181 | 72 |
| StateMem | 117 | 0.363 | 158 | 36 |
| StateMem without dependency propagation | 120 | 0.373 | 157 | 36 |

Source: Tables 3 and 14 · [Paper](https://arxiv.org/pdf/2608.19652v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## State-chain contribution with matched context

Frozen 60-probe set, 30 short and 30 long probes from 22 long scenarios. Units are percent correct, k=10; each store is built once with identical retrieved chunks and a fixed DeepSeek-V4-Pro judge. Control and wrapper both see transcript plus retrieval and use one answer call with a maximum 250-word preliminary section. Backend-alone sees retrieval only. Its entire gain cannot be attributed to state structure.

| Backbone / backend | Backend alone (%) | Matched control (%) | State wrapper (%) |
|---|---|---|---|
| Qwen-3.5-9B / Mem0 | 25.0 | 28.3 | 56.7 |
| DeepSeek-V4-Flash / Mem0 | 28.3 | 56.7 | 71.7 |
| Qwen-3.5-9B / BM25 | 20.0 | 31.7 | 56.7 |
| DeepSeek-V4-Flash / BM25 | 21.7 | 48.3 | 70.0 |

Source: Table 6; Appendices F.2–F.5 · [Paper](https://arxiv.org/pdf/2608.19652v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

On DeepSeek, StateMem raises full-set accuracy from the strongest retrieval baseline’s 0.205 to 0.363, yet roughly half of probes still select the drift target. Removing dependency propagation reaches 0.373, revealing over-propagation on anti-traps rather than a monotonic benefit from every component. On Qwen, StateMem scores 0.233 versus GraphRAG’s 0.224, with paired p=0.82, so superiority is not established. External tests show trade-offs: DeepSeek StateMem/full-context scores are 0.656/0.666 on LongMemEval and 0.592/0.587 on LoCoMo; Qwen LoCoMo is 0.566/0.612. These do not justify an unconditional claim of no recall loss.

The wrapper’s controlled results support question-conditioned revision chains, but it does more than rewrite retrieved snippets. Relative to the transcript-matched control it adds about 155 input and 169–188 output tokens without extra calls; relative to a bare backend it also adds full history, with median inputs around 8,600 tokens here and 87,000 on LongMemEval. The 60-probe subset overweights anti-traps, so its scores are not directly comparable with the full 322-probe ranking.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

Trap policies and StateMem’s design are aligned; the authors treat own-benchmark margins as optimistic upper bounds and use external tasks to test generalization. Short/long sets also change thread composition and category mix, so aggregate differences cannot isolate a pure length effect. Small-to-mid-scale backbones, a same-family DeepSeek judge, Claude rendering and single runs limit generalization. Near-floor LightMem/MemoryOS results may reflect workload sensitivity or integration gaps; the authors exclude them from best-capability claims. The 35B Qwen context was reduced to 16,384 tokens after memory exhaustion, causing long-set tail truncation. A small human audit assigns less drift than model judges, so cross-benchmark prevalence retains a judge-labeled upper-bound interpretation. A stronger next test preregisters unseen revision mechanisms, matches complete input and cost, and evaluates models not used for scenario filtering.

Table 6 and Appendix F.4 require a unit correction: the wrapper set has 30 short probes and 30 probes drawn from 22 long scenarios, not 30 complete long scenarios. Appendix Table 12’s Dense-alone category cells imply roughly 5% on Qwen and 0% on DeepSeek, conflicting with Table 6’s 21.7%/31.7% on the purported same 60 probes. These cells are not merged here, and maximum gain ranges are not treated as unambiguous. Some Qwen grading-drop descriptions also do not align cleanly with full-table denominators; the main selected rows above use the clearer DeepSeek counts.
<!-- EVIDENCE:limitations:END -->
