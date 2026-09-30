# AutoResearchBench: literature search needs both target finding and unknown-size set discovery

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-04 · paper v1<br>
> **Claude-Opus-4.6 / ReAct — Deep Research accuracy: 9.39%**; **Gemini-3.1-Pro-Preview / ReAct — Wide Research IoU: 9.31%**<br>
> Subtask bests within the controlled ReAct comparison of Table 2; excludes 50-question end-to-end-system tests and distinguishes IoU from accuracy. [Original source](https://arxiv.org/html/2604.25256v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](autoresearchbench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–5, construction, metrics, experiments and analysis; appendices inspected: A–G, limitations, statistics, verification, runtime/tool details, results, errors and both full system prompts/case traces. Not performed: No code/data audit, rerun or resolution of task-denominator and verification inconsistencies

[arXiv v1, 2026-04-28](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Like SAGE’s target/open-set distinction, AutoResearchBench adds adversarial difficulty filtering, no-answer cases and set IoU to emphasize exact constraints and extra-paper penalties. It stresses scholarly retrieval while compressed tool evidence and denominator gaps constrain interpretation.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Over more than three million arXiv papers accessible through DeepXiv, the benchmark constructs 600 Deep and 400 Wide queries. Deep tasks identify one paper through full-text details, citation relations and lexical obfuscation; sixty no-answer cases perturb a core constraint. Questions easily solved by GPT-5.4 query rewrites, Sonnet/Flash agents or ten-minute human searches are removed. Wide tasks derive conjunctive conditions from topical candidates, expand them and audit full texts, yielding two to thirty-four gold papers per query, averaging 9.23. Deep accuracy requires exact predicted/gold set equality; Wide averages per-query intersection-over-union, penalizing omissions and extra papers.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The main ReAct loop exposes only search: at most thirty turns, a 110,000-token soft context budget, 4,096 new tokens per completion, temperature 0.6 and ten papers per default call, via official APIs or SGLang. Although DeepXiv stores full text, the agent sees search_evidence compressed by an auxiliary LLM from the first available body-section snippet; no separate full-paper open tool is exposed. Errors and context/turn caps terminate runs. End-to-end products use a separate random fifty-query sample. Repeated sampling reports Deep pass@k and Wide oracle best@k; the latter is not deployable gold-free selection.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Reported main-track scores and cost

Nominally 600 Deep and 400 Wide queries; effective Deep denominators remain unresolved and values are attributed to the table. Time is mean seconds per query; IoU is mean per-query set overlap×100. The search-only ReAct interface is shared but model reasoning implementations differ.

| Model | Deep accuracy percent | Deep seconds | Wide IoU percent | Wide seconds |
|---|---|---|---|---|
| GPT-5.4 | 7.44 | 72.5 | 8.12 | 115.98 |
| Gemini-3.1-Pro-Preview | 7.93 | 1221.4 | 9.31 | 235.3 |

Source: Table 2; Appendix Tables 8–9 · [Paper](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Literature-search backend swap within one framework

Same ReAct and nominal 600/400 tasks, with the Deep denominator gap noted above. Units are percentages and calls per query. Jina open-web search is arXiv-biased; DeepXiv indexing and evidence presentation differ.

| Gemini-3.1-Pro backend | Deep accuracy percent | Wide IoU percent | Wide calls |
|---|---|---|---|
| Open web | 6.82 | 7.37 | 2.92 |
| DeepXiv | 7.93 | 9.31 | 3.49 |

Source: Table 3 · [Paper](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Results must be scoped to interfaces and samples. In the main ReAct track, Opus reports 9.39% Deep accuracy and Gemini-Pro 9.31% Wide IoU, while GPT Deep Research answers eleven of fifty in a separate product sample. Not every system is below ten percent. With ten percent empty-gold Deep tasks and exact set matching, an always-empty predictor would score ten percent under the stated formula. The paper does not report that baseline or resolve effective denominators, so the “best only 9.39%” interpretation needs this caveat. Full-text-detail tasks paired with compressed-snippet access also prevent attributing low scores solely to scientific reasoning.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Model/human difficulty filtering deliberately selects adversarial tasks rather than a representative distribution of literature requests. Finite searches cannot formally prove absence or exhaustive sets. The audit claiming 96% invalid extra predictions omits its sample size and does not guarantee gold completeness. Auxiliary summarization, candidate accumulation and temporal corpus boundaries affect scores. Next, publish per-question denominators, an empty-set baseline and the actual verification protocol, add matched-budget full-paper reading, and have humans review valid unlisted papers.

Nominal Deep count is 600 with 60 no-answer tasks; several main accuracies including 9.39% do not fit a single 600-question binary average. Effective counts, exclusions or repeated-run aggregation are unspecified. The always-empty baseline would be 10% if the stated set metric includes all 600. Main Section 2.2.2 says newly admitted Wide papers require unanimous three-model consensus and meticulous final human audit; Appendix D.2 says majority vote, fifty-percent human sampling and a 75% precision threshold. These are materially different verification protocols. Wide supplementation statistics use 704 queries/4,887 passing papers, while the final benchmark has 400 queries/3,692 gold papers; transition/filtering details are not fully reconciled. Sonnet Wide IoU is 5.83% in Table 2 but 4.96% in Appendix Table 9; DeepSeek non-thinking Wide is 7.70% in Table 2 and 5.96% in Table 4. Appendix error analysis calls Claude Opus 4.5 while main experiments name 4.6; do not transfer exact error percentages across versions. The related-work claim that SAGE lacks an interactive agent environment conflicts with SAGE’s explicit DR Tulu MCP experiments.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [sage](sage.en.md) · [scholarquest](scholarquest.en.md)
