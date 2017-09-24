
# use this to collect all user tweets
import tweepy #https://github.com/tweepy/tweepy
import pandas as pd
import csv
from user_id import get_userid
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from try_again_with_all_the_screen_names import try_again_with_all_the_screen_names

consumer_key = #<---add--->
consumer_secret = #<---add--->
access_key = #<---add--->
access_secret = #<---add--->

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def preset_csv():
    with open('tweets_by_user.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["count_for_each_user", "userid", "screen_name","tweet_id",  "tweet_complete_url",
                         "lang", "created_at", "retweet", "retweet_from", "source",
                         "text", "favorite_count", "retweet_count", 
                         "in_reply_to_screen_name","hastages_count", "hashtags", 
                         "mentions_count", "user_mentions", "urls",
                          "media_type", "photo_media_url", "media_url2"])




def get_all_tweets(user_screennames):
    preset_csv()
    time_count = 0
    for user_screenname in user_screennames:
        #Twitter only allows access to a users most recent 3240 tweets with this method
        #authorize twitter, initialize tweepy
            
        if time_count % 900 == 0:
            time.sleep(600)

        try: 
        
            #user = api.get_user(user_screennames)

            #initialize a list to hold all the tweepy Tweets
            alltweets = []  

            #make initial request for most recent tweets (200 is the maximum allowed count)
            new_tweets = api.user_timeline(screen_name = user_screenname, count=200)
            time_count +=1
            #save most recent tweets
            alltweets.extend(new_tweets)

            #save the id of the oldest tweet less one
            try:
                oldest = alltweets[-1].id - 1
            except IndexError:
                continue

            #keep grabbing tweets until there are no tweets left to grab
            while len(new_tweets) > 0:
                print "getting tweets before %s" % (oldest)

                #all subsiquent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = user_screenname,count=200,max_id=oldest)
                time_count +=1

                #save most recent tweets
                alltweets.extend(new_tweets)

                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1

                print "...%s tweets downloaded so far" % (len(alltweets))
               

            #transform the tweepy tweets into a 2D array that will populate the csv 
            outtweets = []
            count = 0
            for tweet in alltweets:
                count += 1
                try:
                    media_type = tweet.entities['media'][0]['type']
                except KeyError or IndexError :
                    media_type = "NAN"

                try:
                    media_url = tweet.entities['media'][0]['display_url']
                except KeyError or IndexError :
                    media_url = "NAN"

                try:
                    hashtags_lst = []
                    hashtags_count = len(tweet.entities['hashtags'])
                    for i in xrange(hashtags_count):
                        hashtags_lst.append((tweet.entities['hashtags'][i]['text']).encode("utf-8"))
                    hashtags = ','.join(hashtags_lst)
                except IndexError :
                    hashtags  = "NAN"

                try:
                    mentions_lst = []
                    mentions_count = len(tweet.entities['user_mentions'])
                    for i in xrange(mentions_count):
                        mentions_lst.append(tweet.entities['user_mentions'][i]['screen_name'])
                    mentions = ','.join(mentions_lst)
                except IndexError:
                    mentions  = "NAN"

                try:
                    media_url2 = tweet.entities['urls'][0]['expanded_url']
                except IndexError:
                    media_url2 = "NAN"   
                    
                try:
                    if tweet.retweeted_status:
                        retweet_status = True
                        retweet_from = tweet.retweeted_status._json['user']['screen_name']
                except AttributeError :
                    retweet_status = False
                    retweet_from = "NAN"
                
                try: 
                    url_in_tweets = tweet.entities['urls'][0]['display_url']
                except IndexError :
                    url_in_tweets = "NAN"
                        

                tweet_complete_url = "https://twitter.com/"+ tweet.user.screen_name + "/status/" + tweet.id_str
                
                outtweets.append([count, tweet.user.id, tweet.user.screen_name, tweet.id_str,  tweet_complete_url, tweet.lang, tweet.created_at, retweet_status, retweet_from, 
                                  tweet.source,
                          tweet.text.encode("utf-8"), tweet.favorite_count, tweet.retweet_count,
                          tweet.in_reply_to_screen_name, hashtags_count, hashtags,
                           mentions_count, mentions,
                           url_in_tweets, 
                          media_type, media_url, media_url2])

            #write the csv  
            with open('tweets_by_user.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerows(outtweets)
        
        except tweepy.TweepError:
            time_count +=1
            print "Failed to run the command on that user, Skipping...{}".format(user_screenname)
            continue


if __name__ == "__main__":
    df = pd.read_csv('twitter_users.csv')
    user_screennames = list(df['screen_name'])
    get_all_tweets(user_screennames)
    print "completed"
