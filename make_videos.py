import os
import math
import numpy as np
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips, vfx

# Input / Output paths
IMAGES_DIR = "out/images"
VIDEOS_DIR = "out/videos"
os.makedirs(VIDEOS_DIR, exist_ok=True)

# Video settings
duration = 4  # seconds per image
final_size = (1080, 1920)  # Instagram Reels / Shorts size

clips = []

# Loop through images in the output folder
for filename in sorted(os.listdir(IMAGES_DIR)):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(IMAGES_DIR, filename)

        # Load image with Pillow
        pil_img = Image.open(img_path).convert("RGB")

        # Convert to NumPy array for MoviePy
        clip = ImageClip(np.array(pil_img)).set_duration(duration)

        # Resize slightly larger for subtle motion zoom
        clip = clip.fx(vfx.resize, 1.04).set_position(
            lambda t: ("center", final_size[1] / 2 + 30 * math.sin(t / 2.5))
        )

        # Resize to final video size (using Pillow's modern resampling method)
        clip = clip.resize(newsize=final_size)

        clips.append(clip)

# Concatenate all image clips
if clips:
    final_video = concatenate_videoclips(clips, method="compose")
    output_path = os.path.join(VIDEOS_DIR, "slideshow.mp4")

    # Write the final video
    final_video.write_videofile(
        output_path, fps=30, codec="libx264", audio=False, threads=4
    )

    print(f"Video saved to {output_path}")
else:
    print("No images found to make videos.")
