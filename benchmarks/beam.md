# BEAM：把长期记忆压力推到 10M-token coherent conversations

**中文** | [English](beam.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2510.27246) · [代码](https://github.com/mohammadtavakoli78/BEAM)

## 它在测什么

BEAM 用 100 段连贯对话和 2,000 个验证问题，把历史长度分到 128K、500K、1M 和 10M tokens，并覆盖十类 memory abilities。相比随机拼接 needle，它强调 narrative coherence、跨事件关系以及随长度增长的退化，因此能直接观察 long-context / RAG 在极长历史上的 scaling failure。

## 相比什么前进了

LoCoMo 把 multi-session 对话拉到约 16K tokens；BEAM 把同类问题推进到百万乃至千万 token，并让 conversation 仍保持主题和互动结构。它测的是“memory quality 随 horizon 扩大是否崩掉”，而不只是某个固定 context size 的最终准确率。

## 决定性证据与分数边界

论文报告：即使支持 1M context 的 LLM、包括带 retrieval augmentation 的版本，也会随着 dialogue length 增长明显退化；作者的 LIGHT memory framework 相比各 backbone 的 strongest baseline 平均提升约 3.5%–12.69%，且 episodic memory、working memory、scratchpad 的 ablation 显示三者均有互补贡献。这证明 BEAM 能暴露 scale-induced failure；但 LIGHT 的增益仍是 bundled design evidence，不能从总分单独推导某个 component 的普遍因果优势。

## 公平比较条件

必须锁定 backbone、context-window support、conversation length bucket、retrieval budget 与问题类型。128K 与 10M 的分数不能混成一个不加权的“当前最好”；不同模型是否真正支持完整输入也会改变系统可见证据。

## 下一步评测坐标

BEAM 仍以 synthetic coherent conversation + QA 为主。下一步需要把同样的 million-token pressure 放到真实 agent trajectories、持续写入/更新以及未来 action success 上。
