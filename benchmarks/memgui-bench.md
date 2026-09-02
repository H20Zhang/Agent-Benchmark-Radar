# MemGUI-Bench：用重复 GUI 执行测 experience reuse

**中文** | [English](memgui-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.06075) · [代码](https://github.com/lgy0404/MemGUI-Bench)

## 它在测什么

MemGUI-Bench 含 128 个任务、64 组 mirror pairs，跨 26 个 mobile apps 与 68 个 scenarios；89.8% 需要跨时间或跨空间保留信息。它通过 pass@k、trajectory 和 progressive scrutiny 测短期 retention、跨 session learning、cross-app transfer 与 failure recovery。

## 相比什么前进了

MemoryArena 已让 memory 影响 future action；MemGUI-Bench 进一步把 action 放到可执行 mobile UI 中，测试之前一次尝试的步骤、失败和视觉状态能否帮助下一次执行，而不是只在文本环境复用经验。

## 分数边界

更高 pass@k 支持“在该 mobile snapshot、agent 与 retry budget 下，prior experience 改善执行”。它不能单独证明 memory module 更好，因为 UI perception、runtime 与 retry budget 都是关键 confounders。

## 公平比较条件

锁定 app/runtime snapshot、agent backbone、perception model、judge 与 retries。跨 app version 的结果可能反映 UI drift 而不是 memory change。

## 下一步评测坐标

需要从 snapshot-based tasks 走向长期真实设备状态、权限与不可逆操作，检验 memory 带来的风险与恢复能力。
