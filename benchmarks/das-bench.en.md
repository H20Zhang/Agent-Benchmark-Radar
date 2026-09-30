# DAS-Bench / DAS-Eval: evidence, organization and artifact quality in surveys

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.18034)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](das-bench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all thirty-five pages and Appendices A–H, including metadata extraction/audits, role states and repairs, all sixteen rubric definitions, topics/timeouts, ablations, blinded experts and cross-judge results; visually checked Tables 2–4. Also checked the official repository’s release status on 2026-09-30; no generation-system execution.

[arXiv 2608.18034v1 · 2026-08-18](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DAS-Bench fixes thirty survey topics, twenty-one CS and nine interdisciplinary, requiring complete English survey PDFs. DAS extracts eight groups/twenty-five fields, retrieves candidates, and grounds taxonomy planning in those candidates rather than topic alone. Each paper is routed to at most three sections. Paragraph planning precedes explicit claim/citation groups and drafting. For example, a retrieval-method section first organizes sparse/dense/hybrid families; papers support both methods and limitations. A missing comparison condition can trigger replanning of one paragraph’s claims and draft rather than whole-corpus retrieval. Review selects acceptance, direct paragraph edits, paragraph replanning or section replanning; finalization builds figures, BibTeX and LaTeX and compiles the manuscript.

Editorial placement: AutoSurvey/SurveyForge connect retrieval, outlines and survey writing, while DeepSurvey already includes full-paper analysis and section evidence. DAS adds reusable paper representations, explicit writing states and scoped state reactivation. Evaluation extends beyond answer/citation quality to taxonomy, hierarchical discourse and rendered manuscripts. This motivates a measurable design, not proof of a generally superior shared data layer or of every component’s necessity.

[Source](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Reproducible systems share Qwen3.5-397B-A17B-FP8 but retain native workflows and available literature resources. Systems lacking reproducible retrieval receive the same three hundred candidates as DAS; closed systems retain native search/configuration, so the full comparison is not uniformly controlled. DAS retrieves up to one thousand papers and uses three hundred for taxonomy/routing. Parsed-source access is capped at one request per paragraph/two per section; review permits three rounds and drafting/checking six attempts per paragraph. DAS-Eval equally averages sixteen 1–5 criteria: four each for Balanced Scholarly Citation Quality (BSC), Taxonomic Synthesis Quality (TSQ), Hierarchical Discourse Quality (HDQ), and Manuscript Assembly Reliability (MAR). These are rubric scores, not accuracy. The main judge shares the generation backbone at temperature 0.2; Kimi K2.6 rejudges at 0.6. Citation judgments trust evidence cards only, missing evidence is unassessable rather than an error, and long-document MAR uses sampled pages. A twelve-hour failure to produce a PDF receives no quality score, not zero.

[Source](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Results on the same twenty-one CS topics

Main Qwen3.5 judge, per-criterion means over twenty-one topics and equal aggregation of sixteen criteria. DAS/Naive RAG share three hundred candidate representations; AutoSurvey retains its 530K corpus. Topics/backbone match, but retrieval resources, workflow and costs do not all match.

| System | BSC (1–5) | TSQ (1–5) | HDQ (1–5) | MAR (1–5) | Total (1–5) |
| --- | --- | --- | --- | --- | --- |
| DAS | 3.87 | 4.18 | 4.25 | 5.00 | 4.32 |
| Naive RAG | 3.67 | 4.00 | 4.11 | 4.07 | 3.96 |
| AutoSurvey | 3.81 | 3.74 | 3.69 | 3.67 | 3.73 |

Source location: Table A16, Appendix F.1, PDF p. 31 · [Source](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Quality/cost trade-offs in scoped repair

Thirty topics, identical pre-review checkpoints, model, prompts, three-round limit and deterministic checker. Pass rate divides reviewed subsections that obtain Reviewer PASS within budget by reviewed subsections; it is neither factual-claim accuracy nor total pipeline cost.

| Repair policy | Review pass rate (%) | Review/repair tokens per survey (millions) | HDQ (1–5) |
| --- | --- | --- | --- |
| Direct Edit Only | 58.42 | 0.95 | 4.24 |
| Paragraph Replan Only | 53.69 | 0.96 | 4.38 |
| Full DAS | 74.59 | 0.79 | 4.28 |

Source location: Table 4 and Appendix F.3, PDF pp. 9,31–32 · [Source](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

DAS leads matched-topic comparisons, but its displayed 4.34 tie with human surveys does not establish interchangeability: human references were not generated from identical inputs, and assessors do not verify every domain claim. Three external experts specialize in AI/survey assessment rather than each non-CS field. Cross-judge submetric correlation is moderate (overall ρ=0.507); shared generator/judge and metadata can introduce correlated bias. The semantic Reviewer does not read sources, and deterministic checks verify syntax/identifiers rather than entailment. Components trade dimensions: removing candidate-grounded taxonomy yields 4.35 versus full DAS 4.34. Runtime excludes full offline-lake construction; DAS 1.49 hours versus Naive RAG 0.20 reflects different execution structures, not pure model speed.

DAS-2M’s roughly two million is acquisition scale; 1.53 million papers survive deduplication/parsing. After PDF parsing, preprocessing removes HTML tables, images and trailing reference/appendix material, disables formula recognition and truncates long inputs: this is not a lossless full-evidence lake. Monthly ingestion appends new papers without guaranteeing automatic replacement of older versions. In the twenty-paper model audit, only 16/20 evaluation-result domains are correct; structural validity is not factual reliability. The official repository still marks core method implementation as pending, distinct from the paper’s references to accompanying code materials: [release status](https://github.com/ZhikaiXu24/DAS).

Independently audit source-level numerical, conditional and attribution errors with subject specialists rather than recycling the same evidence cards. Match candidate pools, backbone, total tokens and visual budgets; report scholarly scores without MAR plus utility including timeouts. Stress shared representations with stale versions, conflicting sources and incremental updates, then amortize offline extraction cost when measuring cross-topic reuse.

[Source](https://arxiv.org/pdf/2608.18034v1)
<!-- EVIDENCE:limitations:END -->
