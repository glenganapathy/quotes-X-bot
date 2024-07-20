import tweepy
import tweepy.client
from selectquote import randomly_select_and_remove_quote

#API keys
api_key = 'your_api_key'
api_secret_key = 'your_api_secret_key'
bearer_token = 'your_bearer_token'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authentication of app on X
client = tweepy.Client(bearer_token, api_key, api_secret_key, access_token, access_token_secret)

# to access v1 endpoints
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

csv_file = r'path\to\your\quotes.csv'


#to tweet multiple tweets at the same time
#change n value to number of tweets and uncomment the below snippet
'''
n = 10
while n:    
    tweet = randomly_select_and_remove_quote(csv_file)

    print(tweet)
    n-=1

    #tweet
    client.create_tweet(text=tweet)
'''

tweet = randomly_select_and_remove_quote(csv_file)
#print(tweet)

#create a tweet
client.create_tweet(text=tweet)
