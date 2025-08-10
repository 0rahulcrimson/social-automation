import sys

video_path = sys.argv[1] if len(sys.argv) > 1 else None
caption = sys.argv[2] if len(sys.argv) > 2 else " "

print("Instagram upload not executed in this placeholder.")
print("You need to host the video at a temporary URL then:")
print("1) POST /{ig-user-id}/media?media_type=VIDEO&video_url=...&caption=...")
print("2) POST /{ig-user-id}/media_publish?creation_id=...")
print("Env needed: IG_USER_ID, IG_ACCESS_TOKEN")
print("Video to upload:", video_path)
print("Caption:", caption)
