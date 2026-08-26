# Snapshot Compatibility Audit

- **测量对象：** RAG corpus snapshot 增长时，同一个 agent 的答案是否发生超出自身采样波动的稳定翻转。
- **最近前身：** Stable-RAG / Con-RAG 控制固定证据扰动；这里用 nested corpus snapshot 模拟部署升级，并减去 within-snapshot disagreement。
- **决定性证据：** NQ 的 excess churn 为 6.438pp exact 与 10.250pp semantic，即使 aggregate EM 只变化 −1.50pp；40 个稳定翻转贡献了 10.00pp semantic churn。
- **结论上限：** 证明 snapshot compatibility failure，不证明翻转一定有事实性伤害。
- **最强混淆：** 单一 shard ordering、主要一个 generator family、未记录 temperature/top-p、semantic judge 非人工。
- **未覆盖：** live refresh、多步轨迹、因果 document attribution 与 harm measurement。
- **谱系：** 将 corpus version 本身纳入 RAG regression contract；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2608.22856

