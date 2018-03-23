# Dependencies
import tweepy
import json
import time
# Twitter API Keys
consumer_key = "QiXSjj5Jdr3rgST8mRefRaVU0"
consumer_secret = "2G1vw2GqzGg1iN0zKoR4EXzwRgnrSMRUfZviOdwlghOcJwikVo"
access_token = "936508446-Y4rpk0TmJsgH1s35Ot2qdJy2yidK9zNGjPvBxa6v"
access_token_secret = "ZhosHPGiHkY1h7vDgr14nk4cmPfJyDEqNO6nAUVmyKNg0"
# Weather API
api_key = "14ac49b5c9e1c8fc43ab267ab462e621"
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "London Weather as of %s: %s F" %
        (datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)