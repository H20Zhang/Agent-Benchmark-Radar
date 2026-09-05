# T²-RAGBench：text-table financial QA 在拿掉 oracle context 后才真正变成 RAG

**中文** | [English](t2-ragbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.eacl-long.8/) · [代码](https://github.com/uhh-hcds/g4kmu-paper)

## 它在测什么

当前 T²-RAGBench release 含 23,088 个 question-context-answer triples，覆盖 7,318 份 financial reports，来源于 FinQA、ConvFinQA first turn 与 TAT-DQA；最初 paper 报告 32,908，后续移除 VQAonBD。benchmark 同时测 text/table retrieval MRR@3 与 numerical answer，并提供 oracle-context upper bound。

## 相比什么前进了

原 financial QA dataset 通常直接给出正确 context，无法评价 retrieval。T²-RAGBench 去掉 oracle evidence，把 end-to-end text-table retrieval 与 numerical reasoning 接起来，并保留 oracle baseline 来定位 retrieval loss。

## 分数边界

retrieval MRR 与 numerical accuracy 支持当前 dataset/version、serialization 与 reader 下的表现；release 已发生样本组成变化，因此 paper 初版与 current artifact 不是同一 track。

## 公平比较条件

锁定 dataset version、document serialization、chunk/index pipeline、reader 与 corpus-size setting，并显式区分 oracle-context 与 retrieved-context。

## 下一步评测坐标

下一步应覆盖更长 financial collections、cross-report aggregation 与 provenance，评价数字答案是否由完整证据链支持。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究真实文本与表格文档中的检索加数值推理。把已知正确上下文拿走，是它区别于纯表格问答的关键；文档序列化和解析也可能决定结果，不能把全部误差都归到语言推理。

### 一个具体任务长什么样

示意任务：问题不指明报告位置，系统需找到对应报告与表格，再理解行列语义并执行计算。检索到正确文件但未保留表头或单位，仍可能得到数量级错误的答案。

### 最有判别力的实验

固定数据发布版本，对比完整检索、正确文档给定与正确表格给定，分别测检索和数值答案。扫描语料规模时保持题目一致，并明确是否采用已移除的数据来源，避免版本不同却直接比较。

### 建议搭配

[mudabench](mudabench.md) · [lit-ragbench](lit-ragbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
