# RAGTruth：把 RAG hallucination 从 answer-level 拉到 word-level

**中文** | [English](ragtruth.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2401.00396)

## 它在测什么

RAGTruth 收集近 18K 条自然生成的 RAG responses，并由人工在 case 与 word level 标注 hallucination 与严重程度。它的测量对象是生成结果相对 retrieved evidence 的局部 grounding failure，而不是只给整段回答一个 faithful/unfaithful 标签。

## 相比什么前进了

早期 hallucination evaluation 常依赖自动 judge 或粗粒度 answer labels。RAGTruth 提供细粒度人工标注，使 detector 可以定位哪一段文字超出了证据，并比较不同领域和 source LLM 的 hallucination pattern。

## 决定性证据与分数边界

它证明“RAG 生成了看似正确的长回答”仍可能包含局部、不同严重度的 unsupported spans。Detector 分数支持 hallucination detection under the annotated distribution；它不衡量 adaptive retrieval policy，也不能把 hallucination 率变化直接归因给 retriever，因为 source LLM 与 retrieval setup 都是 confounders。

## 公平比较条件

锁定 source-response set、annotation policy、severity definition 与 detector input。换一批生成模型或 retrieval setup 后，hallucination distribution 本身就变了，应分 track 报告。

## 下一步评测坐标

下一步要从事后 detector 推进到闭环 correction：检测到 unsupported claim 后，agent 是否能找到缺失证据、修订答案并保留 citation-level trace。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究回答中的局部幻觉检测与忠实性评价。细粒度标注让错误位置可见，但检测器能指出错误，不代表原系统会自动避免或修复错误；检测与生成应保持不同的研究主张。

### 一个具体任务长什么样

示意任务：回答的大部分内容有来源支持，只有一句话或几个词扩大了证据中的结论。整体看起来正确的回答仍需被局部标记；将整段答案只打一个真伪标签会失去这种诊断信息。

### 最有判别力的实验

按未见过的生成模型和领域划分检测测试，分别报告定位与整条回答判别。随后用检测信号驱动修复，并验证修复后的支持关系与内容完整性，防止删除大量内容获得表面更高的忠实性。

### 建议搭配

[ragbench](ragbench.md) · [claimprobe](claimprobe.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
