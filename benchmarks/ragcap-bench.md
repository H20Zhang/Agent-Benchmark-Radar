# RAGCap-Bench：end-to-end score 之前，先问 agentic RAG 的中间能力到底会不会

**中文** | [English](ragcap-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2510.13910)

## 它在测什么

RAGCap-Bench 从 agentic-RAG workflow 中反复出现的任务与 failure patterns 抽取 targeted capability tests，例如 retrieval planning 与 intermediate reasoning。它的目的不是重新造一个大而全的 final-answer benchmark，而是把 black-box failure 拆成可单独测试的中间能力。

## 相比什么前进了

传统 RAG benchmark 看到 end-to-end accuracy 下降时，很难判断问题是 retrieval、planning 还是 reasoning。RAGCap-Bench 的增量是让 capability decomposition 本身成为 evaluation layer，从而可以在系统实验前先建立局部能力画像。

## 分数边界

capability score 只支持模型在该 isolated task/prompt harness 上掌握某项能力；它只有在能预测 matched end-to-end system behavior 时才具有系统意义。一个模型在 isolated planning task 上高分，不代表它在真实 tool budget、error propagation 与 stopping pressure 下仍会规划正确。

## 公平比较条件

锁定 capability definition、prompt harness、backbone 与 resource budget，并在可能时报告 capability→system transfer correlation，而不是只排名局部准确率。

## 下一步评测坐标

下一步最重要的是建立 intervention validity：针对某个低 capability 做定向增强后，真实 agentic-RAG trajectory 是否按预测改善。
