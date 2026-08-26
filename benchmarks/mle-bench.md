# MLE-bench

- **测量对象：** 智能体能否从竞赛描述和数据出发，在离线环境中迭代实验并提交可由重建测试集和历史私榜门槛评分的预测文件。
- **最近前身：** MLAgentBench 只有 13 个、常带 baseline 的任务；MLE-bench 扩到 75 个 from-scratch competition，并用 human-relative medal contract。
- **决定性证据：** 同一 GPT-4o 在 MLAB、OpenHands、AIDE scaffold 下 Any Medal 分别为 0.8%、4.4%、8.7%；pass@6 又大幅高于 pass@1。
- **结论上限：** headline score 测的是 model+scaffold+retry+resource system，不能作为基础模型 MLE 能力的纯证据。
- **最强混淆：** scaffold、retry、时长、硬件、工具和 prompt assistance 都是 load-bearing；后续官方还暂停 leaderboard 以处理公平性与版本问题。
- **未覆盖：** 问题定义、数据/指标设计、杂乱研究仓库、方法新颖性与人类协作。
- **谱系：** 补齐 Data Agent 的自主 ML engineering 分支：MLAgentBench→MLE-bench→MLE-Dojo→DeltaML/AI4AI；`map_delta=splits`。

Primary: https://arxiv.org/abs/2410.07095

