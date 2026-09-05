# MemGUI-Bench：跨步骤、跨 App、跨 session 的可执行 GUI memory

**中文** | [English](memgui-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.06075) · [项目页](https://lgy0404.github.io/MemGUI-Bench/) · [代码](https://github.com/lgy0404/MemGUI-Bench)

## 它到底测什么

MemGUI-Bench 把 memory 放进 **真实 mobile GUI action trajectory**：agent 要在多步骤、多个 App、重复尝试乃至跨 session 之间保留信息，并用先前经验继续操作。memory 可能是视觉状态、一次操作结果、某个 App 的 procedure，或者在另一个应用里看到的信息。

## 相比此前评测多测了什么

传统 mobile-agent benchmark 主要看当前屏幕 grounding 和一次性 task completion。MemGUI-Bench 对现有 benchmark 的审计发现，真正依赖 memory 的任务只占很小比例，而且几乎不测 cross-session learning。因此它把 temporal/spatial retention 与 experience reuse 从长 trajectory 的副作用提升成任务本身。

## 决定性证据

套件包含 128 个任务、26 个 App、68 个 scenario，其中 89.8% 被归为 memory-intensive；论文评估 5 类架构下的 11 个 agent，并用 progressive scrutiny 和多个 memory-oriented metric 评估。结果显示即使较强 GUI agent，在跨时间或跨应用的信息依赖上仍有明显空间。

## 这个分数能证明什么

task success 与 repeated-attempt 指标反映的是 **GUI perception × memory × planning × execution** 整体系统。它不能单独证明某个 memory module 更强，因为 OCR/vision、app grounding、click execution 或 recovery 都可能在 memory 已经取对后继续失败。

## 公平比较契约

要固定 device/emulator state、App 版本、账号/数据状态、action budget、retry 数、observation resolution 和 model/harness。首轮成功率应与多次尝试后的提升分开报告，否则更强的基础 GUI policy 容易被误认为更会复用经验。

## 还没有测什么

真实 App 会持续更新，reproducibility 依赖环境 snapshot；benchmark 也还没有证明跨数周/月的 retention、跨 App privacy-aware memory，或 procedure 对新版本界面的迁移能力。

## 下一步最有判别力的验证

设计完全相同初始 UI state 下的 fresh-agent vs experienced-agent paired run，并加入 oracle-memory injection，直接估计 retained experience 相比 generic GUI competence 的边际贡献。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究跨应用与跨尝试的经验是否改善移动界面操作。重试次数本身会增加成功机会，因此应区分记忆带来的迁移与单纯多试几次；界面识别错误也不能全部归到记忆模块。

### 一个具体任务长什么样

示意任务：一次界面操作暴露了路径或失败原因，后续镜像任务在相关场景中再次出现。系统需要复用有效经验并识别当前界面差异，而不是原样重放旧点击序列。

### 最有判别力的实验

固定设备快照、视觉骨干和尝试总数，比较无记忆、原始轨迹与提炼经验。除 pass@k 外报告首次成功和每次尝试成本，再按跨步骤、跨应用与跨会话拆分，检查收益发生在哪种迁移距离。

### 建议搭配

[memoryarena](memoryarena.md) · [mem2actbench](mem2actbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-session GUI grounding → cross-step retention → cross-session experience reuse`

它把重复 GUI 操作真正变成了 memory-learning 问题，而不是更长的一次性轨迹。