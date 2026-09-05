# AMA-Bench：从对话历史走向 agent-environment trajectory memory

**中文** | [English](ama-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.22769) · [项目页](https://ama-bench.github.io/) · [代码](https://github.com/AMA-Bench/AMA-Bench)

## 它到底测什么

AMA-Bench 评估的是 **agent-environment trajectory** 上的 memory，而不再只是 human-agent conversation。问题覆盖 Recall、Causal Inference、State Updating、State Abstraction，需要理解 action、observation 与环境状态变化之间的关系。

## 相比此前评测多测了什么

LoCoMo、LongMemEval 建立了长期对话 memory 的基础，但 history 主要还是 communication artifact。AMA-Bench 把 memory source 换成机器生成的 experience：agent 做了什么、environment 返回了什么、state 怎样变化。因此 causality 与 objective state 比对话表述本身更重要。

## 决定性证据

项目报告 206 个 trajectory sample、2,471 个 QA pair、6 个 domain 和 4 类核心能力。AMA-Agent 使用 causality graph + tool-augmented retrieval，平均 accuracy 为 57.22%，比论文中最强 baseline 高 11.16 个百分点。

## 这个分数能证明什么

benchmark 能证明系统是否会对 stored trajectory 做 memory reasoning，也提示 causal structure 与 active retrieval 可能有效。但方法增益仍是 system-level evidence：graph construction、retrieval tool、backbone 与 answerer 一起变化。另外终点仍然是“对 experience 做 QA”，不是“未来环境任务做得更好”。

## 公平比较契约

应固定 trajectory set、backbone、retrieval/tool budget、evidence visibility 与 QA evaluator，并拆分四类能力报告；raw recall 强不代表 state abstraction 或 causal inference 强。tool-augmented system 还应披露额外 search call 与 latency。

## 还没有测什么

它只是间接测试 trajectory memory 会不会改善后续 acting；长期 error accumulation、experience deletion、policy learning 和对 unseen environment 的 transfer 都是不同问题。

## 下一步最有判别力的验证

在同一批 trajectory 后追加 paired future task，让最优 action 必须依赖刚才的 causal/state memory，从而把 trajectory QA 真正连接到 behavior improvement。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究智能体执行轨迹的记忆，而不只是人机对话的个人事实。轨迹中工具输出和环境状态的因果关系更重要；但对过去轨迹回答得好，仍不等于能在新任务中采取更好的行动。

### 一个具体任务长什么样

示意任务：智能体先运行工具，看到状态变化，再修改后续操作；稍后询问某个状态为何出现。系统需要把行动、反馈与结果对应起来，不能仅检索最后一次状态描述。

### 最有判别力的实验

在完整轨迹、只保留观察结果、保留行动—反馈配对三种记忆条件下比较同一组问题。随后把记忆用于相邻的可执行任务，单独报告行动收益；这样才能区分轨迹理解与经验迁移。

### 建议搭配

[longmemeval-v2](longmemeval-v2.md) · [memoryarena](memoryarena.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`conversation history → agent trajectory → causal/state memory of experience`

它是从 conversational memory 走向 acting-agent memory 的一座桥。