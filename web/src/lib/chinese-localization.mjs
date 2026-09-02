const PHRASE_REPLACEMENTS = [
  ["memory write representation", "记忆写入表征"],
  ["write-side representation", "写入侧表征"],
  ["write representation", "写入表征"],
  ["write-time enrichment", "写入时增强"],
  ["write enrichment", "写入增强"],
  ["memory pipeline", "记忆流程"],
  ["memory system", "记忆系统"],
  ["memory corpus", "记忆语料"],
  ["query distribution", "查询分布"],
  ["query expansion", "查询扩展"],
  ["query set", "查询集合"],
  ["retrieval accessibility", "检索可达性"],
  ["retrieval failure", "检索失败"],
  ["retrieval family", "检索方法类别"],
  ["retrieval gain", "检索收益"],
  ["retrieval top-k", "检索 top-k"],
  ["retrieval-only", "仅检索"],
  ["downstream benchmark", "下游基准"],
  ["full-context", "完整上下文"],
  ["research claim", "研究主张"],
  ["canonical record", "规范记录"],
  ["gold definition", "标准答案定义"],
  ["test set", "测试集"],
  ["leaderboard", "排行榜"],
  ["benchmark", "基准"],
  ["protocol", "评测协议"],
  ["split", "数据切分"],
  ["downstream", "下游"],
  ["reranker", "重排模型"],
  ["embedder", "嵌入模型"],
  ["embedding model", "嵌入模型"],
  ["answerer", "回答模型"],
  ["retrieval", "检索"],
  ["query", "查询"],
  ["memory", "记忆"],
  ["utility", "效用"],
  ["enrichment", "增强"],
  ["intervention", "干预"],
  ["corpus", "语料"],
  ["reader", "阅读模型"],
  ["evidence", "证据"],
  ["task", "任务"],
  ["environment", "环境"],
];

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

function replaceLowercaseTechnicalTerms(text) {
  let output = String(text ?? "");
  for (const [from, to] of PHRASE_REPLACEMENTS) {
    const escaped = from.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    output = output.replace(new RegExp(`\\b${escaped}\\b`, "g"), to);
  }
  return output;
}

export function localizeChineseProse(value, lang) {
  if (lang !== "zh" || value == null) return value;
  return replaceLowercaseTechnicalTerms(value);
}

export function localizeChineseHtml(html, lang) {
  if (lang !== "zh" || !html) return html;
  const protectedBlocks = [];
  let safe = String(html).replace(/<(code|pre)\b[^>]*>[\s\S]*?<\/\1>/gi, (block) => {
    const token = `__ZH_PROTECTED_${protectedBlocks.length}__`;
    protectedBlocks.push(block);
    return token;
  });
  safe = safe.split(/(<[^>]+>)/g).map((chunk) => chunk.startsWith("<") ? chunk : replaceLowercaseTechnicalTerms(chunk)).join("");
  protectedBlocks.forEach((block, index) => {
    safe = safe.replace(`__ZH_PROTECTED_${index}__`, block);
  });
  return safe;
}

export function localizeTechnicalToken(value, lang, fallbackFormatter) {
  if (lang !== "zh") return fallbackFormatter ? fallbackFormatter(value) : value;
  return TOKEN_ZH.get(String(value)) || (fallbackFormatter ? fallbackFormatter(value) : value);
}
