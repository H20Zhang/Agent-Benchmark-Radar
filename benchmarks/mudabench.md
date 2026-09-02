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
