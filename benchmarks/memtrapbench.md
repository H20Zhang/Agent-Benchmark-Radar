# MemTrapBench

- **测量对象：** 当历史记忆被正确保存且与当前问题语义相关时，智能体能否判断它是否仍应影响当前推理，而不是机械复用。
- **最近前身：** LoCoMo / LongMemEval 一类评测主要问“能否回忆”；MemTrapBench 把失败坐标转到“相关记忆是否应该被采用”。
- **决定性证据：** 同一当前任务配对比较 memory 与 no-memory 条件；四个子集共 1,050 个多轮样例，覆盖 reasoning fixation 与 belief distortion。作者报告所有受测 memory strategy 均低于 no-memory，最强下降超过 10 个百分点。
- **结论上限：** 分数支持“在刻意构造的上下文转移中，相关但不再有效的历史记忆会造成可测负效应”；它不支持“长期记忆平均而言有害”。
- **最强混淆：** 最终问题被设计为不依赖历史即可作答，因此 no-memory 天然避开 planted prior；合成对话、judge、framework × backbone 交互会影响下降幅度。
- **未覆盖：** 自然工作流里这类 harmful reuse 的真实发生率，以及智能体在开放环境中自主判定记忆适用边界的能力。
- **谱系：** `early_signal`。与 staleness/update benchmark 形成“memory validity before use”方向的独立证据，但单篇工作不足以改写 durable Benchmark Map。

Primary: https://arxiv.org/abs/2608.20202
