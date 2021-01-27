from tweepy.streaming import StreamListener
# # # # TWITTER STREAMER to JSON File # # # #


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
