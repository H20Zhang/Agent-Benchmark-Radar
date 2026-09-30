# LoHoSearch: long-horizon search with large candidate sets and complex constraints

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-11<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.12837)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](lohosearch.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read the complete substantive v2 text, limitations and Appendices A–D, including graph construction, filtering, calibration formula, full prompt/tool definitions and both cases; visually checked Tables 2–3.

[arXiv 2606.12837v2 · 2026-06-17](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

A graph of approximately 7.62 million English Wikipedia entities and 265 million directed hyperlink edges supports sampling low-popularity entities with large relation-specific candidate sets. Tree questions require intersecting constraints to identify an answer; graph questions add cycles/cross-constraints with up to ten entities. DeepSeek-V3.2 verbalizes obfuscated structures and assists validation/difficulty filtering. The 544 questions comprise 282 tree and 262 graph cases across eleven categories. An illustrative workflow eliminates candidates through relationships among an album, singers and producers, then returns one entity and confidence rather than a locally matching candidate.

Editorial placement: the paper directly compares BrowseComp. LoHoSearch replaces manually constructed hard searches with graph-controlled candidate spaces and constraint structure, adding structural difficulty and context-management stress. It is not a recent-fact benchmark; LiveBrowseComp’s freshness diagnosis is complementary rather than interchangeable.

[Source](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Models receive shared search/browse definitions supporting up to five queries and three pages per call, temperature 1.0 and 200K context split into 184K input/16K output; reasoning follows official defaults. Total calls, wall-clock caps and main-table repeat counts are unspecified. Scores average accuracy from GPT-4.1 with the BrowseComp judge prompt and Qwen2.5-32B with the SimpleQA prompt, not their consensus. ECE uses five equal-width confidence bins, with missing confidence fields adding noise. Summary/discard interventions trigger above 80% context usage; Verify checks constraints before submission, without matched additional cost.

[Source](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected model scores and calibration error

All 544 v2 questions; each judge uses question-level accuracy and the two values are averaged. Lower ECE is better, with missing-confidence handling incompletely specified. Reasoning modes differ rather than matching inference compute.

| Model | Mean two-judge accuracy (%) | ECE (%) |
| --- | --- | --- |
| GPT-5.5 | 34.74 | 48 |
| Claude-Opus-4.6 | 15.62 | 31 |
| DeepSeek-V4-Flash | 10.02 | 48 |

Source location: Table 2, p. 5; Appendix A, pp. 10–11 · [Source](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Context interventions with DeepSeek-V4-Flash fixed

544 questions with the same backbone/tools; history is managed above 80% context use. Verify additionally checks conditions before submission, without equalized realized compute. Three selected strategies; the gain is 6.80 percentage points, not a 6.8% relative increase.

| Strategy | LoHoSearch accuracy (%) |
| --- | --- |
| Baseline | 10.02 |
| Summary | 11.31 |
| Discard-all + Verify | 16.82 |

Source location: Table 3, p. 5; Section 3.3, p. 6 · [Source](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

The matched-backbone context experiment supports particular intervention bundles, not a pure window-size effect. Graph/tree differences also vary entity and edge structure. The rise from 35 to 61 mean tool calls concerns correct trajectories only, not all-task cost. Sixteen samples yield 38.3% pass@16 versus 24.6% confidence-based selection: at-least-once coverage and actual selection are distinct. Difficulty filtering by one DeepSeek-family model, English Wikipedia grounding and incomplete uniqueness verification limit generalization.

This note uses v2 dated June 17, not the unverified June 11 initial-release reference. The reported “6.8% gain” is 16.82−10.02=6.80 percentage points. Human reviewers could not conclusively exclude alternatives for 29.2% of questions, so within-graph uniqueness is not open-world uniqueness. Table 2 marks GPT-5.5 and Claude rows as non-reasoning while most others use reasoning; service instability and safety refusals also affect some rows.

Freeze tasks, independently vary candidate counts and constraint density, and match total tokens/calls when comparing summaries, explicit candidate state and final verification. Add human-confirmed alternative answers and independent judges, reporting costs and failures for all runs, selection policy and calibration.

[Source](https://arxiv.org/pdf/2606.12837v2)
<!-- EVIDENCE:limitations:END -->
