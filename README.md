# social-automation-starter

Minimal GitHub Actions pipeline that **generates images + vertical videos** on a free GitHub-hosted runner (CPU only). No AI models used. Easy to upgrade to AI later (Stable Diffusion, etc.).

## What it does
- Creates 5 quote images (1080×1350)
- Creates 3 vertical reels (1080×1920, 60–90s)
- Saves them as build artifacts
- (Optional) Uploads 1 video to YouTube Shorts / Instagram via scripts

## Quick start
1. Push this repo to GitHub.
2. In the repo, open **Actions** tab → run **Generate Media & (Optional) Post** via *Run workflow*.
3. Download artifacts from the run to verify outputs.

## Local run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python make_images.py
python make_videos.py
```
Outputs are in `out/images` and `out/videos`.

## Optional: posting
- **YouTube Shorts**: add repo **Secrets**:
  - `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`
- **Instagram**: add `IG_USER_ID`, `IG_ACCESS_TOKEN` (business/creator account + FB Page). The provided script is a placeholder—host the MP4 at a temporary URL and call the Graph API.

## Upgrade to AI later
Swap `make_images.py` / `make_videos.py` with model code in **new steps** (or same steps). If it needs GPU, move to a **self-hosted runner** and set `runs-on: [self-hosted, gpu]`.

## Notes
- MoviePy needs **FFmpeg** (installed in the workflow).
- No ImageMagick dependency (text is rendered with Pillow).
