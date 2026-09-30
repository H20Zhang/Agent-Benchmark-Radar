# LiveBrowseComp: recent long-tail facts and search-dependence diagnostics

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-05 · paper v1<br>
> **GPT-5.4 / search-augmented agent — LiveBrowseComp avg@4: 43.2%**<br>
> Best LiveBrowseComp average accuracy in Tables 3 and 5; avg@4 is not success on any of four attempts (pass@4). [Original source](https://arxiv.org/html/2605.28721v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](livebrowsecomp.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read Sections 1–6 and Appendices A–G, including all three diagnostics, filtering thresholds, judging prompt, search/closed-book settings, human review and domain results; visually checked Table 3 and Figure 7.

[arXiv 2605.28721v1 · 2026-05-27](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

LiveBrowseComp contains 335 human-authored short-answer questions seeded from six updating news, film, game, vulnerability, sports and earthquake sources. At least one indispensable clue must originate within ninety days of construction; easy direct-search and unstable-answer cases are filtered. Authors record evidence chains, while independent reviewers check correctness, uniqueness, difficulty and temporal dependence; a question is excluded if any of three solvers finishes within thirty minutes. Separate diagnostics on older benchmarks remove tools, block answer evidence and trace query provenance to study the mixture of prior knowledge and evidence discovery. Closed-book success establishes that retrieval was unnecessary for that attempt, not training-data leakage.

Editorial placement: BrowseComp is the direct reference; LiveBrowseComp adds recent long-tail facts and closed-book/evidence-blocking diagnostics to separate prior knowledge from discovery. One example combines a recent short film’s production-company clues and creator roles to identify its title. This differs from LoHoSearch’s candidate-space difficulty: recency is neither automatic difficulty nor permanent decontamination.

[Source](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Search experiments use a RedSearcher-style scaffold, Serper with up to ten results, Jina goal-conditioned page retrieval and the stated auxiliary tools. Temperature is 0.7, top-p 0.9, with 256K context and a 250-step cap, no historical-summary compression, and forced final answers at the limit. Four independent attempts per question yield avg@4 mean accuracy and pass@4 at-least-once success. A GPT-OSS judge compares final short answers with references, allowing aliases and surface variation; it does not grade full reasoning or citation quality, and its exact model size is unspecified. The evidence-blocking pilot instead uses Qwen3-8B-Embedding retrieval over a corpus stripped of evidence/gold documents, retaining irrelevant/hard negatives and disabling additional internet access.

[Source](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Search-augmented mean accuracy in the reported study

Four attempts per question; all 335 LiveBrowseComp questions, with BrowseComp a different question set rather than a same-item intervention. Both columns retain Table 3’s avg@4 label. Up to 250 steps/256K context, GPT-OSS grading, with the auxiliary-tool mismatch described above.

| Model | BrowseComp avg@4 (%) | LiveBrowseComp avg@4 (%) |
| --- | --- | --- |
| GPT 5.4 | 72.1 | 43.2 |
| GLM 5.1 | 68.0 | 33.9 |
| DeepSeek v3.2 | 51.4 | 37.6 |

Source location: Table 3, p. 9; Appendices B–C, pp. 17–18 · [Source](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Pilot evidence blocking on an older question corpus

Intervention on the BrowseComp-Plus document index, measuring success at least once in four attempts. The exact question count is not stated and must not be replaced with 335. Only irrelevant/hard negatives remain, not a generic search-failure setting; these pass@4 scores are not interchangeable with avg@4 above.

| Model | Closed-book pass@4 (%) | Evidence-blocked pass@4 (%) |
| --- | --- | --- |
| MiniMax M2.5 | 44.5 | 8.0 |
| Kimi-K2.6 | 25.5 | 2.3 |

Source location: Table 1, p. 4; Appendix C.2, pp. 18–19 · [Source](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

The recent set reduces closed-book performance for tested models without guaranteeing novelty for future models. Cross-benchmark score changes also involve domain, question and tool differences. Similar human solve rates—60/200 and 62/200 observations in Figure 6—are a reference, not randomization proving that all model loss comes from prior knowledge. Worse performance after evidence removal may reflect negative-document distraction or poor abstention; it does not establish that retrieval is valueless. Roughly half the questions concern films/entertainment, only one search backend is used, and ninety days is a heuristic rather than a known training cutoff.

The main text describes shared tools, but Appendix C makes Python, Google Scholar and Maps model-dependent; closed-book reasoning modes and output budgets also differ. Figure 7 is labeled avg@4 while several static scores repeat earlier pass@4 values, and two bars are 2.0%, contradicting “all below 2%”; no gain is calculated from those mixed labels here. Appendix B requests structured yes/no output but describes an A/B first-character parser, requiring the actual scorer to be pinned. The evidence-blocking sample count is not explicit; that study uses the BrowseComp-Plus document index, not LiveBrowseComp’s live web.

Retain fact dates, sources and web snapshots, repeat closed-book diagnostics, align actual tools/reasoning budgets and pin the scorer. Compare supporting, absent, irrelevant and adversarial-negative evidence on identical questions to separate discovery, evidence use and abstention. Calibrate refreshes with anchor questions and shared models.

[Source](https://arxiv.org/pdf/2605.28721v1)
<!-- EVIDENCE:limitations:END -->
