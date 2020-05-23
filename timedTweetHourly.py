import tweepy
import time
import os

twitter_auth_keys = {
    "consumer_key":   'consumer key',
    "consumer_secret":   'consumer secret',
    "access_token":   'access token',
    "access_token_secret":  'access secret'
    }

auth = tweepy.OAuthHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
    )

auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']

    )

api = tweepy.API(auth)

# tweet directory
basepath = 'C:/Path to frames collection/'

# Saved code for adding features
# Tweet time message
# tweetText = "Tweeting on time"
#
# for count in range(10):
#    api.update_status(tweetText + time.ctime())
#    time.sleep(3600)

for entry in os.listdir(basepath):
    if os.scandir(basepath):
        frameUpload = api.media_upload(entry)
        post_result = api.update_status(media_ids=[frameUpload.media_id])
        time.sleep(3600)