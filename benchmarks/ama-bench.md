# AMA-Bench：从 conversation memory 转向 agent trajectory memory

**中文** | [English](ama-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.22769) · [代码](https://github.com/AMA-Bench/AMA-Bench) · [项目页](https://ama-bench.github.io/)

## 它在测什么

AMA-Bench 的 memory source 是 agent 与环境交互产生的 trajectories，而不是只来自 human-agent dialogue。官方套件覆盖 GAIA、WebArena、BALROG、ALFWorld、SWE-bench 等真实/近真实 agent 场景，并通过统一的 `memory_construction → memory_retrieve` 两阶段接口比较 long context、RAG 与 memory-agent methods；项目页报告主实验共评 2,471 个 QA pairs。

## 相比什么前进了

LoCoMo / LongMemEval 主要回答“过去对话里发生了什么”。AMA-Bench 把需要记住的对象改成 action、objective state、causal transition 与工具执行经验，因此更接近 agent 真正需要复用的 experience。统一两阶段接口也比完全自由的 agent stack 更有利于观察 memory construction 与 retrieval 的差异。

## 决定性证据与分数边界

官方结果明确显示 long-context baseline 会随 trajectory horizon 增长而退化，并提供 recall、causal inference、state updating、state abstraction 等分项。当前项目页同时出现两组不同的 AMA-Agent headline 数字（55.80%/+10.88pp 与 57.22%/+11.16pp），因此 Radar 不把其中任意一组未经版本解释的数字写成唯一“当前最好”。这正说明成绩追踪必须绑定具体 snapshot、base model 与 judge，而不是只复制首页 headline。

## 公平比较条件

锁定 Qwen3-32B 等 base model、open-ended QA split、LLM-as-judge、trajectory subset 与 memory interface。官方仓库还展示不同 judges 的严格程度差异，因此 judge 变化本身足以移动绝对 accuracy。跨 judge、跨 backbone 的数字应拆成不同 tracks。

## 下一步评测坐标

AMA-Bench 已把 memory 放进 agent trajectories，但终点仍是 trajectory QA。下一步应直接执行未来 tasks，验证记忆到的 workflow/causal knowledge 是否提升 action success，并同时计入 memory construction 与 retrieval cost。
