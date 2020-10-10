import tweepy
import time
#twitter permmisions

auth = tweepy.OAuthHandler('Api keys','Api secret')
auth.set_access_token('Acess tokens','Access secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

#likes and retweets

search = '100DaysOfCode'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
