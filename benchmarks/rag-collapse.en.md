# RAG Collapse

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.22118)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](rag-collapse.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–17, all simulation definitions, metrics, results, mechanism analyses and limitations; appendices inspected: A.1–A.3 complete Replace One results; visual checks: Appendix Figures 29–31 inspected in rendered pages 34–36; other figures read with their detailed accompanying text/captions. Not performed: No raw-data rerun, human judge validation or real-web deployment measurement

[arXiv 2608.22118v1 — arXiv v1, margin 2026-08-22; title page 2026-08-25](https://arxiv.org/pdf/2608.22118v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike recursive-training collapse, this fixes weights and repeatedly feeds answer-derived articles into retrieved context. It adds longitudinal diversity feedback to single-answer evaluation, without equating simulated collapse with real-web or factual-quality degradation.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The study tests whether repeated retrieval of self-authored articles reduces a fixed model’s answer diversity, without weight training. Each round generates ten answers, removes citations and expands selected answers into articles using the same model while preserving their substance. Replace All replaces every reference; Replace One replaces one original reference per round; Search adds one self-authored article to a pool retaining originals and retrieves ten chunks. Seed references are January 2026 ChatGPT or Google AI Overview citations, scraped to main text, URL-hidden and shuffled. There are 1,019 unique questions and 1,528 simulations, mainly entity comparisons and open-ended advice.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Caps are ten Replace All rounds, twenty Replace One and thirty Search rounds. The latter two author one article from one answer; Replace All uses ten. At least five references are required; replacement experiments retain at most ten longest sources and use model-selected relevant excerpts, while Search indexes full text with OpenAI vector stores’ default chunking, without exact chunker/embedding version specifications. Temperature remains default 1.0. Main comparisons use GPT-5.2 Chat, larger experiments GPT-5.2, and Gemini 3 Pro/Claude Sonnet 4.5 only Replace One. Most questions have one simulation. GPT-5.2 judges paraphrases, extracts entities and rates source quality; only ten of forty-five answer pairs are sampled each round. Entity collapse means identical entity sets across ten answers; editorial collapse means all ten sampled pairs are paraphrases. Large runs stop early after four consecutive rounds of one-hundred-percent same-answer rate.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Three feedback mechanisms within one model

GPT-5.2 Chat, ten answers per round. Entity collapse requires identical sets; editorial collapse requires all ten sampled pairs to be equivalent. Round caps and context units differ, preventing a single matched-budget treatment interpretation. Start precedes added self-authored articles.

| Simulation / question type | Questions | Collapsed at start percent | Collapsed at end percent |
|---|---|---|---|
| Replace All / entity | 101 | 2.97 | 88.12 |
| Replace One / entity | 101 | 2.97 | 88.12 |
| Search / entity | 101 | 1.98 | 77.23 |
| Search / editorial | 57 | 31.58 | 75.44 |

Source: Table 3; Sections 8–9.2 · [Paper](https://arxiv.org/pdf/2608.22118v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Larger Search simulations on additional questions

GPT-5.2 rather than the Chat variant; at most thirty rounds with early stopping after four fully same-answer rounds. One simulation per question, definitions as above; this is not a paired model-version comparison.

| Question type | Questions | Collapsed at start percent | Collapsed at end percent |
|---|---|---|---|
| Entity | 742 | 7.01 | 73.85 |
| Editorial | 102 | 7.84 | 83.33 |

Source: Table 3; Section 9.4 · [Paper](https://arxiv.org/pdf/2608.22118v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

The 79.6 percent, 1,216/1,528, is terminal collapse across heterogeneous simulations, not a unique-question rate, new-collapse rate above baseline or real-internet probability. Replace One reaches 22.8 percent entity collapse in round two after one self-authored article, showing risk under this intervention rather than inevitability from any single article. In 193 quality-matched references, self-authored citation rate is 38.2 versus 13.3 percent. The eight-quality-variable regression’s +0.26 self-authorship coefficient remains a conditional association, not exclusion of direct-answer, style or unmeasured-quality confounding.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

The simulation continually adds derivatives of the same question without new human or independent information. Replacement forces self-authored content into context; Search competes within a finite pool. Marketing-related keywords and search/reference filters limit representativeness, and factual consensus can appropriately have low diversity. Real multi-turn agentic search, cross-model recursion and deduplication/diversity mitigations are untested, usually without repeated seeds. Next retain external information inflow, separately control style and answer content, blind humans to judge equivalence/factual quality, and repeat retrievers/seeds while reporting diversity and correctness together.

The PDF margin date is August 22 while the title page says August 25; both belong to the reviewed v1. The phrase same-answer percentage 100% concerns ten sampled pairs out of forty-five, not proof that all ten answers are mutually equivalent or that the full output distribution is degenerate. Model comparison in Section 9.3 uses the 41 entity/45 editorial intersection, unlike full Table 3 group counts; initial references also differ across families. The claim seed contamination can only make effects conservative is an untested directional assumption, not demonstrated by a control varying seed self-authorship. AI-written source rates are GPTZero predictions with unknown error in this sample, not verified author provenance.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [snapshot-compatibility-audit](snapshot-compatibility-audit.en.md) · [kbgym](kbgym.en.md)
