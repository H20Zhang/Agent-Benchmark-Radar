# Choose evaluations by research question

[Back to the main README](../README.en.md#evaluation-recipes) · [中文](evaluation-recipes.md)

These suites are editorial suggestions, not automatic evidence for a claim. Core and Complement have different roles. Changing the selection or protocol requires revalidating the supported claim.

<!-- EVALUATION-RECIPES:START -->

<a id="recipe-memory"></a>
## Agent Memory

| Research question | Core | Complement | Claim boundary and next validation |
|---|---|---|---|
| **Long-term conversational memory and temporal reasoning** | [LoCoMo](../benchmarks/locomo.en.md) | [LongMemEval](../benchmarks/longmemeval.en.md) | Supports system-level claims about recall, integration, and temporal reasoning over long conversations.<br>Next: Pair with action-oriented evaluation to measure how retained experience improves future action. |
| **State update and stale-information handling** | [StateMemBench](../benchmarks/statemembench.en.md) | [LongMemEval](../benchmarks/longmemeval.en.md) · [membench (staleness)](../benchmarks/membench-staleness.en.md) | Supports system-level claims about state revision and preservation of current state.<br>Next: Use component-level ablations to attribute gains to write, update, and retrieval. |
| **Memory improves later action** | [MemoryArena](../benchmarks/memoryarena.en.md) | [PAST-Bench](../benchmarks/past-bench.en.md) · [Mem2ActBench](../benchmarks/mem2actbench.en.md) | Supports claims that memory creates action utility in later executable tasks.<br>Next: Validate general memory quality over broad personal long-term histories. |
| **Multimodal long-term memory** | [MemEye](../benchmarks/memeye.en.md) | [Mem-Gallery](../benchmarks/mem-gallery.en.md) · [WorldMemArena](../benchmarks/worldmemarena.en.md) | Supports claims about visual evidence recall, temporal state integration, and multimodal memory use.<br>Next: Add lifecycle coverage for access control, poisoning, and compaction. |
| **Memory security and lifecycle governance** | [InjecMEM](../benchmarks/injecmem.en.md) | [Utility Under Attack](../benchmarks/utility-under-attack.en.md) · [GateMem](../benchmarks/gatemem.en.md) · [The Compaction Cliff](../benchmarks/compaction-cliff.en.md) | Supports system-level claims about persistent-memory write, retrieval, authority, and compaction integrity.<br>Next: Pair with general utility, recall, and reasoning evaluation. |

<a id="recipe-rag"></a>
## RAG / Agentic Retrieval

| Research question | Core | Complement | Claim boundary and next validation |
|---|---|---|---|
| **Reasoning-intensive retrieval quality** | [BRIGHT](../benchmarks/bright.en.md) | [BEIR](../benchmarks/beir.en.md) · [Bright-Pro](../benchmarks/bright-pro.en.md) | Supports retrieval claims where relevance depends on reasoning about the information need.<br>Next: Pair with live, iterative web-search evaluation. |
| **Deep / long-horizon web search** | [BrowseComp](../benchmarks/browsecomp.en.md) | [LiveBrowseComp](../benchmarks/livebrowsecomp.en.md) · [LoHoSearch](../benchmarks/lohosearch.en.md) | Supports claims about evidence discovery and final-answer quality in long-horizon web search.<br>Next: Add trajectory-level diagnostics to localize key failure stages. |
| **Search-trajectory diagnosis and tool policy** | [SearchAuditBench](../benchmarks/searchauditbench.en.md) | [AgenticRAGTracer](../benchmarks/agenticragtracer.en.md) · [VAKRA](../benchmarks/vakra.en.md) | Supports claims about localization, attribution, repair, and tool policy in search trajectories.<br>Next: Add broad live-web retrieval and corpus-robustness evaluation. |
| **Dynamic, writable, feedback-forming corpora** | [KBGym / Training a Knowledge Base](../benchmarks/kbgym.en.md) | [Snapshot Compatibility Audit](../benchmarks/snapshot-compatibility-audit.en.md) · [RAG Collapse](../benchmarks/rag-collapse.en.md) | Supports claims about knowledge-base editing, version changes, and recursive feedback effects.<br>Next: Pair with conventional retrieval-quality evaluation on a static corpus. |
| **Multimodal search and visual-document retrieval** | [VisDocAgentBench](../benchmarks/visdocagentbench.en.md) | [MC-Search](../benchmarks/mc-search.en.md) · [MERRIN](../benchmarks/merrin.en.md) | Supports claims about page-level visual evidence discovery, modality choice, and multi-hop retrieval.<br>Next: Stratify results by modality and tool interface to produce comparable headline scores. |

<a id="recipe-data"></a>
## Data Agents

| Research question | Core | Complement | Claim boundary and next validation |
|---|---|---|---|
| **Text-to-SQL / warehouse task capability** | [Spider 2.0](../benchmarks/spider-2.en.md) | [Spider](../benchmarks/spider.en.md) · [WarehouseReliabilityBench](../benchmarks/warehouse-reliability-bench.en.md) | Supports claims about SQL generation and execution correctness in complex database environments.<br>Next: Extend evaluation to the full data-understanding, analysis, and delivery workflow. |
| **End-to-end data-science agent** | [DataSpace](../benchmarks/dataspace.en.md) | [DSAgentBench](../benchmarks/dsagentbench.en.md) · [DataClawBench](../benchmarks/dataclawbench.en.md) | Supports end-to-end system claims across tools, heterogeneous data, and complete deliverables.<br>Next: Use component-level evaluation to validate statistical and modeling quality. |
| **Data understanding and autonomous exploration** | [Data Exploration Benchmark](../benchmarks/data-exploration-benchmark.en.md) | [DataClawBench](../benchmarks/dataclawbench.en.md) · [AgenticDataBench](../benchmarks/agenticdatabench.en.md) | Supports claims about structural discovery, semantic understanding, and autonomous exploration.<br>Next: Pair with downstream model, causal, and business-decision quality evaluation. |
| **Statistical and causal analysis** | [CausalDS](../benchmarks/causalds.en.md) | [StatABench](../benchmarks/statabench.en.md) | Supports claims about statistical modeling, causal identification, effect estimation, and uncertainty handling.<br>Next: Extend evaluation to real warehouse, repository, and data-engineering constraints. |
| **Long-horizon ML engineering / research improvement** | [MLE-bench](../benchmarks/mle-bench.en.md) | [DeltaML-Bench](../benchmarks/deltaml-bench.en.md) · [AI4AI-Bench](../benchmarks/ai4ai-bench.en.md) | Supports claims about long-horizon experimentation, repair, and verifiable improvement in real training repositories.<br>Next: Pair with BI, warehouse-semantics, and general analytics evaluation. |

<!-- EVALUATION-RECIPES:END -->
