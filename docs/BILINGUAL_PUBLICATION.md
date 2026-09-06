# Chinese-First Bilingual Publication Contract

Agent Benchmark Radar is bilingual, with Simplified Chinese as the default reader experience.

## Public file convention

- `README.md` — default Simplified Chinese landing page.
- `README.en.md` — complete English counterpart.
- Reader-facing Benchmark Library/genealogy pages, high-value benchmark notes, and public weekly/monthly/yearly synthesis should have both Chinese and English forms.
- Canonical registry, schemas, maintenance docs, scheduler prompts, and validation output remain single-source. **No public operational run logs.** `runs/README.md` is static policy only; operational traces remain only in ignored `.radar-private/` state or ephemeral Agent memory.

## One judgment, two editorial projections

Chinese and English derive from one semantic benchmark judgment: identity, importance/evolution role, predecessor, measurement delta, protocol facts, what a score supports, strongest confounder, coverage gap, genealogy, and links.

Chinese is the primary editorial surface. English preserves the same depth rather than becoming a shortened translation. Material interpretation changes update both public variants in the same transaction.

## Terminology

Keep benchmark/paper titles, dataset/model/metric/tool/protocol names, and standard acronyms in canonical English when that improves search and precision. Do not mechanically repeat bilingual terminology after it is established.

## Editorial quality

Chinese should be natural technical Chinese rather than translated English syntax. Warn on repeated empty transitions and templates such as `真正重要的是…`, `关键不在于…而在于…`, `值得注意的是…` when they become house style.

English follows the same Research Radar Editor standard: concrete language, predecessor/comparison before praise, explicit attribution boundaries, and no repetitive LLM sentence skeletons.

## Canonical content and rendering

`data/locales/zh/benchmarks.json` stores the Chinese one-sentence descriptions keyed
by stable registry id. English descriptions stay in the canonical registry.
The website does not parse README tables for its content. Both README variants
are generated projections of those same descriptions, date events, result counts
and evaluation recipes. Run `node web/scripts/sync-publication.mjs`, then its
`--check` mode; CI rejects stale projections.

Long-form `benchmarks/<id>.md` and `<id>.en.md` remain authored sources. A Markdown
AST renderer preserves paragraphs, negation, lists, tables and code; it removes
maintenance comments and resolves relative note links to their actual web routes.
It never performs global term replacements or rewrites caveats as opportunities.
The brief selects complete maintained sections from the appropriate language note.
English-only scale/protocol metadata is labeled as source wording rather than
presented as a pseudo-translated Chinese sentence.
