# BrowseComp：把 web search 的 persistence 与 creativity 拉到极限

**中文** | [English](browsecomp.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[官方说明](https://openai.com/index/browsecomp/) · [代码](https://github.com/openai/simple-evals)

## 它在测什么

BrowseComp 有 1,266 个短答案、可验证但极难找到的 web questions。成功通常需要持续 browsing、query reformulation、跨页面追踪和寻找非显然 source，因此它比普通 factual QA 更直接测 information-seeking persistence。

## 相比什么前进了

HotpotQA 等 benchmark 固定 corpus 和 evidence；BrowseComp 把环境换成 live web，让“找到哪里搜、怎么继续搜”成为主要难点。代价是 search provider、web drift 与 tool interface 也进入 benchmark contract。

## 决定性证据与当前成绩

OpenAI 原始评测报告 Deep Research 51.5%、o1 无浏览 9.9%、GPT-4o browsing 1.9% 等，说明强 browsing agent 与纯 parametric answering 存在巨大差距。网页 result track 保留这组 2025-04-10 官方 snapshot；它不与后续不同 search provider、tool budget 或 BrowseComp-derived variants 混排。原始发布还明确指出 Deep Research 曾用 BrowseComp-style data 训练，因此 leakage/benchmark familiarity 是重要解释变量。

## 公平比较条件

锁定题集版本、搜索提供方、browser/tool interface、tool-call budget、knowledge cutoff 与 evaluator。live-web time drift 意味着 result date 必须和 score 一起保存。

## 下一步评测坐标

BrowseComp 的短答案无法评价 citation quality、evidence portfolio 与长文 synthesis；BrowseComp-Plus 等工作随后用 fixed corpus 来换取 attribution 与 reproducibility。
