# VisDocAgentBench: evidence-directed retrieval across visual document pages

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-18<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.17889)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](visdocagentbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all thirty pages and Appendices A–H, including path construction, full-document review, tool/ranking protocols, resources, stratified results, complete success/failure traces and licensing; visually checked Tables 3 and 5 and Figure 3. No experiment rerun or independent audit of the hundred source papers.

[arXiv 2608.17889v1 · 2026-08-18](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

One hundred 2026 papers, ten per topic, yield 2375 rendered pages; 2324 content pages support construction. GPT-5.5 extracts query anchors, hidden semantic bridges and visual-target descriptors. Embedding candidates plus VLM verification connect pages into direct, one-bridge and two-bridge paths. One author and a separate AI review 1522 paths in full-document context; both scores must reach 60/100. The final set has forty queries per level and 120 unique targets. Queries expose relations but hide bridge identities, titles, page numbers and exact captions. An example follows a task failure into its broader taxonomy before locating a yellow-labeled page bearing the related error name. Appearance-only matching can retrieve a plausible wrong page. Full-document checks and top-ten hard-negative review reduce ambiguity without exhaustively labeling the entire corpus.

Editorial placement: compared with page retrieval in MMDocIR/IRPAPERS and final QA in ViDoRAG, the added coordinate is a common ranked-page endpoint for static rankers and iterative agents, with latent paths and discovery/examination/ranking separated. It connects visual-document retrieval with agentic search, but six cross-document paths cannot establish a mature large-scale cross-document measure.

[Source](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Static rankers order all pages once. Agents receive twelve one-action steps and, if needed, one ranking-only final call. Visual search uses Qwen3-VL-Embedding-8B; OCR search embeds PaddleOCR-VL-1.6 output with Qwen3-Embedding-8B. Both can inspect up to ten pages per batch and crop them. Searches expose opaque handles/scores without snippets or document identity. Final lists contain up to ten distinct discovered pages, exactly ten when enough are available. R@1 is the query fraction ranking the unique target first; R@10 measures top-ten inclusion and MRR@10 averages truncated reciprocal rank. Invalid outputs score zero; rationales are not graded. Supported planners use medium effort; open Qwen3.5-397B-A17B runs BF16 on sixteen A100 GPUs with thinking on/off.

[Source](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## From direct matching to two-bridge retrieval

Overall n=120; L1/L3 each n=40. Nemotron uses one-shot static MaxSim; the other rows are twelve-step agents over a shared visual index, not compute-matched systems. Higher rank-one accuracy does not imply higher top-ten coverage than every static ranker.

| Visual retrieval system | Overall R@1 (%) | L1 R@1 (%) | L3 R@1 (%) | Overall R@10 (%) |
| --- | --- | --- | --- | --- |
| Nemotron ColEmbed | 40.00 | 97.50 | 2.50 | 70.00 |
| GPT-5.6-sol | 61.67 | 85.00 | 40.00 | 68.33 |
| Claude Opus 5 | 67.50 | 92.50 | 47.50 | 75.00 |

Source location: Tables 3 and 12, PDF pp. 9,23 · [Source](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Support pages improve coverage while ranking losses remain

Same forty L3 queries, corpus and twelve-step tool budget; intervention prepends all gold support pages without role labels. R@10 rises 22.50 pp while R@1 rises 5.00 pp, separating coverage from final ranking rather than measuring answer accuracy.

| GPT-5.6-sol / visual L3 condition | R@1 (%) | R@10 (%) | MRR@10 (%) |
| --- | --- | --- | --- |
| Standard | 40.00 | 52.50 | 43.36 |
| Support provided | 45.00 | 75.00 | 55.19 |

Source location: Table 5, PDF p. 11 · [Source](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Visual retrieval consistently beats the OCR index within planners, supporting the value of discovery representation, but embedding models differ and not every visual tool helps. Agent gains over static/fixed-candidate ranking include extra inference/input costs. Removing crops raises visual R@1 from 61.67 to 64.17, contradicting any blanket all-tools-help reading. Gold supports improve retrieval but do not guarantee correct ranking. Only 120 English scientific queries, author-led construction, absent repeat-run intervals and six cross-document cases limit transfer. Source licenses may require local page reconstruction; annotation licensing does not authorize redistribution of all underlying papers.

OCR-Text describes corpus-wide search representation: both agent routes can inspect page images and crops, so this is not a pure text-only versus visual-model experiment. Figure 3 is conditional on prior discovery/examination: its final OCR count of forty-two is not the forty-four rank-one successes over all 120 queries in Table 3. Support-provided initialization gives gold support observations upfront; equal action counts do not mean equal information or token budgets. Retrieval uses defaults, but complete closed-model temperatures, output limits and repeat-run uncertainty are not reported.

Match planner, actual token/image budget and candidate exposure while comparing visual, OCR and hybrid indices. Separately measure not-discovered, discovered-but-unexamined, and examined-but-misranked targets; add equal-information non-gold controls to support initialization. Expand cross-document, form and multilingual cases and report repeated-seed paired intervals before claiming robust path reasoning.

[Source](https://arxiv.org/pdf/2608.17889v1)
<!-- EVIDENCE:limitations:END -->
