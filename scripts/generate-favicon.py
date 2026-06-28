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

    # 'JSF' monogram centered
    font_size = int(size * scale * 0.46)
    font = ImageFont.truetype(FONT_PATH, font_size)

    text = "JSF"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size * scale - text_w) // 2 - bbox[0]
    y = (size * scale - text_h) // 2 - bbox[1]
    # Slight upward nudge to optically center given Georgia's J descender
    y -= int(size * scale * 0.02)
    draw.text((x, y), text, font=font, fill=WHITE)

    return canvas.resize((size, size), Image.LANCZOS)


def main() -> None:
    import sys
    suffix = sys.argv[1] if len(sys.argv) > 1 else ""
    ICONS_DIR.mkdir(exist_ok=True)
    sizes = {
        f"favicon-16x16{suffix}.png": 16,
        f"favicon-32x32{suffix}.png": 32,
        f"favicon-48x48{suffix}.png": 48,
        f"apple-touch-icon{suffix}.png": 180,
    }
    images = {}
    for fname, size in sizes.items():
        img = make_icon(size)
        out_path = ICONS_DIR / fname
        img.save(out_path)
        images[size] = img
        print(f"Wrote {out_path} ({size}x{size})")

    if not suffix:
        ico_path = ICONS_DIR / "favicon.ico"
        images[16].save(
            ico_path,
            format="ICO",
            sizes=[(16, 16), (32, 32), (48, 48)],
        )
        print(f"Wrote {ico_path} (multi-size)")


if __name__ == "__main__":
    main()
