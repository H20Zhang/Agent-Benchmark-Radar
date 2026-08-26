# MPBench

- **测量对象：** 六类恶意内容经四种写入渠道进入持久记忆后，是否被写入，并在另一次会话中被相关查询检索。
- **最近前身：** LoCoMo / LongMemEval 测良性 fidelity，AgentDojo / InjecAgent 测同会话 hijacking；MPBench 把写入和后续检索拆成跨会话协议。
- **决定性证据：** OpenClaw 的平均 ASR / conditional RSR 为 34.25% / 17.40%，HERMES 为 66.67% / 64.70%；PromptArmor 在 1% FPR 下的最佳 TPR 仅 67.67%。
- **结论上限：** 分数描述 system+harness 的 persistent-poisoning exposure，不能单独归因给模型。
- **最强混淆：** 两个 agent 的写入与检索策略不同，部分渠道还是静态标注上下文。
- **未覆盖：** 多 backbone、完全可执行的 delivery、自然 memory drift 与 benign utility。
- **谱系：** 补上 memory safety 从良性 fidelity 到 persistent poisoning 的关键过渡；`map_delta=splits`。

Primary: https://arxiv.org/abs/2606.04329

