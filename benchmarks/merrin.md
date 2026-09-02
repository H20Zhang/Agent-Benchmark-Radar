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
