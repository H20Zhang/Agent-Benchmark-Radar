# CausalDS：Data Science Agent 不应把 correlation、intervention 与 counterfactual 混成一种分析

**中文** | [English](causalds.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.08093) · [代码](https://github.com/andleb/causalds)

## 它在测什么

CausalDS 从 sampled structural causal models 生成 observational data 与 graph-faithful realistic stories，再导出 Pearl 三个 rungs 的任务：prediction/association、causal structure/identification/effect estimation，以及 counterfactual/mediation 等。frozen main exam 有 100 tasks，并将无可识别答案时的 abstention 设为一等结果；大多数任务还需要 coding/tool use。

## 相比什么前进了

传统 causal benchmark 偏 symbolic；传统 data-science benchmark 又常没有 principled causal ground truth。CausalDS 用 hidden SCM 同时提供 executable data work 与精确 causal truth，使“算得出来”和“因果上有资格回答”可以分开。

## 分数边界

CausalDSScore/accuracy 支持在 synthetic SCM generator、observation model 与 frozen exam 下的 causal data-science competence；它不证明真实领域因果假设正确，因为真实世界最大难点往往是 model specification 本身。

## 公平比较条件

锁定 main exam/ablation config、public/private boundary、observation variant、tool/runtime、agent budget 与 grader。clean/noisy/proxy observations 必须分开。

## 下一步评测坐标

下一步应加入 imperfect causal assumptions、human domain constraints 与 experimental intervention cost，测试 agent 能否质疑 SCM，而不仅是在已定义 SCM 内推理。
