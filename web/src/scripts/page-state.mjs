export function translatedFragment(hash, fragments = {}) {
  if (!hash.startsWith("#note-")) return hash;
  let key; try { key = decodeURIComponent(hash.slice(1)); } catch { return "#interpretation"; }
  return `#${encodeURIComponent(fragments[key] || "interpretation")}`;
}
/** Keep language handoff and history synchronized with the visible workspace state. */
export function syncLanguageLinks() {
  let fragments = {};
  try { fragments = JSON.parse(document.querySelector("[data-language-fragments]")?.dataset.languageFragments || "{}"); } catch { /* Missing mapping returns to the interpretation section. */ }
  for (const link of document.querySelectorAll("[data-language-path]")) {
    link.href = `${link.dataset.languagePath}${location.search}${translatedFragment(location.hash, fragments)}`;
  }
}
export function writePageState(params, mode = "replace") {
  const next = `${location.pathname}${params.size ? `?${params}` : ""}${location.hash}`;
  if (next !== `${location.pathname}${location.search}${location.hash}`)
    history[mode === "push" ? "pushState" : "replaceState"]({}, "", next);
  syncLanguageLinks();
}
