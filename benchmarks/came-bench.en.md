# CAME-Bench: retrieval under repeated entities and changing goals

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-01-15<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.584/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](came-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 35 proceedings pages, pp.12008–12042: §§1–7, limitations and Appendices A–K, including construction, ground-truth audits, retrieval diagnostics, cost, robustness, all twelve prompt listings and both trajectory showcases. Visually checked main results/ablations and retrieval prompts.

[ACL 2026 / 2026-07 / 2026.findings-acl.584](https://aclanthology.org/2026.findings-acl.584.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Closed-world entities feed symbolic action plans, which are realized as dialogue and rewritten to add indirect references and split turns. Questions test state revision, context-specific facts, multi-hop references and synthesis (§3; Appendix A). In the travel showcase, two breakfast candidates precede intervening lunch/dinner discussion; a later ordinal reference asks about the second breakfast venue, not whichever restaurant was mentioned most recently (Appendix J).

STITCH learns scope, event and entity-type labels online, resolves references, writes compact notes, and ranks retrieval by label overlap before semantic similarity. Its labels are inferred, not benchmark-provided gold intent.

### Measurement genealogy

LongMemEval supplies a close reference for updates and long histories, while LoCoMo supplies social-dialogue transfer. CAME-Bench increases repeated-entity and interleaved-goal interference. The coordinate is context-valid evidence use; it does not execute bookings or directly evaluate deletion/repair policies.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Fourteen synthetic trajectories contain 373 questions: Small/Medium/Large have 6/6/2 trajectories averaging 23K/137K/408K tokens. Retrieval systems share GPT-5-mini with medium reasoning and a 4,096-token evidence cap. STITCH initializes/updates labels in 50-step batches, considers five event labels and retrieves forty snippets before truncation. GPT-4.1-mini judges at T=0, top_p=0.9. Single answers use a permissive containment judgment; sets use candidate matching and question-macro F1. Human validation covers four Small trajectories, not every partition.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected end-task F1 comparisons, not retrieval recall or full leaderboard. The full-context row has a different input budget; the ablations retain the STITCH harness. Scores are question-macro averages, not percentages of fully correct trajectories.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| STITCH / GPT-5-mini | CAME-Bench S / M / L; 144 / 168 / 61 questions | Answer-set macro-F1 (0–1), S / M / L | 0.844 / 0.682 / 0.592 | GPT-5-mini medium reasoning; 4,096 retrieved tokens; GPT-4.1-mini judge | Table 1, p.12014 (PDF p.7) |
| Secom / GPT-5-mini | CAME-Bench S / M / L; 144 / 168 / 61 questions | Answer-set macro-F1 (0–1), S / M / L | 0.501 / 0.114 / 0.236 | GPT-5-mini medium reasoning; 4,096 retrieved tokens; GPT-4.1-mini judge | Table 1, p.12014 (PDF p.7) |
| STITCH without thematic scope | CAME-Bench S / M / L; 144 / 168 / 61 questions | Answer-set macro-F1 (0–1), S / M / L | 0.463 / 0.257 / 0.213 | GPT-5-mini medium reasoning; 4,096 retrieved tokens; GPT-4.1-mini judge | Table 2, p.12014 (PDF p.7) |
| STITCH without coreference rewriting | CAME-Bench S / M / L; 144 / 168 / 61 questions | Answer-set macro-F1 (0–1), S / M / L | 0.578 / 0.489 / 0.404 | GPT-5-mini medium reasoning; 4,096 retrieved tokens; GPT-4.1-mini judge | Table 2, p.12014 (PDF p.7) |
| GPT-5-mini / full context | CAME-Bench S / M / L; 144 / 168 / 61 questions | Answer-set macro-F1 (0–1), S / M / L | 0.804 / 0.566 / 0.212 | 400K window; oldest content truncated if exceeded; same judge | Table 1, p.12014 (PDF p.7) |

Source: [Table 1, p.12014 (PDF p.7); Table 2, p.12014 (PDF p.7)](https://aclanthology.org/2026.findings-acl.584.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The Large gap is 0.592−0.236=0.356 F1, or 35.6 percentage points on a percent scale; the prose’s “100% relative” is not reproduced by those cells. Table 9 also reports different GPT-5-mini STITCH Medium/Large values from Tables 1–2 without explaining the run distinction. Large has only two trajectory clusters, and length groups are not the same questions padded to different lengths. Ablations support contributions within this co-designed synthetic setting, not a universal causal account of retrieval error. The ingestion-token table lacks a clear per-step/trajectory denominator, so it cannot establish total deployment cost.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Hold entities and answer evidence fixed while swapping only the active goal and interference distance. Compare inferred labels, gold labels and embedding retrieval at matched ingestion/query budgets; audit online access within each 50-step buffer. Add independent trajectories and cluster confidence intervals by trajectory, then test whether retrieval supports an executable plan revision.
<!-- EVIDENCE:next:END -->
