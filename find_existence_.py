


import time
import tweepy
import numpy as np
import csv


def generate_random_userID(maxi, size):
    sample_id = np.random.randint(1, high= maxi, size = size)
    return sample_id

def grap_the_existent_users(sample_id_lst):

    consumer_key = #<--add --> 
    consumer_secret = #<--add --> 
    access_key = #<--add --> 
    access_secret = #<--add --> 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    screen_name = []
    name= []
    created_at= []
    location= []
    lang = []
    description= []
    statuses_count= []
    verified= []
    friends_count= []
    followers_count= []
    favourites_count= []
    profile_image_url= []
    profile_background_image_url_https= []
    lastT_id_str= []
    lastT_text= []
    lastT_created_at= []

    count, real = 0, 0
    for i in sample_id_lst:
        count +=1
        if count % 900 == 0:
            time.sleep(600)
        else:
            try:
                users_list = api.get_user(i)
                screen_name.append(users_list.screen_name)
                name.append((users_list.name).encode('utf8'))
                created_at.append(str(users_list.created_at))
                location.append((users_list.location).encode('utf8'))
                lang.append(users_list.lang)
                description.append((users_list.description).encode('utf8'))
                statuses_count.append(users_list.statuses_count)
                verified.append(users_list.verified)
                friends_count.append(users_list.friends_count)
                followers_count.append(users_list.followers_count)
                favourites_count.append(users_list.favourites_count)
                profile_image_url.append(users_list.profile_image_url)
                profile_background_image_url_https.append(users_list.profile_background_image_url_https)
                real +=1
                print str(count) + "trails real_person: " + str(real) + " " + users_list.screen_name + ' successfully captured'

            except tweepy.TweepError:
                print "NO USER ASSOCIATE WITH " + str(i)
                screen_name.append('NAN')
                name.append('NAN')
                created_at.append('NAN')
                location.append('NAN')
                lang.append('NAN')
                description.append('NAN')
                statuses_count.append('NAN')
                verified.append('NAN')
                friends_count.append('NAN')
                followers_count.append('NAN')
                favourites_count.append('NAN')
                profile_image_url.append('NAN')
                profile_background_image_url_https.append('NAN')

    with open('existence2.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(zip(sample_id_lst,
                            screen_name,
                            name, 
                            created_at, 
                            location, 
                            lang,
                            description,
                            statuses_count,
                            verified,
                            friends_count,
                            followers_count,
                            favourites_count,
                            profile_image_url,
                            profile_background_image_url_https))
    
if __name__ == "__main__":
    sample_id = generate_random_userID(maxi = 4915953956, size = 50000)
    grap_the_existent_users(sample_id)