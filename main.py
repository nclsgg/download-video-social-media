from twitter import getTweetVideo


print("Insert twitter URL: ")
url = input()

if "https://twitter.com/" in url:
  getTweetVideo(url)
else: 
  print("This URL is not a valid twitter URL")
