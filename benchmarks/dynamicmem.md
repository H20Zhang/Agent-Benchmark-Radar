# DynamicMem：2.2M-token 用户轨迹下，memory 的难点变成更新而非单次 recall

**中文** | [English](dynamicmem.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.22877) · [代码](https://github.com/wenyaxie023/DynamicMem)

## 它在测什么

DynamicMem 为每个用户生成 15 个月、平均 2.2M tokens、1,772 个 grounded events、跨 16 apps 的长期活动，并在五个季度 checkpoint 上分别测 State Completion 与 Personalized Service。目标是 profile attributes、habits 与 preferences 是否随生活变化被持续维护和用于服务。

## 相比什么前进了

静态 memory QA 只问某个事实是否存在。DynamicMem 把时间推进和 repeated updates 放到 benchmark core，使“保留稳定事实”和“替换已经变化的状态”必须同时成立。

## 决定性证据与分数边界

论文的 failure attribution 显示超过 93% failures 与 retrieval 相关，同时没有系统同时做好 stable-fact retention 与 changing-fact replacement。这支持 retrieval/update coupling 是当前瓶颈，但仍是 synthetic trajectory 与 reference-profile contract 下的结论，不等于真实用户 deployment。

## 公平比较条件

锁定 trajectory synthesis、app-event schema、profile ground truth、retrieval budget 与 judge，并按季度 checkpoint 报告。最终时点单一分数会掩盖 staleness trajectory。

## 下一步评测坐标

下一步需要真实 consent/permissions、unmodeled behavior，以及错误 profile 驱动 tool actions 后的外部后果。
