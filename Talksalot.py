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
# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 15
# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1