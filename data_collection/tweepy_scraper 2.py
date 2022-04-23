
import tweepy as tw
import pandas as pd
from datetime import datetime
import os

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''
numTweets = 3000

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "(russia OR ukraine OR putin OR zelensky OR russian OR ukrainian OR keiv OR kyiv OR #RussianUkranianWar OR #RussiaUkraineConflict OR #RussiaUkraineWar OR #UkraineRussiaWar OR #StopRussia OR #RussianWarCrimes OR Putin OR Kharkiv)"
mod_search = search_words + " -filter:retweets"
tweets = tw.Cursor(api.search_tweets, q=mod_search, lang="en", tweet_mode='extended').items(numTweets)
# Store these tweets into a python list
tweet_list = [tweet for tweet in tweets]

# Begin scraping the tweets individually:
db_tweets = pd.DataFrame(columns = ['text','id', 'author_id', 'parent_tw_id', 'username',
                                        'created_utc', 'location','rewtweet_count', 'fav_count'])

for tweet in tweet_list:
    # Pull the values
    text = tweet._json["full_text"]
    tw_id = tweet.id
    author_id = tweet.author.id,
    parent_tw_id = tweet.in_reply_to_status_id,
    username = tweet.user.screen_name,
    created = tweet.created_at,
    location = tweet.user.location,
    rt_count = tweet.retweet_count,
    fav_count = tweet.favorite_count

    ith_tweet = [text, tw_id, author_id, parent_tw_id, username, created, location, rt_count,
                 fav_count]

    # Append to dataframe - db_tweets
    db_tweets.loc[len(db_tweets)] = ith_tweet

# Obtain timestamp in a readable format
to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')

# Define working path and filename
path = os.getcwd()
filename = to_csv_timestamp + 'twitter_data.csv'

# Store dataframe in csv with creation date timestamp
db_tweets.to_csv(filename, index=False)