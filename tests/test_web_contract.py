from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://h20zhang.github.io/Agent-Benchmark-Radar/"


class WebPublicationContractTest(unittest.TestCase):
    def test_pages_workflow_cannot_republish_the_app(self):
        text=(ROOT/'.github/workflows/pages.yml').read_text()
        self.assertIn('workflow_dispatch', text)
        for forbidden in ('  push:', 'withastro/action', 'actions/deploy-pages', 'pages: write', 'contents: write'):
            self.assertNotIn(forbidden, text)
    def test_validation_prioritizes_readme_without_a_website_build(self):
        text=(ROOT/'.github/workflows/validate.yml').read_text()
        self.assertIn('node scripts/render-readme.mjs --check',text)
        self.assertIn('python scripts/validate_reading.py',text)
        self.assertNotIn('npm run build',text)
        self.assertNotIn('smoke-live.py',text)
    def test_readmes_are_self_contained_primary_reading_surfaces(self):
        for suffix in ('','.en'):
            text=(ROOT/f'README{suffix}.md').read_text()
            self.assertNotIn(SITE_URL,text)
            for area in ('agent-memory','rag','data-agent'):
                self.assertIn(f'TABLE-FIRST:AREA:{area}:START',text)
            self.assertIn(f'benchmarks/locomo{suffix}.md',text)
            self.assertIn('https://github.com/snap-research/locomo',text)

    def test_public_web_source_is_content_first_indexable_and_timeline_first(self):
        public_paths = [
            ROOT / "web" / "src" / "components",
            ROOT / "web" / "src" / "layouts",
            ROOT / "web" / "src" / "pages",
            ROOT / "web" / "src" / "scripts",
        ]
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for directory in public_paths
            for path in directory.rglob("*")
            if path.is_file()
        )
        home = (ROOT / "web" / "src" / "pages" / "[lang]" / "index.astro").read_text(
            encoding="utf-8"
        )
        timeline = (ROOT / "web" / "src" / "pages" / "[lang]" / "timeline" / "index.astro").read_text(
            encoding="utf-8"
        )

        self.assertNotIn("coverage_gap", source)
        self.assertNotIn("```mermaid", source)
        self.assertIn("data-filter-form", source)
        self.assertIn('robots="index,follow"', home)
        component = (ROOT / "web/src/components/Timeline.astro").read_text()
        self.assertIn("<Timeline", home)
        self.assertLess(home.index("<Timeline"), home.index('id="field-map"'))
        self.assertIn("<Timeline", timeline)
        self.assertIn("inReleaseWindow", component)
        self.assertIn("data-timeline-record", component)
        self.assertNotIn("loadAllResultSets", component)
        self.assertNotIn("evolution_role", component)
        self.assertIn("site.css", (ROOT / "web/src/layouts/BaseLayout.astro").read_text())
        self.assertNotIn("wip-shell", home)
        self.assertNotIn("Website under improvement", home)
        self.assertIn("result-summary", source)
        self.assertIn("data-suite-builder", source)
        self.assertNotIn("evaluation-loop", source)


if __name__ == "__main__":
    unittest.main()
