import os

POSTS_DIR = "notes"
NAVIGATION_FILE = "navigation.html"

files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
files.sort()

with open(NAVIGATION_FILE, "w", encoding="utf-8") as f:
    for filename in files:
        f.write(f'<a hx-get="{POSTS_DIR}/{filename}" hx-target="#content">{filename.replace(".html", "")}</a>\n')
