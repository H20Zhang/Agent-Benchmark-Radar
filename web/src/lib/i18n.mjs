export const LOCALES = /** @type {const} */ (["zh", "en"]);
export const AREAS = /** @type {const} */ ([
  "agent-memory",
  "rag",
  "data-agent",
]);

const COPY = {
  zh: {
    langTag: "zh-CN",
    languageName: "中文",
    siteName: "Agent Benchmark Radar",
    nav: {
      explorer: "筛选 Radar",
      methodology: "评测方法",
      github: "GitHub",
      language: "English",
    },
    hero: {
      eyebrow: "面向 Agent 评测设计的研究索引",
      title: "找到真正匹配研究问题的 Benchmark",
      description:
        "按能力、环境、协议与演进阶段浏览 Agent Memory、Agentic Retrieval 和 Data Agents 评测。",
      primaryAction: "开始筛选",
      secondaryAction: "查看方法",
      registry: "完整 registry",
      areas: "研究领域",
      updated: "最近核验",
    },
    filters: {
      title: "缩小评测空间",
      search: "搜索 benchmark、能力或协议",
      searchPlaceholder: "例如 temporal reasoning、live web、text-to-SQL",
      area: "研究领域",
      role: "演进阶段",
      artifact: "开放资源",
      year: "发布年份",
      advanced: "更多条件",
      capability: "能力",
      environment: "环境",
      protocol: "评测协议",
      sort: "排序",
      reset: "查看全部",
      results: "个 benchmark",
      expandResults: "调整条件以扩展结果",
      sortOptions: {
        newest: "最新发布",
        oldest: "最早发布",
        citations: "引用上下文",
        name: "名称 A–Z",
      },
    },
    roles: {
      precursor: "前身",
      foundation: "基石",
      transition: "过渡",
      frontier: "前沿",
    },
    artifacts: { paper: "论文", code: "代码", data: "数据" },
    card: {
      released: "发布",
      citations: "引用",
      openDetail: "查看评测设计",
      verified: "核验",
    },
    detail: {
      measurement: "测量推进",
      scale: "评测规模",
      capabilities: "能力覆盖",
      environments: "评测环境",
      protocols: "评测协议",
      sources: "开放资源与来源",
      citationContext: "引用上下文",
      lastVerified: "最后核验",
      backToArea: "返回领域",
      registryRecord: "查看 registry",
      githubExplainer: "阅读 GitHub 解读",
    },
    areas: {
      "agent-memory": {
        label: "Agent Memory",
        short: "长期状态与经验",
        intro:
          "评测从跨会话事实召回扩展到在线更新、结构化与多模态记忆、行动衔接、隐私控制和全生命周期完整性。",
      },
      rag: {
        label: "RAG / Agentic Retrieval",
        short: "证据发现与执行",
        intro:
          "评测从文档相关性扩展到多跳证据、实时搜索、跨来源执行、轨迹审计与持续演化的语料状态。",
      },
      "data-agent": {
        label: "Data Agents",
        short: "数据工作流与研究",
        intro:
          "评测从 Text-to-SQL 与代码生成扩展到完整分析、长时程 ML engineering、统计与因果研究及业务语义可靠性。",
      },
    },
    footer: {
      statement: "把 benchmark 当作测量仪器，而不是排行榜。",
      data: "Machine-readable data",
    },
  },
  en: {
    langTag: "en",
    languageName: "English",
    siteName: "Agent Benchmark Radar",
    nav: {
      explorer: "Explore Radar",
      methodology: "Methodology",
      github: "GitHub",
      language: "中文",
    },
    hero: {
      eyebrow: "A research index for agent evaluation design",
      title: "Find the benchmark that matches the research question",
      description:
        "Explore Agent Memory, Agentic Retrieval, and Data Agent evaluations by capability, environment, protocol, and evolution stage.",
      primaryAction: "Explore benchmarks",
      secondaryAction: "Read methodology",
      registry: "Complete registry",
      areas: "Research areas",
      updated: "Latest verification",
    },
    filters: {
      title: "Narrow the evaluation space",
      search: "Search benchmarks, capabilities, or protocols",
      searchPlaceholder: "Try temporal reasoning, live web, or text-to-SQL",
      area: "Research area",
      role: "Evolution stage",
      artifact: "Open resources",
      year: "Release year",
      advanced: "More filters",
      capability: "Capability",
      environment: "Environment",
      protocol: "Evaluation protocol",
      sort: "Sort",
      reset: "View all",
      results: "benchmarks",
      expandResults: "Adjust filters to expand the result set",
      sortOptions: {
        newest: "Newest release",
        oldest: "Earliest release",
        citations: "Citation context",
        name: "Name A–Z",
      },
    },
    roles: {
      precursor: "Precursor",
      foundation: "Foundation",
      transition: "Transition",
      frontier: "Frontier",
    },
    artifacts: { paper: "Paper", code: "Code", data: "Data" },
    card: {
      released: "Released",
      citations: "Citations",
      openDetail: "Inspect evaluation design",
      verified: "Verified",
    },
    detail: {
      measurement: "Measurement advance",
      scale: "Evaluation scale",
      capabilities: "Capability coverage",
      environments: "Evaluation environments",
      protocols: "Evaluation protocols",
      sources: "Open resources and sources",
      citationContext: "Citation context",
      lastVerified: "Last verified",
      backToArea: "Back to area",
      registryRecord: "View registry",
      githubExplainer: "Read GitHub explainer",
    },
    areas: {
      "agent-memory": {
        label: "Agent Memory",
        short: "Long-term state and experience",
        intro:
          "Evaluation expands from cross-session factual recall to online updates, structured and multimodal memory, action, privacy control, and lifecycle integrity.",
      },
      rag: {
        label: "RAG / Agentic Retrieval",
        short: "Evidence discovery and execution",
        intro:
          "Evaluation expands from document relevance to multi-hop evidence, live search, cross-source execution, trajectory audit, and continuously evolving corpora.",
      },
      "data-agent": {
        label: "Data Agents",
        short: "Data workflows and research",
        intro:
          "Evaluation expands from text-to-SQL and code generation to complete analytics, long-horizon ML engineering, statistical and causal research, and business-semantic reliability.",
      },
    },
    footer: {
      statement: "Treat benchmarks as measurement instruments, not a leaderboard.",
      data: "Machine-readable data",
    },
  },
};

/** @param {"zh" | "en" | string} lang */
export function copyFor(lang) {
  const copy = COPY[lang];
  if (!copy) throw new Error(`Unsupported locale: ${lang}`);
  return copy;
}

/** @param {"zh" | "en"} lang */
export function otherLocale(lang) {
  return lang === "zh" ? "en" : "zh";
}
