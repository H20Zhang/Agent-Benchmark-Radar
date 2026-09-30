# BrowseComp-Plus_CM: projecting agentic search onto an independent large corpus

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2026-08-18 · paper v1 snapshot<br>
> **Independent 553M-document corpus / GPT-5.6 Sol — Answer accuracy: 80.7%** (Cross-corpus answer accuracy)<br>
> Selected original-track results; metrics, subsets, and systems are not pooled into one winner. [Original source](https://arxiv.org/abs/2608.20317)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](browsecomp-plus-cm.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–7, all projection stages, failure cases, paired corpus and closed-book evaluations; appendices inspected: A–B, complete corpus duplication analysis, examples and evaluation/judge prompts. Not performed: No data/code rerun or private hop-label inspection

[arXiv v1, 2026-08-20](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

It directly projects BrowseComp-Plus questions onto independent ClimbMix, retaining a fully grounded subset. The corpus-first design replaces query-conditioned document selection, while also changing selection bias and relevance-set denominators.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

BrowseComp-Plus questions are retained while their evidence is projected onto independently assembled ClimbMix: about 553 million documents and nominally 400 billion tokens, measured at 410.6 billion with Llama-2 tokenization, in a 559-GB Lucene index. GPT-5.5/Codex decomposes questions using gold answers and original support as hints, then grounds atomic facts through BM25 search and full-document reading. Of 830 questions, 326 are answerable; requiring evidence for both necessary and redundant confirmatory hops leaves 65. Independent PIIKA/GPT-5.5 answers all 65 with supplied evidence; author review of qualifiers such as dates leaves 57. Opus 5 pools candidates, removes unsupported hop associations and expands exact and verified near duplicates into question-level qrel unions.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The same 57 questions are paired across the original roughly hundred-thousand-document corpus and ClimbMix. PIIKA uses Pyserini BM25 and full-document tools with GPT–5.6 Sol at max effort, Gemma 4 31B IT and Qwen 3.5 9B. A GPT judge checks final-answer semantic equivalence; the exact judge version, common absolute token/call cap and sampling configuration are not fully specified. Recall averages relevant documents shown in search results, not documents actually read, used or required-hop coverage. Closed-book runs disable tools at execution level. Only completed runs count; three initially incomplete GPT ClimbMix queries were rerun under the same setup and all failed, yielding 46/57. Construction revisits near misses at k=500, which is not a documented universal evaluation depth.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Paired questions across corpora

The same 57 tasks, GPT at max effort. Accuracy is final-answer correctness; recall macro-averages coverage of each corpus’s own qrels, whose denominators differ. Calls are mean retrieval calls. Only completed runs are included; no confidence intervals are given.

| Model / corpus | Accuracy percent | Qrel recall percent | Calls per query |
|---|---|---|---|
| GPT–5.6 Sol / BrowseComp-Plus | 86.0 | 84.3 | 60.2 |
| GPT–5.6 Sol / ClimbMix | 80.7 | 21.4 | 98.3 |
| Gemma 4 31B IT / BrowseComp-Plus | 26.3 | 24.9 | 24.5 |
| Gemma 4 31B IT / ClimbMix | 15.8 | 2.8 | 23.4 |

Source: Table 1; Section 6 · [Paper](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Closed-book success and projection selection

All tools are disabled at execution level; only the question is supplied, with the same answer-equivalence judge. Denominators are 830 and 57, not independent identically distributed samples. Correctness does not prove memorization of the exact benchmark item.

| Model | All 830 accuracy percent | Projected 57 accuracy percent |
|---|---|---|
| GPT–5.6 Sol (max) | 46.1 | 70.2 |
| Gemma 4 31B IT | 0.8 | 1.8 |
| Qwen 3.5 9B | 0.1 | 0.0 |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

The strongest model shifts from 86.0 to 80.7 percent accuracy, 84.3 to 21.4 percent recall and 60.2 to 98.3 calls. However, ClimbMix qrel sets are larger and unevenly redundant, changing the recall denominator: the 62.9-point drop is not the same amount of necessary evidence lost. The same model answers 70.2 percent of these tasks closed-book, so correct answers do not prove evidence retrieval, and instructions banning internal knowledge cannot guarantee compliance. Only 57 of 830 questions survive and this subset is substantially easier closed-book. Conclusions apply to the selected subset and BM25, without isolating corpus size or proving general deployment behavior.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

The 57 tasks are strongly selected and lack reported confidence intervals. Construction and validation share a model family; author review has no annotation-agreement estimate. Failing to find a hop does not prove absence from 553 million documents; lexical access and agent budgets constrain construction. Of 347 question–hop pairs, forty have at most two supporting documents while roughly a quarter exceed forty, biasing union recall toward redundant hops; hop labels are withheld. A question-independent corpus is neither contamination-free nor an unfiltered natural web distribution. Next compare dense/hybrid retrieval under controlled corpus sizes and matched budgets, reporting required-hop coverage, citation support and closed-book gains, with independently auditable hidden-label scoring.

The prose names get_document while the released evaluation prompt uses read_document; these may be wrapper aliases, but exact executable schemas are not in the paper. The conclusion attributes perfect supplied-evidence answering to the evaluated strong agent, whereas the explicitly specified independent validation stage uses GPT-5.5 on 65 tasks and the main evaluation uses GPT–5.6 Sol on 57; exact oracle-run configuration is not fully reconciled. The original BrowseComp-Plus 86.5% evidence-in-top-five-prefix finding is restated as truncation removing necessary evidence for 13.5% of questions; that stronger causal necessity claim does not follow directly from the original audit. Closed-book success demonstrates answers available without retrieval but does not identify whether the exact benchmark question was memorized, its source facts learned or constraints solved from prior knowledge.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [browsecomp-plus](browsecomp-plus.en.md) · [livebrowsecomp](livebrowsecomp.en.md)
