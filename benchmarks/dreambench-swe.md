# DreamBench-SWE

- **测量对象：** 多会话软件工程中，后续代码任务能否正确利用或抑制早期会话里、无法从当前仓库重新推断的记忆证据，并通过隐藏可执行 oracle 验证最终修改。
- **最近前身：** MemoryArena / WorldMemArena 把记忆连到后续行动，SWE-bench 提供可执行代码任务；DreamBench-SWE 把两者交叉成受控 repository-continuation memory-hygiene 陷阱。后来出现的 Agent Memory Bench (coding agents) 则提供真实仓库上的互补对照。
- **决定性证据：** v2 每个完整 condition 为 60 traps × 3 seeds = 180 个 S3 cells；successor 中 B0 为 21/180、B5 为 82/180、typed-plus-raw reference probe 为 83/180、一个 pinned Mem0 literal-storage 配置为 97/180，所有可用 memory-vs-B0 比较经 Holm 校正后均拒绝零假设。
- **结论上限：** 这些结果支持 DreamBench-SWE 作为有区分力的可执行 profile benchmark；不支持 memory-bearing conditions 之间的机制优越性、等价性或广泛产品泛化。
- **最强混淆：** 使用合成 fixture repository 与单一 pinned wake/judge/model stack；filesystem 隔离不等于 network isolation，memory 配置与 coding harness 也会共同影响结果。
- **未覆盖：** 真实生产仓库与跨模型/跨 harness 迁移；C9/C10 缺少 B0 headroom，不能据此做广义 rejection/abstention 能力结论。
- **谱系：** 把“过去记忆是否帮助后续行动”继续拆成 retained evidence 是否仍然 current、scoped、authorized/relevant，以及何时应被抑制；`map_delta=early_signal`。

Primary: https://arxiv.org/abs/2608.20664
