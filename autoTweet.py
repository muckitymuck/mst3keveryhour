
import tweepy

twitter_auth_keys = {
    "consumer_key":   'DeGuuX7YYmZ9irk5FP6b2TH5H',
    "consumer_secret":   '1rNDiSLtBfsD9fLiG0ZrUWCSlLjPmd8M5T9RUkC8c0Jc7F9rTA',
    "access_token":   '14414455-eKInljrZxpbL9KY9gRYA3XPe8iA7c9kvKeGQIbXDl',
    "access_token_secret":  'nRsN2Z84G20gAlsmOdHotOcu6YsgJ6zgngP2DELsDHAHa'
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
