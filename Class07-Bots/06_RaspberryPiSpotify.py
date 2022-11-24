import spotipy
import json
import webbrowser
import urllib.request
import spotipy.util as util
import sys

# open file with keys and set the path to your credentials JSON file
credentials = "spotify_keys.json"
with open(credentials, "r") as keys:
    api_tokens = json.load(keys)

# read the keys and assign each to a variable
# A redirect URI, or reply URL, is the location where the authorization server sends the user once the app has been 
# successfully authorized and granted an authorization code or access token.
client_id = api_tokens["client_id"]
client_secret = api_tokens["client_secret"]
redirectURI = api_tokens["redirect"]
username = api_tokens["username"]
weather_key = api_tokens["weather_api"]

# UNCOMMENT TO USE SYSTEM ARGUMENTS!!!
# city = sys.argv[1]
# request = urllib.request.Request("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + weather_key)

# copy and paste the url into your browser to see what data you are getting back
request = urllib.request.Request("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=" + weather_key)
response = urllib.request.urlopen(request)

weather = json.loads(response.read())
forecast = weather["weather"][0]["description"]


scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=redirectURI)

# Create Spotify Object
sp = spotipy.Spotify(auth=token)

# learn about more query strings for spotify here: https://developer.spotify.com/documentation/web-api/reference/#/operations/search
track_results = sp.search(q=forecast, type='track', limit=50)
tracks = track_results['tracks']['items']

# URI = uniform resource identifier
track_selection_list = []

for song in tracks:
    track_selection_list.append(song['uri'])

my_playlist = sp.user_playlist_create(user=username, name=forecast, public=True,
                                      description="Songs for the weather")
results = sp.user_playlist_add_tracks(username, my_playlist['id'], track_selection_list)
webbrowser.open(my_playlist['external_urls']['spotify'])

