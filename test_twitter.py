import os
import twitter

api = twitter.Api(consumer_key=os.environ.get("CONSUMER_KEY"), consumer_secret=os.environ.get("CONSUMER_SECRET"), access_token_key=os.environ.get("ACCESS_TOKEN"), access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"))
