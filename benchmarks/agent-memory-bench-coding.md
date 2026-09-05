# Agent Memory Bench：编码智能体中的因果记忆复用

**中文** | [English](agent-memory-bench-coding.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、任务、预注册与 pilot](https://github.com/GiulioDER/agent-memory-bench)

## 它到底测什么

Agent Memory Bench 测的是 **过去 repository-task experience 是否因果地改善后续 coding action**。它不是把“有 memory 的 agent”和“没有 memory 的 agent”随意横比，而是在中性、逐字一致的 session feed 与隐藏 executable oracle 下，插入一个可拔插 memory layer，并验证该 layer 是否真的被集成、是否真的在后续 session 中可用和被使用。

## 相比前身多测了什么

PAST-Bench 等工作已经推动 memory 从 QA 走向 future action；这里进一步把 **treatment validity** 做成协议的一部分。很多 memory 实验的隐藏问题是：系统配置里“有 memory”并不意味着任务执行时 agent 实际看到了、检索到了或使用了它。integration hash 与 proof-of-treatment gate 试图把“memory treatment 真发生了”从最终 task success 中独立验证。

## 决定性证据

公开 corpus 包含 **24 个真实仓库任务、24 条 precursor transcript 与 99 个 distractor**。各 arm 共用 baseline 和逐字 session feed；在隐藏 executable oracle 评分前，integration hash 与 proof-of-treatment gate 验证 memory 确实可用并被使用，同时显式记录 ingestion/session cost 与 negative transfer。当前预注册 pilot 最终只有 **13 个 survivor**，相对 CLAUDE.md baseline 的估计提升只有 **+0.014**，区间跨过零。

## 这个分数支持什么判断

当前 pilot 支持的是“在这组 survivor、Claude-specific 环境和所测 memory product 下，还没有足够证据证明稳定正向收益”。它**不支持**“memory 对 coding agent 无用”：样本远低于目标统计功效，proof-of-treatment 又产生 survivor selection，而且参测 Recall memory 产品由作者开发。这里最重要的产出是因果评测 protocol，而不是一个确定的产品排名。

## 公平比较条件

需要固定 coding agent/backbone、repo/task、session feed、tool permissions、execution budget、memory ingestion timing、retrieval visibility 与 executable grader。任何 memory 方法都应同时报告 integration success、treatment exposure、task success、negative transfer 与总成本。若只在“memory 成功接入”的 survivor 上报告结果，还必须同时给出 survivor rate，避免把 integration failure 从评价对象中消失。

## 研究上怎么用

这个 benchmark 对 memory paper 最值得借鉴的是 **proof-of-treatment + executable outcome + cost accounting**。如果声称某个 memory mechanism 改善 coding/data agent，应先证明 memory 真被读取和利用，再用 matched baseline 判断 action utility；否则“配置里有 memory”只是 treatment assignment，不是 treatment received。

## 下一步最有价值的验证

最大的缺口是统计功效、跨 backbone/harness 迁移与 author-built treatment 的独立性。最高杠杆的下一步是扩大真实 repo task 数，在多个 coding agent 上运行相同 neutral-feed protocol，并预先规定 intention-to-treat 与 treatment-on-treated 两套 estimand；这样既不会因接入失败丢样本，也能回答 memory 真被使用时是否有收益。

## 谱系位置

`map_delta=reinforces`，绑定 `memory-action-utility`。它独立加强了 PAST-Bench 所代表的因果 treatment 评测方向，但目前零结果本身不修改 defining chain。真正值得推广的是“**验证 memory 被用过，再谈 memory 带来的因果收益**”这一 benchmark contract。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验编码智能体是否真的使用了前序任务记忆，而不是只把记忆服务接进系统。处理组实际生效的证据尤其重要；低样本量试验和存活样本筛选，仍不足以证明某种产品普遍优于其他方案。

### 一个具体任务长什么样

示意任务：前序会话中存在无法仅从当前仓库推出的任务经验，后续编码任务需要利用它，最终由隐藏可执行检查器评分。中性输入控制保证不同记忆系统不是先拿到了不同质量的提示。

### 最有判别力的实验

除遵守中性输入和处理生效检查外，报告所有分配样本的结果，以及只在处理生效样本上的条件结果。比较无记忆和原始记录检索，并纳入写入、查询与编码会话成本，避免存活筛选夸大净收益。

### 建议搭配

[past-bench](past-bench.md) · [dreambench-swe](dreambench-swe.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
