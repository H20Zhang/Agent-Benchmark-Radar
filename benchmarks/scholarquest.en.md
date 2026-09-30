# ScholarQuest: paper-set retrieval conditioned on research intent

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-19<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.20235)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](scholarquest.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read Sections 1–6 and Appendices A–E, including construction settings, the human confusion matrix, complete tool-call cases and gold lists, four intent examples and all prompts; visually checked Table 2, Figure 4 and appendix cases.

[arXiv 2606.20235v1 · 2026-06-18](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

Qwen3-Max maps 1,682 ACM topics to arXiv categories, retaining 1,638 CS seeds, generates four intents per seed and filters to 1,111 queries. Gold construction searches multiple sources using ten rewrites and expands references/citations up to two hops. Papers are deduplicated by arXiv ID and assessed by multiple unnamed LLMs using titles, abstracts and metadata. An illustrative query requests remote-replication papers while excluding local replication; treating the excluded concept as a positive keyword explores the wrong neighborhood. Gold relevance does not amount to full-text verification of every detailed claim.

Editorial placement: direct references are PaSa’s RealScholar/AutoScholar and SPARBench. ScholarQuest adds taxonomy-driven topics, controlled intents and a shared agent backend. Unlike MAPLE’s many queries per paper, it retrieves many papers for one query, measuring set coverage and scope preservation rather than full-text fact checking or survey quality.

[Source](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

ScholarBase uses abstract-bearing S2/arXiv records with BGE-M3 dense retrieval, BM25/RRF hybrid retrieval, metadata lookup and citation expansion. PaSa, SPAR and PaperScout retain released code/checkpoints while sharing the backend; precise backbones, maximum call/token/time budgets and repeats are not fully specified. External search systems return up to three hundred papers per query rather than using one common internal ranker. Recall@100 measures gold recovery within the top hundred; Recall@All uses all returned items, summarized across queries rather than pooling every gold paper. Human auditing samples 150 pairs from each automatic-label tier, totaling 450, with majority judgments from three PhD experts.

[Source](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected overall recall and scope-control results

All 1,111 queries, with unequal gold-set sizes and reported answer-size bins spanning 5–200 papers. Overall columns summarize query-level recall; scope control uses its subset. Agent and one-shot budgets differ, preventing a matched-compute ablation interpretation.

| System | Overall R@100 (0–1) | Overall R@All (0–1) | Scope-control R@100 (0–1) |
| --- | --- | --- | --- |
| Hybrid Retrieval | 0.214 | 0.244 | 0.091 |
| PaSa | 0.281 | 0.310 | 0.193 |
| PaperScout | 0.314 | 0.355 | 0.182 |

Source location: Table 2, p. 5; Section 4.1 and Appendix A.2 · [Source](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Selected agent search workload

Process statistics on the same 1,111 queries. Candidate/call counts are not tokens, latency or monetary cost, and ratios of aggregate means must not be substituted for the paper’s query-level efficiency summaries. Total compute is not matched.

| System | Mean tool calls/query | Mean observed candidates/query |
| --- | --- | --- |
| PaSa | 60.1 | 744 |
| PaperScout | 45.0 | 408 |

Source location: Figure 4, p. 5; Section 4.3, pp. 6–7 · [Source](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

PaperScout leads overall recall but trails PaSa on scope-controlled R@100, so it does not win every intent. Only 129/150 automatically high-scoring pairs are strict human matches, versus 148/150 relaxed matches. High relaxed agreement does not remove gold-label errors or quantify relevant papers missed before candidate collection. Policies, backbones and actual budgets differ, preventing exclusive attribution to autonomous planning. Extensive exploration can remain off-intent under the gold labels, but missing gold does not establish that every out-of-gold retrieval is useless.

The historical block records May 19, whereas the inspected arXiv v1 is June 18; this does not disprove an earlier public artifact, so the block is preserved pending verification. BQ_002897 has twelve gold papers in Tables 10–11 but eleven in Appendix D, which omits 2002.03740; no unified denominator is inferred from that case. Actual intents are method, setting, scope control and claim comparison, not generic survey or method-comparison categories. The paper explicitly supports a million-scale backend, not the original note’s unverified approximately three-million count.

Fix backbone, backend and call/candidate budgets while separately enabling rewrites, citation expansion and exclusion checking. Independently audit full texts for selected gold and out-of-gold results, reporting precision, deduplicated recall and marginal evidence utility. Stratify by intent and answer-set size, and reconcile the versioned case lists.

[Source](https://arxiv.org/pdf/2606.20235v1)
<!-- EVIDENCE:limitations:END -->
