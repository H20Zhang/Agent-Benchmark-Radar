# MultiHop-RAG: retrieval must compose evidence, not only rank passages

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2024-01<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2401.15391)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](multihop-rag.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–6 and limitations; Appendix A generation prompts, Appendix B examples; Tables 1–15; Tables 5–6/Figure 3 visually verified

[v1,2024-01-27](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Relative to HotpotQA’s Wikipedia multi-hop QA, this benchmark uses newer news and separates retrieval quality from generation with supplied evidence. It retains evidence composition while adding temporal and null-answer conditions; different corpora and denominators prevent direct predecessor score comparisons.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

From 609 news articles, extract facts and generate GPT-4 claims; shared entities/topics bridge 2–4 facts into questions, checked with UniEval/GPT-4. The 2556 questions include inference, comparison, time and 301 null cases.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The 609 news articles date from 2023-09-26 to 2023-12-26. Of 2,556 questions, 301 are unanswerable; retrieval evaluation uses 2,255 non-null questions. LlamaIndex creates 256-token chunks, cosine retrieval selects twenty, and bge-reranker-large reranks them. Generation receives the top six voyage-02/reranker chunks, capped at 2,048 tokens. GPT-4 is cited as gpt-4-1106-preview; Mixtral is 8x7B-Instruct. Hits@k means the fraction of gold evidence recovered, rather than the probability of at least one hit.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Matched retriever with/without reranking

Across 2,255 non-null questions, Hits@k is the fraction of gold evidence recovered, on a 0–1 scale; reranking starts from the top 20 candidates.

| Pipeline | Hits@10 | Hits@4 |
|---|---|---|
| voyage-02 | 0.6506 | 0.4619 |
| voyage-02+bge-reranker-large | 0.7467 | 0.6625 |

Source: Table 5 · [Paper](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Answer results: unequal denominators

Answer accuracy on a 0–1 scale; retrieved evidence uses all 2,556 questions while gold evidence uses 2,255 non-null questions, so the difference is not a matched retrieval-loss estimate.

| Model | Retrieved(all 2556) | Gold(non-null 2255) |
|---|---|---|
| GPT-4 | 0.56 | 0.89 |
| Mixtral-8x7B-Instruct | 0.32 | 0.36 |

Source: Table 6, section 4.2 · [Paper](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Retrieval and evidence reasoning remain imperfect, but .56→.89 also changes sample composition; it is not a pure retrieval effect. Hits is not complete-chain recovery.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

At most four evidence pieces, short answers and generator-assisted validation; freshness is historical. Next: matched non-null questions and budgets for retrieval/oracle controls.

All-query retrieved versus non-null oracle comparison is an explicit protocol asymmetry, not an error to hide. GPT-3.5 is named ChatGPT in Table 6; exact snapshot not clearly supplied.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [hotpotqa](hotpotqa.en.md) · [agenticragtracer](agenticragtracer.en.md)
