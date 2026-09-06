import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {loadRegistry} from "../src/lib/registry.mjs";
import {loadAllResultSets} from "../src/lib/results.mjs";
import {loadDeepRead, getAuthoredBrief} from "../src/lib/deep-reads.mjs";
import {getStableFacetValues} from "../src/lib/research-model.mjs";
import {parseFilterState, serializeFilterState, filterBenchmarks, replaceFilterDimension, migrateFacetParams} from "../src/lib/filters.mjs";
import {translatedFragment, writePageState} from "../src/scripts/page-state.mjs";
const registry=loadRegistry(), sets=loadAllResultSets();
const models=registry.map(item=>({...item, stableFacets:getStableFacetValues(item), resultStatus:sets.has(item.id)?"tracked":"untracked",resultTrackingStatus:sets.get(item.id)?.tracking_status || "untracked"}));

test("source type intersects availability rather than widening it",()=>{
 const state=parseFilterState(new URLSearchParams("status=tracked&source=paper-snapshot"));
 const actual=filterBenchmarks(models,state).map(x=>x.id).sort();
 const expected=models.filter(x=>x.resultStatus==='tracked'&&x.resultTrackingStatus==='paper-snapshot').map(x=>x.id).sort();
 assert.deepEqual(actual,expected);assert.ok(actual.length>0&&actual.length<sets.size);
 assert.equal(filterBenchmarks(models,parseFilterState(new URLSearchParams("status=untracked&source=paper-snapshot"))).length,0);
 assert.deepEqual(parseFilterState(new URLSearchParams("status=tracked&status=paper-snapshot")),state);
});
test("editing one control retains legacy constraints, repeated years and tags",()=>{
 let params=new URLSearchParams("capability=temporal-reasoning&environment=long-term-chat-history&protocol=question-answering&year=2024&year=2026&tag=abstention&tag=temporal-reasoning");
 params=replaceFilterDimension(params,'sort',['name']);
 const state=parseFilterState(params), roundtrip=new URLSearchParams(serializeFilterState(state));
 for(const key of ['capability','environment','protocol','year','tag']) assert.deepEqual(roundtrip.getAll(key).sort(),params.getAll(key).sort());
 assert.equal(state.sort,'name');
});
test("unambiguous facet aliases migrate, ambiguous ones do not broaden a result set",()=>{
 const keys=['environment:conversation','objective:retrieval-quality','rag-capability:retrieval-quality'];
 const params=migrateFacetParams(new URLSearchParams('facet=conversation&facet=retrieval-quality'),keys);
 assert.deepEqual(params.getAll('facet'),['environment:conversation','retrieval-quality']);
 assert.equal(filterBenchmarks(models,parseFilterState(params)).length,0);
});
test("all bilingual note fragments resolve to an existing counterpart or explicit section fallback",()=>{
 for(const item of registry)for(const lang of ['zh','en']){
  const note=loadDeepRead(item.id,lang), other=loadDeepRead(item.id,lang==='zh'?'en':'zh');
  const available=new Set(['interpretation',...other.headings.map(h=>h.id)]);
  for(const heading of note.headings){const target=decodeURIComponent(translatedFragment('#'+encodeURIComponent(heading.id),note.languageFragments).slice(1));assert.ok(available.has(target),`${item.id}/${lang}/${heading.id}`);}
 }
 const note=loadDeepRead('structmemeval','zh');
 assert.match(decodeURIComponent(translatedFragment('#note-什么时候值得用',note.languageFragments)),/when-to-use-it/);
 assert.equal(translatedFragment('#results',{}),'#results');
});
test("authored score boundaries are extracted despite translated heading variants",()=>{
 for(const id of ['bright-pro','searchauditbench','evobrowsecomp'])for(const lang of ['zh','en']){
  const brief=getAuthoredBrief(id,lang);assert.ok(brief.supports.length>40,`${id}/${lang}`);assert.ok(brief.controls.length>40,`${id}/${lang}`);
 }
});
test("targeted taxonomy review removes frozen/live and rubric/execution confusions",()=>{
 const facets=id=>getStableFacetValues(registry.find(x=>x.id===id));
 assert.ok(!facets('agent-retrieval-bench').includes('rag-capability:live-retrieval'));
 assert.ok(facets('kbgym').includes('rag-capability:corpus-state'));
 assert.ok(!facets('bright').includes('environment:code-workspace'));
 assert.ok(facets('searchauditbench').includes('evaluator:llm-judge'));
 assert.ok(!facets('searchauditbench').includes('evaluator:executable'));
 assert.ok(!facets('searchauditbench').includes('objective:execution-success'));
});
test("paired research notes retain the same load-bearing result values and model conditions",()=>{
 const contracts=JSON.parse(readFileSync(new URL('../../data/editorial/bilingual-contracts.json',import.meta.url)));
 for(const [id,{shared}] of Object.entries(contracts))for(const lang of ['zh','en']){
  const text=loadDeepRead(id,lang).markdown.toLowerCase();
  for(const value of shared) assert.ok(text.includes(value.toLowerCase()),`${id}/${lang}: missing ${value}`);
 }
});
test("SearchAuditBench FPS is explicitly rubric-graded, not re-executed task success",()=>{
 const rs=sets.get('searchauditbench');
 for(const track of rs.tracks.filter(t=>t.metric.id==='fps')){
  assert.match(track.task.en,/not search re-execution/);assert.match(track.task.zh,/不是重跑/);
 }
});

test("writing page state does not depend on a fragment mapping variable",()=>{
 const prior={location:globalThis.location,history:globalThis.history,document:globalThis.document};
 const writes=[];
 globalThis.location={pathname:"/en/benchmarks/",search:"",hash:""};
 globalThis.history={replaceState:(_,__,url)=>writes.push(url)};
 globalThis.document={querySelector:()=>null,querySelectorAll:()=>[]};
 try {writePageState(new URLSearchParams("q=长期"));assert.equal(writes.length,1);assert.match(writes[0],/q=/);}
 finally {for(const [key,value] of Object.entries(prior)){if(value===undefined)delete globalThis[key];else globalThis[key]=value;}}
});


test("paper-only records cannot be presented as leaderboard snapshots",()=>{
 for(const result of sets.values()){
  const sources=result.tracks.flatMap(t=>t.entries.map(e=>e.source));
  if(sources.every(url=>/^https:\/\/(arxiv.org|aclanthology.org)\//.test(url))) assert.notEqual(result.tracking_status,"live",result.benchmark_id);
 }
});
