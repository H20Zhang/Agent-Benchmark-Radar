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

## 演化位置

`RAG output score → failure labels → evaluator validity and actionable diagnosis`

它的重要性在于：benchmark/evaluator 本身也成为 RAG 系统研究对象。