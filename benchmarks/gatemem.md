# GateMem：共享 memory 同时要有用、守权限、能删除

**中文** | [English](gatemem.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.18829) · [代码](https://github.com/rzhub/GateMem)

## 它到底测什么

GateMem 测共享 memory agent 能否在保持 utility 的同时，正确执行 **谁可以访问什么、什么必须被忘掉**。它覆盖医疗、办公、教育、家庭等多 principal 场景，通过长 episode、增量 memory injection、隐藏 checkpoint、访问边界和 deletion target 来评估治理能力。

## 相比此前评测多测了什么

多数 memory benchmark 奖励“记得更多”；privacy benchmark 又常只看泄露，不看系统还能不能正常服务。GateMem 把冲突本身变成评测对象：utility、access-control violation 与 deletion leakage 必须一起看。全部存下来不行，什么都不记同样不行。

## 决定性证据

论文发现，没有一种被测方案能同时在 utility、access control 与 active forgetting 上都表现强。long-context baseline 往往治理更稳，但 token cost 高；retrieval / external-memory 方案成本更低，却可能重新暴露无权限或已经请求删除的信息。公开 evaluator 也保留了 utility、privacy leakage、deletion leakage 等独立坐标。

## 这个分数能证明什么

GateMem 能支持特定 principal / policy model 下 **governed memory system** 的系统级判断，但不能直接定位泄漏来自 storage、indexing、retrieval filtering、generation 还是 policy interpretation。因此 aggregate score 必须和三个子轴一起看。

## 公平比较契约

应固定 principal、policy rule、deletion request、memory history、model、retrieval top-k 与 query set，同时报告 latency/token/storage overhead，因为更严格的治理可能只是靠昂贵的 full-context inspection 实现。隐藏 leak-target annotation 属于 evaluator metadata，不能泄露给 agent。

## 还没有测什么

真实企业策略还包括嵌套 group、delegated authority、purpose limitation、retention schedule、审计和动态 policy change；cryptographic deletion 与物理数据擦除也不是语言层 benchmark 能验证的。

## 下一步最有判别力的验证

在同一批任务上分别把 policy enforcement 放到 write、index、retrieval、generation 四个阶段。真正的系统问题是：把权限/删除约束放在哪里，才能在不付出 full-context 成本的情况下显著减少 violation。

## 演化位置

`remember more → remember selectively → governed multi-principal memory`

它把 privacy 与 forgetting 从附带 caveat 提升成了 memory system 的一等目标。