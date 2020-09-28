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

def get_all_mentions_screen_names():
        
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
        
    # fetching the statuses 
    mentions_list = api.mentions_timeline()
  
    file = open('mention_screen_names.json', 'w') 
    print "Writing tweet objects to JSON please wait..."
    if not mentions_list:
        file.write('No mentioned history.\n')
    else:
        for mention in mentions_list: 
            json.dump(mention.user.screen_name,file,sort_keys = True,indent = 4)
            file.write('\n')

    #close the file
    print "Done"
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_mentions_screen_names() 

