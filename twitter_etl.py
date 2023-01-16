# import the necessary packages
# import tweepy to access the Twitter API
import tweepy
import pandas as pd 
import json
from datetime import datetime
# import s3fs to interact with Amazon S3 as if it were a local file system.
import s3fs 

def run_twitter_etl():

    #  authenticate and authorize access to my twitter account account
    access_key = "" 
    access_secret = "" 
    #  identify the application that is making requests to the Twitter API
    consumer_key = ""
    consumer_secret = ""


    # Twitter authentication
    authentification = tweepy.OAuthHandler(access_key, access_secret)   
    authentification.set_access_token(consumer_key, consumer_secret) 

    # Creating an instance of the tweepy.API
    api = tweepy.API(authentification)
    
    # print(tweets)
    
    # retrieve the tweets from a user's home timeline. For example :
    users = ['@elonmusk','@BarackObama','@BillGates','@Tim_Cook','@YouTube','@SatyaNadella','@jack','@finkd','@jeffweiner ']
    tweets_list = []
    for user in users:
        tweets = api.user_timeline(screen_name=user, 
                            count=200,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )
        # we store these information in a list
        tweets_list.append(tweets)

    tweets_infos = []
    for tweet in tweets_list:
        # for each tweet we exctract the user name, the tweet, number of likes, number of retweets and the date of creation of the tweet
        text = tweet._json["full_text"]

        tweet_infos = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        # we store these information in a list
        tweets_infos.append(tweet_infos)

    # Convert the list into a dataframe
    df = pd.DataFrame(tweets_infos)
    # Connect to the S3 bucket
    fs = s3fs.S3FileSystem()

    # write the DataFrame to the specified S3 bucket
    with fs.open('s3://nadine_airflow_bucket/tweets.csv', 'w') as f:
       df.to_csv(f)
       df.to_csv('s3://nadine-tweets-bucket/tweets.csv')
