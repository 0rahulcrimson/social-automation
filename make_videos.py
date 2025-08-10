import os, random, math
from datetime import datetime
from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip, vfx
from PIL import Image, ImageDraw, ImageFont
from utils.texts import QUOTES

OUT_DIR = "out/videos"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1080, 1920  # vertical
D_MIN, D_MAX = 60, 90

def load_font(size):
    for name in ["Arial.ttf", "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try:
            from PIL import ImageFont
            return ImageFont.truetype(name, size)
        except:
            continue
    return ImageFont.load_default()

def render_quote_frame(quote: str):
    img = Image.new("RGB", (W, H), color=(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40)))
    draw = ImageDraw.Draw(img)
    title_font = load_font(92)
    body_font = load_font(42)

    import textwrap
    wrapped = "\n".join(textwrap.wrap(quote, width=18))
    bbox = draw.multiline_textbbox((0,0), wrapped, font=title_font, align="center", spacing=10)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.multiline_text(((W-tw)//2, (H-th)//2 - 40), wrapped, font=title_font, fill=(245,245,245), align="center", spacing=10)

    footer = "@yourhandle"
    fw, fh = draw.textbbox((0,0), footer, font=body_font)[2:]
    draw.text(((W - fw)//2, H - fh - 60), footer, font=body_font, fill=(230,230,230))

    return img

for i in range(3):
    duration = random.randint(D_MIN, D_MAX)
    quote = random.choice(QUOTES)
    pil_img = render_quote_frame(quote)
    clip = ImageClip(pil_img).set_duration(duration)

    clip = clip.fx(vfx.resize, 1.04).set_position(lambda t: ("center", H/2 + 30*math.sin(t/2.5)))
    clip = clip.set_fps(30)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(OUT_DIR, f"reel_{ts}_{i}.mp4")
    clip.write_videofile(out_path, codec="libx264", audio=False, fps=30, preset="medium", threads=2)
    print("Saved", out_path)

print("Videos saved to", OUT_DIR)
