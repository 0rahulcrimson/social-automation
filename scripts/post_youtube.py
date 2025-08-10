import sys, os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# Usage: python scripts/post_youtube.py <video_path> "<title>"
if len(sys.argv) < 2:
    print("Usage: python scripts/post_youtube.py <video_path> \"<title>\"")
    sys.exit(1)

video_path = sys.argv[1]
title = sys.argv[2] if len(sys.argv) > 2 else "Shorts"

creds = Credentials(
    None,
    refresh_token=os.environ["YT_REFRESH_TOKEN"],
    client_id=os.environ["YT_CLIENT_ID"],
    client_secret=os.environ["YT_CLIENT_SECRET"],
    token_uri="https://oauth2.googleapis.com/token",
    scopes=["https://www.googleapis.com/auth/youtube.upload"],
)

youtube = build("youtube", "v3", credentials=creds)
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {"title": title, "description": "", "categoryId": "22"},
        "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False},
    },
    media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True),
)
response = None
while response is None:
    status, response = request.next_chunk()
    if status:
        print(f"Uploaded {int(status.progress()*100)}%")
print("YouTube upload complete:", response.get("id"))
