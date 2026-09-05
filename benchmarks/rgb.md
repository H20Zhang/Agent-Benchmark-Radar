# RGB：把 RAG 的“会不会用 context”拆成四种 failure modes

**中文** | [English](rgb.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2309.01431)

## 它在测什么

RGB 用中英文四组 diagnostic testbeds 分别检查 noise robustness、negative rejection、information integration 与 counterfactual robustness。它不问 retriever 找得多准，而是把 retrieved context 已经给到 generator 后，模型是否能正确使用、拒绝或整合这些证据。

## 相比什么前进了

普通 RAG benchmark 常把 retrieval 与 generation 压成一个 final-answer score。RGB 把 generator 对 context 的处理能力独立出来，使“检索到了但没用对”“没有答案却硬答”“多证据无法整合”等失败可以被区分。

## 决定性证据与分数边界

论文显示当 context 含噪、缺证据或存在 counterfactual information 时，主流 LLM 的行为明显不稳定。这个结论支持 RAG 需要 context-use diagnostics；它不能说明某个 retriever 更好，因为 evaluation 直接控制了 supplied context。不同 prompt 和 generator 的分数也不能归因给 retrieval。

## 公平比较条件

必须锁定 generator、prompt、constructed negatives/counterfactuals 与每个 diagnostic split。四种能力不应随意压成一个 SOTA 总分，否则会掩盖能力间的 trade-off。

## 下一步评测坐标

下一步要把这些 context-use failures 接回真实 retrieval loop：观察 agent 是否能发现证据冲突、主动补搜并在工具预算内恢复，而不只是被动读取固定 context。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合隔离生成器如何使用给定证据，尤其是噪声、反事实与不可回答情形。它不是检索器评测；如果把更好的上下文直接交给模型，所得提升不能用来证明搜索策略更好。

### 一个具体任务长什么样

示意任务：同一问题搭配正确、混有干扰、缺乏答案或与参数知识冲突的上下文，要求模型据证据回答。系统需要识别哪些材料值得采用，以及什么时候应该拒绝给出未经支持的答案。

### 最有判别力的实验

对同一生成器改变上下文条件，按四类能力分别报告，并把固定上下文诊断与真实检索端到端测试分开。尤其检查模型是否过度相信检索文本或完全忽略文本，避免只提高一个方向的鲁棒性。

### 建议搭配

[ragtruth](ragtruth.md) · [lit-ragbench](lit-ragbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
