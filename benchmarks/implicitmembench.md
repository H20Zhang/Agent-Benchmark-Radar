# ImplicitMemBench：不经显式回忆也会改变第一反应的记忆

**中文** | [English](implicitmembench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2604.08064) · [ACL 2026](https://aclanthology.org/2026.acl-long.1301/) · [项目页](https://www.chonghanqin.com/project/implicitmembench/)

## 它到底测什么

ImplicitMemBench 测 **implicit / non-declarative memory**：过去的学习、priming 或 conditioning 能不能在测试 prompt 没有要求显式回忆时，自动改变 agent 的第一次行为。它统一覆盖 Procedural Memory、Priming 和 Classical Conditioning，并采用 learn/prime → interference → test 的流程。

## 相比此前评测多测了什么

传统长期 memory benchmark 主要奖励 declarative access：找回事实、回答问题、总结历史。这里把可观测量改成“过去经历是否在需要时直接改变行为”。first-attempt scoring 很关键，因为允许反复 prompting 后，原本的 implicit effect 会重新退化为显式推理问题。

## 决定性证据

在 300 个 item、17 个模型上，没有模型总体超过 66%。论文报告 DeepSeek-R1 65.3、Qwen3-32B 64.1、GPT-5 63.0；更有信息量的是 inhibition 与 preference 的明显不对称：17.6% 对 75.0%。这意味着模型更容易形成正向偏好，而不擅长抑制已经被 prime 的行为。

## 这个分数能证明什么

它证明的是 **prior exposure 是否造成行为适应**，不应直接被解释成外部 agent-memory store 的能力。model context、prompt、latent adaptation 和显式 memory module 都可能影响结果。因此它首先是 measurement target 的扩展，而不是干净的 memory component benchmark。

## 公平比较契约

需要固定 backbone/version、learning examples、interference sequence、test prompt、decoding policy 与 first-attempt rule。若一边允许显式 reflection/retrieval loop，另一边只看即时第一反应，比较对象已经从 implicit memory 变成了 explicit reasoning。

## 还没有测什么

它没有证明这种学习能跨越长期真实时间，也没有定位行为变化究竟存在哪里。安全相关的持久性、forgetting、跨任务 transfer，以及与 external memory 的交互仍是空白。

## 下一步最有判别力的验证

在同一个模型上比较 no-memory、episodic retrieval、procedural summary、learned skill representation，并保持 test prompt 完全一致。真正的问题是：哪种 representation 能提升 first-action transfer，同时又不引入有害的过度持久化。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合诊断经历是否在没有显式回忆要求时改变首次行为。它强调自动使用而非事实复述；短学习片段中的行为变化不能直接当作跨会话、长期持久的外部记忆能力。

### 一个具体任务长什么样

示意任务：学习阶段展示一种操作惯例，插入干扰内容后出现相关场景，测试系统的第一反应是否遵循所学规则。允许多次修正会改变测量对象，因此首次尝试与重试后成功应分开。

### 最有判别力的实验

保持学习内容相同，分别在同一上下文、新会话加外部记忆和完全无记忆条件下测试。再增加干扰距离，判断效果来自最近上下文、持久记忆还是响应偏置；不要用同一会话成绩声称长期记忆已成立。

### 建议搭配

[evomembench](evomembench.md) · [past-bench](past-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`explicit recall → retained experience → automatic behavior change`

它把 memory 从“存了什么”推进到“经历是否已经改变行为”。