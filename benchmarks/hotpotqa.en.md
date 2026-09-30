# HotpotQA: making multi-hop evidence composition an explicit evaluation target

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2018-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/D18-1259/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](hotpotqa.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–7; Appendices A–C; Tables 1–9; Table 4–7 PDF rendering verified

[EMNLP 2018 — EMNLP 2018 camera-ready](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with earlier single-passage or single-hop QA, HotpotQA requires cross-paragraph composition and supporting-sentence annotation. The measurement shifts from answer-only correctness to joint answer/evidence correctness, while stopping short of autonomous open-web research.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Sample hyperlink-connected paragraphs and comparable entities; crowdworkers supply questions, answers and supporting sentences. Three-fold model filtering separates medium/hard questions; development/test contain hard questions. The baseline jointly predicts answers and support.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The corpus contains first paragraphs from English Wikipedia dated 2017-10-01. Training has 90,564 questions and development 7,405; the two test settings have separate sets of 7,405. Distractor supplies two gold and eight tf-idf distractor paragraphs. Fullwiki starts with at most 5,000 inverted-index candidates from roughly five million pages, then selects ten by bigram tf-idf. The baseline is an RNN reader with character representations, self-attention and bidirectional attention, jointly predicting supporting sentences and yes/no/span answers. Joint scoring multiplies answer and support precision/recall before computing per-example F1 and averaging.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Two evidence settings on development

The same 7,405 development questions, in percent; answer, supporting-fact and joint metrics are computed per example and averaged. Distractor supplies two gold and eight distractor paragraphs; Fullwiki retrieves from the corpus.

| Setting | Answer_EM | Answer_F1 | Support_F1 | Joint_F1 |
|---|---|---|---|---|
| Distractor dev | 44.44 | 58.28 | 66.66 | 40.86 |
| Fullwiki dev | 24.68 | 34.36 | 40.98 | 17.73 |

Source: Table 4, section 5.2 · [Paper](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Support supervision and supplied evidence

Mean answer F1 in percent on 7,405 distractor development questions; removing support supervision differs from supplying gold evidence.

| Condition | Answer_F1 |
|---|---|
| Baseline | 58.28 |
| No support supervision | 56.19 |
| Gold paragraphs only | 63.58 |
| Gold supporting sentences only | 66.98 |

Source: Table 7 · [Paper](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Answer and evidence correctness differ: distractor-development answer F1 is 58.28 versus joint 40.86. Test settings use different samples; development is the cleaner paired comparison.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Model filtering, first-paragraph corpora and 100-example manual analysis limit generality; 6% were single-hop, 2% unanswerable. Next: fixed-reader, budget-matched iterative retrieval.

No substantive numeric inconsistency found in selected rows. Appendix C truncates missing paragraph ranks at candidate-count+1; mean rank is optimistic, not an unrestricted corpus rank.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [multihop-rag](multihop-rag.en.md) · [browsecomp-plus](browsecomp-plus.en.md)
