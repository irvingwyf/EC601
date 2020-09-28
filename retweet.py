#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu


import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = "************************"
consumer_secret = "***************************************"
access_key = "*****************************************"
access_secret = "*********************************************"

def get_all_retweet_screen_names(ID):
        
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
        
    # fetching the statuses 
    retweets_list = api.retweets(ID,count=200) 
  
    file = open('retweet_screen_names.json', 'w') 
    print "Writing tweet objects to JSON please wait..."
    for retweet in retweets_list: 
        json.dump(retweet.user.screen_name,file,sort_keys = True,indent = 4)
        file.write('\n')

    #close the file
    print "Done"
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_retweet_screen_names("1308813203619549184") 

