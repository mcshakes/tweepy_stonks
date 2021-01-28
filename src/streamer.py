from listener import TwitterListener
from authenticator import TwitterAuthenticator
from tweepy import Stream

# # # # TWITTER STREAMER to JSON File # # # #


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
