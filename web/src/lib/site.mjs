export const SITE_ORIGIN = "https://h20zhang.github.io";
export const BASE_PATH = "/Agent-Benchmark-Radar";
export const REPOSITORY_URL =
  "https://github.com/H20Zhang/Agent-Benchmark-Radar";

/** @param {string} path */
export function sitePath(path = "/") {
  const normalized = path.startsWith("/") ? path : `/${path}`;
  if (normalized === BASE_PATH || normalized.startsWith(`${BASE_PATH}/`)) {
    return normalized;
  }
  return `${BASE_PATH}${normalized}`.replace(/\/{2,}/g, "/");
}

/** @param {string} path */
export function absoluteUrl(path = "/") {
  return new URL(sitePath(path), SITE_ORIGIN).href;
}

/** @param {"zh" | "en"} lang @param {string} suffix */
export function localePath(lang, suffix = "/") {
  const clean = suffix.replace(/^\/+/, "");
  return `/${lang}/${clean}`.replace(/\/{2,}/g, "/");
}

/** @param {string} value */
export function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

/** @param {string} value */
export function displayToken(value) {
  return value
    .split("-")
    .filter(Boolean)
    .map((part) => part.length <= 3 ? part.toUpperCase() : part)
    .join(" ");
}
