# BrowseComp-Plus: fixing the corpus to separate agent and retriever progress

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2508.06600)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](browsecomp-plus.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, all analyses and ablations; appendices inspected: A–H, evidence mining, annotation example, excluded cases, search/judge prompts and costs; visual checks: Tables 4–5 rendered page 11. Not performed: No experiments rerun, no later-version reconciliation

[arXiv v1 (2025-08-08) — arXiv v1, 2025-08-08; not asserted identical to ACL 2026 version](https://arxiv.org/pdf/2508.06600v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

It directly reuses BrowseComp questions while replacing the web with a fixed document collection and relevance labels. This better separates retriever, agent and interaction effects; the later ClimbMix projection challenges the ease of a small query-conditioned corpus.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Starting from 1,266 BrowseComp question–answer pairs, o3 searches for evidence with the answer supplied. Questions with scraping failures or unverifiable complete evidence chains are removed. Fourteen annotators mark supporting text spans, leaving 830 questions. GPT-4o decomposes the original questions for Google-based hard-negative mining, producing a deduplicated corpus of 100,195 documents. Evidence documents support clues, whereas gold documents directly or implicitly contain the final answer; their qrels are evaluated separately. Agents iteratively retrieve from this fixed corpus, receiving the first 512 tokens of each of the top five documents per call, then produce an answer, document citations and confidence.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

All 830 questions share 100,195 fixed documents. BM25 uses Pyserini and dense retrieval Tevatron; defaults return five documents with 512 tokens each. GPT-5, o3 and gpt-oss use high reasoning in the main comparison. Search-R1 retains its training prompt while the others share a tool prompt. gpt-4.1 judges reference-answer equivalence. Exact dated agent snapshots and a common absolute stopping/token budget are not fully specified. The oracle supplies all labeled documents directly, causing fifty Qwen3-32B context overflows. API costs cover the full 830-question agent experiment, excluding retrieval infrastructure.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Same agent, different retriever

GPT-5 high on 830 questions; accuracy and evidence recall are percentages, calls are per-question means, and dollars cover the full experiment’s agent API use, excluding retrieval infrastructure.

| GPT-5 retriever | Accuracy | Evidence recall | Search calls | Total agent API USD |
|---|---|---|---|---|
| BM25 | 55.9 | 61.7 | 23.23 | 400.36 |
| Qwen3-Embedding-8B | 70.12 | 78.98 | 21.74 | 360.71 |

Source: Table 1; Appendix H Table 8 · [Paper](https://arxiv.org/pdf/2508.06600v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Benefit of reading full documents

830 questions with Qwen3-Embedding-8B throughout; accuracy is in percent and calls are per-question means; previews contain only the first 512 tokens per document.

| GPT-4.1 interface | Accuracy | Search calls | Get-document calls |
|---|---|---|---|
| Preview only | 35.42 | 8.67 | — |
| Preview + get-document | 43.61 | 10.03 | 1.85 |

Source: Table 5; Section 4.8.3 · [Paper](https://arxiv.org/pdf/2508.06600v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## More reasoning effort also increases search

830 questions with Qwen3-Embedding-8B fixed; accuracy and recall are percentages and search calls are per-question means; search budgets are not matched.

| gpt-oss-20B effort | Accuracy | Evidence recall | Search calls |
|---|---|---|---|
| Low | 13.37 | 17.37 | 1.87 |
| High | 34.58 | 49.29 | 23.87 |

Source: Table 4 · [Paper](https://arxiv.org/pdf/2508.06600v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Holding GPT-5 fixed, replacing BM25 with Qwen3-Embedding-8B raises accuracy from 55.90% to 70.12% and reduces mean search calls from 23.23 to 21.74. This supports a retriever effect under this corpus and interface, rather than a ranking against live BrowseComp or a claim that fewer calls guarantee lower total compute. Full-document reading is already tested: adding get-document raises GPT-4.1 accuracy from 35.42% to 43.61%, making the reading interface an important control variable.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Selection by scrapability, answer verification and human effort changes the original 1,266-question population; 42 map-distance and 13 ambiguous questions are excluded. The first 512 tokens retain an answer in at least one gold document for 86.5% of questions, without guaranteeing visibility of every clue. The oracle condition changes both evidence selection and visible document length, so its entire gap cannot be assigned to ranking. Newly added corpus documents are unjudged and may be false negatives. The next test should fix total tokens, calls and reading access, use an independently sampled larger corpus with additional judgments, and cross agent and retriever choices.

The selected results are directly reported in arXiv v1 Table 1; no equivalence with the later ACL 2026 version is assumed. Section 4.8.4 calls 9,771,311 documents roughly ten times 100,195, but the ratio is about 97.5. Preserve exact counts, not the stated multiplier. BM25 original Recall@1000 is 13.7 in Table 2 and 13.6 in Table 6. Main citation metrics have no complete formulas clarifying treatment of zero-citation outputs; document-level precision must not be labeled claim-level entailment accuracy.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [browsecomp](browsecomp.en.md) · [browsecomp-plus-cm](browsecomp-plus-cm.en.md)
