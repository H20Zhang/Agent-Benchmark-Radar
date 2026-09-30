# RAGBench: benchmarking the evaluator, not only the RAG system

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2024-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2407.11005)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ragbench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–8; Appendix 9.1–9.7 including prompts, postprocessing, training, OOD; Tables 1–4; Table 3 visually verified

[arXiv v1 — v1; PDF header 2024-06-25; do not reinterpret as verified first-public date](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Relative to answer-only QA benchmarks, RAGBench turns document–question–response triples into evaluator training/testing data and separates relevance, evidence use and faithfulness. It belongs to the evaluator branch; fitting evaluator labels is not a gain in generator capability.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Normalize 12 sources into documents, question, response; GPT-4-0125-preview labels relevant, used and supporting sentences. TRACe measures relevance, utilization, completeness and adherence; sentence labels train token-level DeBERTa heads.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Training, development and test contain approximately 78,000, 12,000 and 11,000 examples, split by question within each source. Responses mainly come from GPT-3.5-0125 and Claude 3 Haiku at temperature one, with some inherited responses. GPT-4-0125-preview supplies supervision. The actual scorer is a DeBERTa-v3-Large NLI checkpoint with three heads, trained for three epochs on an A100, with binary threshold 0.5. Hallucination detection uses AUROC; relevance and utilization use RMSE. Completeness is defined but lacks a separate main-table prediction result.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Retain improvements and counterexamples

Source-specific test sets; higher hallucination AUROC and lower relevance RMSE are better, both on a 0–1 scale; labels come from GPT-4 and row-specific test denominators are not given here.

| Dataset/metric | GPT3.5 | RAGAS | DeBERTa |
|---|---|---|---|
| HotpotQA/Hall_AUROC | 0.59 | 0.62 | 0.85 |
| DelucionQA/Hall_AUROC | 0.57 | 0.7 | 0.64 |
| PubMedQA/Rel_RMSE | 0.21 | 0.37 | 0.26 |

Source: Table 3, section 5 · [Paper](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Cross-domain training degradation

Hallucination AUROC on a 0–1 scale for the same source test sets; all-domain versus general-knowledge-only training, with per-source test denominators unspecified here.

| Dataset | All-domain train | General-knowledge-only train |
|---|---|---|
| FinQA | 0.81 | 0.67 |
| TechQA | 0.86 | 0.76 |

Source: Table 4, Appendix 9.7 · [Paper](https://arxiv.org/pdf/2407.11005v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Use DeBERTa-v3-Large; the abstract says RoBERTa inconsistently. Gains are not universal. Completeness is defined but lacks standalone main-table prediction results.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

GPT-4 labeling can transfer bias; synthetic-system ranking validation is not per-example human validity. Next: independent human labels, held-out generators and cost-matched judges.

Abstract RoBERTa vs§5.2/Table 3 DeBERTa. §6 universal-superiority wording contradicts Table 3 exceptions. TechQA Table 1 gives 5 documents; Appendix 9.2 says subsample 10.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [ragtruth](ragtruth.en.md) · [claimprobe](claimprobe.en.md)
