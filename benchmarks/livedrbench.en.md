# LiveDRBench: separating broad claim discovery from report writing

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-08-06 · paper v1<br>
> **OpenAI deep research — Overall F1: 0.55**<br>
> Best deep-research system in the initial experiment, scoring structured claim discovery across 100 tasks, not report style. [Original source](https://arxiv.org/abs/2508.04183v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](livedrbench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, formal definition, construction, claim metrics, experiments and trace analysis; appendices inspected: A–D, every task example, agreement/trace prompts and author-rejudged results. Not performed: No execution or code audit; commercial internal budgets and versions remain opaque

[arXiv v1, 2025-08-06](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with DeepResearch Bench’s long-report evaluation, LiveDRBench constrains outputs to structured claims and subclaims. It isolates evidence discovery and field extraction while not directly assessing free-form report organization.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The hundred tasks span eight categories: materials 17, geoscience 19, novel-dataset identification 6, identification/extraction 11, peer-dataset retrieval 3, prior art 17, entity enumeration 20 and flight investigations 7. Papers, reviews and investigation reports are inverted into search-and-reasoning requests whose nested JSON answers contain top-level claims and supporting subclaims. Standard precision/recall combine top-level agreement with recursive subclaim credit before computing per-query F1. Finding the paper while extracting the wrong material therefore receives less credit. A strict worst-subclaim variant is defined but not used in the main results. Authors inspect all systems’ outputs and enrich gold answers with valid omissions before rescoring; this improves coverage without proving web-wide exhaustiveness.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The three Deep Research systems run manually through chat interfaces, with a fixed proceed response to clarification questions. Search-enabled baselines use APIs: o4-mini at low effort, Sonar reasoning at medium and Gemini 2.5 Pro with 128 thinking tokens, described as roughly thirty seconds. OpenAI/Perplexity search context is medium; other parameters default. These are not compute-matched DR comparisons. GPT-4o judges claim agreement. NovelDS/Flights first align dictionaries by primary keys, then grade each field from zero to three, allowing one-percent numeric error. Some Gemini prose reports are manually parsed into JSON. F1 is calculated per question and averaged, not recomputed from aggregate precision/recall. Appendix D repeats scoring with author judgments without reporting independent blinded annotation or an agreement coefficient.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Overall scores under two aggregations

One hundred tasks and eight categories; all metrics are on zero-to-one scales, higher is better. GPT-4o judges agreement. Count weighting corresponds to a query average; macro averaging weights categories equally. Commercial DR budgets are opaque and unmatched.

| System | Weighted precision | Weighted recall | Weighted F1 | Category macro F1 |
|---|---|---|---|---|
| OpenAI Deep Research | 0.629 | 0.519 | 0.55 | 0.555 |
| Perplexity Deep Research | 0.462 | 0.286 | 0.331 | 0.355 |
| Gemini Deep Research 2.5 Pro | 0.309 | 0.215 | 0.236 | 0.263 |

Source: Table 2; Section 5.2 · [Paper](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Category structure and author rejudgment

Materials has seventeen tasks and geoscience nineteen; the final columns are eight-category macro averages over one hundred tasks, on zero-to-one scales. Materials requires nested extraction unlike geoscience, so cross-category gaps do not isolate retrieval ability. Independent annotation agreement is not reported for author rejudgment.

| System | Materials F1 GPT-4o | Geoscience F1 GPT-4o | Macro F1 GPT-4o | Macro F1 authors |
|---|---|---|---|---|
| OpenAI Deep Research | 0.314 | 0.721 | 0.555 | 0.556 |
| Perplexity Deep Research | 0.15 | 0.186 | 0.355 | 0.361 |
| Gemini Deep Research 2.5 Pro | 0.022 | 0.316 | 0.263 | 0.261 |

Source: Table 2; Appendix D Table 11 · [Paper](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Question-count-weighted F1 is 0.550, 0.331 and 0.236, whereas equal-category macro F1 is 0.555, 0.355 and 0.263; the aggregations must remain separate. On materials, OpenAI’s paper-title F1 is 0.735 and material-name F1 0.504, but joint F1 is only 0.314, illustrating why isolated field retrieval does not establish a correct evidence chain. Author rejudgment preserves the macro ranking without establishing unbiased grading for all future systems. F1 per source or backtrack is a behavioral proxy, not dollar, latency or token efficiency.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Category sizes are small and uneven, with only three peer-retrieval questions; differing answer nesting also changes scoring difficulty. Authors construct and rejudge the benchmark, and gold enrichment depends on answers discovered by tested systems. Opaque commercial interfaces lack reproducible internal versions, tools and compute budgets, so these historical results are not current product rankings. Public summarized traces are not complete internal reasoning, and branch/backtrack associations are not causal evidence. “Live” describes refreshable construction, whose ongoing update history was not verified here. Next, fix versions/budgets, preregister independent human judges, release per-question outputs and gold additions, and test sensitivity to field-match strictness and missing sources.

Section 4.2.1 says 31 SciFacts tasks, but Table 1 lists 17 materials plus 19 geoscience, totaling 36 and making the full benchmark total 100. Materials prose gives Perplexity joint F1 0.158 and Gemini 0.023, whereas Table 2 gives 0.150 and 0.022; retain table-specific attribution. Appendix B permits CNN and ResNet as equivalent strings, a broad semantic matching example that may erase meaningful specificity. The author-rejudged results in Table 11 are an alternative judgment condition, not corrections to be substituted silently into GPT-4o Table 2.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [deepresearch-bench](deepresearch-bench.en.md) · [claimprobe](claimprobe.en.md) · [mr-lhdr](mr-lhdr.en.md)
