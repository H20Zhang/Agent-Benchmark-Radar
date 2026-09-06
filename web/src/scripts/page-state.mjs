/** Keep language handoff and history synchronized with the visible workspace state. */
export function syncLanguageLinks() {
  for (const link of document.querySelectorAll("[data-language-path]")) {
    link.href = `${link.dataset.languagePath}${location.search}${location.hash}`;
  }
}
export function writePageState(params, mode = "replace") {
  const next = `${location.pathname}${params.size ? `?${params}` : ""}${location.hash}`;
  if (next !== `${location.pathname}${location.search}${location.hash}`)
    history[mode === "push" ? "pushState" : "replaceState"]({}, "", next);
  syncLanguageLinks();
}
