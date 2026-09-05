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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究增量写入、更新和选择性遗忘，而不是只评估一个静态向量库。关键实验单位应是持续吸收信息的记忆系统；一次性把全部历史重新建立索引，会改变所要证明的在线能力。

### 一个具体任务长什么样

示意任务：信息按多轮输入逐步到达，系统先保存事实，再遇到修订或需要遗忘的内容，之后回答依赖当前记忆的问题。观察点既包括最终答案，也包括历史信息进入、保留与退出记忆的过程。

### 最有判别力的实验

保留相同输入顺序，对比增量维护与每轮全量重建，并计入两者全部写入计算。再在固定回答模型下替换写入或遗忘机制，检查收益是否跨四类能力保持，而不是以遗忘能力下降换取检索分数。

### 建议搭配

[longmemeval](longmemeval.md) · [memevobench](memevobench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
