# MuDABench：从“找几篇支持文档”推进到 collection-wide extraction + aggregation

**中文** | [English](mudabench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.341/) · [代码](https://github.com/Zhanli-Li/MuDABench)

## 它在测什么

MuDABench 包含 332 个 financial analytical questions，覆盖超过 80K report pages；当前仓库组织 166 simple + 166 complex questions 与 589 source PDFs。任务要求跨大量文档做 extraction、aggregation 与 numerical/code-assisted reasoning，并提供 intermediate-fact coverage 诊断。

## 相比什么前进了

Multi-document QA 常只需两三份 supporting documents。MuDABench 把 candidate collection 扩到真正的 report collection，使系统必须先找到一组分散事实，再进行汇总或计算。

## 分数边界

final accuracy 与 intermediate-fact coverage 支持在当前 document release、PDF extraction 与 harness 下的 collection-scale analysis。annotation 与 document coverage 仍在演化，因此不同 release 的数字必须绑定版本。

## 公平比较条件

锁定 PDF corpus、annotation version、extraction pipeline、retrieval budget、agent harness 与 numerical evaluator。修订 annotation 后不应和旧 snapshot 混排。

## 下一步评测坐标

下一步应评价 evidence completeness 的置信度与 missing-document detection：系统何时知道自己的 collection 不完整，而不是只输出一个数字。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究跨大量文档的抽取与聚合，而不只是找到几篇相关材料。分析型问题需要覆盖应纳入计算的整个集合；高 top-k 相关性可能仍漏掉改变汇总结果的文档。

### 一个具体任务长什么样

示意任务：需要从多份财务报告提取同口径数字，按实体与时期对齐后做计算。单篇报告抽取正确还不够，漏掉一个范围内对象或混入不同口径，就可能得到貌似精确的错误结果。

### 最有判别力的实验

把文档覆盖、字段抽取和最终聚合分别评分，加入完整文档集合给定与正确中间表给定条件。核对标注修订及 PDF 解析版本，判断瓶颈是在发现、解析还是运算，而不是统称为推理失败。

### 建议搭配

[t2-ragbench](t2-ragbench.md) · [dataspace](dataspace.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
