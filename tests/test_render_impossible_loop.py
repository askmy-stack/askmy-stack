import importlib.util
import hashlib
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RENDERER_PATH = ROOT / "scripts" / "render_impossible_loop.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("render_impossible_loop", RENDERER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ImpossibleLoopRendererTests(unittest.TestCase):
    def test_contract_and_copy(self):
        renderer = load_renderer()

        self.assertEqual((renderer.WIDTH, renderer.HEIGHT), (900, 340))
        self.assertEqual(renderer.FPS, 12)
        self.assertEqual(renderer.FRAME_COUNT, 216)
        self.assertLessEqual(renderer.DURATION_MS, 84)
        self.assertEqual(sum(renderer.FRAME_DURATIONS), 18_000)
        self.assertTrue(renderer.FONT_PATH.exists())

        copy = "\n".join(renderer.COPY)
        for phrase in (
            "MODELS PREDICT.",
            "AGENTS DELIVER.",
            "SYSTEMS ANCHOR CONTEXT.",
            "EXECUTION REVEALS THE TRUTH.",
            "WHEN ABSTRACTIONS LEAK,",
            "EXAMINE THE PRIMITIVES.",
            "WHEN COMPLEXITY BLINDS,",
            "ISOLATE THE ARCHITECTURE.",
            "ORCHESTRATION IS THE PULSE.",
            "AUTONOMY IS THE ENDGAME.",
        ):
            self.assertIn(phrase, copy)

        source = RENDERER_PATH.read_text(encoding="utf-8").lower()
        for required in ("prism", "pixel", "ray", "primitive_nodes", "ai systems // signal spectrum"):
            self.assertIn(required, source)
        for forbidden in ("ask my stack", "askmy-stack", "cortex", "myelinmesh", "parallax", "meridian", "repository", "system/2086", "prism-core", "sad face", "emoji"):
            self.assertNotIn(forbidden, copy.lower())
            self.assertNotIn(forbidden, source)

    def test_rendered_assets_are_animated_and_within_budget(self):
        renderer = load_renderer()

        with tempfile.TemporaryDirectory() as temp_dir:
            gif_path = Path(temp_dir) / "loop.gif"
            poster_path = Path(temp_dir) / "poster.png"
            renderer.render(gif_path, poster_path)

            self.assertTrue(gif_path.exists())
            self.assertTrue(poster_path.exists())
            self.assertLess(gif_path.stat().st_size, 5 * 1024 * 1024)
            self.assertEqual(
                hashlib.sha256(gif_path.read_bytes()).hexdigest(),
                hashlib.sha256((ROOT / "assets" / "the-impossible-loop.gif").read_bytes()).hexdigest(),
            )
            self.assertEqual(
                hashlib.sha256(poster_path.read_bytes()).hexdigest(),
                hashlib.sha256((ROOT / "assets" / "the-impossible-loop-poster.png").read_bytes()).hexdigest(),
            )

            with Image.open(gif_path) as animation:
                self.assertEqual(animation.size, (900, 340))
                self.assertTrue(animation.is_animated)
                self.assertGreaterEqual(animation.n_frames, 100)
                self.assertEqual(animation.info.get("loop"), 0)
                total_duration = 0
                for frame_index in range(animation.n_frames):
                    animation.seek(frame_index)
                    total_duration += animation.info["duration"]
                self.assertEqual(total_duration, 18_000)

            with Image.open(poster_path) as poster:
                self.assertEqual(poster.size, (900, 340))
                self.assertEqual(poster.mode, "RGB")

    def test_readme_uses_the_single_gif_hero(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("assets/the-impossible-loop.gif", readme)
        self.assertEqual(readme.lower().count(".gif"), 1)
        self.assertNotIn("assets/perspective-dark.svg", readme)


if __name__ == "__main__":
    unittest.main()
