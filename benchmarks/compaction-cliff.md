# The Compaction Cliff

- **测量对象：** 有限上下文中的安全约束，能否在反复压缩、分解与检索后仍被完整保留，并继续约束行动。
- **最近前身：** MaRS 有 typed memory，但用统一效用；LLMLingua-2 与生产 compactor 则不区分知识类型。这里把 exact constraint preservation 扩展到三个 context-management operator。
- **决定性证据：** Sonnet `/compact` 的约束保留率五轮后从 0.53 降到 0.10；TypeCompact 稳定在 0.96，TypeDecompose 的 locality violation 为 0%，TypeRetrieve 的 recall@50 为 100%。
- **结论上限：** 支持“typed retention 在这些协议下更能保留规则”；不证明所有长期智能体都能因此更安全。
- **最强混淆：** 行为实验并未严格 token-match；TypeCompact 保留更多上下文，且安全保证继承 classifier 的漏检率。
- **未覆盖：** 在线约束识别、企业分布、跨智能体记忆与 token-matched behavior。
- **谱系：** 与 MPBench、InjecMEM、Utility Under Attack 一起把 memory safety 拆到写入、检索、压缩等生命周期阶段；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2608.22752

