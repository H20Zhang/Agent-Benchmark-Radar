# PerMemSafe：个性化 memory 会让通用 safety rule 不再够用

**中文** | [English](permemsafe.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[ACL 2026](https://aclanthology.org/2026.findings-acl.320/)

## 它到底测什么

PerMemSafe 评估长期 self-evolving agent 的 **implicit personalized safety**。一个对普通用户完全安全的回答，可能因为 memory 中积累的特定用户风险而变得危险；而且这些风险会随时间出现、变化或解除。

## 相比此前评测多测了什么

传统 safety benchmark 主要根据当前 prompt 与 context-independent policy 判断；personalized-memory benchmark 又通常奖励更丰富的 user modeling。PerMemSafe 把两者的张力暴露出来：个性化越强，agent 需要正确 retrieve 和推理的 latent safety context 反而越多。

## 决定性证据

论文报告，即使最强的被测 self-evolving agent，safety rate 也只有约 50%。SentinelMem 显式建模 personalized risk inference 与 memory evolution，相比既有 memory framework 把 implicit personalized safety 提升 23.8%，同时保持 helpfulness。

## 这个分数能证明什么

benchmark 能支持“memory-augmented agent 是否会在 evolving history 下识别 user-specific risk”的系统级判断；SentinelMem 的提升不能拆成某一个 memory operation 的因果增益，因为 risk extraction、update、retrieval 与 response policy 是联合设计的。

## 公平比较契约

应固定 backbone、conversation history、risk evolution、helpfulness task、safety policy 与 retrieval budget，并同时报告 safety 与 helpfulness；一律拒绝个性化服务不算优秀 memory system。stale-risk、resolved-risk、newly-emerging-risk 也应拆开报告。

## 还没有测什么

benchmark 不可能覆盖所有医疗/法律/物理风险与真实 user consent；错误推断个性化风险本身也可能造成伤害，敏感 risk memory 的长期 privacy/governance 又是另一层问题。

## 下一步最有判别力的验证

重点测 calibration：什么时候应该基于记忆风险直接行动，什么时候应该 clarification，什么时候应该把它判为 stale。frontier 不只是“记住 safety context”，而是管理 personalized risk belief 的 confidence 与 lifecycle。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验单看当前请求很正常、结合个人历史却需要谨慎处理的情形。个性化安全不仅要记住风险，还要在风险解除或条件变化后更新；永久沿用旧风险也会降低帮助质量。

### 一个具体任务长什么样

示意任务：早期历史表达了一项与服务选择相关的个体限制，之后该限制被明确修订。系统面对类似的新请求时，需要应用当前有效状态，而不是机械地沿用最早的安全判断。

### 最有判别力的实验

构造风险有效、风险已解除和无相关风险三组配对历史，固定当前请求。分别检查漏用相关记忆与过度沿用旧风险，并联合报告安全和帮助质量，才能评价更新策略而不是一律保守的回答倾向。

### 建议搭配

[longmemeval](longmemeval.md) · [memtrapbench](memtrapbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`generic safety → personalized memory → evolving personalized risk state`

它说明 personalization 和 safety 是耦合目标，不能再当成两个独立模块。