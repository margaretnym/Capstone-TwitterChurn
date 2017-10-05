
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline 
#import matplotlib
#matplotlib.style.use('ggplot')

#import seaborn as sns
#sns.set(style="ticks")

from datetime import datetime

from scipy import stats
import csv


def churn(person_screen_name):
    timeuntil = datetime.strptime('2017-09-17 00:00:00', '%Y-%m-%d %H:%M:%S')
    diff = []
    df = df_5[df_5['screen_name'] == person_screen_name]
    for i in xrange(df.shape[0]-1):
        
        diff.append(float((df.iloc[i]['created_timestramp'] - df.iloc[i+1]['created_timestramp']).days))
    	
    print person_screen_name 
    #print diff    

    delta_mean = np.mean(diff)
    max_ = max(diff)
    untiltoday = float((timeuntil - df['created_timestramp'].max()).days)
    #t_test = stats.ttest_1samp(diff, untiltoday)
    
    return round(delta_mean,3), round(max_,3), round(untiltoday, 3)


def plot_distribution():
    
    delta_mean_lst, delta_max_list, untiltoday_list, user_all3 = [], [], [], []

    count = 0
    for i in df_5['screen_name'].unique():
        count +=1
	#user_all3 = []
	print count
        mean_, max_, untiltoday_ = churn(i)
        delta_mean_lst.append(mean_)
        delta_max_list.append(max_)
        untiltoday_list.append(untiltoday_)
        user_mean_max_tiltoday = [i, mean_, max_, untiltoday_]
        
        with open('all_user_mean_max33.csv', 'a') as f1:
            writer = csv.writer(f1)
            writer.writerow(user_mean_max_tiltoday)
    
    print 'completed ' + str(len(delta_mean_lst)) + ' ' + str(len(delta_max_list)) + ' ' + str(len(untiltoday_list))
   
    return delta_mean_lst, delta_max_list, untiltoday_list

if __name__ == "__main__":
    df_tweets = pd.read_csv('tweets_combo_0924.csv')
    df_have_fifth_tweet = df_tweets[df_tweets['count_for_each_user'] == 5]['screen_name']
    df_5 = df_tweets[df_tweets['screen_name'].isin(list(df_have_fifth_tweet ))]
    df_5['created_timestramp'] =  pd.to_datetime(df_5['created_at'], infer_datetime_format=True)
    delta_mean_lst, delta_max_list, untiltoday_list = plot_distribution()
