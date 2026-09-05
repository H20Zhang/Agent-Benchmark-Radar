# LifeSide：长期用户理解不等于 factual recall

**中文** | [English](lifeside.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

LifeSide 将长期个人 memory 扩展到 2,000 个 personas、约 111K tasks，覆盖 memory tracking、user understanding、privacy control 与 emotional companionship。它关心的不只是“用户以前说过什么”，而是系统是否能从长期互动形成适当、受边界约束的用户模型并据此响应。

## 相比什么前进了

LoCoMo/LongMemEval 主要围绕对话事实和推理。LifeSide 把长期 user understanding、隐私与陪伴质量放进同一评测空间，直接挑战“现有 memory benchmark 已接近饱和，因此 personalized memory 已解决”的前提。

## 决定性证据与分数边界

论文报告即使在既有 memory benchmarks 上接近饱和的模型，面对长期 user understanding 与 companionship 仍明显失败。这个结果支持 benchmark coverage 存在缺口；它不证明任何单一 memory architecture 是瓶颈，因为 backbone、persona construction 与 judge 共同影响结果。

## 公平比较条件

需要锁定 persona/history generation、privacy policy、answerer 与 judge，并按 task family 分开看。将 factual recall 与 emotional/privacy tasks 压成一个总分会掩盖能力结构。

## 下一步评测坐标

下一步应把长期用户模型连接到真实 permission、deletion、tool-mediated actions 与错误个性化的外部后果。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合观察长期陪伴任务中记忆、用户理解和隐私控制的交互，而不是给记忆模块单独排名。人格与环境均来自模拟时，结果首先说明系统在这些模拟规则下的表现，真实长期关系的外推需要另外验证。

### 一个具体任务长什么样

示意任务：同一用户跨会话改变目标或情绪，助手需要利用相关历史，同时避免在不合适的场景暴露个人内容。回答是否贴合用户与信息是否被恰当地使用，是两个需要同时评价的维度。

### 最有判别力的实验

在相同模拟用户轨迹上独立改变记忆策略与隐私策略，报告帮助质量和不当披露，而非只看综合奖励。再更换未参与开发的模拟器，检查结果是否主要依赖人格生成方式或评价模型偏好。

### 建议搭配

[dynamicmem](dynamicmem.md) · [gatemem](gatemem.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
