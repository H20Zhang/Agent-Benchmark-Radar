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

## 演化位置

`single-source analytics → heterogeneous evidence workflows → multi-source data-agent orchestration`

它把 data-agent 的评测对象从 query execution 扩成了 evidence orchestration。