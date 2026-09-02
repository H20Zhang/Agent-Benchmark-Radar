# MemoryArena：记忆是否真的改善后续行动

**中文** | [English](memoryarena.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.16313) · [项目页](https://memoryarena.github.io/) · [代码](https://github.com/ZexueHe/MemoryArena)

## 它到底测什么

MemoryArena 测的是 agent 能不能把早期交互经验转化成 **后续更好的决策**。它使用多 session 的 Memory–Agent–Environment 闭环：agent 的 action 会产生 feedback，其中真正有用的经验需要被提炼，并在之后相互依赖的任务里再次使用。这里的 memory 不只是“能否回答历史里出现过什么”，而是“过去经历是否改变下一次怎么做”。

## 相比此前评测多测了什么

LoCoMo 一类 benchmark 主要测对历史对话的回忆与推理。MemoryArena 把因变量从 retrospective QA 改成 downstream action quality，并覆盖网页导航、带偏好约束的规划、渐进式信息搜索和连续形式推理。因此，有价值的 memory 可能是一条失败路径、环境约束或策略经验，而不是历史中能直接匹配的事实。

## 决定性证据

论文的关键观察是：一些在 LoCoMo 上已经接近饱和的系统，进入这种 agentic multi-session 场景后仍明显表现不佳。公开 harness 同时覆盖 long-context、词法/向量检索、图检索和专门 memory system，因此这个落差很难简单归结为“少了某一种 retriever”。

## 这个分数能证明什么

它主要提供固定模型、工具接口、环境和 session protocol 下 **experience-to-action 整体闭环** 的系统级证据。它不能单独证明某个 memory representation、retriever 或 consolidation 算法造成了增益，因为 planning 与 tool execution 也位于因果链上。

## 公平比较契约

比较时应固定 backbone、环境版本、工具接口、session 边界、action budget 与 observation access，并单独报告 memory 写入/更新成本和在线行动成本。如果某个系统拥有更多 observation 或 retry，它测到的是不同的 agent loop，而不是更干净的 memory component 差异。

## 还没有测什么

它仍是有边界的 benchmark environment，而不是数月开放式部署；governance、删除、隐私边界和跨用户 memory 不是主目标。同时它还不能充分区分：到底是写错了经验、取错了经验，还是取对了但 agent 没有用。

## 下一步最有判别力的验证

在同一批 trajectory 上加入 oracle-write、oracle-retrieve、oracle-use 三类 counterfactual。这样才能把“系统做不好”进一步定位到 memory lifecycle 的具体断点。

## 演化位置

`conversation recall → trajectory memory → experience-conditioned action`

它真正重要的变化，是把成功标准从“记住过去”推进到“改变未来行为”。