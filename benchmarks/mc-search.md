# MC-Search：multimodal agentic RAG 需要同时测 planning、modality choice 与每一 hop evidence

**中文** | [English](mc-search.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.00873) · [代码](https://github.com/YennNing/MC-Search)

## 它在测什么

MC-Search 包含 3,333 个 tasks、平均约 3.7 hops、五种 reasoning topologies，并为每一步标注 subquestion、retrieval modality、supporting evidence 与 intermediate answer。paper 描述的 KB 含约 389,750 张图片和 784,473 段文本；当前 released artifact 规模更小，因此 artifact version 本身需要记录。

## 相比什么前进了

普通 multimodal QA 只看最终答案；普通 agentic search 又常缺 gold trajectory。MC-Search 提供 hop-level retrieval、planning accuracy、gold-evidence answering 与 rollout deviation，使 over/under-retrieval、modality error 和 chain drift 可分开。

## 分数边界

高 planning/retrieval score 支持和 benchmark gold trajectory 的一致性，但 single-gold trajectory 可能惩罚其他有效路径。paper/released artifact 的 KB scale mismatch 也意味着结果必须绑定具体 version，不能混成一个 leaderboard。

## 公平比较条件

锁定 KB artifact、multimodal backbone、hop budget、judge 与 trajectory policy。gold-evidence 与 free-search conditions 应独立 track。

## 下一步评测坐标

下一步要允许 multiple valid trajectories，并将 modality choice 与真实 latency/cost 及 final evidence sufficiency 联合评价。
