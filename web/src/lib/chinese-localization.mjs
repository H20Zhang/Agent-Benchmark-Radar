const TOKEN_ZH = new Map([
  ["long-range-recall", "长程召回"],
  ["temporal-reasoning", "时间推理"],
  ["knowledge-update", "知识更新"],
  ["multi-hop", "多跳推理"],
  ["multi-session", "跨会话"],
  ["retrieval", "检索"],
  ["reasoning", "推理"],
  ["planning", "规划"],
  ["tool-use", "工具使用"],
  ["web-search", "网页搜索"],
  ["live-web", "实时网页"],
  ["text-to-sql", "Text-to-SQL"],
  ["code-generation", "代码生成"],
  ["data-analysis", "数据分析"],
  ["machine-learning", "机器学习"],
  ["multimodal", "多模态"],
  ["long-context", "长上下文"],
  ["agentic-search", "Agentic Search"],
  ["rag", "RAG"],
  ["structured-data", "结构化数据"],
  ["unstructured-data", "非结构化数据"],
  ["interactive", "交互式"],
  ["offline", "离线"],
  ["online", "在线"],
  ["static", "静态"],
  ["dynamic", "动态"],
]);

/** Authored prose is immutable at presentation time. Translate at its canonical source. */
export function localizeChineseProse(value, lang) {
  return value;
}
export function localizeChineseHtml(html, lang) {
  return html;
}
export function localizeTechnicalToken(value, lang, fallbackFormatter) {
  if (lang === "zh" && TOKEN_ZH.has(String(value)))
    return TOKEN_ZH.get(String(value));
  return fallbackFormatter ? fallbackFormatter(value) : value;
}
