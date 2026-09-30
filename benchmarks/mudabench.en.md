# MuDABench: from finding a few supporting documents to collection-wide extraction and aggregation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-19<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.341/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mudabench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, metric formulas, algorithm, all results and limitations; appendices inspected: A.1–A.8, matched human subset, cases, data/model sources, merger strategy and complete prompts/examples. Not performed: No experiments rerun, no exact evaluation denominator reconstruction from released files

[ACL 2026 Findings, pp. 6877–6898](https://aclanthology.org/2026.findings-acl.341.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike multi-hop QA needing a few supporting passages, MuDABench requires extraction, calculation and aggregation across supplied document collections. It shifts toward collection coverage and computation completeness without testing archive-wide discovery.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

A corpus of 589 Chinese/U.S. annual reports, ESG disclosures and announcements exceeds 80,000 pages. Each analytical question receives five to thirty-eight PDFs, averaging 14.8. Metadata records ticker, fiscal year and document type; experts turn structured financial-database metrics into intermediate natural-language facts and instantiate 332 simple/complex analytical questions. The proposed workflow creates metadata-conditioned per-document question templates, extracts through single-document RAG, normalizes records into a shared flat JSON schema in batches, then generates code to analyze the complete records. It targets filtering, aggregation and cross-year computation over a specified collection rather than retrieving a few snippets.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Standard RAG uses OpenAI File Search and GPT-4o-2024-11-20 with chunk budgets of 1/1.5/2/2.5 times document count, capped at fifty by the API. Workflow planning/code use DeepSeek-R1-0528, normalization V3-0324, and single-document QA mainly GPT-4.1-mini-2025-04-14 with three or five chunks per document. A separate GPT-4o large-chunk setting is not a matched-backbone budget comparison. Temperatures are zero. Kimi K2 handles final/other judgments and DeepSeek-V3.2 aligned-cell judgments. Standard-RAG process scoring takes the minimum of estimated coverage and one minus missing/error rate; workflow process scoring counts correct metric cells in aligned rows. Full accuracy requires both perfect process and correct answer; numerical judgments generally require integer digits and the first decimal place to match.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## More chunks need not improve the final answer

On a 0–1 scale for complex standard-RAG tasks; chunk budget scales with documents per question, capped at fifty. Effective run denominators are not inferred from rounded decimals.

| GPT-4o retrieval budget | Process score | Final accuracy | Full accuracy |
|---|---|---|---|
| 1 × document count | 0.1459 | 0.0482 | 0.0181 |
| 2.5 × document count | 0.2623 | 0.0482 | 0.012 |

Source: Table 2, standard RAG without metadata, Complex · [Paper](https://aclanthology.org/2026.findings-acl.341.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Final-answer comparison on the same human subset

On a 0–1 scale for the matched selected human-evaluation subset in Table 5 only. Two volunteers participate; exact subset and per-row effective counts are not clearly reported. These are not full-332-task human accuracies.

| System | Simple final accuracy | Complex final accuracy |
|---|---|---|
| Workflow GPT-4.1-mini 5 chunks | 0.2 | 0.3333 |
| Human volunteers | 0.8334 | 0.7334 |

Source: Appendix A.1 Table 5 · [Paper](https://aclanthology.org/2026.findings-acl.341.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Extraction is the weak stage in the diagnostic sample

Thirty randomly selected five-chunk workflow examples, with each stage checked independently; this is not the accuracy conditional on all preceding stages being correct.

| Stage | Independent accuracy percent |
|---|---|
| Planning | 90.0 |
| Extraction | 30.0 |
| Code | 93.3 |

Source: Table 4; Section 5.3 · [Paper](https://aclanthology.org/2026.findings-acl.341.pdf)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

More retrieved chunks improve estimated process coverage without reliably improving answers: on complex standard-RAG tasks, increasing from |D| to 2.5|D| raises process score from 0.1459 to 0.2623 while final accuracy stays 0.0482 and full accuracy falls from 0.0181 to 0.0120. Human/workflow comparisons should use the matched-subset Appendix Table 5 rather than subtracting differently scoped main-table results. In thirty diagnostic examples, independent extraction accuracy is 30.0%, below planning’s 90.0% and code’s 93.3%; this is a small-sample diagnostic, not proof that all errors are retrieval errors.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Fact granularity affects process scoring: a growth rate and two yearly values may be equivalent but counted differently, while numeric tolerance is not exact financial verification. Language, document type and length co-vary, so length correlations are not controlled causal effects. Questions come with document collections and do not establish exhaustive selection from a whole enterprise archive. Next, disclose per-run denominators/costs, match backbone and extraction budgets, intervene separately on planning/extraction, and programmatically verify key values and complete lists.

Standard RAG and workflow process scores use different judge protocols and atomic units; they are diagnostic signals rather than directly matched retrieval recall. Per-configuration successful-run denominators are not explicitly listed; displayed workflow percentages cannot simply be assumed to use all 332 questions. Human performance uses a subset; Appendix A.1 provides the appropriate matched workflow comparison, unlike a direct full-main-table human gap. The paper describes public financial documents, but Appendix Table 6 also uses commercial WIND/CSMAR sources for announcements/structured gold data; distinguish public filings from gold-data provenance. Figure 8’s error case asks about 2023 while its restriction shows 2021, in addition to the narrated schema problem; it is not an isolated single-factor schema example.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [t2-ragbench](t2-ragbench.en.md) · [dataspace](dataspace.en.md)
