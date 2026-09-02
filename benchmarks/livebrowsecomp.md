# LiveBrowseComp：用最近 90 天的低显著性事实减少“模型本来就知道”

**中文** | [English](livebrowsecomp.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.28721) · [数据](https://huggingface.co/datasets/Forival/LiveBrowseComp)

## 它在测什么

LiveBrowseComp 有 335 个 human-authored questions，基于 benchmark 构建前 90 天内、来自六类持续更新 sources 的低显著性事实。protocol 包含 closed-book diagnostic、agentic web search 与 answer-source-removal ablation，试图区分“模型已知后去 web 验证”和“真正发现新 evidence”。

## 相比什么前进了

BrowseComp 很难，但随着训练和传播可能逐渐进入模型参数。LiveBrowseComp 把 freshness 与 intrinsic-knowledge diagnosis 作为显式变量，让 knowledge cutoff 与 evidence discovery 更容易区分。

## 分数边界

short-answer accuracy 支持某个 dated web snapshot 与 model cutoff 下的 fresh retrieval；benchmark 本身快速老化，因此 current score 必须带 result date，不能长期冻结为 SOTA。

## 公平比较条件

锁定 benchmark snapshot、search provider、tool interface、model cutoff 与 source-removal protocol。不同日期结果需要独立 tracking。

## 下一步评测坐标

下一步应建立连续 refresh lineage：同一 search agent 在多期 fresh snapshots 上是否稳定，而不是只在某一批 recent facts 上表现好。
