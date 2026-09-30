# OntologyBench

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.08174)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ontologybench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–8, split-integrity audit, metrics, training, ontology reference, reranking, discussion and limitations; appendices inspected: A–H, all examples/statistics/training/metric formulas/scoring prompt/full result grids/error rules. Not performed: No code/data rerun; exact ontology snapshot versions and failure-subset denominator not fully specified

[arXiv v1, 2026-09-08](https://arxiv.org/pdf/2609.08174v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with BEIR/NFCorpus semantic document relevance, this defines directional relations and phenotype intersections through ontologies. It targets structural compatibility, while shared concepts/relations make it transductive and ontology references use a different information regime.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Eight tasks use 6,611 MONDO diseases, 8,253 HPO phenotypes and 2,345 HGNC/NCBI genes: three alias-to-definition tasks, four directional disease/phenotype/gene relations and phenotype-triplet-to-disease retrieval. The 471,854 training and 125,744 evaluation relevance pairs are not independent query counts. Triplets come from one disease and target diseases compatible with all constraints; training has 5,642 queries with 4.39 positives on average, evaluation 2,537 with 2.26. Exact directed pairs do not overlap within tasks, but inverse relations can appear in other training tasks and 146 test triplets occur with different training targets. This is transductive relational/compositional transfer over a shared vocabulary.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Each task ranks its complete corpus without ontology pruning; binary nDCG/MRR/Hit macro-average questions. Grounding-only and all-task supervision use BioLORD cached multiple-negative loss, Qwen0.6B InfoNCE and ModernColBERT MaxSim contrastive training. Within architectures both regimes run two epochs on one H100 MIG at seed 42, not multi-seed averages. Bi-encoders cap at 256 tokens; ColBERT uses 48 query/300 document tokens. Tier 3 reranking fixes the unified-supervision Qwen top fifty: 2,083 of 2,537 queries contain a positive and 454 remain zero-credit failures. LLMs independently score each triplet/disease-description pair from zero to 100 without outside medical knowledge. Phenomizer-style references directly access ontology information unavailable in full to text models.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Supervision tradeoffs within one architecture

Definition retrieval has 4,581 test queries and triplet retrieval 2,537. Metrics are zero-to-one query macro-averages over each full task corpus. Fine-tuning uses two epochs/one seed. The 0.234 cell follows the appendix; prose 0.170 remains unresolved.

| Qwen3-Embed-0.6B setting | Phenotype-definition nDCG@10 | Triplet-disease nDCG@10 | Triplet Hit@10 |
|---|---|---|---|
| Pretrained | 0.605 | 0.109 | 0.234 |
| Grounding-only fine-tuning | 0.864 | 0.158 | 0.321 |
| All-tier fine-tuning | 0.572 | 0.313 | 0.572 |

Source: Table 2; Appendix Table 12 · [Paper](https://arxiv.org/pdf/2609.08174v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## End-to-end reranking of fixed top-fifty candidates

All 2,537 queries, including 454 zero-credit cases with no positive in the top fifty; metrics zero-to-one. Scorers reorder candidates without adding diseases; paired confidence intervals are unavailable.

| Method | MRR@10 | Hit@10 | nDCG@10 |
|---|---|---|---|
| Qwen0.6B all-tier retriever | 0.297 | 0.572 | 0.313 |
| ModernColBERT | 0.168 | 0.384 | 0.18 |
| Qwen3.6-27B scorer | 0.306 | 0.571 | 0.315 |
| GPT-5.4-mini scorer | 0.301 | 0.574 | 0.312 |

Source: Table 4 · [Paper](https://arxiv.org/pdf/2609.08174v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

All-task supervision raises Qwen0.6B triplet nDCG from 0.109 to 0.313 while lowering phenotype-definition nDCG from 0.605 to 0.572, showing task tradeoffs. Fixed-candidate reranking peaks at nDCG 0.315 or Hit 0.574, near the retriever’s 0.313/0.572. Without paired uncertainty, these small changes do not establish a winner. The ontology reference’s 0.739 demonstrates the value of explicit structure without attributing the entire gap to an inherent inability of embeddings to represent composition.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Disease descriptions may omit structure used to define relevance. Candidate spaces, ambiguity and positive counts differ across tiers, preventing isolated complexity conclusions. Equal epochs do not equalize training data or optimizer updates; all-task gains need not arise solely from ontology structure. Failure classes prioritize low information content, then phenotype overlap/reference rank, making them operational categories rather than causal cognitive diagnoses. No disease course, prevalence, demographics or full patient context is modeled, so this is not clinical diagnostic validation. Next match supervision volume, hold out inverse relations and full triplet combinations across tasks, use multiple seeds and equal candidate information, and human-audit joint constraint satisfaction.

Section 5.5 says pretrained Qwen Tier 3 Hit@10 is 0.170, but Appendix Table 12 reports 0.234; use table-attributed 0.234, leaving the prose conflict explicit. The introductory roughly-five compatible diseases refers to ontology-wide triplet statistics, not the evaluation AvgPos 2.26 or training 4.39. The four failure percentages lack a clear absolute failure-subset count and specific model identity in the reviewed error appendix; they should not be reported as proportions of all 2537 queries. Task-specific held-out pairs do not imply unseen entities/relations: inverse associations and 5.8% repeated triplet queries are explicitly present.
<!-- EVIDENCE:limitations:END -->
