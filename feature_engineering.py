# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from datetime import datetime
import csv

def created_date_til_today(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    created_timestramp =  pd.to_datetime(df['created_date'], infer_datetime_format=True)
    timeuntil = datetime.strptime('2017-07-19 00:00:00', '%Y-%m-%d %H:%M:%S')
    days_between = (timeuntil - created_timestramp)
    days = days_between.values.astype('timedelta64[D]')
    return days / np.timedelta64(1, 'D')

def locationY_N(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    if df['location'].values[0] == "NaN":
        return False
    else:
        return True

def descriptionY_N(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    if df['description'].values[0] == "NaN":
        return False
    else:
        return True

def statuses_fav_count_by_lifespan(person_screen_name):
    df_tweet = df_alltweets[df_alltweets['screen_name'] == person_screen_name].tail(1)
    last_tweets_timestramp = pd.to_datetime(df_tweet['created_at'], infer_datetime_format=True)
    df_people = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    created_timestramp =  pd.to_datetime(df_people['created_date'], infer_datetime_format=True)
    
    days_between = last_tweets_timestramp.values[0] - created_timestramp.values[0]
    days = days_between.astype('timedelta64[D]')
    lifespan =  days / np.timedelta64(1, 'D')
    
    status_lifespan = df_people.statuses_count.values[0]/float(lifespan+0.1)
    fav_lifespan = df_people.favorites.values[0]/float(lifespan+0.01)
    
    return status_lifespan, fav_lifespan

def verifiedY_N(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    if df['verified'].values[0]:
        return True
    else:
        return False

def friends_followers_follower_friend_ratio(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    ratio = df['followers'].values[0]/(df['friends'].values[0] + 0.01) * 1.0
    return df['friends'].values[0], df['followers'].values[0], ratio


def profilepicY_N(person_screen_name):
    df = df_allpeople[df_allpeople['screen_name'] == person_screen_name]
    if df['profilepic'].values[0] == 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png':
        return False
    else:
        return True

def average_len(person_screen_name):
    list_of_len = []
    df = df_alltweets[df_alltweets['screen_name'] == person_screen_name]
    for i in xrange(df.shape[0]):
        list_of_len.append(len(df.iloc[i]['text']))       
    print person_screen_name
    mean = np.mean(list_of_len)
    return mean

def retweet_ratio(person_screen_name):
    count_retweet = 0
    df = df_alltweets[df_alltweets['screen_name'] == person_screen_name]
    for i in xrange(df.shape[0]):
        if df.iloc[i]['retweet']:
            count_retweet += 1
    return count_retweet/float(df.shape[0]+ 0.01)

def orginal_favorite_retweet_hastages_mention_url_media_count(person_screen_name):
    df = df_alltweets[df_alltweets['screen_name'] == person_screen_name]
    df = df[df['retweet']!= True]
    sum_fav, sum_retweet,sum_hastages, sum_mentions, sum_url, sum_media_type  = 0, 0, 0, 0, 0, 0
    
    for i in xrange(df.shape[0]):
        
        if df['favorite_count'].iloc[i] != 0 and df['retweet'].iloc[i] != True:
            sum_fav += 1 
            
        if df['retweet_count'].iloc[i] != 0 and df['retweet'].iloc[i] != True:
            sum_retweet += 1

        if df['hastages_count'].iloc[i] != 0 and df['retweet'].iloc[i] != True:
            sum_hastages += 1
        
        if df['mentions_count'].iloc[i] != 0 and df['retweet'].iloc[i] != True:
            sum_mentions += 1
    
        if df['urls'].iloc[i] != "NAN" and df['retweet'].iloc[i] != True:
            sum_url += 1
    
        if df['media_type'].iloc[i] != "NAN" and df['retweet'].iloc[i] != True:
            sum_media_type += 1
    
    return sum_fav/float(df.shape[0] + 0.01), sum_retweet/float(df.shape[0]+ 0.01), sum_hastages/float(df.shape[0]+ 0.01), \
     sum_mentions/float(df.shape[0]+ 0.01), sum_url/float(df.shape[0]+ 0.01), sum_media_type/float(df.shape[0]+ 0.01)

def freq_source_group(person_screen_name):
    app_list = ['Twitter for iPhone','Twitter for Android', 'Twitter for  Android', 'Twitter for BlackBerry®', 'Mobile Web (M2)',
                'iOS' ,'Twitter for iPad','UberSocial for BlackBerry', 'Twitter Lite', 'Echofon','TweetCaster for Android' , 
                'Twitter for Windows Phone', 'Mobile Web', 'iOS', 'Foursquare', 'Path']
    computer_list = ['Twitter Web Client', 'TweetDeck','twitterfeed', 'Twitter for Websites', 'Google', 'Hootsuite']
    soialmedia = ['Facebook','Tumblr', 'Instagram']
    bot = ['twittbot.net', 'Tweetbot for iΟS', 'Twittascope']
    
    app_list_counts, computer_list_counts, soialmedia_counts, bot_counts, other_counts = 0,0,0,0,0
    
    
    df = df_alltweets[df_alltweets['screen_name'] == person_screen_name]
    if df['source'].values[0] in app_list:
        app_list_counts += 1
    elif df['source'].values[0] in computer_list:
        computer_list_counts += 1
    elif df['source'].values[0] in soialmedia:
        soialmedia_counts += 1
    elif df['source'].values[0] in bot:
        bot_counts += 1
    else:
        other_counts += 1
    
    d = {'app': app_list_counts, 'computer': computer_list_counts, 'social_media': soialmedia_counts, 'bot': bot_counts, 'other': other_counts}
    return max(d, key=d.get)


def features_print_out():    
    count = 0
    for i in df_alltweets['screen_name'].unique():
        count +=1 
        print str(count) + " " + str(i)
    
        created_date_since_today_ = created_date_til_today(i)
        location_ = locationY_N(i)
        description_ =  descriptionY_N(i)
        status_lifespan_, fav_lifespan_ = statuses_fav_count_by_lifespan(i)
        verified_ = verifiedY_N(i)
        friends_count_, followers_count_ , ratio = friends_followers_follower_friend_ratio(i)
        profile_ = profilepicY_N(i)
        avg_len_ = average_len(i)
        retweet_ratio_ = retweet_ratio(i)
        org_fav_, org_retweet_,org_hastages_ ,org_mentions_ ,org_url_ ,org_media_type_ = orginal_favorite_retweet_hastages_mention_url_media_count(i)
        source_ = freq_source_group(i)

    
        list_to_print = [i,created_date_since_today_,location_, status_lifespan_, fav_lifespan_, verified_, friends_count_, followers_count_, ratio,\
                        profile_, avg_len_, retweet_ratio_, org_fav_, org_retweet_,org_hastages_ ,org_mentions_ ,org_url_ ,org_media_type_, \
                        source_]
    
        with open('features3.csv', 'a') as f1:
            writer = csv.writer(f1)
            writer.writerow(list_to_print)

if __name__ == "__main__":   
    df_allpeople = pd.read_csv('all_user_list.csv', error_bad_lines=False)
    df_alltweets  = pd.read_csv('combo.csv', error_bad_lines=False )
    features_print_out()


