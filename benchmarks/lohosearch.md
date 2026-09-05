# LoHoSearch：控制 search-space size 与 constraint-graph complexity，而不是只说“这题很难”

**中文** | [English](lohosearch.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.12837) · [数据](https://huggingface.co/datasets/meituan-longcat/LoHoSearch)

## 它在测什么

LoHoSearch 含 544 个 human-verified questions、11 个 domains，分成 282 个 tree-structured 与 262 个 graph-structured tasks，源自超过 7M Wikipedia entities 的 knowledge graph。它显式控制 candidate search-space size 与 structural constraint complexity，并评价 long-context search 与 calibration。

## 相比什么前进了

很多 deep-search benchmark 的难度来自 annotator intuition。LoHoSearch 用结构化生成把“候选空间有多大、约束图有多复杂”变成可观测变量，使 long-horizon context management 的难度更容易分层比较。

## 分数边界

dual-judge accuracy 与 calibration 支持在 Wikipedia-derived search space、指定 provider/tool 下的 long-horizon constraint reasoning；synthetic question generation 和 live search provider 仍影响外部有效性。

## 公平比较条件

锁定 tree/graph slice、search provider、tool interface、context window、judge 与 search budget，并单独报告 calibration。

## 下一步评测坐标

下一步应将结构难度与真实用户 query distribution 对齐，验证 controlled complexity 是否预测自然搜索任务中的资源消耗与失败概率。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究大候选空间和复杂约束图带来的长程搜索压力。调用轨迹长不等于问题重要，搜索成功也不保证置信度可靠；应同时检查候选排除效率、上下文管理和最终判断的校准。

### 一个具体任务长什么样

示意任务：多个条件共同确定目标，任何单一条件都会产生大量候选。系统需要维持已验证与未验证约束，并逐步排除候选；遗忘一个早期限制可能让后续搜索围绕错误对象展开。

### 最有判别力的实验

在树状与图状任务中分别固定总工具预算，比较无压缩、摘要压缩与显式候选状态。报告完成率、约束覆盖和置信度校准，并分析失败是否因证据缺失还是早期有效约束被遗忘。

### 建议搭配

[browsecomp](browsecomp.md) · [compaction-cliff](compaction-cliff.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
