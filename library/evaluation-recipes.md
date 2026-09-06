# 按研究问题选评测

[返回主入口](../README.md#evaluation-recipes) · [English](evaluation-recipes.en.md)

这些组合是编辑建议，不自动证明某个研究主张。Core 是核心评测，Complement 是补充评测；更换组合或协议后需重新核验支持范围。

<!-- EVALUATION-RECIPES:START -->

<a id="recipe-memory"></a>
## Agent Memory

| 研究问题 | 核心（Core） | 补充（Complement） | 支持范围与下一步 |
|---|---|---|---|
| **长期对话记忆与时间推理** | [LoCoMo](../benchmarks/locomo.md) | [LongMemEval](../benchmarks/longmemeval.md) | 支持长程对话中的召回、整合与时间推理系统级判断。<br>下一步：结合行动导向评测，验证历史经验对后续行动的改善。 |
| **状态更新与过期信息处理** | [StateMemBench](../benchmarks/statemembench.md) | [LongMemEval](../benchmarks/longmemeval.md) · [membench (staleness)](../benchmarks/membench-staleness.md) | 支持多轮状态修订和当前状态保持的系统级判断。<br>下一步：通过组件级消融定位 write、update 与 retrieval 的贡献。 |
| **记忆改善后续行动** | [MemoryArena](../benchmarks/memoryarena.md) | [PAST-Bench](../benchmarks/past-bench.md) · [Mem2ActBench](../benchmarks/mem2actbench.md) | 支持记忆在后续可执行任务中产生行动效用的判断。<br>下一步：在大规模个人长期历史上验证通用 memory quality。 |
| **多模态长期记忆** | [MemEye](../benchmarks/memeye.md) | [Mem-Gallery](../benchmarks/mem-gallery.md) · [WorldMemArena](../benchmarks/worldmemarena.md) | 支持视觉证据召回、跨时刻状态整合与多模态记忆使用的判断。<br>下一步：补充权限、污染与压缩等完整 memory lifecycle 评测。 |
| **Memory 安全与生命周期治理** | [InjecMEM](../benchmarks/injecmem.md) | [Utility Under Attack](../benchmarks/utility-under-attack.md) · [GateMem](../benchmarks/gatemem.md) · [The Compaction Cliff](../benchmarks/compaction-cliff.md) | 支持持久记忆写入、检索、授权与压缩完整性的系统级判断。<br>下一步：结合一般 utility、recall 与 reasoning 评测。 |

<a id="recipe-rag"></a>
## RAG / Agentic Retrieval

| 研究问题 | 核心（Core） | 补充（Complement） | 支持范围与下一步 |
|---|---|---|---|
| **推理密集型 Retrieval 质量** | [BRIGHT](../benchmarks/bright.md) | [BEIR](../benchmarks/beir.md) · [Bright-Pro](../benchmarks/bright-pro.md) | 支持需要先理解问题再识别相关文档的检索质量判断。<br>下一步：结合 live、迭代式 web search 评测。 |
| **Deep / long-horizon web search** | [BrowseComp](../benchmarks/browsecomp.md) | [LiveBrowseComp](../benchmarks/livebrowsecomp.md) · [LoHoSearch](../benchmarks/lohosearch.md) | 支持长时程网页搜索中的证据发现与最终回答能力判断。<br>下一步：加入轨迹级诊断，定位搜索过程中的关键失效阶段。 |
| **搜索轨迹诊断与工具策略** | [SearchAuditBench](../benchmarks/searchauditbench.md) | [AgenticRAGTracer](../benchmarks/agenticragtracer.md) · [VAKRA](../benchmarks/vakra.md) | 支持搜索轨迹中的定位、归因、修复与工具策略判断。<br>下一步：补充广覆盖 live-web retrieval 与 corpus robustness 评测。 |
| **动态、可写、会反馈的语料** | [KBGym / Training a Knowledge Base](../benchmarks/kbgym.md) | [Snapshot Compatibility Audit](../benchmarks/snapshot-compatibility-audit.md) · [RAG Collapse](../benchmarks/rag-collapse.md) | 支持知识库写入、版本变化和递归反馈影响的判断。<br>下一步：结合传统静态 corpus 上的 retrieval-quality 评测。 |
| **多模态搜索与视觉文档 Retrieval** | [VisDocAgentBench](../benchmarks/visdocagentbench.md) | [MC-Search](../benchmarks/mc-search.md) · [MERRIN](../benchmarks/merrin.md) | 支持页面级视觉证据发现、模态选择与多跳检索判断。<br>下一步：按 modality 与 tool interface 分层报告，建立可比的 headline score。 |

<a id="recipe-data"></a>
## Data Agents

| 研究问题 | 核心（Core） | 补充（Complement） | 支持范围与下一步 |
|---|---|---|---|
| **Text-to-SQL / Warehouse 任务能力** | [Spider 2.0](../benchmarks/spider-2.md) | [Spider](../benchmarks/spider.md) · [WarehouseReliabilityBench](../benchmarks/warehouse-reliability-bench.md) | 支持复杂数据库环境中的 SQL 生成与执行正确性判断。<br>下一步：扩展到完整的数据理解、分析与交付工作流。 |
| **端到端 Data Science Agent** | [DataSpace](../benchmarks/dataspace.md) | [DSAgentBench](../benchmarks/dsagentbench.md) · [DataClawBench](../benchmarks/dataclawbench.md) | 支持跨工具、多源数据和完整交付物的端到端系统能力判断。<br>下一步：通过组件级评测验证统计建模质量。 |
| **数据理解与自主探索** | [Data Exploration Benchmark](../benchmarks/data-exploration-benchmark.md) | [DataClawBench](../benchmarks/dataclawbench.md) · [AgenticDataBench](../benchmarks/agenticdatabench.md) | 支持数据结构发现、语义理解与自主探索过程的判断。<br>下一步：结合下游模型、因果结论与业务决策质量评测。 |
| **统计与因果分析** | [CausalDS](../benchmarks/causalds.md) | [StatABench](../benchmarks/statabench.md) | 支持统计建模、因果识别、效应估计与不确定性处理判断。<br>下一步：扩展到真实 warehouse、repo 与数据工程约束。 |
| **长时程 ML Engineering / Research Improvement** | [MLE-bench](../benchmarks/mle-bench.md) | [DeltaML-Bench](../benchmarks/deltaml-bench.md) · [AI4AI-Bench](../benchmarks/ai4ai-bench.md) | 支持真实训练仓库中的长时程实验、修复与可核验改进判断。<br>下一步：结合 BI、warehouse semantics 与一般数据分析能力评测。 |

<!-- EVALUATION-RECIPES:END -->
