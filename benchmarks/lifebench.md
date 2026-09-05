# LifeBench：长期 memory 不只包括显式事实

**中文** | [English](lifebench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.03781) · [代码与数据合成](https://github.com/1754955896/LifeBench)

## 它到底测什么

LifeBench 评估 agent 能否在长期、多源 life-event stream 中整合 **declarative 与 non-declarative memory**。除了显式的 episodic / semantic fact，它还要求从分散在时间和数据源中的重复行为推断 habit 与 procedure。

## 相比此前评测多测了什么

conversation-memory benchmark 主要编码“用户明确说过什么”；LifeBench 开始问“用户反复做过什么，因此可以推断出什么”。长周期事件模拟彼此关联，并注入现实先验，所以好的 representation 不能只把每条 event 当作独立 chunk 去 retrieve，还要做跨事件 aggregation 与 behavioral abstraction。

## 决定性证据

论文报告当前最强一批 memory system 的准确率也只有 55.2%。这里的难度不只是 context length，而是 semantic、episodic、habitual、procedural memory 混合在多源 trace 里，需要做 evidence integration 与行为模式推断。

## 这个分数能证明什么

LifeBench 能支持系统整体是否会重建和推理长期生活模式，但不能干净地区分 retrieval、aggregation 与 inference 的贡献；同时 synthetic event generator 中的行为先验未必等价于真实用户。

## 公平比较契约

应固定 event stream、backbone、可访问 source、temporal cutoff、retrieval budget 与 answer evaluator，并按 memory type 拆分报告，否则 explicit episodic fact 上的强表现会掩盖 habit/procedure 的失败。评估早期时间点时必须防止 future-event leakage。

## 还没有测什么

真实个人数据更稀疏、更矛盾、更隐私，而且 habit / intent 往往没有客观 label；benchmark 也没有判断推断出的 habit 是否应该被长期保存，或能否在未经确认时直接用于行动。

## 下一步最有判别力的验证

把 inferred habit/procedure 连接到未来 decision，再加入用户显式 correction，测试系统能否既推断 latent pattern，又在行为变化时及时撤销旧判断。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究分散行为中的习惯和程序性知识，而不是把记忆限定为明确说过的事实。选用时应强调跨来源推断；合成生活轨迹上的正确画像，尚不能证明系统理解真实用户或拥有实际个性化效用。

### 一个具体任务长什么样

示意任务：多个来源分别记录用户在不同情境下的重复行为，之后的问题不直接复述某一条记录，而要求归纳惯常做法。系统需要聚合经历，同时避免把一次偶然行为升级为稳定习惯。

### 最有判别力的实验

比较单来源、完整多来源和来源标识被打乱的输入，固定推理模型与记忆预算。按显式事实、习惯推断和程序知识分项报告；如果只在来源模式固定时有效，应优先检验生成器先验，而非宣称通用用户理解。

### 建议搭配

[dynamicmem](dynamicmem.md) · [memfusebench](memfusebench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`explicit conversational facts → multi-source life traces → inferred habitual/procedural memory`

它把 memory 的对象从“用户说了什么”扩展到“用户长期行为里有什么规律”。