# DI-Bench: generating benchmarks for rule-grounded retrieval and computation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-04<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.05776)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](di-bench-data-intelligence.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all nineteen pages of v1, its limitations and Appendices A–L, including rule generation, graph sampling, validation prompt, human audit, ablations, all cases and pipeline pseudocode; visually checked Figure 2 and Tables 5, 11 and 13.

[arXiv 2609.05776v1 · 2026-09-04](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DI-Bench is both a benchmark-generation method and a fixed task collection. A typed dependency graph links tables, metrics, rule documents and dimensions: schema/metric edges are extracted directly, while DeepSeek V3.2 identifies rule effects. Metric-centered subgraphs are selected using quality scores and Jaccard-distance MMR, with augmentation for rare task types. Reference answers come from SQL templates, human-verified rule modifications and analysis-specific post-processing; a model then generates questions backward, followed by programmatic filters and eight-dimensional LLM quality screening. The 731 tasks span nine analysis types, with 449 Brazilian e-commerce and 282 Czech banking tasks. Relational data are public, but each domain’s twenty-nine metrics and seventeen rule documents are synthetic, not actual enterprise policies.

[Source](https://arxiv.org/pdf/2609.05776v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: BIRD supplies knowledge that can assist SQL; DI-Bench explicitly retrieves rules from a separate corpus and applies them to computation, with a graph-based regeneration pipeline. It adds retrieval-to-rule-compilation coordination. Synthetic rules and the noted necessity-check conflict limit extrapolation to real enterprise knowledge governance.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Agents use native Amazon Bedrock Converse tool calls for SQL and knowledge retrieval, with schemas in the system prompt, at most twenty turns per task, temperature zero and 4,096 maximum output tokens. Answers are matched to execution-grounded references under task-specific tolerances without partial reasoning credit; knowledge tasks use their expected text or required information, while rankings and multi-row answers require complete matches. DeepSeek V3.2 screens task quality rather than judging main agent answers. Knowledge, Knowledge + Analytics and Knowledge + Analytics + Rule groups contain 137, 419 and 175 structurally different tasks. The matched ablation fixes metrics, dimensions, time windows, analysis types and answer formats while comparing retrieved rules, directly supplied rules and removal of rule adjustments. Repeated-run intervals and a complete numeric-tolerance specification are absent.

[Source](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected full-set accuracy and call counts

449 e-commerce and 282 banking tasks, totaling 731; three selected rows from the four-model experiment. Shared tool protocol, at most twenty turns, temperature zero and 4,096 maximum output tokens; call count is not latency or monetary cost.

| Model | E-commerce accuracy (%) | Banking accuracy (%) | Overall accuracy (%) | Mean model calls/task |
| --- | --- | --- | --- | --- |
| Claude Opus 4.6 | 59.2 | 55.7 | 57.9 | 5.5 |
| DeepSeek V3.2 | 56.1 | 42.6 | 50.9 | 11.5 |
| Qwen3-80B | 53.0 | 39.7 | 47.9 | 5.2 |

Source location: Table 3 and Section 4.1, p. 6 · [Source](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Matched rule ablation: supplying a rule versus removing its adjustment

Matched variants of the same 175 rule tasks, fixing metric, slice, time window, analysis type and answer format; aggregate averages four models. The no-rule condition uses the corresponding standard metric and reference, not a retrieval ablation against an unchanged target answer. Percentages are retained without inferring integer correct-task counts.

| Model or aggregate | Retrieve/apply rule (%) | Oracle rule (%) | No rule adjustment (%) |
| --- | --- | --- | --- |
| Claude Opus 4.6 | 35.0 | 37.3 | 53.6 |
| DeepSeek V3.2 | 34.0 | 31.4 | 54.3 |
| Four-model average | 32.5 | 32.7 | 52.9 |

Source location: Table 5 and Section 5, p. 7 · [Source](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Whether a paired rule actually changes the computed answer

175 rule tasks pooled across both domains; fixed task skeletons with rules re-paired and queries re-executed. Semantic and Random choose other rules. This measures pairing validity, not agent accuracy; the discrepancy with Figure 3’s strict retention claim remains unresolved.

| Pairing method | Answer-changing pairings (%) |
| --- | --- |
| Graph | 82 |
| Semantic | 29 |
| Random | 22 |

Source location: Appendix C, Table 8, pp. 11–12; contrast Figure 3, p. 19 · [Source](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The approximately 82%→50%→32% cross-group decline combines different task structures and does not alone identify a retrieval effect. In the matched ablation, the four-model average moves from 32.5% with rules to 32.7% with oracle access and 52.9% without rule adjustments, locating a bottleneck beyond retrieval hits for these synthetic tasks. Execution ensures agreement with specified SQL, not automatically correct rule encoding. Shared generation and validation models can introduce bias; generator swaps and four-judge sensitivity checks reduce but do not eliminate that concern. The two-expert reference reports thirteen correct tasks out of fifteen, a small sample. The reduction from roughly 420 to 22 human construction hours is an author estimate, not a controlled timing experiment.

Table 8 reports answer-changing rules for only 82% of the same 175 rule tasks, whereas Figure 3 says every rule-bearing task with an unchanged answer is rejected; this boundary is unexplained, so universal rule necessity is not established. Figure 2 gives DeepSeek/Qwen rule-group scores of 33/30%, while Table 5 gives 34.0/31.0%; this note retains Table 5 for the matched ablation. Table 11’s 99% is a dimension-averaged audit of twenty-five admitted tasks, not correctness over all 731; its Scope=99% also cannot be directly reconstructed from binary counts over twenty-five tasks. Case 2 describes suppressing fewer-than-three-seller results yet expects several HHI=1 categories, requiring inspection of the underlying rule and reference SQL.

First reconcile the 175 tasks’ base/rule SQL, answer changes and labels with the 82% validity result and stronger filtering claim. Then freeze tasks over authorized real business documents, independently audit rule compilation, match retrieval/SQL budgets and repeat runs. Report retrieval recall, correct rule application and final-answer accuracy separately, with complete tolerances and per-task evidence.

[Source](https://arxiv.org/pdf/2609.05776v1)
<!-- EVIDENCE:limitations:END -->
