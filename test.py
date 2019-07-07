import tweepy

#Authenticate to twitter - OAtuh
auth = tweepy.OAuthHandler("dCAaZvpTfdZAT3vHHr4ZGvONu","6Ejzbi1htkXmzr0leJh6wwYtp017P5z8dtREzy80izZVfz7umt")
auth.set_access_token("1003775737-UwnqTGdyYB3knxGyHGYYxE9GjakSzb1XxMzFsTu","HxLxwY1Cnv3Jgm6zVcfj6pC8ecOKl7TqMKKPj6Uph1InT")

#Create API object - API Class
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#Listing recent trends
