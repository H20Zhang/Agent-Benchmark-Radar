# SCALE-QA

- **测量对象：** 在没有 session/topic 边界的混合长对话里，后续任务决策依赖早期、局部且休眠的约束时，memory system 能否重建真正有因果关系的 episode，而不是只找到语义相似片段。
- **最近前身：** LongMemEval 已覆盖跨 session 推理、更新与弃答，但保留 timestamped session structure；SCALE-QA 去掉显式边界，把“哪一段历史构成当前有效 episode”本身变成待恢复对象。
- **决定性证据：** benchmark 含 3,000 个审计问题、10 个领域与 4,346 个精确 evidence snippets；同一 deterministic runtime 可从 16K 扩到 128K，并提供 400 题的 1M diagnostic。GPT-4o-mini 在 128K Full Context 下即使 evidence containment 为 100%，准确率仍只有 29.8%，说明“证据在上下文里”与“重建正确 episode”不是同一测量对象。
- **结论上限：** 这些结果支持 SCALE-QA 作为 episode-integrity 的高区分度诊断；TSIM 在不同 backend 上领先最强对应 baseline 5.6–17.6pp 是 system-level evidence，不能单独归因于某个 segmentation、index 或 routing 组件。
- **最强混淆：** 数据采用 counterfactual synthetic construction，主协议是 deterministic four-way MCQ；answerer、retrieval context budget 与 runtime noise construction 仍会影响系统分数。
- **未覆盖：** 真实长期日志、开放式回答、工具跟进与后续行动；论文在 LongMemEval 上的 transfer diagnostic 采用 transductive configuration selection，不能当作 held-out 泛化证据。
- **谱系：** 把 LongMemEval 式“跨会话记住并更新”进一步拆成“在交错历史里先恢复当前任务真正绑定的 episode 与约束”；`map_delta=early_signal`，单篇工作不足以改写 durable Benchmark Map。

Primary: https://arxiv.org/abs/2608.25655
Code/data: https://github.com/LordTARN1SHED/SCALE-QA
