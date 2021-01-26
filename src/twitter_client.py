from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient

import numpy
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")

# # # # TWITTER AUTHENTICATOR # # # #


class TwitterAuthenticator():
    def authenticate(self):
        auth = OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
        auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                              os.getenv("ACCESS_TOKEN_SECRET"))
        return auth


# # # # TWITTER CLIENT # # # #

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_client(self):
        return self.twitter_client

# # # # TWITTER STREAMER # # # #


class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # Handles Twitter authentication and connection to Twitter Streaming API

        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate()

        stream = Stream(auth, listener)
        print("")
        print("----------------------")
        print("Streaming: ", stream)
        print("----------------------")
        print("")
        stream.filter(languages=["en"], track=hash_tag_list)


class TwitterListener(StreamListener):
    """
    This is a basic listener class that prints tweets to stdout
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            # print(data)
            with open(self.fetched_tweets_filename, "a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data in case rate limit occurs. Important!
            return False
        print(status)


class TweetAnalyzer():
    """
    Analize and categorize content from tweets
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):


if __name__ == "__main__":
    # twitter_client = TwitterClient()

    # api = twitter_client.get_client()

    # tweets = api.user_timeline(screen_name="unusual_whales", count=20)
    # print(tweets)
    hash_tag_list = ["$GME", "$PLTR", "$TSLA", "$MT", "$BB"]

    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
