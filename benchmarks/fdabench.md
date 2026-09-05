# FDABench：在异构 evidence 上做完整分析的数据 agent

**中文** | [English](fdabench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://fdabench.github.io/)

## 它到底测什么

FDABench 评估 data agent 能否在 **异构 evidence** 上完成 analytical query：结构化数据库、文档、web、图片、视频、音频都可能参与，并要求 planning、tool use、reflection 或 multi-agent workflow，而不是一次 SQL/code 调用。

## 相比此前评测多测了什么

Text-to-SQL / notebook benchmark 通常只有一种主数据模态。FDABench 把 source selection 与 cross-modal evidence composition 放进 analytical workflow，并同时看最终结果与 reasoning trace。

## 决定性证据

benchmark 有 2,007 个任务、50+ domain、3 类 task type 与多种 heterogeneous source；评测包含 choice correctness、rubric report、DAG trace metric、latency 和 token cost，因此 workflow structure 与资源消耗也成为可见结果。

## 这个分数能证明什么

它能支持给定 scaffold 下 multi-source analytical agent 的 end-to-end 能力，但任务广并不等于能做 component attribution；planning、retrieval、multimodal perception、tool execution 与 backbone 都可能造成差异。

## 公平比较契约

应固定可访问 source、model、toolset、agent scaffold、latency/token budget 与 evaluator，并把 deterministic choice 与 rubric report 分开；否则更昂贵的 scaffold 可以仅靠更多探索取得优势。

## 还没有测什么

task-local data 仍避开 enterprise longitudinal change、permission、write、collaboration 与 semantic definition 演化；report judge 也带来 evaluator dependence。

## 下一步最有判别力的验证

为同一 analytical question 构造 single-source / heterogeneous paired version，再对 source routing 做 intervention，量化真正来自 cross-source integration 的难度，而不是泛化的 reasoning difficulty。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究跨结构化、文档和多模态来源的分析工作流。它把数据获取、工具使用和报告放在一起，但异构任务的统一总分容易掩盖失败位置；应同时保留正确性、报告质量与资源成本。

### 一个具体任务长什么样

示意任务：分析请求需要同时查看表格、文档和媒体材料，系统规划访问顺序并形成结论。缺少一类来源可能导致片面报告；报告写得完整，也不保证支撑结论的计算和证据都正确。

### 最有判别力的实验

固定工具与骨干，按来源组合和任务类型拆分，并用正确来源集合给定条件定位发现瓶颈。把选择题、报告评分和轨迹指标分别展示，计入多模态解析成本，避免通过更昂贵的输入处理获得不透明优势。

### 建议搭配

[dataspace](dataspace.md) · [kramabench](kramabench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-source analytics → heterogeneous evidence workflows → multi-source data-agent orchestration`

它把 data-agent 的评测对象从 query execution 扩成了 evidence orchestration。