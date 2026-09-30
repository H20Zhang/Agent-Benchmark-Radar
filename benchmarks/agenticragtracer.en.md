# AgenticRAGTracer: locating failure along the retrieval-reasoning chain

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.19127)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agenticragtracer.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–5, all result and diagnostic analyses; appendices inspected: A–E, examples, prior-benchmark critiques, all construction/evaluation prompts, error traces and human review; visual checks: Figure 2 count labels checked on rendered page 4. Not performed: No rerun, code audit or corpus/index configuration verification

[arXiv v1, 2026-02-22](https://arxiv.org/pdf/2602.19127v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with MultiHop-RAG’s retrieval/generation endpoints, this adds path and step diagnostics for multi-hop processes. It seeks failure localization, while planned depth, executed steps and final correctness remain distinct quantities.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The pipeline samples Wikipedia documents from the FlashRAG collection and removes title overlaps with existing multi-hop benchmarks. GPT-4o-mini generates atomic questions, filtering those answerable without evidence or unsolved even with evidence, then composes sequential-inference and comparison questions of two to four hops. Checks reject intermediate-answer leakage and invalid entity links and test whether removing a supporting document prevents a solution. Three annotators independently decide retain/discard, with Fleiss κ=0.65. Corresponding lower-hop questions and evidence are retained so final failures can be compared with shorter-question performance and actual search steps.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The 1,305 questions comprise comparison two/three/four-hop subsets of 471/182/64 and inference subsets of 393/111/84. Thirteen models use Qwen-Agent/ReAct: first emit a plan, then execute one prompted search step at a time while choosing top-k. EM and F1 score answers; GPT-4o-mini at temperature zero supplies an additional judge score, but conversion from its raw 0/1/2 rubric to table percentages is unclear. Exact retriever/index parameters, dated model snapshots and common absolute token/step caps are not fully specified in the paper. A shared framework does not imply equal evidence or compute.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Answer success by topology and depth

Each EM denominator is the row’s question count and the unit is percent. The Qwen-Agent framework is shared, but model-selected top-k does not guarantee equal retrieved volume.

| GPT-5 subset | Question count | EM percent |
|---|---|---|
| Comparison 2-hop | 471 | 76.2 |
| Comparison 4-hop | 64 | 26.6 |
| Inference 2-hop | 393 | 48.4 |
| Inference 4-hop | 84 | 22.6 |

Source: Table 1; Figure 2 · [Paper](https://arxiv.org/pdf/2602.19127v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Failures can be too long or too short

Eighty-four four-hop inference questions, with mean steps conditioned separately on final success and failure. Column denominators differ, and exact diagnostic group counts are not supplied alongside the table.

| Model | Correct mean steps | Incorrect mean steps |
|---|---|---|
| GPT-5 | 4.48 | 8.25 |
| DeepSeek-R1 | 4.17 | 2.76 |

Source: Table 2, four-hop inference · [Paper](https://arxiv.org/pdf/2602.19127v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

GPT-5 inference EM falls from 48.4% at two hops to 22.6% at four; comparison EM falls from 76.2% to 26.6%, so topology and hop count both matter. Failed trajectories are not uniformly longer: on four-hop inference GPT-5 averages 8.25 steps when wrong versus 4.48 when correct, while DeepSeek-R1 averages 2.76 versus 4.17. These describe both premature termination and over-searching, but outcome-conditioned means do not establish that step-allocation policies cause failure.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Title deduplication does not exclude semantic overlap or pretraining knowledge, and document-removal tests depend on the filtering model rather than proving every agent needs the same hop count. Plan-first and stepwise prompts shape trajectories, while model-selected top-k changes evidence budgets. Next, fix retrieval, visible evidence and compute, compare prompts allowing replanning, annotate actual evidence chains, and publish the MaxD formula and per-question traces to test early-stopping/over-search explanations.

Section 4.5 broadly says failed steps exceed successful steps; Table 2 includes the opposite, such as DeepSeek-R1 four-hop inference 2.76 versus 4.17. Table 2 three-hop comparison and inference Steps-I cells repeat identically across all thirteen models, and many Steps-C cells also repeat. Retain source attribution and request trace-level confirmation before treating this as independent topology evidence. MaxD is described through corresponding lower-hop questions yet some reported means exceed the maximum strictly lower hop count; its exact aggregation is ambiguous and must not be rebranded as an observed trace-prefix success metric. The judge is called near-perfectly aligned on twenty instances per subset but no numerical confusion matrix or confidence interval is supplied. Its 0/1/2 prompt-to-table normalization is also unclear. Several prompt examples contain internal issues, including naming Luigi Nono a painter; successful prompting rules do not prove all generated chains are valid.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [multihop-rag](multihop-rag.en.md) · [searchauditbench](searchauditbench.en.md)
