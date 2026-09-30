# BEIR: retrieval quality, cost and judgment bias across domains

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2021-04<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2104.08663)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](beir.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

v4 main Sections 1–7 plus appendix dataset/model/corpus inventories and experimental settings; key Tables 3, 9, 10 and Figures 3–4 checked in the PDF.

[arXiv:2104.08663v4](https://arxiv.org/pdf/2104.08663v4)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

Corpus, queries and relevance labels form one retrieval interface across 18 English evaluation datasets. MS MARCO is the in-domain reference. nDCG@10 accommodates binary/graded relevance; retrieval, reranking and adaptation retain distinct resource settings.

[Primary source](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

Main metric is nDCG@10 (0–1), computed with pytrec_eval and no LLM judge. MS MARCO is the in-domain reference; out-of-domain retrieval uses each dataset's relevance judgments. BM25 uses Anserini k=0.9, b=0.4; TAS-B is MS-MARCO-trained DistilBERT; BM25+CE reranks the first 100 hits with MiniLM-L6. Most neural inputs use the first 512 wordpieces; ColBERT has a separate length-300 setting. Hardware, corpus and truncation belong with the scores.

[Setup source](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## In-domain advantage does not guarantee transfer

Selected datasets from Table 2, nDCG@10 on 0–1; compare within rows rather than treating absolute scores across datasets as a common difficulty scale. Query counts for the three splits are 6,980, 500 and 49 respectively; nDCG@10 is averaged over queries.

| Dataset / split | BM25 nDCG@10 | TAS-B nDCG@10 | BM25+CE nDCG@10 |
|---|---|---|---|
| MS MARCO dev | 0.228 | 0.408 | 0.413 |
| BioASQ test | 0.465 | 0.383 | 0.523 |
| Touché-2020 test | 0.367 | 0.162 | 0.271 |

TAS-B beats BM25 on in-domain MS MARCO but reverses on these two out-of-domain examples. Transfer needs testing; this is not a universal claim against dense retrieval.

Fact source: Table 2, section5 · [Source](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## The paper did measure latency and index size

One million DBpedia documents, Xeon 8168 / 8 CPU cores and V100 GPU; dense retrieval uses exact search and a dash means unreported.

| System | CPU latency (ms) | GPU latency (ms) | Index (GB) |
|---|---|---|---|
| BM25 | 20 | — | 0.4 |
| TAS-B | 125 | 14 | 3 |
| BM25+CE | 6100 | 450 | 0.4 |

Latency/index size are not wholly unmeasured gaps. They still need revalidation with modern hardware, indexing and workloads.

Fact source: Table 3, section5.1 · [Source](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Additional judgments change the interpretation

TREC-COVID with 980 added human query-document judgments; judgment sets change on the same dataset, still using nDCG@10.

| System | Original-judgment nDCG@10 | Expanded-judgment nDCG@10 |
|---|---|---|
| BM25 | 0.656 | 0.668 |
| ANCE | 0.654 | 0.735 |

ANCE moves from just below BM25 to above it, demonstrating sensitivity to lexical annotation-pool bias. The expanded judgments are not exhaustive ground truth for every unjudged relevant document.

Fact source: Table 4, section6 · [Source](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

These are retrieval-ranking results, not direct evidence of multi-step search or final RAG answer quality. Text says docT5query beats BM25 on 11/18 while Figure 3 shows 12/18; no reconciliation is invented. Compared with single-dataset optimization, BEIR foregrounds domains, resources and judgments. Next, fix corpus/truncation/hardware/judgments, match cost and expand relevance assessment.

[Primary evidence](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [BRIGHT](bright.en.md) · [RAGBench](ragbench.en.md) · [KILT](kilt.en.md)

<!-- RESEARCH-DECISION:END -->
