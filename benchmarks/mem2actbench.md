# Mem2ActBench：memory 的价值落在 tool call 上

**中文** | [English](mem2actbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.acl-long.370/) · [代码](https://github.com/Cantaloupe-M/Mem2ActBench)

## 它在测什么

Mem2ActBench 有 400 个 tool-use tasks，来自 2,029 个 sessions，平均约 12 个 user-assistant-tool turns；91.3% tasks 被判断为强 memory-dependent。系统需要根据长期 preference 与 task state 选择正确工具并填对参数。

## 相比什么前进了

对话 QA 只能间接看 memory utility。Mem2ActBench 直接评价 tool-call correctness，使“记住了用户偏好却没有用于参数 grounding”的失败可见，也把 action-level utilization 从 retrieval quality 中分离出来。

## 分数边界

tool-call success 支持 memory 在给定 schema/backbone/harness 下被正确用于行动；它不能说明 memory representation 本身更优，因为 synthetic generation、tool schema 与 agent backbone 都影响结果。

## 公平比较条件

锁定 tool schemas、allowed calls、backbone、memory implementation 与 synthetic task version。不同工具集合或 parameter constraints 必须分 track。

## 下一步评测坐标

下一步要让 tool call 改变持久环境，并验证错误 memory 导致的 downstream state 是否能被检测和恢复。
