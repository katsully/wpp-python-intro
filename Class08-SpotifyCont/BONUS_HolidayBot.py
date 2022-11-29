import json
import tweepy
import requests
import urllib.request
import io
import random
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

# we'll be using the Public Holiday API to see the next public holiday
# documentation can be found here: https://date.nager.at/Api
# put this URL in your browser to see the data! - highly recommend installing a JSON formatter chrome extension as well
holiday_url = "https://date.nager.at/Api/v2/NextPublicHolidaysWorldWide"
# this returns a list of dictionaries containing all public holidays for the next 7 days
holiday_data = requests.get(holiday_url).json()

def botTweet():
	# pick one of the upcoming holidays and determine which country is celebrating the holiday
	# we subtract one from the length because if the length is 10, the last index in the list will be 9
	random_holiday = holiday_data[random.randint(0, len(holiday_data)-1)]
	country_code = random_holiday['countryCode']

	# we'll be using the world countries API to find the flag for whichever country is celebrating the holiday
	# we can also convert the country code (ie FR) to the full country name
	# see API documentation here: http://www.geognos.com/geo/en/world-countries-API.html
	flag_url = "http://www.geognos.com/api/en/countries/flag/" + country_code + ".png"
	country_data = requests.get("http://www.geognos.com/api/en/countries/info/" + country_code + ".json").json()
	country_name = country_data["Results"]["Name"]

	# compose the tweet
	tweet = "Upcoming Holiday Alert: " + random_holiday['localName'] + " on " + random_holiday['date'] + " in " + country_name

	# get flag image and post tweet
	img = urllib.request.urlopen(flag_url).read()
	file_like_object = io.BytesIO(img)

	api.update_status_with_media(tweet, country_code, file=file_like_object)
	print(tweet)

# post every 30 seconds
# that's WAY too much for a bot but 30 seconds is nice when you're trying something out
while True:
	botTweet()
	time.sleep(30)
