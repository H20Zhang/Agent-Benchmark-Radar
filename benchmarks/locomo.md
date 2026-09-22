# LoCoMo：把长期对话记忆变成可测量对象

**中文** | [English](locomo.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2024.acl-long.747/) · [代码](https://github.com/snap-research/locomo)

## 它在测什么

LoCoMo 把长期对话记忆从短上下文问答拉到真正的多 session 历史：对话平均约 600 turns、16K tokens，最长跨 32 个 sessions，并同时覆盖 QA、event summarization 和 multimodal dialogue generation。关键不只是“能否找回一句话”，还包括跨很远时间间隔的 temporal / causal reasoning 与对整段经历的压缩理解。

## 相比什么前进了

此前大量 long-context 测试更接近 needle retrieval 或单文档理解。LoCoMo 的增量是让信息以连贯互动形式逐步积累，并要求模型在多个任务上使用这段历史，因此成为后续 LongMemEval、MemoryAgentBench 等工作的基础参照。它建立的是“长期历史值得单独评测”这个坐标，而不是给某一种 memory architecture 背书。

## 决定性证据与分数边界

ACL 论文报告的核心现象是：long-context LLM 与 RAG 都能改善表现，但在理解长对话、长距离 temporal / causal dynamics 上仍明显落后于人类。这个结果支持“扩大 context window 并没有解决长期记忆”这一测量结论；它不能区分收益究竟来自写入、索引、检索、reader 还是 judge。本仓库只有在协议可对齐时才把系统分数放入独立 result track，第三方用不同 judge 或题集规模得到的 LoCoMo 排名不会混成一个榜单。

## 公平比较条件

必须对齐使用的 LoCoMo 问题版本、answerer/reader、retrieval budget、可见历史以及 QA/summary 的评分器。尤其是 LLM-as-judge 与不同问题过滤会显著改变绝对分数，因此只看一个 Overall 数字很容易把 harness 差异误认为 memory gain。

## 下一步评测坐标

LoCoMo 主要问“过去发生了什么”。下一步更重要的是验证 remembered experience 是否改变之后的行动、规划与长期用户状态维护，并把 update、forget、conflict 和成本从 end-to-end QA 分数中拆出来。

## 后续对照：对话中的记忆调用与任务完成

**LoCoMo-Conv（2026-09-03）**保留原 LoCoMo 的标准答案和证据 `dia_ids`，把查询改写为 dialog、implicit、counterfactual、composed 四种形式，同时测检索召回与自由文本回答质量。官方仓库提供 top-K、oracle、no-memory 等对照，以及 1,069 个双问题组合的多记忆簇。它让“查询已明确提示要找哪段记忆”这个混杂因素更容易被检查；但改写后的既有对话并不等于自然发生的长期用户交互。[论文](https://arxiv.org/abs/2609.03467) · [官方协议与代码](https://github.com/MiuLab/LoCoMo-Conv)

**DolphinBench（2026-09-21）**的论文摘要描述了三个知识工作角色，每个角色约 500K tokens 的用户历史、200 个任务，并要求报告准确率、总成本和延迟。任务筛选要求指定智能体在有相关历史时成功、无相关历史时失败。这个对照检查的是在指定智能体与筛选协议下的历史依赖，不能推成所有模型都必须依赖记忆，也不能单凭任务成功率证明某个写入或检索组件更好。[论文摘要](https://arxiv.org/abs/2609.24971)

**研究建议：** 保留 LoCoMo 作为显式历史问答基线，另设“未直接索取历史事实的对话”与“需要历史才能完成的任务”两类实验。固定回答模型、可见信息、重试和预算，分别报告证据召回、回答或行动结果，以及构建与查询成本；不要把三类总分混成一个排名。

**证据边界：** LoCoMo-Conv 的上述设计已核对官方 README；DolphinBench 的上述信息仅核对论文摘要。这里是后续工作的对照说明，不代表完成了两项新基准的全文审计、正式入库或独立复现。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合把长期对话记忆作为能力起点，但不宜单独支撑‘记忆让智能体越用越好’。选型时先分清要证明的是历史信息可被找回，还是经验能改变未来行为；LoCoMo 主要为前者提供证据。

### 一个具体任务长什么样

示意任务：早期对话提到一次搬家，后续会话更新工作安排，当前问题要求串起两件事的先后关系。系统需要保留人物、时间与事件联系；仅返回包含相同关键词的一句话可能仍无法回答。

### 最有判别力的实验

固定回答模型与问题集合，比较完整历史、等预算检索片段和所需证据直接给定三种条件，同时记录支持证据召回与最终答案。检索条件落后于证据给定条件，才有理由优先优化记忆访问；两者都差则先检查阅读与时间推理。

### 建议搭配

[longmemeval](longmemeval.md) · [memoryarena](memoryarena.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
