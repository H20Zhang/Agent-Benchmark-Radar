# AuthMem-Bench: when retained information acquires unwarranted authority

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-03<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.01679)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](authmem-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–6 and Appendices A–F, including all detailed results, audit/decomposition tables and PDF-only judge, consolidator, source-predictor and action prompts. No implementation audit or independent reproduction.

[arXiv 2608.01679v2 (2026-08-04)](https://arxiv.org/html/2608.01679v2)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

AuthMem-Bench places the same claim in sources with different authority, then asks for the same native tool action using its operative value. A third-party address report and the user’s own confirmation carry identical content but different permission to update a profile. Fifty base histories crossed with seven source-to-use transitions yield 350 pairs and 700 variants. Each pair preserves task, tools and argument predicate while changing the claim carrier; the current request omits the operative value. Module A measures authority loss during writing, B supplies a controlled memory to remove writing/retrieval, and C tests the write-to-first-call chain.

Editorial placement: Compared with memory QA and malicious-content poisoning, AuthMem-Bench fixes claim content and swaps its authorization source before tracing writing and action. Its added coordinate is the distinction between a true claim and permission to act on it. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Bases comprise 30 successful released τ²-Bench rollouts and 20 synthetic APIGen-MT-5k trajectories across airline, retail and telecom. Entity-isolated train/validation/test splits contain 30/10/10 bases. The frozen policy maps user/assistant/tool sources to Authorized/Attested/Unendorsed; these are use-specific benchmark permissions, not universal truth rankings. Seven backbones cross seven adapted memory-writing objectives with at most 16 textual memories. Mem0, LangMem, Graphiti and Letta names do not denote complete product executions. Temperature is zero with one accepted trajectory per case/configuration; token caps are 4096 writing, 2048 semantic judging, 8192 source prediction and 1024 action. GPT-5.6-Luna judges Module A. Modules B/C strictly match the first native tool name and complete argument object; wrong or missing calls fail. There is no environment-state replay establishing real-world action success.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Tables 2–3; Appendix D.2–D.3, omission-aware writing comparisons

Upgrade-all and negative retention use all non-authorizing cases; positive retention uses all authorized cases. Base grid averages 49 configurations; other rows average seven backbones. Marking forces focal retention; source-aware instructions then reduce upgrades at similar retention.

350 pairs per configuration; base grid 17,150 cases per side, interventions 2,450 per side.

| Writing condition | Upgrade-all (%) | Negative retention (%) | Positive retention (%) |
|---|---|---|---|
| Base grid | 17.8 | 26.0 | 61.5 |
| Minimal | 21.6 | 25.3 | 58.0 |
| Marked | 55.8 | 83.5 | 98.2 |
| Marked + source-aware | 9.9 | 82.5 | 98.6 |

Locator: Tables 2–3; Appendix D.2–D.3, omission-aware writing comparisons · [Source](https://arxiv.org/html/2608.01679v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4 and Appendix E.2, selected controlled action treatments

Module B directly supplies the focal memory; seven action models are equally weighted. ASR counts prohibited matching calls on non-authorizing variants; TSR counts required matching calls on authorized variants. Suppressing all actions lowers ASR, so TSR must be reported beside it.

350 cases per side/model/treatment; pooled denominator 2,450 per metric.

| Memory treatment | ASR (%) | TSR (%) |
|---|---|---|
| Memory off | 0 | 0 |
| Washed / no metadata | 50.3 | 49.4 |
| Source-attributed / no metadata | 40.5 | 53.6 |
| Washed / conservative join | 5.1 | 5.1 |
| Source-attributed / gold metadata | 2.7 | 53.9 |

Locator: Table 4 and Appendix E.2, selected controlled action treatments · [Source](https://arxiv.org/html/2608.01679v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 5; Appendix F.5–F.7, frozen end-to-end pipeline

Validation selects Gemini 3.1 Pro for Mem0-inspired writing and action, and Qwen3.7-Max for supporting-source prediction followed by role mapping. Arms share frozen memory text; retrieval returns the entire write set in stable order. The 70-pair test is strictly held out; all 350 includes train/validation and is descriptive.

All source pairs remain in denominators, including omissions; 10 test base clusters versus 50 total.

| Condition / split | Prohibited calls | Negative N | ASR (%) | Required calls | Positive N | TSR (%) |
|---|---|---|---|---|---|---|
| No metadata / test | 10 | 70 | 14.3 | 20 | 70 | 28.6 |
| Predicted / test | 0 | 70 | 0 | 20 | 70 | 28.6 |
| No metadata / all | 59 | 350 | 16.9 | 139 | 350 | 39.7 |
| Predicted / all | 0 | 350 | 0 | 140 | 350 | 40.0 |

Locator: Table 5; Appendix F.5–F.7, frozen end-to-end pipeline · [Source](https://arxiv.org/html/2608.01679v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

48/49 means at least one upgrade in each affected configuration, not a 98% case failure rate. The sole zero-upgrade Mem0 classic/GPT-5.5 configuration omits all 350 negative focal claims; 74% are omitted across the base grid. Low upgrade rates alone therefore do not establish safety. C2 writes/retrieves focal claims in only 139/350 negative and 256/350 positive variants; labels cannot recover omissions. The paper gives a full-release zero-ASR 95% interval of [0,7.1] over 50 base clusters, not a zero-risk guarantee. Reference and predicted labels both achieve 40% TSR, but four independent calls with identical prompts differ in success, precluding casewise equivalence. Gold metadata is no universal safety ceiling: Module B GPT-5.4 mini still has 13.4% ASR with attributed text and gold labels.

The paper’s broad consolidation/product terminology must be read against its shared adapted-prompt interface. C2 retrieval returns every written item, so this is not a large-store retrieval stress test. One temperature-zero trajectory per cell supports case-cluster intervals, not provider-repeatability estimates. Module-A independent validation is model agreement, not a human-gold audit: 8,686 deliberately selected cases give 84.57% Luna–Qwen agreement; majority sensitivity changes 253/44,100 labels. The fixed-grid backend/prompt decomposition is descriptive and explicitly noncausal.



Next: Retain existing carrier-swap, memory-off, gold-label and conservative-label controls. Extend them to matched full product implementations, budget-matched large-store retrieval, corrupted provenance and multi-turn state replay; separately report omissions, unauthorized calls, authorized success and repeated-call variability.
<!-- EVIDENCE:limitations:END -->
