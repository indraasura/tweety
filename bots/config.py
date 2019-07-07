# Reusable script

import tweepy
import logging


logger = logging.getLogger()

def create_api():
    # Read env variables and create auth object
    consumer_key = "dCAaZvpTfdZAT3vHHr4ZGvONu"
    consumer_secret = "6Ejzbi1htkXmzr0leJh6wwYtp017P5z8dtREzy80izZVfz7umt"
    access_token = "1003775737-UwnqTGdyYB3knxGyHGYYxE9GjakSzb1XxMzFsTu"
    access_token_secret = "HxLxwY1Cnv3Jgm6zVcfj6pC8ecOKl7TqMKKPj6Uph1InT"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api