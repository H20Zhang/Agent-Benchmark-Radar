# MEMPROBE：先审计 memory store 到底留下了什么

**中文** | [English](memprobe.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.24595) · [代码](https://github.com/sora1998/MemProbe)

## 它在测什么

MEMPROBE 对 50 个 simulated users 的 final memory artifacts 做 post-interaction reconstruction，共 31 个 hidden dimensions、1,550 个 recovery targets。它同时提供 full-store access 与 top-k retrieval 条件，区分“信息根本没写进 store”和“写进去了但查不到”。

## 相比什么前进了

许多 benchmark 只看最终答案，因此 write-side information loss 会与 retrieval/reader failure 混在一起。MEMPROBE 直接把 memory artifact 设为被审计对象，能够定位 retention 与 accessibility 两个不同层级。

## 分数边界

recoverability 支持 memory artifact 保留了多少 structured user state，却不等于这些信息应该被保存，也不证明它有 downstream utility。过高 recovery 甚至可能意味着 unnecessary profiling，因此 privacy/consent 不能被高分替代。

## 公平比较条件

锁定 synthetic persona、serialization、memory budget、slot filler/judge 与 retrieval query formulation；full-store 与 top-k 必须分 track。

## 下一步评测坐标

下一步要把 recoverability 与 consent、deletion、usefulness 和 future action 绑在一起，避免把“记得更多”误当成唯一优化目标。
