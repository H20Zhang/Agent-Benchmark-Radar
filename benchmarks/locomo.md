# LoCoMo：把长期对话记忆变成可测量对象

**中文** | [English](locomo.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2024.acl-long.747/) · [代码](https://github.com/snap-research/locomo)

## 它在测什么

LoCoMo 把长期对话记忆从短上下文问答拉到真正的多 session 历史：对话平均约 600 turns、16K tokens，最长跨 32 个 sessions，并同时覆盖 QA、event summarization 和 multimodal dialogue generation。关键不只是“能否找回一句话”，还包括跨很远时间间隔的 temporal / causal reasoning 与对整段经历的压缩理解。

## 相比什么前进了

此前大量 long-context 测试更接近 needle retrieval 或单文档理解。LoCoMo 的增量是让信息以连贯互动形式逐步积累，并要求模型在多个任务上使用这段历史，因此成为后续 LongMemEval、MemoryAgentBench 等工作的基础参照。它建立的是“长期历史值得单独评测”这个坐标，而不是给某一种 memory architecture 背书。

## 决定性证据与分数边界

ACL 论文报告的核心现象是：long-context LLM 与 RAG 都能改善表现，但在理解长对话、长距离 temporal / causal dynamics 上仍明显落后于人类。这个结果支持“扩大 context window 并没有解决长期记忆”这一测量结论；它不能区分收益究竟来自写入、索引、检索、reader 还是 judge。当前站点只有在协议可对齐时才把系统分数放入独立 result track，第三方用不同 judge 或题集规模得到的 LoCoMo 排名不会混成一个榜单。

## 公平比较条件

必须对齐使用的 LoCoMo 问题版本、answerer/reader、retrieval budget、可见历史以及 QA/summary 的评分器。尤其是 LLM-as-judge 与不同问题过滤会显著改变绝对分数，因此只看一个 Overall 数字很容易把 harness 差异误认为 memory gain。

## 下一步评测坐标

LoCoMo 主要问“过去发生了什么”。下一步更重要的是验证 remembered experience 是否改变之后的行动、规划与长期用户状态维护，并把 update、forget、conflict 和成本从 end-to-end QA 分数中拆出来。
