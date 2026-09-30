# RealMem: response consistency in evolving project dialogues

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-01<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.703/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](realmem.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 17 proceedings pages, pp.14349–14365: §§1–6, limitations and Appendix A.1–A.6, including scenario definitions, supplementary baselines/judges, human protocol, complete provided cases and scoring prompts. Visually checked Table 2 and inspected the scoring rubric.

[ACL 2026 / 2026-07 / 2026.findings-acl.703](https://aclanthology.org/2026.findings-acl.703.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Project blueprints produce events and interleaved session plans. Simulated users see current/prior events, while an assistant uses extracted memories and a global schedule; extraction, deduplication and schedule updates feed later dialogue generation. Evaluation queries arise within the dialogue rather than only afterward (§3).

A travel-planning example keeps a twelve-day limit while adding two West Coast days. A suitable answer must identify existing commitments that must change, rather than simply append destinations (Appendix A.5). QA judging checks consistency with the latest relevant memory, not completion of the trip.

### Measurement genealogy

Relative to LoCoMo’s conversational history and LongMemEval’s updating questions, RealMem makes interleaved project states and naturally occurring continuation requests the evaluation object. HaluMem is a further reference for memory consistency. The next coordinate is executing a plan revision or artifact change while respecting current commitments.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The synthetic corpus covers eleven scenarios, over 2,000 sessions and 1,415 queries; only 24 are temporal-reasoning items. GPT-4o-mini extracts memory; answerers are GPT-4o-mini or GPT-4o, with GPT-4o judging. Memory-only uses top-20 entries; session context uses top-5 associated original sessions. MemoryOS lacks the session track. Embedders/hyperparameters follow each implementation; exact decoding, context budgets and repetitions are not pinned (§5; Appendix A.1).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected Table 2 facts. Every row uses GPT-4o as answerer and judge, but memory and session tracks expose different evidence. Values are retained on the paper’s reported scale because its mapping from the 0–3 response-consistency rubric is not stated. Oracle is a gold-evidence control.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| LightMem / GPT-4o / session | RealMem; benchmark contains 1,415 evaluated query items | Reported QA Score; rubric 0–3, table scaling unspecified | 0.623 | Top-5 source sessions; GPT-4o judge | Table 2, p.14355 (PDF p.7) |
| Mem0 / GPT-4o / session | RealMem; benchmark contains 1,415 evaluated query items | Reported QA Score; rubric 0–3, table scaling unspecified | 0.609 | Top-5 source sessions; GPT-4o judge | Table 2, p.14355 (PDF p.7) |
| Graph Mem / GPT-4o / session | RealMem; benchmark contains 1,415 evaluated query items | Reported QA Score; rubric 0–3, table scaling unspecified | 0.567 | Top-5 source sessions; GPT-4o judge | Table 2, p.14355 (PDF p.7) |
| MemoryOS / GPT-4o / memory | RealMem; benchmark contains 1,415 evaluated query items | Reported QA Score; rubric 0–3, table scaling unspecified | 0.567 | Top-20 memory entries; GPT-4o judge | Table 2, p.14355 (PDF p.7) |
| Oracle / GPT-4o / memory | RealMem; benchmark contains 1,415 evaluated query items | Reported QA Score; rubric 0–3, table scaling unspecified | 0.804 | Gold relevant memory; not deployable retrieval; GPT-4o judge | Table 2, p.14355 (PDF p.7) |

Source: [Table 2, p.14355 (PDF p.7)](https://aclanthology.org/2026.findings-acl.703.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Table 2’s session winner depends on answerer; with GPT-4o it is LightMem, not Graph Mem as the prose broadly claims. The judge rubric spans 0–3, but main-table fractional scaling is unexplained, so these are not verified accuracy percentages. Human validation uses 30 four-way comparisons, with unclear overlap between two annotators each assigned 15. Synthetic frequency does not establish the real-world prevalence of temporal tasks. No tool execution is evaluated.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Publish item-level rubric scores and normalization, then fix answerer, embedder and context tokens across tracks. Replay the same project revisions in different orders and score an executable plan update, including whether cancelled requirements reappear. Cluster uncertainty by user/project rather than treating queries as independent.
<!-- EVIDENCE:next:END -->
