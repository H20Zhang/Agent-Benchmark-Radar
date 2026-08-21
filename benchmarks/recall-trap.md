# The Recall Trap：RAG / retrieval validity

**中文** | [English](recall-trap.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.14838) · [复现实验](https://doi.org/10.5281/zenodo.21879550)

用 downstream executable outcome 审计“更高 recall 就更好”的 proxy 假设。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 在固定 context slots 下，提高 file recall 是否真的提高 issue resolution？

**测量对象：** 有效性审计：在固定槽位代码检索协议下，更高 file recall 可能降低下游修复成功率。

**规模与协议：** Paired fixed-pack evaluations on SWE-bench Verified with an open-weight preregistered replication. 协议包括 paired-dedup-ablation, official-docker-grading, repository-clustered-inference。

## 分数能说明什么

paired fixed-pack evaluation 与 official Docker grading 显示 dense retrieval 的 higher recall 可对应 lower resolve rate，并有 open-weight replication。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

compound dedup treatment 同时改变 breadth、depth、rank、position、tokens 与 distractors；结论只适用于 fixed slots。 关键混杂包括 compound-packing-treatment, fixed-slot-context, single-shot-no-tools-harness。

## 还没有覆盖什么

dedup 开关在 single-shot、无工具 harness 中同时改变 breadth、depth、rank、position、token 数和 distractor。

## 放进演化图怎么看

`map_delta=reinforces`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。
