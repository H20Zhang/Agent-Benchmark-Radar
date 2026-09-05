# AgentDS：Data Agent benchmark 也应该比较 human-only、AI-only 与 human-AI collaboration

**中文** | [English](agentds.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.19005) · **领域：Data Agent**

AgentDS 的关键价值不是再做一个“谁的 agent 分数最高”的榜单，而是把 **AI-only、human-only 与 human-AI collaboration** 放进同一个评测问题：AI 到底替代了多少工作，哪些环节仍依赖人的判断，以及协作是否真的比单独使用 AI 更好。

## 它到底测什么

AgentDS 基于 **17 个 data-science challenges、6 个 industries、29 teams / 80 participants**，使用 synthetic enterprise-pattern data 与 hidden leaderboard 评价完整分析或建模成果。

评测对象因此不是单一步骤的 SQL、代码生成或统计问答，而是较完整的数据科学任务交付。更重要的是，它把完成任务的 **工作方式** 本身纳入比较：同一个 challenge 可以由 AI 独立完成，也可以由人和 AI 协作完成。

## 相比此前评测多测了什么

MLE-bench、DSAgentBench、DataSpace 等 benchmark 主要回答“一个 agent 能不能把任务做完”。AgentDS 多问了一层更接近组织采用的问题：

- AI-only 是否已经达到可用水平；
- human-AI 是否稳定优于 AI-only；
- AI 带来的收益是提高结果质量，还是只是节省一部分执行时间；
- 哪些任务的瓶颈仍然是 problem framing、结果判断或业务经验，而不是代码执行。

因此它更适合支撑 **augmentation / substitution** 相关结论，而不是单纯的模型能力排名。

## 实际怎样评测

一个可解释的 AgentDS 结果至少需要同时固定 challenge release、数据版本、hidden evaluator、AI 工具和模型、时间预算、参与者选择以及 collaboration rules。

AI-only、human-only 与 human-AI 必须看作不同 track。尤其 human-AI track 中，AI 能否主动执行、人工是否必须逐步确认、参与者是否能自由选择工具，都会显著改变最终结果。

这意味着 headline score 之外，实验设计本身就是结果的一部分。

## 分数能说明什么

challenge score 可以说明：在当前 participant pool、数据、工具、时间预算和 hidden tests 下，这种工作方式能否产出更好的任务结果。

它不能直接支持“AI 可以替代 data scientist”这样的宏观结论。原因是替代关系不仅由最终分数决定，还涉及人工时间、review burden、错误严重度、问题选择、沟通与长期维护成本。

同样，human-AI 优于 AI-only 也不自动说明“human expertise 是决定性因素”：提升可能来自额外时间、更多重试、更好的 prompt engineering，或人工承担了 evaluator-sensitive 的最后一步。

## 最主要的混杂因素

**Human variance 是 AgentDS 相比纯 agent benchmark 最大的额外变量。** 参与者的数据科学经验、对工具的熟悉程度以及协作策略都会进入结果。

另一个关键限制是 synthetic enterprise-pattern data。它可以提供可控和可核验的任务，但真实企业分析还包含脏 schema、权限、历史口径、组织知识和无法完全写进 evaluator 的业务价值判断。

因此跨论文复现时，只报告模型名和总分远远不够。

## 公平比较条件

至少应对齐：

- challenge / hidden-test version；
- participant selection 与经验分布；
- AI model、tool access 与 agent harness；
- 每个 track 的时间和 retry budget；
- human-AI collaboration contract；
- 最终 evaluator 和人工可见反馈。

如果这些条件不同，最好报告为不同 protocol cell，而不是直接做单一排行榜。

## 还没有覆盖什么

AgentDS 已经把“人是否还重要”带进 benchmark，但还没有完整回答：

- 长期使用后团队生产率是否继续提高；
- review / correction 的人力是否抵消自动化收益；
- 低频但高代价错误如何计分；
- AI 是否改善最终业务决策，而不只是 challenge metric；
- 人会不会因为依赖 AI 而改变技能和验证行为。

## 下一步最有判别力的验证

最值得增加的不是更多静态 challenge，而是 **longitudinal controlled deployment**：在相同团队和任务分布下持续观察 human-only、AI-only、human-AI 三种模式，联合记录结果质量、人工分钟数、返工次数、严重错误和最终决策影响。

这样才能区分“agent 在 benchmark 上变强”和“agent 真正减少 data-team 工作量”。

## 演化位置

`单项 data task → 端到端 data-science agent → human–AI team effectiveness`

AgentDS 的特殊位置在最后一步：它把研究问题从“agent 会不会做”推进到“**agent 进入真实工作组织之后究竟创造什么增量**”。
