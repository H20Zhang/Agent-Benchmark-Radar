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
