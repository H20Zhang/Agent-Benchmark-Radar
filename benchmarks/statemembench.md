# StateMemBench

- **测量对象：** 在跨会话事实、约束与决定持续被修订时，回答是否使用当前有效状态，而不是已被替代的旧状态。
- **最近前身：** LongMemEval / MemoryAgentBench 已覆盖 update，但 StateMemBench 用 symbolic event program、deterministic replay 与 closed-pool grader，把 state drift 从 retrieval / generic reasoning failure 中更直接地隔离。
- **决定性证据：** 234 个多会话场景、322 个 probe；grader 区分 current、targeted superseded 与 other。StateMem 在 DeepSeek 同 backbone 下从 0.205 提到 0.363；length/cost-matched control 仍保留 +15–32 point 的结构收益。
- **结论上限：** 分数支持在显式依赖、受控修订协议下维护当前状态的能力；它不等价于一般 memory quality，也不直接证明真实环境中的长期行动收益。
- **最强混淆：** benchmark 与 state-structured 方法存在任务—方法对齐；对话由模型合成、关系依赖显式给出，并使用固定 LLM judge。
- **未覆盖：** 潜在关系发现、真实用户/环境漂移、隐私治理，以及 state tracking 是否改善后续 closed-loop action。
- **谱系：** `early_signal`。它把 update 从“新旧事实都在不在”推进到“当前 operative state 是什么”，但 durable map 暂不改。

Primary: https://arxiv.org/abs/2608.19652
