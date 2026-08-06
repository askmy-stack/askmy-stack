import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class ProfileReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = README.read_text(encoding="utf-8")

    def test_hero_is_single_versioned_gif(self):
        gif_images = re.findall(
            r'<img\s+[^>]*src="[^"]+\.gif(?:\?[^"]*)?"',
            self.content,
            flags=re.IGNORECASE,
        )
        self.assertEqual(len(gif_images), 1)
        self.assertIn("assets/the-impossible-loop.gif?v=prism-rays-2", self.content)

    def test_futuristic_identity_and_sections_are_present(self):
        required = (
            "<samp>AI SYSTEMS ENGINEER // RESEARCHER</samp>",
            "CONTEXT &rarr; ORCHESTRATION &rarr; EXECUTION &rarr; AUTONOMY",
            "01 // PERSPECTIVE",
            "02 // OPERATING LAYERS",
            "03 // SYSTEM STACK",
            "04 // TRANSMISSION",
            "`CONTEXT`",
            "`ORCHESTRATION`",
            "`EXECUTION`",
            "`RELIABILITY`",
            "`LEARNING`",
        )
        for text in required:
            self.assertIn(text, self.content)

    def test_removed_paragraph_stays_removed(self):
        self.assertNotIn("I work at the layer where intelligence becomes useful", self.content)

    def test_all_external_destinations_remain(self):
        expected = [
            "https://askmystack.space",
            "https://linkedin.com/in/abhinaysai-kamineni",
            "https://github.com/askmy-stack",
            "https://medium.com/@kamineniabhinaysai",
            "https://huggingface.co/askhugsai",
        ]
        transmission = self.content.split("### `04 // TRANSMISSION`", maxsplit=1)[1]
        self.assertEqual(re.findall(r'<a href="([^"]+)">', transmission), expected)


if __name__ == "__main__":
    unittest.main()
