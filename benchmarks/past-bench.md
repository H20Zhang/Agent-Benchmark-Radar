# PAST-Bench：Agent Memory / 跨 episode 因果归因

**中文** | [English](past-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.04003) · [代码](https://github.com/Gen-Verse/PAST-Bench)

从可见历史问答转向 persistence 是否因果改善后续 executable task。

## 它接在什么之后

前一代评价通常把该问题压成较短的最终分数或单一 proxy。这个评测把 predecessor critique 变成 capability × environment × protocol 的显式差异，并保留可执行或可复核资产。

## 实际怎样评测

**问题：** 清空上下文后，保留的 state 是否真正造成后续任务收益？

**测量对象：** 通过配对持久状态控制，检验跨 episode 经验是否因果改善后续可执行工作的基准。

**规模与协议：** 26 task families and 204 executable episodes with paired persistence controls. 协议包括 persistence-on-off-pairs, matched-seeds-prompts-graders, artifact-and-trace-evidence。

## 分数能说明什么

26 families、204 episodes 使用 persistence on/off、matched seeds/prompts/graders 与 artifact/trace evidence。 它支持的是该环境、harness、model/tool/resource configuration 下的 system-level evidence；除非其他变量匹配，否则不能把榜单差异归因给单一组件。

## 最主要的混杂因素

generated tasks 与 closely related graders 可能产生 model-family template familiarity；也未覆盖 months-long deployment。 关键混杂包括 task-generator-model-family, grader-coupling, tool-harness。

## 还没有覆盖什么

生成式任务和评判器可能偏向同源前沿编码模型的模板，也没有覆盖数月级部署。

## 放进演化图怎么看

`map_delta=early_signal`。一篇论文只是一项 signal；持久方向判断必须由绑定同一 canonical direction key 的独立记录支撑。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合为‘跨任务持久状态带来收益’提供配对因果证据。重点不是系统能保存文件，而是相同后续任务在保留与不保留先前状态时是否改变结果；生成任务上的结论仍需受任务分布限制。

### 一个具体任务长什么样

示意任务：前一回合产生可复用经验，新智能体会话处理相关任务。两组拥有相同提示、种子和评分器，唯一关键区别是是否能读取先前状态，因此可以直接观察持久化的净效果。

### 最有判别力的实验

保留持久状态开关的配对设计，再加入等长度无关状态与原始轨迹两组。报告配对差值、任务族分布和全周期成本；只有在控制额外文本与计算后仍有效，才支持经验内容本身的贡献。

### 建议搭配

[memoryarena](memoryarena.md) · [agent-memory-bench-coding](agent-memory-bench-coding.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
