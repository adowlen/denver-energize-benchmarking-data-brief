"""Composite the headline figure over the generated hero illustration.
Run by the morning QA run (parent) after inspecting the illustration.
Text sits on a gradient scrim across the top for legibility; headline
text is the exact text specified in hero_source/hero-brief.md."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

root = pathlib.Path(__file__).resolve().parent.parent
cands = sorted((root / "hero_source").glob("*.webp")) + \
        sorted((root / "hero_source").glob("*.png")) + \
        sorted((root / "hero_source").glob("*.jpg"))
cands = [c for c in cands if c.name != "hero.png"]
if not cands:
    raise SystemExit("no hero illustration in hero_source/ - hero stays pending")
img = Image.open(cands[0]).convert("RGB")
W, H = img.size

# Gradient scrim: solid dark charcoal at the very top, fading to
# transparent at 42 percent of the height.
band = int(H * 0.42)
overlay = Image.new("L", (1, band))
for yy in range(band):
    t = yy / band
    overlay.putpixel((0, yy), int(255 * (1 - t) ** 1.4))
overlay = overlay.resize((W, band))
scrim = Image.new("RGB", (W, band), (13, 17, 20))
img.paste(scrim, (0, 0), overlay)
d = ImageDraw.Draw(img)


def font(size, bold=True):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p, size)


def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= maxw:
            cur = trial
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


MAXW = W - 124
headline = "53.1 vs 64.8"
d.text((60, 36), headline, font=font(int(H * 0.098)), fill=(245, 168, 0))
sub_f = font(int(H * 0.034), bold=False)
y = 36 + int(H * 0.128)
sub = ("Median site EUI (kBtu per square foot): the 984 buildings reporting in "
       "both 2016 and 2025 report 53.1 in 2025 against 64.8 in 2016")
for line in wrap(sub, sub_f, MAXW):
    d.text((62, y), line, font=sub_f, fill=(242, 242, 242))
    y += int(H * 0.050)
src_f = font(int(H * 0.024), bold=False)
srcline = ("Machine Readable - Energize Denver Final Master Datasets 2016 and "
           "2025, pulled Oct 29, 2026 - matched panel of 984 buildings")
for line in wrap(srcline, src_f, MAXW):
    d.text((62, y + 6), line, font=src_f, fill=(150, 210, 200))
    y += int(H * 0.038)
img.save(root / "hero.png")
print("hero", img.size, "from", cands[0].name)
