# MLE-Dojo

- **测量对象：** 智能体在 Gym-style ML engineering 环境中反复查看任务、执行代码、获得错误和 HumanRank 反馈、修改方案并提交结果的完整轨迹。
- **最近前身：** MLE-bench 主要评分最终提交；MLE-Dojo 把 200+ 任务改造成可训练与评测的交互环境，并划分 150/50 train/eval。
- **决定性证据：** 共享 harness 下，不同模型在四类任务上的 HumanRank 和 stepwise progress 被统一记录；错误和行动分解让失败位置可见。
- **结论上限：** 最终分数包含真实 score feedback、scaffold、15-step budget 与 best-of-two，不可与隐藏 score 的 MLE-bench 直接比较。
- **最强混淆：** agent 可依据真实分数反复适配，存在 feedback overfitting；evaluation tasks 也大量继承公开 predecessor suite。
- **未覆盖：** 问题定义、数据获取、指标设计、研究仓库修复与方法新颖性。
- **谱系：** 在 MLE-bench 之后把终局评分推进到可训练的交互轨迹；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2505.07782

