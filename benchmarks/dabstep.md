# DABStep：复杂 data workflow 应该有可验证的 intermediate milestones

**中文** | [English](dabstep.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DABStep 的 paper 描述约 450 个 tasks、来自 95 个 workflows、覆盖超过 100K payment transactions；当前公开 dataset 约 460 rows。任务把 data analysis 拆成一组可验证 steps，并通过 deterministic final answers、hidden tests/online leaderboard 检查 agent 是否真正完成 workflow，而不是只生成合理解释。

## 相比什么前进了

开放式 analyst benchmark 的难点是最终报告很难归因。DABStep 用 step structure 建立中间 execution contract，使 schema inspection、transformation、aggregation 等错误可以在 final answer 前被定位。

## 分数边界

final/step success 支持 payments data 与当前 workflow definitions 下的执行可靠性；paper 与 public artifact 的规模差异意味着必须绑定 release，不应把不同 task set 的结果混排。

## 公平比较条件

锁定 dataset release、workflow version、runtime、hidden tests、tool budget 与 agent scaffold，并记录 public/online evaluator generation。

## 下一步评测坐标

下一步应将 step correctness 与 business invariant、recovery 和 artifact provenance 联合起来，区分“步骤执行了”与“业务状态正确”。
