# MERRIN：先判断需要哪种 modality，再去 noisy web 找证据

**中文** | [English](merrin.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.13418) · [代码](https://github.com/HanNight/MERRIN)

## 它在测什么

MERRIN 有 162 个 human-annotated short-answer questions，答案依赖 image、video、audio、chart 或多模态组合，而且 query 不显式告诉 agent 应搜索哪种 modality。benchmark 比较 no-search、native-search 与 agentic-search，并分析 resource use。

## 相比什么前进了

普通 web-search benchmark 大多是 text-first；multimodal QA 又通常预先给定图像。MERRIN 把 modality inference 放在 retrieval 之前，使“选错搜索媒介”成为独立 failure，而不仅是后续 VLM reasoning 错误。

## 分数边界

short-answer accuracy 支持在当前 live web、search provider 与 multimodal backbone 下的 evidence discovery；它不能稳定代表长期 SOTA，因为 web drift 和 proprietary search interface 会改变候选证据。

## 公平比较条件

锁定 result date、search provider、tool interface、backbone、judge 与 allowed modalities。不同 provider 或 web snapshot 应分 track。

## 下一步评测坐标

下一步需要 citation-level multimodal evidence portfolios 与可重放 snapshots，区分 modality selection、retrieval 与 final reasoning 的贡献。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究系统能否在没有模态提示时主动寻找合适的图像、视频或音频证据。它把‘知道该看什么’放进搜索任务；实时网页与专有搜索接口的差异意味着结果通常先是系统级证据。

### 一个具体任务长什么样

示意任务：文字问题的答案藏在一段视频画面或图表中，普通文本搜索只提供线索。系统需要选择模态、定位相关片段并核对噪声或冲突材料，而不是把搜索摘要当作最终证据。

### 最有判别力的实验

固定多模态骨干和工具，比较自主模态选择、正确模态提示与正确证据给定。记录每种模态的调用与延迟，并保留闭卷条件，区分模态路由、内容理解和参数知识造成的差异。

### 建议搭配

[mc-search](mc-search.md) · [browsecomp](browsecomp.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
