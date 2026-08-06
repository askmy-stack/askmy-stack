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
FRAME_COUNT = 120
DURATION_MS = round(1000 / FPS)
FRAME_DURATIONS = tuple(90 if index % 3 == 2 else 80 for index in range(FRAME_COUNT))

COPY = (
    "THE IMPOSSIBLE LOOP",
    "INSERT CONTEXT",
    "OBSERVE",
    "MEMORY ONLINE",
    "REASON",
    "EXPECTED",
    "OBSERVED",
    "DIFFERENCE",
    "UNEXPECTED != UNRECOVERABLE",
    "RECOVERY 1UP",
    "INTELLIGENCE STARTS THE LOOP.",
    "RELIABLE SYSTEMS KEEP IT ALIVE.",
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
    draw.text((54, 31), "THE IMPOSSIBLE LOOP", font=FONT_14, fill=COLORS["warm"])
    draw.text((725, 33), "SYSTEM/2086", font=FONT_12, fill=COLORS["muted"])

    # Cabinet controls double as a visual legend.
    for x, color in ((58, COLORS["cyan"]), (76, COLORS["violet"]), (94, COLORS["amber"]), (112, COLORS["green"])):
        draw.ellipse((x, 295, x + 8, 303), fill=color)
    draw.text((132, 292), "OBSERVE  REMEMBER  REASON  VERIFY  RECOVER", font=FONT_12, fill=COLORS["muted"])
    draw.text((754, 292), "LOOP: READY", font=FONT_12, fill=COLORS["cyan"])
    return image


BASE = _make_base()


def _scene_label(draw: ImageDraw.ImageDraw, label: str, color: str, sublabel: str = "") -> None:
    draw.rounded_rectangle((63, 76, 63 + max(130, len(label) * 12), 108), radius=5, fill="#111A34", outline=color, width=1)
    draw.text((74, 81), label, font=FONT_16, fill=color)
    if sublabel:
        draw.text((70, 246), sublabel, font=FONT_14, fill=COLORS["muted"])


def _draw_intro(image: Image.Image, p: float) -> None:
    draw = ImageDraw.Draw(image)
    _center_text(draw, 98, "INSERT CONTEXT", FONT_28, COLORS["warm"])
    _center_text(draw, 137, "A SIGNAL IS LOOKING FOR A SYSTEM", FONT_14, COLORS["muted"])
    x = 180 + 520 * _ease(p)
    y = 197 + math.sin(p * math.pi * 4) * 8
    for trail in range(7, 0, -1):
        alpha = 30 + trail * 15
        tx = x - trail * 14
        draw.ellipse((tx - 3, y - 3, tx + 3, y + 3), fill=(*ImageColor.getrgb(COLORS["cyan"]), alpha))
    _glow_dot(image, (x, y), 9, COLORS["cyan"])
    draw.rounded_rectangle((x - 40, y - 17, x + 40, y + 17), radius=8, outline=COLORS["warm"], width=1)
    text_box = draw.textbbox((0, 0), "CONTEXT", font=FONT_14)
    draw.text((x - (text_box[2] - text_box[0]) / 2, y - 8), "CONTEXT", font=FONT_14, fill=COLORS["warm"])


def _draw_observe(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "OBSERVE", COLORS["cyan"], "NOISE BECOMES SIGNAL")
    focus = (468, 172)
    rng = random.Random(71)
    points = [(rng.randint(110, 790), rng.randint(116, 235)) for _ in range(34)]
    for index, (sx, sy) in enumerate(points):
        wobble = math.sin(frame * 0.17 + index) * 4
        convergence = _ease(p)
        x = sx + (focus[0] - sx) * convergence
        y = sy + wobble * (1 - convergence) + (focus[1] - sy) * convergence
        color = (COLORS["cyan"], COLORS["violet"], COLORS["warm"])[index % 3]
        draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=color)
    # Satellite flower: a technical instrument rendered as a strange bloom.
    hub = (235, 175)
    for petal in range(8):
        angle = petal * math.pi / 4 + frame * 0.015
        end = (hub[0] + math.cos(angle) * 34, hub[1] + math.sin(angle) * 34)
        draw.line((hub, end), fill=COLORS["violet"], width=2)
        draw.ellipse((end[0] - 8, end[1] - 4, end[0] + 8, end[1] + 4), outline=COLORS["cyan"], width=2)
    _glow_dot(image, hub, 5, COLORS["amber"])
    if p > 0.58:
        _glow_line(image, [(focus[0], focus[1]), (680, 172)], COLORS["cyan"], 2)


def _draw_memory(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "MEMORY ONLINE", COLORS["violet"], "CONTEXT FINDS AN ORBIT")
    center = (450, 174)
    for orbit, (rx, ry) in enumerate(((74, 34), (126, 58), (182, 82))):
        draw.ellipse((center[0] - rx, center[1] - ry, center[0] + rx, center[1] + ry), outline="#3A3565", width=2)
        angle = frame * (0.035 - orbit * 0.007) + orbit * 2.1
        x = center[0] + math.cos(angle) * rx
        y = center[1] + math.sin(angle) * ry
        color = (COLORS["cyan"], COLORS["violet"], COLORS["warm"])[orbit]
        _glow_dot(image, (x, y), 5 + orbit, color)
        # Cassette-like archive tile.
        draw.rounded_rectangle((x - 16, y - 10, x + 16, y + 10), radius=3, outline=color, fill="#10142B", width=1)
        draw.ellipse((x - 8, y - 3, x - 3, y + 2), outline=color)
        draw.ellipse((x + 3, y - 3, x + 8, y + 2), outline=color)
    for node in range(7):
        angle = node / 7 * math.tau
        radius = 18 + 18 * _ease(p)
        x = center[0] + math.cos(angle) * radius
        y = center[1] + math.sin(angle) * radius
        draw.line((center[0], center[1], x, y), fill="#6956A5", width=1)
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=COLORS["violet"])
    _glow_dot(image, center, 7, COLORS["cyan"])


def _draw_reason(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "REASON", COLORS["violet"], "A PATH EARNS ITS LIGHT")
    cols, rows = 11, 5
    x0, y0, dx, dy = 225, 116, 48, 30
    route = [(0, 2), (1, 2), (2, 1), (3, 1), (4, 3), (5, 3), (6, 2), (7, 2), (8, 1), (9, 1), (10, 2)]
    for row in range(rows):
        for col in range(cols):
            x, y = x0 + col * dx, y0 + row * dy
            if col < cols - 1:
                draw.line((x, y, x + dx, y + ((row + col) % 3 - 1) * dy), fill="#273152", width=1)
            draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill="#566184")
    lit = max(1, int(p * len(route)))
    route_points = [(x0 + col * dx, y0 + row * dy) for col, row in route[:lit]]
    if len(route_points) > 1:
        _glow_line(image, route_points, COLORS["violet"], 3)
    point = route_points[-1]
    _glow_dot(image, point, 6, COLORS["cyan"])
    # Tiny geometric spacecraft at the end of the chosen route.
    angle = math.sin(frame * 0.1) * 0.12
    nose = (point[0] + 18, point[1] + math.sin(angle) * 8)
    draw.polygon((nose, (point[0] - 8, point[1] - 7), (point[0] - 4, point[1]), (point[0] - 8, point[1] + 7)), fill=COLORS["warm"])


def _draw_verify(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "VERIFY", COLORS["amber"], "ACTION LEAVES EVIDENCE")
    source = (236, 175)
    prism = ((435, 116), (505, 175), (435, 234))
    _glow_line(image, [source, (435, 175)], COLORS["cyan"], 3)
    draw.polygon(prism, fill="#171B3A", outline=COLORS["warm"])
    beam_labels = (("EXPECTED", COLORS["cyan"], 132), ("OBSERVED", COLORS["violet"], 175), ("DIFFERENCE", COLORS["amber"], 218))
    for index, (label, color, y) in enumerate(beam_labels):
        length = 205 * _ease(_clamp(p * 1.3 - index * 0.12))
        _glow_line(image, [(505, 175), (505 + length, y)], color, 2)
        if length > 145:
            draw.text((695, y - 9), label, font=FONT_14, fill=color)
    pulse = 3 + int((math.sin(frame * 0.35) + 1) * 2)
    _glow_dot(image, source, pulse, COLORS["cyan"])


def _draw_glitch(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "ANOMALY", COLORS["coral"], "THE LOOP NOTICES THE BREAK")
    _center_text(draw, 222, "UNEXPECTED != UNRECOVERABLE", FONT_16, COLORS["warm"])
    # A playful pixel eclipse with an intentionally non-threatening face.
    cx = 450 + math.sin(frame * 0.3) * 18
    cy = 165
    radius = 49
    _glow_dot(image, (cx, cy), radius, COLORS["coral"], 90)
    draw = ImageDraw.Draw(image)
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill="#251326", outline=COLORS["coral"], width=3)
    draw.rectangle((cx - 25, cy - 12, cx - 9, cy + 1), fill=COLORS["warm"])
    draw.rectangle((cx + 9, cy - 12, cx + 25, cy + 1), fill=COLORS["warm"])
    draw.arc((cx - 22, cy + 7, cx + 22, cy + 33), 200, 340, fill=COLORS["coral"], width=3)
    rng = random.Random(frame)
    for _ in range(18):
        gx = rng.randint(290, 610)
        gy = rng.randint(110, 224)
        gw = rng.randint(8, 35)
        color = rng.choice((COLORS["coral"], COLORS["cyan"], COLORS["violet"]))
        draw.rectangle((gx, gy, gx + gw, gy + rng.randint(2, 5)), fill=color)


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


def _draw_recover(image: Image.Image, p: float, frame: int) -> None:
    draw = ImageDraw.Draw(image)
    _scene_label(draw, "RECOVERY 1UP", COLORS["green"], "THE SYSTEM FINDS ITS WAY BACK")
    points = _infinity_points(p)
    if len(points) > 1:
        _glow_line(image, points, COLORS["green"], 4)
        _glow_dot(image, points[-1], 7, COLORS["warm"])
    # The glitch resolves into confetti rather than disappearing violently.
    rng = random.Random(444)
    for index in range(int(28 * p)):
        x = 330 + rng.randrange(240)
        y = 112 + rng.randrange(120)
        color = (COLORS["coral"], COLORS["cyan"], COLORS["violet"], COLORS["amber"])[index % 4]
        offset = math.sin(frame * 0.12 + index) * 6
        draw.rectangle((x + offset, y, x + offset + 3, y + 3), fill=color)


def _draw_final(image: Image.Image, p: float) -> None:
    draw = ImageDraw.Draw(image)
    points = [(x, 205 + (y - 171) * 0.58) for x, y in _infinity_points(1.0)]
    _glow_line(image, points, COLORS["green"], 3)
    veil = Image.new("RGBA", image.size, (8, 11, 24, int(155 * _ease(p))))
    image.alpha_composite(veil)
    draw = ImageDraw.Draw(image)
    _center_text(draw, 91, "INTELLIGENCE STARTS THE LOOP.", FONT_28, COLORS["warm"])
    _center_text(draw, 128, "RELIABLE SYSTEMS KEEP IT ALIVE.", FONT_28, COLORS["cyan"])
    _center_text(draw, 244, "OBSERVE / REMEMBER / REASON / VERIFY / RECOVER", FONT_14, COLORS["muted"])


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

    if t < 0.12:
        _draw_intro(image, _segment(t, 0.0, 0.12))
    elif t < 0.25:
        _draw_observe(image, _segment(t, 0.12, 0.25), frame)
    elif t < 0.38:
        _draw_memory(image, _segment(t, 0.25, 0.38), frame)
    elif t < 0.51:
        _draw_reason(image, _segment(t, 0.38, 0.51), frame)
    elif t < 0.65:
        _draw_verify(image, _segment(t, 0.51, 0.65), frame)
    elif t < 0.76:
        _draw_glitch(image, _segment(t, 0.65, 0.76), frame)
    elif t < 0.88:
        _draw_recover(image, _segment(t, 0.76, 0.88), frame)
    else:
        _draw_final(image, _segment(t, 0.88, 0.93))
        if t > 0.975:
            # A short retro cut returns to the opening composition without
            # superimposing both messages during the loop transition.
            intro = BASE.copy()
            _draw_intro(intro, 0.0)
            image = intro

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
