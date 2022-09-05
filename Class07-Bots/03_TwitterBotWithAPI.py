import tweepy
import json
import xkcd_wrapper
import time

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
random_comic = xkcd_client.get_random()   # comic object of a random comic

def botTweet():
	tweet = "Here's a comic from the year " + str(random_comic.date.year) + " and it's called " + random_comic.title;
	api.update_status(tweet)

while True:
	botTweet()
	time.sleep(30)