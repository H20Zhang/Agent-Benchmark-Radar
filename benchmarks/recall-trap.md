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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验检索指标能否真实预测下游代码修复，而不是寻找一个普遍‘召回越低越好’的结论。上下文打包同时改变广度、深度、位置和干扰时，观测到的效果属于复合处理，需要进一步拆分。

### 一个具体任务长什么样

示意任务：固定数量的代码上下文槽位，可以放入更多文件的浅片段，也可以保留少数文件的深片段。文件召回增加时，关键函数的上下文可能被压缩，最终修复反而更难。

### 最有判别力的实验

独立控制文件广度、每文件深度、顺序和总 token，使用同一修复模型及隐藏执行测试。按仓库配对统计结果，并加入有工具的修复流程，检验现象是否只在单次、无工具的固定打包协议中出现。

### 建议搭配

[beir](beir.md) · [browsecomp-plus](browsecomp-plus.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
