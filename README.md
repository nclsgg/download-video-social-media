# download-video-social-media
A simple social media video downloader

I created this project because everytime i see a funny video on twitter i have to join in a website and make a little survey to download de video. With this script, i just send the tweet url and get the video :)

I have plans to update this project to download videos from other social medias like instagram, youtube, facebook...

PS: Python isn't my main language, so, i dont know about PEP8.

## Required packages

```
- requests
- os
- sys
- urllib.request
- dotenv
```

## How to run application

First of all, install all the required packages if you don't have any of them:

```
pip install [package]
```

Then, you have to add your [TwitterAPI](https://developer.twitter.com/ja/docs/basics/authentication/guides/access-tokens#:~:text=Generating%20access%20tokens&text=Login%20to%20your%20Twitter%20account,%26%20access%20token%20secret%22%20section.) bearer token on the .env file (sorry for that... is just a local application).

One time you added your TwitterAPI Bearer Token, is just run the application :)
```
python ./main.py
```

## How to use the application

When you run the app, you'll be asked for the twitter post URL. So, you just have to copy the post URL and paste in the terminal. If the URL is from a post which have a video media, the application will ask to you choose which bitrate you want to download and will download the video in the folder "videos".

-------------------------------------------------

If you see any bug or have a suggestion to improve the code, just fork the project or DM me on twitter, @NicolasTSX :D
