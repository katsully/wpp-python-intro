import tweepy
import json
import xkcd_wrapper
import time
import urllib.request
import io

credentials = "keys.json"
with open(credentials, 'r') as keys:
	api_tokens = json.load(keys)

bearer_token = api_tokens["bearer_token"]
api_key = api_tokens["api_key"]
api_secret = api_tokens["api_secret"]
access_token = api_tokens["access_token"]
access_secret = api_tokens["access_secret"]

auth = tweepy.OAuthHandler(api_key, api_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
	print("Error during authentication")

# xkcd API request
# documentation for the python wrapper here: https://github.com/Kronopt/xkcd-wrapper
xkcd_client = xkcd_wrapper.Client()

def botTweet():
	random_comic = xkcd_client.get_random()   # comic object of a random comic
	
	# upload your comic image
	url = random_comic.image_url
	tweet = "Here's a comic from the year " + str(random_comic.date.year) + " and it's called " + random_comic.title;
	img = urllib.request.urlopen(url).read()
	file_like_object = io.BytesIO(img)

	# we're passing in the status (ie the tweet), the filename, and the file
	api.update_status_with_media(tweet, random_comic.title, file=file_like_object)
	print(tweet)

while True:
	botTweet()
	time.sleep(30)