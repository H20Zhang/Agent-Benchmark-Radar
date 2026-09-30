# LoCoMo-Plus: applying conversational cues without direct reminders

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-11<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.acl-long.1150/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](locomo-plus.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 16 proceedings pages, pp.25085–25100: §§1–7, limitations, Appendices A–C and all generation/judge prompts. Visually checked the main result and judge-reliability tables. This is the final ACL paper, not a verified initial preprint snapshot.

[ACL 2026 / 2026-07 / 2026.acl-long.1150](https://aclanthology.org/2026.acl-long.1150.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

The pipeline generates short cue dialogues, manually screens their memory relevance, generates semantically distant triggers, filters overlap with BM25/MPNet, and inserts validated pairs into LoCoMo histories after a gap. Questions do not announce a memory-test category (§4).

A user who earlier wanted fewer distractions while preparing for an exam later asks about starting a television series. The response should use the earlier goal without a direct reminder (§1). The cognitive judge labels explicit cue acknowledgment or adaptation as correct, and generic cue-ignoring responses as wrong (Table 7).

### Measurement genealogy

This is a direct extension of LoCoMo: the new coordinate is a weak semantic link between historical cue and present trigger, rather than an additional factual question type. Its next boundary is distinguishing appropriate application from merely mentioning a memory, including cases where a former goal has changed or no longer applies.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Context-only models receive full conversations. RAG retrieves top-5 segments; RAG and memory-system responses use GPT-4o. Gemini-2.5-Flash is the main judge; GPT-4o provides a judge check. Cognitive/temporal/adversarial labels are binary, while factual/commonsense labels allow partial credit. The final cognitive denominator, partial-credit weights, inference temperature, token caps and repeat counts are not specified. Generation uses temperature 0.7, 256 output tokens and 50 samples per relation type; these are not evaluation budgets (§6; Appendices A–B).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected reported percentages. Cognitive scores use binary memory-awareness judgments over the final cognitive set, whose size is not numerically specified in the paper. The factual average is the paper’s reported aggregate across differently graded task types, not assumed to be a five-category macro-average.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| gemini-2.5-pro / factual | LoCoMo; aggregate denominator/weights not specified | Reported factual average (%) | 71.78 | Full context; Gemini-2.5-Flash judge; task-specific labels | Table 1, p.25090 (PDF p.6) |
| gemini-2.5-pro / cognitive | LoCoMo-Plus; final item count unspecified | Binary memory-awareness success (%) | 26.06 | Full context; main judge; no task-type disclosure | Table 1, p.25090 (PDF p.6) |
| gpt-4o / cognitive | LoCoMo-Plus; final item count unspecified | Binary memory-awareness success (%) | 21.05 | Full context; same main judge | Table 1, p.25090 (PDF p.6) |
| A-Mem / GPT-4o / cognitive | LoCoMo-Plus; final item count unspecified | Binary memory-awareness success (%) | 17.20 | Structured memory; exact retrieval/token budget unstated | Table 1, p.25090 (PDF p.6) |

Source: [Table 1, p.25090 (PDF p.6)](https://aclanthology.org/2026.acl-long.1150.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The factual-to-cognitive gap changes tasks and grading criteria; it is not an isolated storage or retrieval effect. Cross-judge stability in Table 3 concerns factual aggregates. Human-agreement sample size and the normalized agreement formula are absent. Appendix B reports camera-ready judge discrepancies under investigation. Cognitive awareness does not establish optimal advice, calibrated uncertainty, or protection from stale-constraint overuse.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Create direct-cue, distant-cue and explicitly obsolete-cue variants for the same histories. Hold answerer and evidence budget fixed; score retrieval, acknowledgment, appropriate adaptation and over-application separately. Use blinded human judgments and a frozen evaluator on the cognitive subset.
<!-- EVIDENCE:next:END -->
