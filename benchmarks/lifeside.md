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
