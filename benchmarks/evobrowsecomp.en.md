# EvoBrowseComp: regenerable bilingual web-search questions and version boundaries

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-06 · paper v1<br>
> **Claude-Opus-4.6 + tools — English accuracy: 44.8%**; **Claude-Opus-4.6 + tools — Chinese accuracy: 36.8%**<br>
> Best tool-enabled entries in Table 2, compared separately by language under the original search budget. [Original source](https://arxiv.org/html/2606.13120v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](evobrowsecomp.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read the complete v2 main text, limitations and Appendices A–F, including all generation/filter/judging prompts, human validation, annual-refresh plan and reasoning-effort intervention; visually checked Tables 3 and 5–7.

[arXiv 2606.13120v2 · 2026-08-30](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

Approximately fifty thousand web seed entities cover nine domains and fifty subdomains. Three DeepSeek-V3.2 agents collect/synthesize QA, check credibility and old-fact popularity, and parse questions into projection/intersection/complement graphs for refinement. Generation requires at least five iterations and five edges, with the answer depending on fresh evidence. An illustrative question links software vendors, partner organizations and cloud platforms with exclusion constraints to identify a new release. Six models answering three times help filter questions, but convergence on one wrong answer is only a heuristic, not exhaustive uniqueness proof. The release retains four hundred questions per language.

Editorial placement: compared with BrowseComp/BrowseComp-ZH’s fixed human-written sets, EvoBrowseComp makes generation a three-agent process in English and Chinese. Relative to LiveBrowseComp’s human recent-fact validation, it adds automated regeneration without demonstrating cross-year difficulty stability or permanent decontamination.

[Source](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Main runs use Search/Visit tools, 128K context, at most forty tool calls, temperature 0.6 and top-p 0.95, normally with maximum reasoning; accuracy averages three independent evaluations per model. Temperature-zero GLM-5-Chat judges final-answer agreement rather than entire trajectories. Two author experts review eight hundred model predictions; the judge’s Spearman correlation is 0.864, not perfect agreement. A four-hundred-question quality audit finds 87.8% passing evidence correctness, question consistency/unambiguity and answer derivability jointly, distinct from the independent human-solving baseline.

[Source](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected v2 results by language and tool access

Four hundred questions per language, averaged over three independent evaluations; 128K context, forty-call cap, maximum reasoning and GLM-5-Chat final-answer grading. This is not at-least-once success over three attempts, nor a matched bilingual same-item comparison.

| Model | English tools (%) | English no tools (%) | Chinese tools (%) | Chinese no tools (%) |
| --- | --- | --- | --- | --- |
| Claude-Opus-4.8 | 46.2 | 9.0 | 38.3 | 14.0 |
| Claude-Opus-4.6 | 44.8 | 6.0 | 36.8 | 8.8 |
| DeepSeek-V3.2 | 23.0 | 6.3 | 30.5 | 10.3 |

Source location: Table 3, p. 8; Section 3.1, p. 7 · [Source](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Reasoning-effort comparison within DeepSeek-V4-Flash

Four hundred questions per language with a forty-call cap. ER is the reported proportion exceeding allowed calls, not error rate or wall-clock timeout. The full termination/final-answer extraction behavior at the cap is not specified.

| Configuration | English accuracy (%) | English exceed ratio (%) | Chinese accuracy (%) | Chinese exceed ratio (%) |
| --- | --- | --- | --- | --- |
| DS-V4-High | 34.5 | 38.8 | 24.8 | 54.5 |
| DS-V4-Max | 16.5 | 75.5 | 10.8 | 82.5 |

Source location: Table 5 and reasoning-effort discussion, p. 8 · [Source](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Tool gains establish a retrieval contribution on this snapshot, not absence of prior knowledge or generation bias. English and Chinese sets are not guaranteed matched question pairs, preventing a direct transfer interpretation. DeepSeek-V4-Flash high reasoning outperforms max alongside fewer call-limit exceedances, showing how strategy changes effective exploration under one cap rather than that less reasoning is always better. Earlier BrowseComp scores are borrowed from technical reports, not rerun under this protocol. Construction still admits incorrect evidence; derivability from the evidence list does not establish real-world truth.

The body uses August 30 v2 while preserving the v1 historical header. V2 prose still claims tool-free scores below 11%, but Table 3 gives Claude-Opus-4.8 14.0% in Chinese. Introductory claims of continuous low-cost refresh contrast with Section 2.4’s annual plan due to scarce fresh knowledge and cost; construction reports approximately 40,000 GPU hours, not an established frequently running service. January 1, 2026 is not every model’s actual training cutoff.

Independently audit source evidence and alternative answers, retaining timestamps and accessible snapshots. Keep anchor questions/shared models across regenerations. Evaluate a reasoning-effort × tool-budget grid on identical tasks, reporting accuracy, forced termination, cost and intervals so task refresh and budget changes are not mistaken for model progress.

[Source](https://arxiv.org/pdf/2606.13120v2)
<!-- EVIDENCE:limitations:END -->
