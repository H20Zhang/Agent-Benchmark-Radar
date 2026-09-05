# AgentFuel：stateful analysis 的价值要通过跨 query 复用来证明

**中文** | [English](agentfuel.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.12483) · **领域：Data Agent / Stateful Analysis**

AgentFuel 的核心问题非常具体：**Data Agent 在处理一串相关分析问题时，保留前序分析 state 到底有没有用？** 它不是把 memory 当作抽象组件，而是把跨 query 的分析状态复用直接变成实验变量。

## 它到底测什么

AgentFuel 当前包含 **72 个 queries、3 个 time-series domains**，每个领域 24 个问题，其中 12 个 stateless、12 个 stateful / incident-oriented；生成数据约 13.5 MB。

评测会比较两种模式：

- 每个 query 都从零开始；
- agent 可以保留 notebook、context、intermediate findings 或其他 analysis state 继续回答后续问题。

因此它测的不是单次分析能力，而是 **state reuse 是否能降低重复探索并提高后续 incident analysis 的质量**。

## 相比什么前进了

传统 data-agent benchmark 常把每道题视为独立 episode。即使一个系统内部用了 memory，也很难从最终总分判断 memory 是否真正有贡献。

AgentFuel 的前进在于做了更接近因果对照的设计：同类问题在 stateless / stateful 两种条件下运行，把 persistence 从“实现细节”提升成可观测变量。

这使它特别适合回答：

- 前一个 query 的中间结论是否能被后续复用；
- state 是否减少重复数据探索；
- stateful agent 的收益来自记住结果，还是记住分析过程；
- incident analysis 是否随着历史积累变得更快或更准。

## 实际怎样评测

解释一个 AgentFuel 结果时，必须同时记录 query order、state persistence policy、data generator、agent scaffold、模型、token / tool budget 和 evaluator。

尤其 **query order 是 protocol 的一部分**。如果后续问题天然依赖前一个问题，顺序变化会改变 state 的价值；如果 agent 可以把几乎全部历史原样保留，那么收益又可能退化成 context carry-over，而不是更有结构的 memory。

因此最好报告 matched stateless/stateful pairs，而不是只给一个聚合总分。

## 分数能说明什么

如果 stateful 条件稳定优于 stateless，可以支持：在当前 synthetic time-series 分布、query sequence 和 harness 下，**跨 query 保存分析状态具有实用价值**。

但这个结果还不能证明系统学到了“semantic memory”或“workflow experience”。增益可能来自：

- 缓存已经计算过的数值；
- 直接保留 notebook cell；
- 复用前一轮生成文本；
- 真正抽象出了可复用的数据语义或分析策略。

这些机制的研究意义完全不同，最终总分本身无法区分。

## 最主要的混杂因素

第一是 **cache vs. memory**：如果 stateful agent 只是避免重复计算，那么它证明的是 computation reuse，而不是更强的长期记忆。

第二是 **state freshness**。当前 setting 更偏向状态持续有用的顺序任务；真实生产分析里数据会更新、假设会被推翻、incident 会关闭，旧 state 可能变成负资产。

第三是复现边界：如果完整数据生成或环境实现不完全公开，那么不同实现得到的 difficulty 可能不一致。

## 公平比较条件

至少需要对齐：

- query sequence 与 matched pair；
- 什么 state 可以跨 query 保留；
- state 容量、压缩和清理策略；
- data snapshot / generator；
- model、agent harness 与工具集合；
- retry、token 和执行预算；
- evaluator 与失败处理。

如果某个方法额外获得了完整历史，而另一个只允许结构化 state，两者不能被当成同一 track。

## 还没有覆盖什么

AgentFuel 目前还没有充分回答：

- cache、structured semantic state 与 learned workflow experience 各自贡献多少；
- 数据更新后 stale state 会不会伤害结果；
- 长时间累积后 state 是否膨胀、污染或相互矛盾；
- agent 何时应该主动忘记或重建 state；
- state reuse 带来的 latency / token / storage 节省是否值得维护成本。

## 下一步最有判别力的验证

最值得做的是一个 **state intervention matrix**：同一组连续 queries 分别只允许 raw cache、structured semantic state、workflow summary 和 full history，并加入数据更新或假设反转。

如果 structured state 在 freshness challenge 下仍优于 raw history / cache，才能更有力地证明“representation 本身”而不仅是“多保留一点上下文”带来了增益。

## 演化位置

`独立 data query → 跨 query state reuse → 可更新、可忘记的长期 analytic state`

AgentFuel 处在中间一步：它把 statefulness 变成了可测量对象，但还没有完全进入动态、长期、自我修正的分析 memory。
