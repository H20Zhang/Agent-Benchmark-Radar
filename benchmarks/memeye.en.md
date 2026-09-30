# MemEye: visual detail and changing-state memory diagnostics

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-14<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.15128)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memeye.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read the substantive content across all 46 pages: §§1–6 and Appendices A–E, including filtering gates, taxonomy audits, implementation budgets, judge prompts, bootstrap analyses, all result matrices and all 13 case examples. Visually checked main results, caption ablations and illustrated state-update cases.

[arXiv v1 / 2026-05-14](https://arxiv.org/pdf/2605.15128v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Questions receive visual-granularity labels X1–X4: scene, region, individual object/person, and fine pixel detail such as small text or color. Memory-operation labels Y1–Y3 denote atomic fact retrieval, relational association across sessions, and synthesis of changing or conflicting states. Thus high-X means X3–X4, while Y3 requires handling updates and overrides. Candidate tests remove robust option-only/text-only shortcuts and minimal-caption successes; gold images check answerability. These gates use GPT-5.4-mini and GPT-5.2 across four answer rotations, followed by human adjudication (Appendix A.4).

A fossil display’s identification tag changes between sessions. Retrieving several older photographs can favor the old tag even when the new photograph is present; the task is to read the latest valid state, not count how often a tag appears (Figure 12).

### Measurement genealogy

Mem-Gallery extends multi-session visual conversation evaluation. MemEye adds explicit evidence-granularity, visual substitution and changing-state controls. Its diagnostic contribution is separating missing details from wrong evidence timing, rather than proving that all captions are intrinsically inadequate. The next coordinate is budget-matched preservation and state selection on independently collected trajectories.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

There are 371 original questions, each in MCQ and open form, over 221 sessions/438 images; MCQs use four rotations. Main GPT-5.4-mini runs use temperature 0 and 128 output tokens; full-context methods cap history at 128K with FIFO truncation. Semantic RAG (SRAG) retrieves ten dialogue rounds with MiniLM text embeddings and, for visual input, SigLIP2. Text streams use GPT-5.2 captions; GPT-5.2 also judges open answers on five grades from 0 to 1. Other methods retain different encoders or iteration budgets; SimpleMem retrieves twenty memories (Appendix C).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected results use GPT-5.4-mini. Main averages are equal-weight means of 12 taxonomy cells, not simple 371-question accuracy. MCQ EM first averages four answer rotations. Caption-control rows are separate matched 80-question high-X evaluations; recency confidence intervals resample original questions 10,000 times.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| SRAG(V) / GPT-5.4-mini / main | 371 questions; 12-cell macro-average | MCQ EM / open Judge (0–1) | 0.6177 / 0.4937 | Top-10 native-image rounds; GPT-5.2 judge | Table 2, p.8 |
| SRAG(T) / GPT-5.4-mini / main | 371 questions; 12-cell macro-average | MCQ EM / open Judge (0–1) | 0.5484 / 0.3909 | Top-10 captioned rounds; GPT-5.2 captions/judge | Table 2, p.8 |
| SRAG(V) / high-X native images | Matched high-X subset; 80 open questions | Mean Judge (0–1) | 0.428 | Native images; fixed answerer | Table 11, p.30 |
| SRAG(T) / high-X generic captions | Matched high-X subset; 80 open questions | Mean Judge (0–1) | 0.235 | GPT-5.2 generic captions | Table 11, p.30 |
| SRAG(T) / high-X task-aware captions | Matched high-X subset; 80 open questions | Mean Judge (0–1) | 0.387 | GPT-5.4-mini captions; typically 2–3 times longer | Table 11, p.30 |
| SRAG(V) + recency / alpha=0.7 / Y3 | Y3; 60 original questions | Paired Judge delta / 95% CI (0–1 units) | +0.067 / [-0.042, +0.175] | Answer regeneration; lambda=0.02; fixed candidate pool | Table 14, p.33 |

Source: [Table 2, p.8; Table 11, p.30; Table 14, p.33](https://arxiv.org/pdf/2605.15128v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Minimal-caption filtering is not proof against arbitrary detailed captions: the task-aware control substantially narrows the gap. Macro-cell scores weight small and large cells equally. Judge validation uses one human and 71 retained predictions after excluding one borderline case; its agreement concerns binary acceptance, not full graded calibration. Recency gains in answer quality are statistically inconclusive. Image preprocessing, method-specific budgets and generated visual states limit architecture-only attribution and deployment generalization.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Match original images against captions at several explicit token budgets, while freezing the answerer and judge. Cross this with supplied latest-clue and all-clue controls; separate state-location questions from genuine change-comparison questions. Report both question-weighted and cell-macro scores, plus trajectory-clustered intervals and ingestion cost.
<!-- EVIDENCE:next:END -->
