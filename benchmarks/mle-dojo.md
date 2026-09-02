# MLE-Dojo

## 它到底测什么

MLE-Dojo 测的是 **交互式 ML engineering trajectory**，不是只看最终提交文件。智能体在 Gym-style 环境中反复读取任务、执行代码、看到错误和 HumanRank 反馈、修改实验方案并再次提交；因此可以观察每一步是否让模型、数据处理或实验状态朝正确方向推进。

## 相比前身多测了什么

MLE-bench 主要把 autonomous ML engineering 压缩成最终 competition submission；MLE-Dojo 将 200+ 任务改造成可训练、可重复交互的环境，并划分约 **150/50 train/eval**。增量在于把 terminal score 变成 trajectory-level signal：失败可以定位到 coding error、实验选择、反馈利用或停止策略。

## 决定性证据

共享 harness 下，不同模型在四类任务上的 HumanRank、stepwise progress 与错误类型被统一记录。这个 benchmark 的关键证据不是某个模型的单一 leaderboard 名次，而是同一交互协议下可以比较“拿到反馈之后能不能持续改善”，以及失败究竟发生在哪一步。

## 这个分数支持什么判断

MLE-Dojo 的结果支持 model + scaffold 在 **带真实 score feedback、有限 step budget 和 best-of-two 设置**下的交互式 ML engineering 能力。它不能和隐藏 score 的 MLE-bench 数字直接横比，也不能把提升纯归因于基础模型，因为 scaffold、feedback exposure 与 search budget 都是 load-bearing 条件。

## 公平比较条件

需要固定任务版本、可见反馈、step budget、best-of-n、硬件、可执行工具、代码 scaffold、错误恢复规则和 HumanRank 计算。尤其要把真实 score feedback 是否可见作为一级变量：能反复依据 leaderboard signal 调参的 agent 与 blind submission agent 测的是不同问题。

## 研究上怎么用

如果研究关注 data/ML agent 的 planning、debugging 或 self-improvement，MLE-Dojo 比只看最终 Kaggle 分数更适合做 mechanism ablation。可以比较：移除 score feedback、限制 retry、固定 scaffold、关闭 history/memory 后，stepwise progress 与最终 HumanRank 分别怎么变，从而区分模型能力和 orchestration benefit。

## 下一步最有价值的验证

它仍没有覆盖问题定义、数据获取、指标设计、研究仓库修复和方法新颖性。更重要的外推问题是 feedback overfitting：agent 是否只是利用同一任务的连续真实分数爬坡，还是学到了能迁移到 held-out task family 的 ML engineering policy。

## 谱系位置

在 MLE-bench 之后，MLE-Dojo 把终局评分推进到可训练的交互轨迹；`map_delta=reinforces`。它和后续 DeltaML / AI4AI 一起推动 Data Agent evaluation 从“交一个结果”走向“评估完整研究/工程循环”。

Primary: https://arxiv.org/abs/2505.07782
