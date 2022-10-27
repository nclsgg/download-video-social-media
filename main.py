from twitter import getTweetVideo
from pathlib import Path

Path("./videos").mkdir(parents=True, exist_ok=True)

print("Insert twitter URL: ")
url = input()

if "https://twitter.com/" in url:
  getTweetVideo(url)
else: 
  print("This URL is not a valid twitter URL")
