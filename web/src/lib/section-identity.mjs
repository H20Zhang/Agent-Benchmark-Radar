/** Semantic section identity is independent of language and Markdown heading level. */
const sections = {
  use: ["什么时候值得用", "When to use it"],
  measurement: ["它到底测什么", "它在测什么", "测量对象", "What it measures", "What it actually measures", "Measurement target"],
  contribution: ["相比此前评测多测了什么", "相比什么前进了", "What it adds", "What it adds over prior work", "What changed relative to prior evaluation", "Compared with what"],
  results: ["当前成绩说明了什么", "What the reported results show", "What the results show", "Decisive evidence"],
  boundary: ["这个分数能证明什么", "结论上限", "分数支持的判断", "结论边界", "分数边界", "决定性证据与分数边界", "What the score establishes", "What the score supports", "Score ceiling", "Score boundary", "Decisive evidence and score boundary"],
  controls: ["公平比较契约", "公平比较条件", "最强混淆", "Fair-comparison contract", "Fair comparison contract", "Strongest confounder", "Fair comparison conditions"],
  example: ["一个具体任务长什么样", "What a concrete task looks like", "A concrete task example"],
  next: ["最有判别力的实验", "下一步最有判别力的验证", "下一步验证", "剩余缺口与下一步", "下一步评测坐标", "Most discriminating experiment", "Next discriminating evaluation", "Next discriminating validation", "Remaining gap and next validation", "Next evaluation coordinate"],
  gaps: ["还没有测什么", "What remains unmeasured", "What it does not measure"],
  related: ["建议搭配", "Recommended complements", "Pair with", "Suggested complements"],
  decision: ["研究决策卡", "Research decision card"],
  evolution: ["演化位置", "Evolutionary position", "Position in the evaluation landscape", "Genealogy"],
};
const normalize = text => text.trim().toLocaleLowerCase().replace(/[：:。.]$/u, "");
const byName = new Map(Object.entries(sections).flatMap(([key,names]) => names.map(name => [normalize(name),key])));
export function sectionIdentity(text) {return byName.get(normalize(text));}
export function pairedHeadingMap(headings, alternate) {
  const occurrence = new Map();
  return Object.fromEntries(headings.map(heading => {
    const key = sectionIdentity(heading.text);
    const index = occurrence.get(key) || 0; occurrence.set(key,index+1);
    const target = key ? alternate.filter(h => sectionIdentity(h.text) === key)[index] : alternate.find(h => h.text === heading.text);
    return [heading.id, target?.id || "interpretation"];
  }));
}
