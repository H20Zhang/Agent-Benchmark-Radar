# MEMPROBE：直接审计最终 memory artifact 里到底留下了什么

**中文** | [English](memprobe.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.24595) · [代码](https://github.com/sora1998/MemProbe)

## 它到底测什么

MEMPROBE 直接评估 **memory artifact 本身**。agent 为一个模拟用户完成常规 assistance 后，benchmark 检查能否仅从留下的 persistent memory 中重建用户的隐藏结构化状态。评测对象因此从“某一道下游题答没答对”变成了 representation coverage。

## 相比此前评测多测了什么

end-task success 会掩盖弱 memory：强模型可能仅靠当前 context 就把任务做对，即使长期 memory 几乎没有保留下关键用户状态。MEMPROBE 把两条轴拆开：先看 assistance，再独立 probe 持久化 artifact 对 hidden user state 的覆盖。

## 决定性证据

benchmark 包含 50 个模拟用户、每个 31 个隐藏维度，共 1,550 个 recovery target，并比较 5 种代表性 memory 条件/系统。即使 memoryless 条件下 assistance 也接近饱和，而 memory 的 category-balanced recovery 仍大约只有 0.6，并且在 top-k access 下进一步下降。核心结论是：**看起来会做事，不等于长期状态真的被保存好了**。

## 这个分数能证明什么

recovery score 能说明 **哪些信息真正进入了可查询的持久 memory representation**，尤其适合定位 write/compression loss。但它不意味着“保留得越多越好”：privacy、data minimization 与 task relevance 都可能让主动不保存成为正确策略。

## 公平比较契约

应固定 interaction history、hidden-state schema、write budget、memory access policy 和 reconstruction model，并分别报告 full-artifact 与 top-k recovery，否则 representation failure 与 retrieval-interface failure 会混在一起。coverage 还应配套 memory size / cost。

## 还没有测什么

它没有直接证明这些被恢复的信息会改善未来行动，也没有判断某项信息是否应该被长期保存。conflict resolution、temporal supersession、provenance 和 deletion correctness 需要单独评估。

## 下一步最有判别力的验证

给每个 hidden-state dimension 同时标注 downstream utility 与 privacy requirement，测 recoverability、未来任务收益、存储成本、data minimization 的 Pareto frontier，而不是单纯最大化 retention。

## 演化位置

`task success → persistent-memory artifact → representation coverage audit`

它暴露了一个容易被忽略的事实：agent 表面上很能干，背后的长期状态却可能非常差。