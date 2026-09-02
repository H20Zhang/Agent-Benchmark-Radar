# ImplicitMemBench：memory 不一定被“问出来”，也可能自动改变第一反应

**中文** | [English](implicitmembench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.acl-long.1301/) · [代码](https://github.com/qinchonghanzuibang/ImplicitMemBench)

## 它在测什么

ImplicitMemBench 有 300 items，均分到 procedural memory、priming 与 classical conditioning，覆盖 18 个 task families。`learning → interference → test` 协议只看 first attempt，检查之前经验是否会自动改变行为，而不是显式提示“请回忆”。

## 相比什么前进了

多数 agent memory benchmark 属于 declarative recall：query 明确指向过去信息。ImplicitMemBench 把非 declarative memory 作为独立对象，使程序、启动效应和条件关联能在没有 recall request 时被观察。

## 分数边界

paired priming controls 可以支持 prior experience 对第一行为产生影响，但 short in-context episodes 仍可能由 recency/ICL 解释，不能证明 durable external memory。不同 backbone 的 susceptibility 也会显著变化。

## 公平比较条件

锁定 learning/interference/test ordering、first-attempt rule、answerer、judge 与 context placement，并保留 paired control，而不是只看 treatment accuracy。

## 下一步评测坐标

下一步应在跨 session、外部 memory 与更长 interference 后复验 implicit effects，并检查它们何时应该被更新或抑制。
