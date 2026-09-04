from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://h20zhang.github.io/Agent-Benchmark-Radar/"


class WebPublicationContractTest(unittest.TestCase):
    def test_pages_workflow_has_minimum_permissions_and_official_actions(self):
        text = (ROOT / ".github" / "workflows" / "pages.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("contents: read", text)
        self.assertIn("pages: write", text)
        self.assertIn("id-token: write", text)
        self.assertIn("withastro/action@v6", text)
        self.assertIn("actions/deploy-pages@v5", text)
        self.assertNotIn("contents: write", text)

    def test_validation_workflow_runs_web_logic_check_and_build(self):
        text = (ROOT / ".github" / "workflows" / "validate.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("actions/checkout@v7", text)
        self.assertIn("actions/setup-node@v7", text)
        self.assertIn("node-version: 24", text)
        self.assertIn("npm install --no-audit --no-fund", text)
        self.assertIn("npm test", text)
        self.assertIn("npm run check", text)
        self.assertIn("npm run build", text)

    def test_readmes_keep_the_wip_website_hidden(self):
        markers = {
            "README.md": "网站待完善；当前内容以本 README 为准。",
            "README.en.md": "Website under improvement; this README is the source of truth for now.",
        }
        for filename, marker in markers.items():
            text = (ROOT / filename).read_text(encoding="utf-8")
            with self.subTest(filename=filename):
                self.assertNotIn(SITE_URL, text)
                self.assertIn(marker, text[:5000])

    def test_public_web_source_uses_positive_fields_and_research_tool_ui(self):
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

        self.assertNotIn("coverage_gap", source)
        self.assertNotIn("```mermaid", source)
        self.assertIn("data-filter-form", source)
        self.assertIn("wip-shell", source)
        self.assertIn("Website under improvement", source)
        self.assertIn('robots="noindex,nofollow"', source)
        self.assertIn("benchmark-at-a-glance", source)
        self.assertIn("data-suite-builder", source)
        self.assertNotIn("evaluation-loop", source)


if __name__ == "__main__":
    unittest.main()
