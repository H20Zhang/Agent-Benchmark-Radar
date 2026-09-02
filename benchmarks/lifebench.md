# LifeBench：把 declarative 与 habitual/procedural memory 放进同一长期生活轨迹

**中文** | [English](lifebench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

LifeBench 构造长期、密集关联的多源 life events，同时评价 declarative facts 与 habitual/procedural patterns。它要求 memory system 不只回忆单个事件，还要从长期行为中形成习惯、程序和跨事件关系。

## 相比什么前进了

多数 conversation-memory benchmark 以显式事实 QA 为中心。LifeBench 把非 declarative memory 拉进评测，意味着“事实都找得到”仍不足以证明 agent 学会了用户反复体现的行为模式。

## 决定性证据与分数边界

论文报告 top-tier memory systems 的最高准确率也只有约 55.2%，说明这一坐标远未饱和。这个 ceiling 支持长期生活模式建模仍困难；它不说明错误来自 storage、retrieval 还是 reasoning，因为 benchmark 仍是 end-to-end system evaluation。

## 公平比较条件

必须锁定 event generation、task family、backbone、memory budget 与 evaluator，并把 declarative 与 habitual/procedural slices 分开报告。一个 aggregate score 不足以诊断 memory representation。

## 下一步评测坐标

更强的 benchmark 应让习惯和程序性 memory 直接影响之后的行动，并观察它们在偏好变化后是否能正确更新而不是固化。
