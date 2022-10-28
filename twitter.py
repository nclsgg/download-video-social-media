import os
import requests
import sys
import urllib.request
from dotenv import load_dotenv

load_dotenv()

def getTweetVideo(tweet_url):

  account_name = tweet_url[20:-27]
  twitter_token = os.getenv("TWITTER_BEARER_TOKEN")

  if twitter_token == "":
    print("Please set your Twitter Bearer Token in the .env file")
    sys.exit()

  headers = {
      'Authorization': 'Bearer {}'.format(twitter_token),
  }

  response = requests.get("https://api.twitter.com/2/tweets?ids={}&tweet.fields=attachments&expansions=attachments.media_keys&media.fields=variants,alt_text,preview_image_url,duration_ms,public_metrics".format(tweet_url[-19:]), headers=headers)

  result = response.json()

  if 'errors' in result:
      print("Error: {}".format(result['errors'][0]['detail']))
      sys.exit(1)

  if 'includes' not in result:
      print("No media found")
      sys.exit(1)

  if 'media' not in result['includes']:
      print("Error: No media found.")
      sys.exit(1)

  if 'variants' not in result['includes']['media'][0]:
      print("Error: No media found.")
      sys.exit(1)

  videoURLs = []

  for variant in result['includes']['media'][0]['variants']:
      if variant['content_type'] == 'video/mp4':
        if variant['bit_rate']:
          videoURLs.append({'url': variant['url'], 'bitrate': variant['bit_rate']})
        else:
          videoURLs.append({'url': variant['url']})
      else:
          continue

  if not videoURLs:
      print("Error: No video found.")
      sys.exit(1)

  if len(videoURLs) == 1:
    urllib.request.urlretrieve(videoURLs[0]['url'], "./videos/video-{}-{}.mp4".format(account_name, tweet_url[-19:]))
    print("Video downloaded successfully.")
  else:
    print("Select the video quality you want to download:")
    for i in range(len(videoURLs)):
      print("{}. {} kbps".format(i, videoURLs[i]['bitrate'] / 1000))
    choice = int(input("Enter your choice: "))
    if choice < 0 or choice >= len(videoURLs):
      print("Invalid choice.")
      sys.exit(1)
    urllib.request.urlretrieve(videoURLs[choice]['url'], "./videos/video-{}-{}-{}kbps.mp4".format(account_name, tweet_url[-19:], videoURLs[choice]['bitrate'] / 1000))
    print("Video downloaded successfully.")

  


