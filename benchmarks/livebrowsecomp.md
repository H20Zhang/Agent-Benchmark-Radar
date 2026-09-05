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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验模型是否真正依赖近期证据完成搜索，而不是借网页验证已知答案。新鲜度是相对于模型和构建时间的属性；同一静态发布随着时间推移，未必仍然保持最初的低记忆泄露条件。

### 一个具体任务长什么样

示意任务：答案来自构建期前不久发布的一项低显著性事实，系统需要找到具体来源。闭卷答对或移除答案来源后仍答对，会削弱该题对真正证据发现能力的支持。

### 最有判别力的实验

对每个模型重新做闭卷与来源移除对照，按事实日期和来源分项，固定搜索预算。若重新发布题目，应报告题集变化而非把不同快照的绝对分数直接当作模型进步曲线。

### 建议搭配

[browsecomp](browsecomp.md) · [evobrowsecomp](evobrowsecomp.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
