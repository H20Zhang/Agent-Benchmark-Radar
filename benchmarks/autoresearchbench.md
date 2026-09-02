# AutoResearchBench：literature search 必须同时测 target finding 与 unknown-size set discovery

**中文** | [English](autoresearchbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.25256) · [代码](https://github.com/CherYou/AutoResearchBench)

## 它在测什么

AutoResearchBench 有 1,000 个 queries、覆盖 8 个 computer-science areas，其中 600 个 Deep Research tasks 要找一个 target paper，400 个 Wide Research tasks 要搜集未知大小的相关论文集合；搜索环境是超过 3M full-text papers 的 DeepXiv fixed corpus。

## 相比什么前进了

known-item search 的停止条件很简单：找到目标即可。Wide Research 的核心难点是 gold set 大小未知，agent 必须在 recall 与 search cost 之间决定何时停止，因此 search stopping 本身成为 evaluation object。

## 分数边界

Deep accuracy、Wide IoU/recall 支持固定 CS corpus 下的 targeted/exhaustive search。wide gold set 仍可能不完整，且固定 DeepXiv 不覆盖 paywalls、live scholarly APIs 与跨领域 literature drift。

## 公平比较条件

锁定 corpus snapshot、gold-set version、search/index backend、agent harness 与 budget，并分别报告 Deep/Wide tracks。

## 下一步评测坐标

下一步应引入 gold-set uncertainty 与 marginal-value stopping：再多搜一次究竟发现多少新高价值 evidence，而不是把不完整 gold set 当绝对真值。
