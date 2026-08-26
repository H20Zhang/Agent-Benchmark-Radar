# InjecMEM

- **测量对象：** 攻击者只通过一次普通交互写入记忆后，能否让未来相关查询检索该记录并输出预设目标。
- **最近前身：** AgentPoison / MINJA 侧重攻击方法；MPBench 提供更宽的 persistent poisoning taxonomy。InjecMEM 隔离 topic-conditioned targeted generation。
- **决定性证据：** Multi-GCG 在 MemoryOS 上达到 46.5% RSR、76.6% conditional ASR 与 35.6% joint ASR；多个通用 filter 几乎不降低 conditional ASR。
- **结论上限：** 证明白盒优化攻击可穿过所测 memory stack；不支持对未见模型家族的黑盒迁移结论。
- **最强混淆：** 最强攻击需要 backbone 白盒访问和 fused prompt 知识。
- **未覆盖：** rewrite-heavy store、真实部署、adaptive defense 与 security–utility 曲线。
- **谱系：** 将 memory security 从“是否写入”推进到 write→drift→retrieve→generate 的端到端轨迹；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2608.23471

