# MemoryAgentBench：把 static long context 改造成 incremental memory agent

**中文** | [English](memoryagentbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2507.05257) · [代码](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

## 它在测什么

MemoryAgentBench 把长期信息以 multi-turn 方式增量喂给 agent，并把 memory 拆成 accurate retrieval、test-time learning、long-range understanding 与 selective forgetting 四个 competencies。核心变化是系统必须在信息逐步到来时形成 memory，而不是只面对一个已经准备好的超长 prompt。

## 相比什么前进了

LoCoMo/LongMemEval 主要把长期历史作为 QA 输入；MemoryAgentBench 明确把“memory agent”本身设为评测对象，并让 forgetting 与 learning 进入同一套框架。这样可以看到一个系统可能很会 retrieval，却在冲突更新或 selective forgetting 上失效，而不再用单一总分掩盖能力不对称。

## 决定性证据与分数边界

论文对从 full-context/RAG 到外部 memory 与 tool-augmented agents 的多类方法进行统一评测，结论是当前方法没有同时掌握四种能力。官方数据在 2025 年还移除了部分低效、高成本样本并修订若干字段，说明 dataset revision 会改变可比性。一个高分支持的是“在该 competency、该数据版本与 grader 下表现好”，不能直接推出 memory architecture 普遍更优。

## 公平比较条件

必须对齐 dataset revision、answerer、embedding/retrieval model、memory harness、ingestion 过程和 grader。尤其不能把一个更强 reader 或更大的 retrieval budget 带来的收益归因给 memory mechanism。

## 下一步评测坐标

四能力分解仍主要以回答问题为结果。下一步应直接测 memory 是否改善之后的 planning/action，并记录 write、consolidation、forgetting 的成本与错误传播。
