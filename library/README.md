# Benchmark Library

**中文** | [English](README.en.md) · [返回入口](../README.md)

这个 Library 用来回答长期问题：**某个 benchmark 为什么出现、它在批评谁、它把 measurement object 改成了什么。**

## 按 Area 浏览

### Agent Memory

`Multi-Session Chat → LoCoMo / LongMemEval → MemoryAgentBench / BEAM → MemoryArena / Mem2ActBench / LoCoMo-Plus / RealMem`

- **Precursor / Foundation：** Multi-Session Chat、LoCoMo、LongMemEval
- **Transition：** MemBench、MemoryAgentBench、BEAM
- **Frontier：** multimodal / acting / persistent-user-state / project-state benchmarks
- [进入 Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)

### RAG / Agentic Retrieval

`HotpotQA / KILT / BEIR → RGB / RAGTruth / CRAG / BRIGHT → BrowseComp / DeepResearch Bench → SGR-Bench / VAKRA`

- **Foundation：** evidence composition、provenance、cross-domain retrieval
- **Transition：** robustness、faithfulness、reasoning-intensive retrieval、freshness
- **Frontier：** stateful information-environment control、cross-source executable trajectories
- [进入 Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

### Data Agents

`WikiSQL / Spider / DS-1000 → BIRD / MLAgentBench / InsightBench / Spider 2.0 → AgenticDataBench / DataSpace / DSAgentBench`

- **Foundation：** executable NL→SQL / data-science code
- **Transition：** realistic schemas、experimentation、business insight、enterprise workflow
- **Frontier：** heterogeneous workspace、real computer、end-to-end verification
- [进入 Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)

## 按 Genealogy 浏览

Genealogy 不是 prestige ranking，而是回答：**上一代哪里不够，下一代具体多测了哪个 coordinate。**

| Role | 含义 | 读法 |
|---|---|---|
| `precursor` | 引入后来 agent benchmark 继承的 evaluation object | 看“问题最初是怎么被形式化的” |
| `foundation` | 建立长期稳定的 coordinate system | 看“后续工作默认在什么坐标系里比较” |
| `transition` | 显著扩大 realism / capability / protocol | 看“旧 benchmark 哪个限制开始被显式修正” |
| `frontier` | 当前时间点的新 measurement direction | 看“领域正在试图把什么变成可测对象” |

完整结构化记录见 [`data/benchmarks.json`](../data/benchmarks.json)。

## 按 Measurement Coordinate 浏览

- **Capability：** recall、reasoning、action、analysis、tool use、verification
- **Environment：** static corpus、live web、state-gated site、heterogeneous workspace、real computer
- **Protocol：** tool interface、hints、retry、stopping rule、judge、executable validation
- **Validity：** contamination、saturation、judge dependence、harness sensitivity、environment drift
- **Cost：** indexing/writing、retrieval/tool calls、token/latency、retry、controller/evaluator cost
- **Long-horizon state：** memory update、workflow state、persistent user/project state、irreversible actions

## 按年份浏览

Chronology 主要用于 provenance 与 release lookup。对研究理解而言，优先使用上面的 area / genealogy / measurement-coordinate 入口。

- [Research compactions](../digests/README.md)
- [Canonical registry](../data/benchmarks.json)

## 记住一个限制

**Benchmark 能测到什么，不等于什么最重要。** 如果某个重要问题暂时没有干净 benchmark，应把它放进首页的“目前仍然测不好的重要问题”，而不是从 research map 中删除。
