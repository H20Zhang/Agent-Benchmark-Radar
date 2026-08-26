# KBGym / Training a Knowledge Base

- **测量对象：** curator 看过监督问答和 gold 后编辑持久知识库，冻结后的 store 是否让独立 reader 用更少行动回答训练内与覆盖分层的未见问题。
- **最近前身：** HippoRAG 等离线结构化是全语料无监督索引；这里把 `(question, answer)` 当训练信号，并显式测结构覆盖。
- **决定性证据：** v2 将 trained-question 结果修正为 25% action saving 与 +.294 F1；both-key 未见问题为 +.176 F1，one-key 为 +.059，neither-key 无收益。
- **结论上限：** 支持收益随 answer-key coverage 变化；只有 27.6% corpus 被覆盖，不能宣称普遍改善知识库。
- **最强混淆：** 单 seed、curator/reader 同模型家族、synthetic atomic documents 与 adapted baselines。
- **未覆盖：** 跨模型迁移、多 seed、自然语料、在线/prequential evaluation。
- **谱系：** 让 corpus 从静态输入变成可训练且可冻结审计的状态对象；`map_delta=early_signal`。

Primary: https://arxiv.org/abs/2608.21829

