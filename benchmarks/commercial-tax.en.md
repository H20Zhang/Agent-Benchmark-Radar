# The Commercial Tax: RAG / deployment validity

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-17<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.16096)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](commercial-tax.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–7 including inference, licensing/disclosure audit, costs, limitations and competing interests; appendices inspected: A–E, complete panel, worked metric, corpus-size audit, remeasurement, all statistical tables and answering prompt. Not performed: No rerun, artifact audit or independent current license/pricing verification

[arXiv v1, 2026-08-17](https://arxiv.org/pdf/2608.16096v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

This audit retains the MuSiQue/HippoRAG-2 retrieval protocol and adds licensing, formatting and cost conditions rather than a new reasoning task. It contextualizes recall for deployment without measuring complete multi-step RAG utility.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

This is a retrieval and disclosure audit of a fixed MuSiQue/HippoRAG-2 protocol, not a new QA dataset. One thousand released development queries share 11,656 Wikipedia passages, uniformly title plus body. Thirteen embedders use exhaustive exact cosine search without query decomposition, rewriting, reranking or graph augmentation. Recall@k averages each question’s fraction of recovered gold supporting passages; it is not complete-chain success. Paired question bootstrapping uses 100,000 resamples; panel inference applies Holm correction and also reports simultaneous leader-referenced intervals. The disclosure audit is a purposive snowball sample: three NV-Embed-v2-dependent systems plus KET-RAG, adding GraphRAG for cost. Omission counts cannot estimate field-wide prevalence.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

NV-Embed-v2 uses the best of four query instructions and Qwen also receives a formatting sweep, while Nemotron-8B and each API use one configuration; intervals exclude unequal tuning-selection uncertainty. APIs use their asymmetric query/document modes, and BGE-M3 is dense-only. Exact search removes ANN loss without establishing production recall. Answering costs fix gpt-4o-mini at temperature zero, thirty-two output tokens and one completion per query, with five or ten passages, short answers and guessing when evidence is absent. Table 5 has twelve models because NV answering was not rerun after index correction. Dollar rates are historical author-used prices from 2026-07-21, not current quotations. Build/embedding costs scale by corpus size and answering by query volume; query-time retrieval-LLM costs of audited systems are not all measured.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Matched retrieval and paired uncertainty

One thousand queries, 11,656 passages, exact cosine. Recall is mean per-query gold-passage coverage×100. Differences are entrant minus NV in percentage points, with 100,000 paired bootstrap resamples. Nemotron p=0.69; the primary Gemini comparison is uncorrected p=0.001. Marginal interval overlap is not a paired test.

| Embedder | Recall@5 percent | Recall@10 percent | Recall@5 difference vs NV | Paired 95% CI |
|---|---|---|---|---|
| NV-Embed-v2 | 69.55 | 78.12 | 0 | reference |
| Nemotron-3-Embed-8B | 69.79 | 77.54 | 0.24 | [-0.94, +1.43] |
| Gemini embedding-001 | 67.24 | 76.35 | -2.31 | [-3.71, -0.91] |

Source: Table 1; Sections 4.2–4.3 · [Paper](https://arxiv.org/pdf/2608.16096v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Paired corpus-format effects

Same thousand questions and query configuration; recalls are percentages and format differences percentage points. These secondary analyses are reported uncorrected. Format gain differs from matched-format rerun drift, which is −0.54 points for the OpenAI row.

| Embedder | Title plus text Recall@5 | Body-only Recall@5 | Format gain points | Paired 95% CI |
|---|---|---|---|---|
| NV-Embed-v2 | 69.55 | 67.09 | 2.46 | [1.59, 3.35] |
| Nemotron-3-Embed-8B | 69.79 | 67.25 | 2.54 | [1.72, 3.38] |
| text-embedding-3-large | 59.48 | 58.69 | 0.79 | [-0.11, +1.71] |

Source: Appendix D Tables 9–10 · [Paper](https://arxiv.org/pdf/2608.16096v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Separate build scenarios and answering costs

The first rows extrapolate third-party $2.30/$24.94 measurements on 5.64 MB, with one TB=1,048,576 MB; they are not measured at scale. The final rows price measured token usage at historical batch rates and exclude retrieval infrastructure/model serving. These denominators do not support a universal cost ratio.

| Condition | Amount USD | Denominator and status |
|---|---|---|
| GraphRAG low-cost build | 428000 | one binary TB; linear scenario |
| GraphRAG high-performance build | 4637000 | one binary TB; linear scenario |
| Nemotron-8B retrieval, k=5 | 0.058 | 1000 gpt-4o-mini answers; batch rate |
| Nemotron-8B retrieval, k=10 | 0.112 | 1000 gpt-4o-mini answers; batch rate |

Source: Tables 3 and 5; Appendix E · [Paper](https://arxiv.org/pdf/2608.16096v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Nemotron-8B minus NV is +0.24 Recall@5 points, with 95% interval [−0.94,+1.43] and p=0.69: this experiment fails to separate them, rather than proving equivalence or zero commercial penalty. The roughly 1.7-point minimum detectable effect and failed ±0.5-point equivalence test are essential. The 2Wiki pilot’s Gemini-minus-NV gap is only −0.12 points and nonsignificant, so MuSiQue’s 2.31-point gap is not universal. Self-hosting’s zero dollars per token means no provider token toll, not zero compute, electricity, labor or total ownership cost. Million-dollar graph builds are linear scenarios extrapolated from a tiny corpus, not measured production bills.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Unequal format search, one main corpus, hosted drift and selective vendor composition limit ranking transfer; 2Wiki is only a three-model pilot. Bootstrap uncertainty covers question resampling, not deployment domains or tuning selection. License conclusions belong to the paper’s model-card audit; deployment requires renewed version/terms verification, and training-data provenance is not a universal legal rule. Costs omit electricity, operations, labor and systems’ query-time retrieval reasoning; thirty-two-token short answers do not represent research reports. Cross-model token-rate reconstruction and binary versus decimal corpus units must remain explicit. Next, use separate tuning data, multiple real domains, fixed versions and measured ANN retrieval, jointly reporting evidence recall, answer quality and full costs.

Appendix D initially says every entrant was measured body-only, but Table 9 and Section 6 explicitly say three cached models were not; only ten have full format ablations. The primary comparison was not externally preregistered. The stated internal dates, July 18 and panel entry July 22, follow Nemotron’s July 16 release, so before it existed is not supported. Abstract/intro calls the panel vendor-neutral, but Section 3.2 explicitly rejects that description because five of thirteen are NVIDIA models. Appendix Table 5 and Section 3.4 initially imply all thirteen answering runs, while the table explicitly has twelve and excludes NV after correction. The paper’s statement that guessing keeps answer F1 purely evidence-supported is not established: guessing can draw on parametric knowledge; no answer-quality evidence in these cost rows establishes support.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [beir](beir.en.md) · [bright](bright.en.md)
