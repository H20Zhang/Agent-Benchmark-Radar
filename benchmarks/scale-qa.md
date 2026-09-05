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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究交错历史中的情节恢复，而不是把长上下文问题简化为‘证据有没有被召回’。证据全部可见仍可能使用错误的情境与约束；因此它更接近任务绑定关系的诊断，而非通用检索排行榜。

### 一个具体任务长什么样

示意任务：多个项目在一条没有明确边界的长对话里交替出现，相同实体被多次提及。当前问题受某个早期项目中的局部约束支配；检索到实体相关片段之后，还要判断这些片段属于哪个情节。

### 最有判别力的实验

固定支持证据与问题，分别提供原始交错历史、正确情节边界和正确有效状态。再改变干扰长度，拆分情节识别与状态推理的损失；论文中的某个完整上下文模型分数只应作为该配置的历史基线，不是全基准当前最好成绩。

### 建议搭配

[came-bench](came-bench.md) · [statemembench](statemembench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
