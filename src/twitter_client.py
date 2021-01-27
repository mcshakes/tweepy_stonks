from tweepy import API
from tweepy import Cursor
from pymongo import MongoClient
from textblob import TextBlob
from streamer import TwitterStreamer

import numpy
import pandas as pd

# MONGO_HOST = os.getenv("MONGO_HOST")

# # # # TWITTER CLIENT # # # #


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_client(self):
        return self.twitter_client


class TweetAnalyzer():
    """
    Analize and categorize content from tweets
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        pass

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(
            data=[tweet.text for tweet in tweets], columns=["tweets"])

        df["id"] = np.array([tweet.id for tweet in tweets])
        df["len"] = np.array([len(tweet.text) for tweet in tweets])
        df["date"] = np.array([tweet.created_at for tweet in tweets])
        df["likes"] = np.array([tweet.favorite_count for tweet in tweets])
        df["retweets"] = np.array([tweet.retweet_count for tweet in tweets])


if __name__ == "__main__":
    # twitter_client = TwitterClient()

    # api = twitter_client.get_client()

    # tweets = api.user_timeline(screen_name="unusual_whales", count=20)
    # print(tweets)
    hash_tag_list = ["$GME", "$PLTR", "$TSLA", "$MT", "$BB"]

    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    tweet_analyzer = TweetAnalyzer()

    tweets = twitter_streamer.stream_tweets(
        fetched_tweets_filename, hash_tag_list)

    # data_frame = tweet_analyzer.tweets_to_data_frame(tweets)

    # data_frame["sentiment"] = np.array(
    #     [tweet_analyzer.analyze_sentiment(tweet) for tweet in data_frame["tweets"]])


# import code
#         code.interact(local=dict(globals(), **locals()))
