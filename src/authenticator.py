from tweepy import OAuthHandler

from dotenv import load_dotenv
import os
load_dotenv()


# # # # TWITTER AUTHENTICATOR # # # #


class TwitterAuthenticator():
    def authenticate(self):
        auth = OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
        auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                              os.getenv("ACCESS_TOKEN_SECRET"))
        return auth
