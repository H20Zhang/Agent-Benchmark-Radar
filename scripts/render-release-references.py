#!/usr/bin/env python3
"""Render frozen source-bounded historical references directly below note titles.

Standard library only. Never reads current result ledgers or selects a maximum.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- RELEASE-REFERENCE:START -->'
END = '<!-- RELEASE-REFERENCE:END -->'
BLOCK = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n*', re.S)
STATUSES = {'release-best', 'release-reference', 'diagnostic', 'later-version', 'paper-reference', 'unverified'}
LABELS = {
    'zh': {
        'release-best': '发布时最佳结果（历史参考）',
        'release-reference': '发布时结果（历史参考，非最佳声明）',
        'diagnostic': '发布时诊断结果（历史参考）',
        'later-version': '历史论文结果（非首版参考）',
        'paper-reference': '历史论文结果（首版归属待核验）',
        'unverified': '发布时最佳结果（待核验）',
    },
    'en': {
        'release-best': 'Best at release (historical reference)',
        'release-reference': 'Release result (historical reference; not a best claim)',
        'diagnostic': 'Release diagnostic (historical reference)',
        'later-version': 'Historical paper result (not the initial version)',
        'paper-reference': 'Historical paper reference (initial version unverified)',
        'unverified': 'Best at release (not yet verified)',
    },
}


def bilingual(value: object, label: str) -> None:
    if not isinstance(value, dict) or set(value) != {'zh', 'en'}:
        raise ValueError(f'{label}: expected matching zh/en text')
    for lang in ('zh', 'en'):
        if not isinstance(value[lang], str) or not value[lang].strip() or '\n' in value[lang]:
            raise ValueError(f'{label}.{lang}: expected a nonempty single line')


def validate_record(ident: str, record: dict) -> None:
    if record.get('status') not in STATUSES:
        raise ValueError(f'{ident}: unknown reference status')
    for field in ('period', 'scope', 'caveat'):
        bilingual(record.get(field), f'{ident}.{field}')
    source = record.get('source')
    if not isinstance(source, str) or urlsplit(source).scheme != 'https' or not urlsplit(source).netloc:
        raise ValueError(f'{ident}: expected primary HTTPS source')
    if not isinstance(record.get('locator'), str) or not record['locator'].strip():
        raise ValueError(f'{ident}: missing source location or explicit verification gap')
    results = record.get('results')
    if not isinstance(results, list):
        raise ValueError(f'{ident}: results must be an explicit list')
    if record['status'] == 'unverified' and results:
        raise ValueError(f'{ident}: unverified record must not publish numbers')
    if record['status'] in {'release-best', 'release-reference', 'later-version', 'paper-reference'} and not results:
        raise ValueError(f'{ident}: numerical result status needs an explicit result')
    if record['status'] == 'release-best' and (not record.get('comparison_scope') or record.get('initial_release') is not True):
        raise ValueError(f'{ident}: a best claim requires its comparison scope and initial version')
    if record['status'] in {'release-reference', 'diagnostic'} and record.get('initial_release') is not True:
        raise ValueError(f'{ident}: a release label requires an initial-version source')
    if record['status'] == 'paper-reference' and record.get('initial_release') is not None:
        raise ValueError(f'{ident}: unverified version identity must remain unknown')
    if record['status'] == 'later-version' and record.get('initial_release') is not False:
        raise ValueError(f'{ident}: later paper must be distinguished from launch')
    for row in results:
        for field in ('system', 'metric', 'score'):
            if not isinstance(row.get(field), str) or not row[field].strip() or '\n' in row[field]:
                raise ValueError(f'{ident}: result {field} must be a nonempty string')
        if 'scope' in row:
            bilingual(row['scope'], f'{ident}.result.scope')
        if 'source' in row:
            url = urlsplit(row['source'])
            if url.scheme != 'https' or not url.netloc:
                raise ValueError(f'{ident}: invalid result source')


def fallback(item: dict) -> dict:
    """Unknown remains unknown even if a newer live score exists elsewhere."""
    artifacts = item.get('artifacts', {})
    source = next((artifacts.get(k) for k in ('paper', 'preprint', 'project', 'code', 'data') if artifacts.get(k)), None)
    released = str(item.get('released', 'unknown'))
    return {
        'status': 'unverified',
        'period': {'zh': f'基准记录日期：{released}', 'en': f'Benchmark recorded date: {released}'},
        'scope': {'zh': '尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。', 'en': 'A best result tied to a model, metric, and protocol in the initial release has not yet been verified.'},
        'results': [], 'source': source,
        'locator': 'Initial-release score and comparison scope not yet verified.',
        'caveat': {'zh': '不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。', 'en': 'No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.'},
        'initial_release': None,
    }


def render_block(record: dict, lang: str) -> str:
    if lang not in ('zh', 'en'):
        raise ValueError('lang must be zh or en')
    label = LABELS[lang][record['status']]
    lines = [START, f'> **{label}** · {record["period"][lang]}  ']
    if record['results']:
        parts = []
        for row in record['results']:
            value = f'**{row["system"]} — {row["metric"]}: {row["score"]}**'
            if row.get('scope'):
                value += f' ({row["scope"][lang]})'
            if row.get('source') and row['source'] != record['source']:
                value += f' [{"来源" if lang == "zh" else "source"}]({row["source"]})'
            parts.append(value)
        separator = '；' if lang == 'zh' else '; '
        lines.append('> ' + separator.join(parts) + '  ')
    lines.append(f'> {record["scope"][lang]} [{"原始来源" if lang == "zh" else "Original source"}]({record["source"]})  ')
    lines.append(f'> {record["caveat"][lang]}')
    lines.append(END)
    return '\n'.join(lines)


def strip_reference(text: str) -> str:
    if text.count(START) != text.count(END) or text.count(START) > 1:
        raise ValueError('Duplicate or unbalanced release-reference markers')
    return BLOCK.sub('', text)


def render_note(text: str, record: dict, lang: str) -> str:
    clean = strip_reference(text)
    match = re.match(r'(#[^\n]*\n)(\n*)(.*)', clean, re.S)
    if not match:
        raise ValueError('Benchmark note must start with its existing H1')
    title, _gap, body = match.groups()
    return title + '\n' + render_block(record, lang) + '\n\n' + body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail without modifying stale notes')
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    items = json.loads((root / 'data/benchmarks.json').read_text(encoding='utf-8'))
    payload = json.loads((root / 'data/release-references.json').read_text(encoding='utf-8'))
    if payload.get('schema_version') != 1:
        raise ValueError('Unsupported release-reference schema version')
    references = payload['benchmarks']
    ids = {x['id'] for x in items}
    if len(ids) != len(items) or set(references) - ids:
        raise ValueError('Duplicate registry ID or orphan release-reference record')
    stale, pending = [], []
    counts = {status: 0 for status in sorted(STATUSES)}
    for item in items:
        record = references.get(item['id'], fallback(item))
        validate_record(item['id'], record)
        counts[record['status']] += 1
        for lang, ext in (('zh', ''), ('en', '.en')):
            path = root / f'benchmarks/{item["id"]}{ext}.md'
            old = path.read_text(encoding='utf-8')
            new = render_note(old, record, lang)
            if old != new:
                stale.append(path.relative_to(root).as_posix())
                pending.append((path, new))
    print(f'Release references: {len(items)} benchmarks / {len(items)*2} bilingual notes; {counts}')
    if args.check and stale:
        print('Stale release references: ' + ', '.join(stale))
        return 1
    if not args.check:
        for path, new in pending:
            path.write_text(new, encoding='utf-8')
    print('Release references ' + ('verified' if args.check else 'rendered') + f'; changed projections: {len(stale)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
