# MEMLENS：长 context 与 external memory 的 multimodal trade-off

**中文** | [English](memlens.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.14906) · [代码](https://github.com/xrenaf/MEMLENS)

## 它在测什么

MEMLENS 有 789 个问题、4,695 张 unique images，并把 context 控制在 32K/64K/128K/256K；memory agents 使用固定 195-question subset。它比较 native long-context VLM 与 external-memory agents 在 visual memory、multi-session/temporal reasoning、update 与 abstention 上的退化。

## 相比什么前进了

单纯扩 context 与先压缩入 memory 代表两种不同策略。MEMLENS 通过 controlled length scaling 与 visual-necessity ablation 直接观察：native model 的 length degradation 与 external memory 的 visual-fidelity loss 是不同瓶颈。

## 决定性证据与分数边界

实验显示移除 evidence images 会让若干 frontier VLM 在大量 visual-dependent questions 上接近失效，多 session reasoning 也仍是明显弱项。结果支持视觉证据在 storage-time compression 中不可随意丢失；但 memory-agent subset 与 full long-context set 不相同，不能混成统一 leaderboard。

## 公平比较条件

锁定 context length、question subset、multimodal backbone、memory adapter/compression、answerer 与 judge；195-subset 与 789-full-set 必须独立 track。

## 下一步评测坐标

下一步要同时度量视觉 fidelity、memory bytes/cost 与后续 action success，而不只 QA。
