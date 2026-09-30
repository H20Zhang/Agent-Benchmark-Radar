# Q2D-Web

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.08887)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](q2d-web.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, query/corpus/label construction, subsampling, all results and error taxonomy; appendices inspected: Appendix A pooling and sampling retriever configurations. Not performed: Private corpus, queries and judgments were not accessible; no leaderboard execution or rerun

[arXiv v1, 2026-09-08](https://arxiv.org/pdf/2609.08887v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with BrowseComp-Plus’s smaller research-question set and BEIR’s heterogeneous collections, Q2D-Web scales both corpus and production agent queries with deeper positive pools. It targets first-stage candidate recall, not final agent answers; its query-conditioned corpus also differs from corpus-first ClimbMix projection.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The benchmark samples 69,721 agent-reformulated queries from roughly 23,000 user searches across nine months: 12,365 primary and 57,356 support queries. Month-stratified sampling preserves domain/language distributions before removing PII, duplicates, sub-three-character queries and filtering operators such as site, retaining ten major query languages. Unioning each query’s top five thousand production results and deduplicating five-gram Jaccard≥0.975 clusters yields roughly 190 million documents; the longest representative inherits labels. Three qrel sets use agent citations, up to fifty production hybrid/reranked results (mean 43.1), and their union with LLM judgments from a separately pooled candidate set. Combined labels average 99.6 positives per query.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Nine pre-2025 retrievers form an RRF pool; DeepSeek-V4-Flash strictly judges the top five hundred previously unlabeled documents for all query constraints, without reported independent human relevance calibration. Thirteen evaluated systems comprise BM25, ten dense and two late-interaction models. Neural checkpoints are temporally held out from pooling, but BM25 participates in both. Dense models use official default instructions. Evaluated document inputs are only the first 512 tokens, with thirty-two query tokens for late interaction, not full-document retrieval. Primary Recall@1000 is complemented by Recall@100 and nDCG@10. Subsampling retains every labeled positive plus one thousand old-model RRF distractors per query, about sixty million documents or 31.7 percent. Corpus, queries and judgments remain private; the public interface is an open-weight-model leaderboard.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Different leaders for deep recall and shallow ranking

69,721 queries and roughly 190 million documents with Combined binary qrels. All metrics×100 and aggregated by query. Neural document inputs cap at 512 tokens with checkpoint instructions; these are not generated-answer scores.

| Retriever | Recall@1000 | Recall@100 | nDCG@10 |
|---|---|---|---|
| pplx-embed-v1-4b | 69.11 | 29.82 | 45.84 |
| Nemotron-3-Embed-8B | 68.58 | 30.03 | 47.44 |
| BM25-tantivy | 44.77 | 18.16 | 30.3 |

Source: Table 3, full corpus Combined columns · [Paper](https://arxiv.org/pdf/2609.08887v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Subsampling preserves order while inflating recall

Same 69,721 queries and Combined qrels, metrics×100. Old-model RRF supplies one thousand distractors per query while retaining all known positives. Kendall τb=1 applies to this thirteen-model panel, not guaranteed future models.

| Retriever | Full Recall@1000 | 31.7 percent subcorpus Recall@1000 |
|---|---|---|
| pplx-embed-v1-4b | 69.11 | 74.07 |
| Nemotron-3-Embed-8B | 68.58 | 72.79 |
| Qwen3-Embedding-8B | 64.53 | 69.61 |

Source: Table 3, Combined Recall@1000 full/sub columns; Section 4.2 · [Paper](https://arxiv.org/pdf/2609.08887v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Under Combined labels, pplx-4B leads deep recall at 69.11 versus Nemotron8B’s 68.58, while Nemotron leads Recall@100 and nDCG@10; Citation deep-recall leadership also differs. The 31.7-percent subcorpus preserves this evaluated panel’s Combined ranking while inflating mean Recall@1000 by about 5.1 points. It is neither unbiased absolute scoring nor a guarantee for future retrievers. BM25 has the lowest aggregate recall yet the largest unique-positive contribution, motivating controlled fusion rather than establishing fusion gains by itself.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

One vendor’s agents generate queries and its production results define the corpus, rather than independent web sampling. Private data reduces contamination exposure but limits independent auditing. Ranking labels and strict LLM labels have different biases; the same judge reclassifies 15.8 percent of four thousand shared hard negatives as relevant, not an estimate of all-label error. Prefix truncation mixes deep-evidence omission with model ability. No comparative confidence intervals are supplied, so small gaps and slices need care; related support queries are not independent user needs. Next cluster statistics by user search, human-audit label sources, hold out independent retrieval pools, and test full documents and cost-matched fusion.

Section 4.2 says evaluation fits in about eight hours on an eight-H200 node, but the same paragraph reports approximately 1,500 H200 GPU-hours for the 4B model, equivalent to about 187.5 hours on eight GPUs at ideal scaling. The eight-hour claim fits only the approximately 70-GPU-hour small model, not all models. The source calls Citation high-precision by construction but explicitly assumes that citation implies relevant supporting use; citation correctness is not independently demonstrated. The paper sometimes describes pooling/evaluation as separate without immediately noting the BM25 overlap; neural temporal holdout does not apply to BM25. Exact nine-month calendar window, production agent/reranker identities and complete ANN/search implementation parameters are not given in the reviewed paper.
<!-- EVIDENCE:limitations:END -->
