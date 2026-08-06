#!/usr/bin/env python3
"""Render the single animated hero for the GitHub profile."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 900
HEIGHT = 340
FPS = 12
FRAME_COUNT = 168
DURATION_MS = round(1000 / FPS)
FRAME_DURATIONS = tuple(90 if index % 3 == 2 else 80 for index in range(FRAME_COUNT))

COPY = (
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
)

COLORS = {
    "space": "#080B18",
    "indigo": "#161B3D",
    "panel": "#10162B",
    "line": "#27325B",
    "cyan": "#58E6FF",
    "violet": "#A98CFF",
    "amber": "#FFC857",
    "coral": "#FF5D73",
    "green": "#65F6A6",
    "warm": "#FFF1C7",
    "muted": "#8290B5",
}

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GIF = ROOT / "assets" / "the-impossible-loop.gif"
DEFAULT_POSTER = ROOT / "assets" / "the-impossible-loop-poster.png"
FONT_PATH = ROOT / "assets" / "fonts" / "ShareTechMono-Regular.ttf"
SCREEN = (48, 61, 852, 279)


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


FONT_10 = _font(10)
FONT_11 = _font(11)
FONT_12 = _font(12)
FONT_14 = _font(14)
FONT_16 = _font(16)
FONT_18 = _font(18)
FONT_20 = _font(20)
FONT_28 = _font(28)


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _ease(value: float) -> float:
    value = _clamp(value)
    return value * value * (3.0 - 2.0 * value)


def _segment(t: float, start: float, end: float) -> float:
    return _ease((t - start) / (end - start))


def _center_text(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill, stroke_width: int = 0) -> None:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    x = (WIDTH - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=COLORS["space"])


def _glow_dot(image: Image.Image, xy: tuple[float, float], radius: int, color: str, intensity: int = 180) -> None:
    x, y = xy
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse((x - radius * 3, y - radius * 3, x + radius * 3, y + radius * 3), fill=(*ImageColor.getrgb(color), intensity // 3))
    glow = glow.filter(ImageFilter.GaussianBlur(radius * 2))
    image.alpha_composite(glow)
    draw = ImageDraw.Draw(image)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)


def _glow_line(image: Image.Image, points: list[tuple[float, float]], color: str, width: int = 3) -> None:
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.line(points, fill=(*ImageColor.getrgb(color), 150), width=width * 4, joint="curve")
    glow = glow.filter(ImageFilter.GaussianBlur(width * 2))
    image.alpha_composite(glow)
    ImageDraw.Draw(image).line(points, fill=color, width=width, joint="curve")


class ImageColor:
    @staticmethod
    def getrgb(value: str) -> tuple[int, int, int]:
        value = value.lstrip("#")
        return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def _make_base() -> Image.Image:
    image = Image.new("RGBA", (WIDTH, HEIGHT), COLORS["space"])
    draw = ImageDraw.Draw(image)

    for y in range(HEIGHT):
        blend = y / HEIGHT
        r = int(8 + 8 * blend)
        g = int(11 + 11 * blend)
        b = int(24 + 30 * blend)
        draw.line((0, y, WIDTH, y), fill=(r, g, b, 255))

    rng = random.Random(2086)
    for _ in range(115):
        x = rng.randrange(18, WIDTH - 18)
        y = rng.randrange(12, HEIGHT - 12)
        radius = rng.choice((1, 1, 1, 2))
        shade = rng.choice((COLORS["muted"], COLORS["violet"], COLORS["cyan"], COLORS["warm"]))
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=shade)

    # Floating cabinet and glass viewport.
    draw.rounded_rectangle((18, 15, 882, 325), radius=22, fill="#090D1C", outline="#43507D", width=2)
    draw.rounded_rectangle((28, 25, 872, 315), radius=17, fill=COLORS["panel"], outline="#222C50", width=2)
    draw.rounded_rectangle(SCREEN, radius=12, fill="#070B17", outline="#3B4770", width=2)
    draw.line((48, 51, 852, 51), fill="#303B65", width=1)
    draw.text((54, 31), "LIGHT STUDY // SPECTRUM", font=FONT_14, fill=COLORS["warm"])
    draw.text((752, 33), "LOOP/014", font=FONT_12, fill=COLORS["muted"])

    # Cabinet controls double as a visual legend.
    for x, color in ((58, COLORS["cyan"]), (76, COLORS["violet"]), (94, COLORS["amber"]), (112, COLORS["green"])):
        draw.ellipse((x, 295, x + 8, 303), fill=color)
    draw.text((132, 292), "PREDICT  DELIVER  ANCHOR  EXAMINE  ORCHESTRATE", font=FONT_12, fill=COLORS["muted"])
    draw.text((754, 292), "LOOP: READY", font=FONT_12, fill=COLORS["cyan"])
    return image


BASE = _make_base()


def _scene_label(draw: ImageDraw.ImageDraw, label: str, color: str, sublabel: str = "") -> None:
    draw.rounded_rectangle((63, 76, 63 + max(130, len(label) * 12), 108), radius=5, fill="#111A34", outline=color, width=1)
    draw.text((74, 81), label, font=FONT_16, fill=color)
    if sublabel:
        draw.text((70, 246), sublabel, font=FONT_14, fill=COLORS["muted"])


def _draw_model(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _center_text(draw, 98, "MODELS PREDICT.", FONT_28, COLORS["warm"])
    _center_text(draw, 137, "A SIGNAL BECOMES A POSSIBILITY", FONT_14, COLORS["muted"])
    points = [(180, 190), (315, 163), (450, 184), (585, 148), (720, 181)]
    for index in range(len(points) - 1):
        _glow_line(image, points[index : index + 2], COLORS["cyan"], 2)
    for index, point in enumerate(points):
        _glow_dot(image, point, 5 + int(3 * p), (COLORS["cyan"], COLORS["violet"], COLORS["amber"])[index % 3])
    draw.line((156, 215, 744, 215), fill="#334064", width=1)
    draw.text((364, 223), "POSSIBILITY FIELD", font=FONT_14, fill=COLORS["muted"])


def _draw_agents(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _center_text(draw, 98, "AGENTS DELIVER.", FONT_28, COLORS["cyan"])
    _center_text(draw, 137, "A POSSIBILITY BECOMES A MOVE", FONT_14, COLORS["muted"])
    gates = ((220, COLORS["cyan"]), (450, COLORS["violet"]), (680, COLORS["amber"]))
    for x, color in gates:
        draw.polygon(((x - 28, 143), (x + 28, 172), (x - 28, 201)), outline=color, fill="#11172F")
        draw.line((x - 18, 172, x + 18, 172), fill=color, width=2)
    path_x = 160 + 580 * _ease(p)
    _glow_line(image, [(150, 172), (750, 172)], COLORS["cyan"], 2)
    _glow_dot(image, (path_x, 172), 8, COLORS["warm"])
    for index, (x, color) in enumerate(gates):
        draw.text((x - 22, 218), f"STEP {index + 1}", font=FONT_12, fill=color)


def _draw_context(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _center_text(draw, 98, "SYSTEMS ANCHOR CONTEXT.", FONT_28, COLORS["violet"])
    _center_text(draw, 137, "THE THREAD CONTINUES BETWEEN MOMENTS", FONT_14, COLORS["muted"])
    center = (450, 177)
    for orbit, (rx, ry) in enumerate(((75, 34), (135, 60), (195, 86))):
        draw.ellipse((center[0] - rx, center[1] - ry, center[0] + rx, center[1] + ry), outline="#3A3565", width=2)
        angle = frame * (0.04 - orbit * 0.008) + orbit * 1.7
        x = center[0] + math.cos(angle) * rx
        y = center[1] + math.sin(angle) * ry
        color = (COLORS["cyan"], COLORS["violet"], COLORS["amber"])[orbit]
        draw.rectangle((x - 7, y - 7, x + 7, y + 7), outline=color, fill="#10142B", width=2)
        _glow_dot(image, (x, y), 4 + orbit, color)
    _glow_dot(image, center, 8, COLORS["cyan"])
    draw.line((center[0] - 22, center[1], center[0] + 22, center[1]), fill=COLORS["warm"], width=2)
    draw.line((center[0], center[1] - 22, center[0], center[1] + 22), fill=COLORS["warm"], width=2)


def _pixel_ray(draw: ImageDraw.ImageDraw, start: tuple[float, float], end: tuple[float, float], color: str, progress: float, seed: int, scatter: float = 0.0) -> None:
    rng = random.Random(seed)
    steps = 16
    for index in range(steps):
        fraction = (index + 1) / steps * _clamp(progress)
        x = start[0] + (end[0] - start[0]) * fraction
        y = start[1] + (end[1] - start[1]) * fraction
        y += (rng.random() - 0.5) * scatter * fraction
        size = 3 + (index % 3)
        draw.rectangle((x - size, y - size, x + size, y + size), fill=color)


def primitive_grid(draw: ImageDraw.ImageDraw, progress: float, frame: int) -> None:
    """Show the small components beneath a failed abstraction."""
    alpha = int(55 + 90 * _clamp(progress))
    for column in range(9):
        x = 238 + column * 53
        draw.line((x, 124, x + math.sin(frame * 0.04 + column) * 8, 224), fill=(86, 102, 158, alpha), width=1)
    for row in range(4):
        y = 132 + row * 28
        draw.line((220, y, 680, y + math.sin(frame * 0.03 + row) * 5), fill=(86, 102, 158, alpha), width=1)
    for column in range(8):
        for row in range(3):
            x = 264 + column * 53
            y = 144 + row * 28
            draw.rectangle((x - 2, y - 2, x + 2, y + 2), fill=COLORS["coral"] if (column + row + frame) % 7 == 0 else COLORS["muted"])


def _draw_execution(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    source = (168, 178)
    prism_center = (450, 178)
    prism = ((405, 122), (495, 178), (405, 234))
    _glow_line(image, [source, prism_center], COLORS["cyan"], 4)
    draw.polygon(prism, fill="#101A35", outline=COLORS["warm"])
    draw.line((405, 122, 405, 234), fill=COLORS["violet"], width=2)
    for index, (color, endpoint) in enumerate(((COLORS["cyan"], (740, 138)), (COLORS["violet"], (748, 178)), (COLORS["amber"], (740, 218)))):
        _glow_line(image, [prism_center, endpoint], color, 2)
        _pixel_ray(draw, prism_center, endpoint, color, p, 200 + index, scatter=6)
    _glow_dot(image, source, 6, COLORS["cyan"])
    _center_text(draw, 98, "EXECUTION REVEALS THE TRUTH.", FONT_28, COLORS["amber"])
    _center_text(draw, 137, "A BEAM LEAVES THE MODEL", FONT_14, COLORS["muted"])


def _draw_prism(image: Image.Image, p: float, frame: int, complexity: bool = False) -> None:
    draw = ImageDraw.Draw(image)
    source = (168, 178)
    prism_center = (450, 178)
    prism = ((405, 122), (495, 178), (405, 234))
    _glow_line(image, [source, prism_center], COLORS["cyan"], 4)
    draw.polygon(prism, fill="#101A35", outline=COLORS["warm"])
    draw.line((405, 122, 405, 234), fill=COLORS["violet"], width=2)
    draw.line((405, 122, 495, 178), fill=COLORS["cyan"], width=1)
    draw.line((405, 234, 495, 178), fill=COLORS["amber"], width=1)
    rays = ((COLORS["cyan"], (740, 128)), (COLORS["violet"], (748, 178)), (COLORS["amber"], (740, 228)))
    for index, (color, endpoint) in enumerate(rays):
        end = (prism_center[0] + (endpoint[0] - prism_center[0]) * _ease(p), prism_center[1] + (endpoint[1] - prism_center[1]) * _ease(p))
        _glow_line(image, [prism_center, end], color, 2)
        _pixel_ray(draw, prism_center, endpoint, color, p, 300 + index, scatter=34 if complexity else 12)
    _glow_dot(image, source, 6, COLORS["cyan"])
    if complexity:
        primitive_grid(draw, p, frame)
        _center_text(draw, 91, "WHEN COMPLEXITY BLINDS,", FONT_28, COLORS["amber"])
        _center_text(draw, 126, "ISOLATE THE ARCHITECTURE.", FONT_28, COLORS["warm"])
    else:
        _center_text(draw, 91, "WHEN ABSTRACTIONS LEAK,", FONT_28, COLORS["coral"])
        _center_text(draw, 126, "EXAMINE THE PRIMITIVES.", FONT_28, COLORS["warm"])



def _infinity_points(progress: float, samples: int = 90) -> list[tuple[float, float]]:
    points = []
    count = max(2, int(samples * _clamp(progress)))
    for index in range(count):
        angle = (index / (samples - 1)) * math.tau - math.pi / 2
        denominator = 1 + math.sin(angle) ** 2
        x = 450 + 185 * math.cos(angle) / denominator
        y = 171 + 92 * math.sin(angle) * math.cos(angle) / denominator
        points.append((x, y))
    return points


def _draw_orchestration(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _center_text(draw, 98, "ORCHESTRATION IS THE PULSE.", FONT_28, COLORS["green"])
    _center_text(draw, 137, "MANY SIGNALS. ONE CONTINUOUS MOTION.", FONT_14, COLORS["muted"])
    center = (450, 178)
    sources = ((175, 135, COLORS["cyan"]), (175, 220, COLORS["violet"]), (725, 135, COLORS["amber"]), (725, 220, COLORS["coral"]))
    for index, (x, y, color) in enumerate(sources):
        _glow_line(image, [(x, y), center], color, 2)
        progress = _clamp(p * 1.4 - index * 0.12)
        _pixel_ray(draw, (x, y), center, color, progress, 600 + index, scatter=12)
    pulse_x = 160 + 580 * ((frame % 28) / 27)
    _glow_line(image, [(150, 178), (750, 178)], COLORS["green"], 4)
    _glow_dot(image, (pulse_x, 178), 8, COLORS["warm"])
    draw.ellipse((center[0] - 22, center[1] - 22, center[0] + 22, center[1] + 22), outline=COLORS["green"], width=2)
    draw.line((center[0] - 14, center[1], center[0] + 14, center[1]), fill=COLORS["green"], width=2)
    draw.line((center[0], center[1] - 14, center[0], center[1] + 14), fill=COLORS["green"], width=2)


def _draw_final(image: Image.Image, p: float) -> None:
    draw = ImageDraw.Draw(image)
    points = [(x, 205 + (y - 171) * 0.58) for x, y in _infinity_points(1.0)]
    _glow_line(image, points, COLORS["green"], 3)
    veil = Image.new("RGBA", image.size, (8, 11, 24, int(155 * _ease(p))))
    image.alpha_composite(veil)
    draw = ImageDraw.Draw(image)
    _center_text(draw, 91, "AUTONOMY IS THE ENDGAME.", FONT_28, COLORS["warm"])
    _center_text(draw, 132, "INTELLIGENCE BECOMES SYSTEMIC.", FONT_28, COLORS["cyan"])
    _center_text(draw, 244, "PREDICT / DELIVER / ANCHOR / EXAMINE / ORCHESTRATE", FONT_14, COLORS["muted"])


def _add_crt(image: Image.Image, frame: int) -> None:
    draw = ImageDraw.Draw(image, "RGBA")
    for y in range(SCREEN[1] + 2, SCREEN[3] - 1, 4):
        draw.line((SCREEN[0] + 2, y, SCREEN[2] - 2, y), fill=(0, 0, 0, 25), width=1)
    sweep_y = SCREEN[1] + ((frame * 3) % (SCREEN[3] - SCREEN[1]))
    draw.line((SCREEN[0] + 3, sweep_y, SCREEN[2] - 3, sweep_y), fill=(88, 230, 255, 9), width=1)
    # Soft glass reflection.
    reflection = Image.new("RGBA", image.size, (0, 0, 0, 0))
    ImageDraw.Draw(reflection).polygon(
        ((63, 73), (320, 73), (190, 267), (63, 267)),
        fill=(255, 255, 255, 7),
    )
    image.alpha_composite(reflection)


def render_frame(frame: int) -> Image.Image:
    image = BASE.copy()
    t = frame / (FRAME_COUNT - 1)

    if t < 0.10:
        _draw_model(image, _segment(t, 0.0, 0.10), frame)
    elif t < 0.20:
        _draw_agents(image, _segment(t, 0.10, 0.20), frame)
    elif t < 0.32:
        _draw_context(image, _segment(t, 0.20, 0.32), frame)
    elif t < 0.45:
        _draw_execution(image, _segment(t, 0.32, 0.45), frame)
    elif t < 0.59:
        _draw_prism(image, _segment(t, 0.45, 0.59), frame, complexity=False)
    elif t < 0.72:
        _draw_prism(image, _segment(t, 0.59, 0.72), frame, complexity=True)
    elif t < 0.83:
        _draw_orchestration(image, _segment(t, 0.72, 0.83), frame)
    else:
        _draw_final(image, _segment(t, 0.83, 0.94))
        if t > 0.975:
            # Hold the final philosophy, then cut cleanly back to the first beat.
            opening = BASE.copy()
            _draw_model(opening, 0.0, 0)
            image = opening

    _add_crt(image, frame)
    return image.convert("RGB")


def _global_palette(frames: list[Image.Image]) -> Image.Image:
    sample_indexes = (0, 15, 31, 46, 62, 78, 94, 108)
    sheet = Image.new("RGB", (WIDTH * 2, HEIGHT), COLORS["space"])
    thumb_size = (WIDTH // 4, HEIGHT // 2)
    for index, frame_index in enumerate(sample_indexes):
        thumb = frames[frame_index].resize(thumb_size, Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((index % 8) * thumb_size[0], (index // 8) * thumb_size[1]))
    return sheet.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)


def render(output_gif: Path = DEFAULT_GIF, output_poster: Path = DEFAULT_POSTER) -> None:
    output_gif = Path(output_gif)
    output_poster = Path(output_poster)
    output_gif.parent.mkdir(parents=True, exist_ok=True)
    output_poster.parent.mkdir(parents=True, exist_ok=True)

    frames = [render_frame(index) for index in range(FRAME_COUNT)]
    frames[-1] = frames[0].copy()
    frames[108].save(output_poster, format="PNG", optimize=True)

    palette = _global_palette(frames)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(
        output_gif,
        save_all=True,
        append_images=indexed[1:],
        duration=FRAME_DURATIONS,
        loop=0,
        optimize=True,
        disposal=2,
    )


if __name__ == "__main__":
    render()
    print(f"Rendered {DEFAULT_GIF}")
    print(f"Rendered {DEFAULT_POSTER}")
