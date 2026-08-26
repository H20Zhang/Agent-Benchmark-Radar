# LitReview Arena / LitReviewBench / LitJudge

- **测量对象：** 面向开放式文献综述，用领域专家的 pairwise preference 评价覆盖、claim support、结构、研究建议与总体 utility，并校准自动 judge。
- **最近前身：** DeepSurveyBench 等静态评估缺少大规模 topic-matched expert preference；SciArena 的竞技协议又未针对完整综述拆维度。
- **决定性证据：** 非人工系统对 human draft 的 decisive overall win 仅 23.0%；通用 judge 与专家 utility 的 ρ=.467，LitJudge 提升到 .792。
- **结论上限：** 支持 expert-calibrated evaluator 更贴近该数据上的专家排序；不能把 agentic-vs-base 差距归因于架构，因为 token/tool/search budget 未匹配。
- **最强混淆：** 专有系统预算不同，公开数据缺少 raw replicate annotations 与完整书面理由。
- **未覆盖：** 领域规范差异、living review、citation verification、cost matching 与真正 held-out judge validation。
- **谱系：** 把 deep-research 评价从结果 rubric 推到专家偏好校准；`map_delta=early_signal`。

Primary: https://arxiv.org/abs/2608.21374

