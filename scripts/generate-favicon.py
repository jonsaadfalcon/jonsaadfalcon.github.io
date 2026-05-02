#!/usr/bin/env python3
"""Generate favicon set for jonsaadfalcon.com.

Design: "J" monogram in Georgia Bold, white on Forest Mint (#2E7D6F),
with rounded corners matching the site's photo style.

Outputs:
  icons/favicon-16x16.png
  icons/favicon-32x32.png
  icons/favicon-48x48.png
  icons/apple-touch-icon.png  (180x180)
  icons/favicon.ico            (multi-size: 16/32/48)
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).parent.parent
ICONS_DIR = ROOT / "icons"
FONT_PATH = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"

ACCENT = (46, 125, 111)     # #2E7D6F
WHITE = (255, 255, 255)


def make_icon(size: int, corner_ratio: float = 0.18) -> Image.Image:
    """Render a single 'J' monogram at the given size."""
    # Render at 4x for anti-aliasing, then downsample
    scale = 4
    canvas = Image.new("RGBA", (size * scale, size * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Rounded square background
    radius = int(size * scale * corner_ratio)
    draw.rounded_rectangle(
        (0, 0, size * scale - 1, size * scale - 1),
        radius=radius,
        fill=ACCENT,
    )

    # 'J' glyph centered
    # Georgia Bold "J" needs a slight horizontal nudge because of its descender
    font_size = int(size * scale * 0.72)
    font = ImageFont.truetype(FONT_PATH, font_size)

    text = "J"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    # offset for the bbox origin
    x = (size * scale - text_w) // 2 - bbox[0]
    y = (size * scale - text_h) // 2 - bbox[1]
    # Slight upward nudge to balance Georgia's J descender
    y -= int(size * scale * 0.04)
    draw.text((x, y), text, font=font, fill=WHITE)

    return canvas.resize((size, size), Image.LANCZOS)


def main() -> None:
    ICONS_DIR.mkdir(exist_ok=True)
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "apple-touch-icon.png": 180,
    }
    images = {}
    for fname, size in sizes.items():
        img = make_icon(size)
        out_path = ICONS_DIR / fname
        img.save(out_path)
        images[size] = img
        print(f"Wrote {out_path} ({size}x{size})")

    # Multi-size .ico: include 16, 32, 48
    ico_path = ICONS_DIR / "favicon.ico"
    images[16].save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    print(f"Wrote {ico_path} (multi-size)")


if __name__ == "__main__":
    main()
