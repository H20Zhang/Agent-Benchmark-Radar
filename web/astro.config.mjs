import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://h20zhang.github.io",
  base: "/Agent-Benchmark-Radar",
  output: "static",
  trailingSlash: "always",
  integrations: [
    sitemap({
      filter: (page) =>
        page !== "https://h20zhang.github.io/Agent-Benchmark-Radar/",
    }),
  ],
});
