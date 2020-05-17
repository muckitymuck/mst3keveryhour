
import tweepy

twitter_auth_keys = {
    "consumer_key":   'consumer key',
    "consumer_secret":   'consumer secret',
    "access_token":   'access token',
    "access_token_secret":  'access token secret'
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

shitpost = "Hello Twitter"

mst3kframe = api.media_upload("mst3k-logo.jpg")

tweet = shitpost
post_result = api.update_status(status=tweet, media_ids=[mst3kframe.media_id])
