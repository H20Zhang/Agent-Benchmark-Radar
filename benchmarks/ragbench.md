# RAGBench：不只评 RAG，也评“评 RAG 的 evaluator”

**中文** | [English](ragbench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.11005) · [数据](https://huggingface.co/datasets/rungalileo/ragbench)

## 它到底测什么

RAGBench 是覆盖 5 个 industry-oriented domain、约 100K example 的 **RAG quality + RAG evaluator** benchmark。TRACe 不只给一个最终分数，而是提供可解释、可行动的 failure label。

## 相比此前评测多测了什么

如果 evaluator 无法区分 retrieval/context defect 与 answer defect，RAG pipeline 就很难有针对性优化。RAGBench 把一部分评测对象从“哪个 RAG 系统赢”转成“负责判分的 evaluator 是否真的识别了失败类型”。

## 决定性证据

数据覆盖多类 RAG task 与 user manual 等 industry corpus。论文发现，通用 LLM-based evaluator 在这个 RAG evaluation task 上甚至可能不如 finetuned RoBERTa，说明 evaluator 看起来更强大，不等于 measurement validity 更强。

## 这个分数能证明什么

RAGBench 能支持其 annotation scheme 下 evaluator quality 与 RAG failure dimension 的判断，但不能证明 adaptive retrieval policy；任何由 evaluator 排出来的系统 leaderboard，也会继承 evaluator 自身的 bias。

## 公平比较契约

应固定 labeled split、evaluator prompt/model/version、threshold 与被评估的 RAG output，并在用 evaluator 排系统之前先报告 agreement/calibration。human label 的不确定性也不应被 aggregate metric 隐藏。

## 还没有测什么

静态 label 不覆盖 live-web drift、iterative tool use、budget allocation 或 stopping；所谓 actionable label 只有在它真的能指导 intervention 并改善 end-to-end behavior 时才有意义。

## 下一步最有判别力的验证

针对每种 diagnostic label 自动触发一种 pipeline intervention，再验证预测的 failure class 是否真的改善，把 explainability 从描述性 taxonomy 变成因果上有用的诊断。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合评价 RAG 评分器与失败诊断，而不只是再给 RAG 系统算一个答案分。评价器和被评价系统属于不同对象；一个自动指标与标注更一致，并不直接证明用它优化后的系统更好。

### 一个具体任务长什么样

示意任务：给定问题、检索上下文和生成答案，评价器需要判断证据是否相关、回答是否忠实以及失败发生在哪一侧。答案看似流畅，仍可能缺少支持；检索正确，也可能在生成时引入新错误。

### 最有判别力的实验

在独立领域的人工标签上比较评价器，并检查错误类型而非只看总体相关系数。再用不同评价器选择系统版本，观察排序是否在独立人工审查中保持；这比只拟合已有标签更接近评价器的实际价值。

### 建议搭配

[ragtruth](ragtruth.md) · [claimprobe](claimprobe.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`RAG output score → failure labels → evaluator validity and actionable diagnosis`

它的重要性在于：benchmark/evaluator 本身也成为 RAG 系统研究对象。