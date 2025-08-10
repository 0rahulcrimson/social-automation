from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime
import os, textwrap, random
from utils.texts import QUOTES

OUT_DIR = "out/images"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1080, 1350  # 4:5 portrait for IG
MARGIN = 80

def random_bg():
    base = Image.new("RGB", (W, H), (random.randint(0, 30), random.randint(0, 30), random.randint(0, 30)))
    overlay = Image.new("RGB", (W, H), (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120)))
    overlay = overlay.resize((W, H)).filter(ImageFilter.GaussianBlur(radius=80))
    base = Image.blend(base, overlay, alpha=0.35)
    return base

def load_font(size):
    for name in ["Arial.ttf", "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except:
            continue
    return ImageFont.load_default()

title_font = load_font(84)
body_font = load_font(40)

for i in range(5):
    img = random_bg()
    draw = ImageDraw.Draw(img)
    quote = random.choice(QUOTES)
    wrapped = textwrap.fill(quote, width=16)
    bbox = draw.multiline_textbbox((0,0), wrapped, font=title_font, spacing=8, align="center")
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.rounded_rectangle([(MARGIN, MARGIN), (W-MARGIN, H-MARGIN)], radius=40, outline=(255,255,255), width=4)
    draw.multiline_text(((W - tw)//2, (H - th)//2 - 20), wrapped, fill=(245,245,245), font=title_font, align="center", spacing=8)

    footer = "@yourhandle"
    fw, fh = draw.textbbox((0,0), footer, font=body_font)[2:]
    draw.text(((W - fw)//2, H - fh - 40), footer, font=body_font, fill=(220,220,220))

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(OUT_DIR, f"card_{ts}_{i}.jpg")
    img.save(path, quality=95)
    print("Saved", path)

print("Images saved to", OUT_DIR)
