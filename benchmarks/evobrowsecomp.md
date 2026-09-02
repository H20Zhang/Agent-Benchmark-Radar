# EvoBrowseComp：如果 benchmark 会过时，就把 regeneration pipeline 也做成 benchmark infrastructure

**中文** | [English](evobrowsecomp.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.13120) · [数据](https://huggingface.co/datasets/Krystalan/EvoBrowseComp)

## 它在测什么

EvoBrowseComp 当前发布 800 个 complex live-web questions：400 English、400 Chinese，由 multi-agent web traversal、synthesis 与 filtering pipeline 自动生成，并设计为可周期 regeneration。它评价 bilingual agentic web search 与 reasoning-graph following。

## 相比什么前进了

LiveBrowseComp 通过手工 recent facts 提升 freshness，但维护成本高。EvoBrowseComp 把“如何持续生成新问题”纳入 benchmark design，目标是让 evaluation 本身随 web 演化。

## 分数边界

一个 snapshot 的 short-answer score 只支持该 generation/filter/judge pipeline 与 web date 下的表现。自动 regeneration 不保证跨版本 difficulty 等价，因此不同 generations 不应直接画成 progress curve，除非先做 calibration。

## 公平比较条件

锁定 snapshot、generation/filter models、judge、language、search provider 与 tool interface。EN/ZH 与不同 regeneration versions 应分 track。

## 下一步评测坐标

最重要的是建立 cross-generation calibration：证明新一代 benchmark 变新了，而不是仅变难/变易或更像生成模型的风格。
