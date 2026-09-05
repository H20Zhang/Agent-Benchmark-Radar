# KBGym / Training a Knowledge Base

## 它到底测什么

KBGym 把知识库从“预先构建好的静态索引”变成一个**可以被监督经验训练、随后冻结并独立评测的持久状态对象**。curator 在看到监督问答与 gold answer 后编辑知识库；冻结后由独立 reader 回答训练内和不同 coverage 层级的未见问题。核心问题不是单次 retrieval，而是训练阶段对知识表示的修改能否迁移到未来 query。

## 相比前身多测了什么

HippoRAG 等结构化检索通常从完整 corpus 无监督地产生图或索引。KBGym 则显式使用 `(question, answer)` 作为训练信号，并把“这个监督信号覆盖了多少未来问题所需的 answer key”作为分析维度，因此能区分 memorizing trained questions、利用共享 key 迁移和真正超出训练覆盖的泛化。

## 决定性证据

v2 修订后的结果显示：trained-question 上约 **25% action saving 与 +0.294 F1**；未见问题按 answer-key coverage 分层后，**both-key 为 +0.176 F1，one-key 为 +0.059，neither-key 无收益**。同时只有 **27.6% corpus** 被训练过程实际覆盖。最重要的结论是收益随覆盖关系显著衰减，而不是“编辑知识库后所有问题都更好”。

## 这个分数支持什么判断

它支持“在该 synthetic atomic-document 设置中，监督问答可以训练一个持久知识状态，并且收益与未来问题是否共享训练 answer key 强相关”。它不支持普遍的 knowledge-base improvement：低 corpus coverage、单 seed、同模型家族 curator/reader 都限制了外推。

## 公平比较条件

比较方法时需要固定 curator/reader 模型、允许的 edit actions、训练 question 数量、冻结时点、reader action budget、document construction 与 evaluation coverage split。必须分别报告 trained、both-key、one-key、neither-key，而不能只给一个平均分掩盖 coverage dependence。

## 研究上怎么用

KBGym 对 **self-improving representation / learned retrieval state** 很有价值，因为它第一次把“agent 从历史问答中应该怎样改变知识库”变成可测对象。对于新方法，比最终 F1 更重要的是画出 benefit vs. supervision coverage 曲线，并比较结构编辑是否比简单 cache / exemplar accumulation 提供超出共享 key 的泛化。

## 下一步最有价值的验证

当前缺口包括跨模型迁移、多 seed、自然语料与 online/prequential evaluation。真正高杠杆的问题是：当 curator 和 reader 不再共享模型家族、文档不是 synthetic atomic facts、问题分布持续变化时，训练出的知识结构是否仍然在 **neither-key** 区域产生可复现增益。

## 谱系位置

KBGym 让 corpus 从静态输入变成可训练且可冻结审计的状态对象；`map_delta=early_signal`。它更接近“representation can learn from query history”的 benchmark，而不是普通 RAG retrieval leaderboard。

Primary: https://arxiv.org/abs/2608.21829

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究优化对象从模型参数转向可编辑知识库时，收益究竟发生在哪些覆盖范围。最关键的不是修改后总体分数提高，而是未见问题、未覆盖键和新结构上是否仍有收益；训练答案写回需要显式防泄漏。

### 一个具体任务长什么样

示意任务：整理者根据训练期问题与反馈编辑持久文档库，之后冻结该库，由固定读者回答测试问题。新增表征可能加速访问，也可能只把训练答案提前保存，两种机制需要不同对照。

### 最有判别力的实验

按问题、实体键和关系结构分别留出测试，比较原库、答案缓存、等预算结构改写与随机编辑。冻结读者，计入整理成本并测试跨读者迁移；只有覆盖外收益才支持超越答案缓存的表征改进。

### 建议搭配

[structmemeval](structmemeval.md) · [snapshot-compatibility-audit](snapshot-compatibility-audit.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
