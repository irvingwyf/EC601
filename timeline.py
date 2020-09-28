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

def get_all_screen_names(screen_name):
        
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
        
    # fetching the statuses 
    statuses = api.user_timeline(screen_name = screen_name,count=200)
           
    #write tweet objects to JSON
    file = open('statuses.json', 'w') 
    print "Writing tweet objects to JSON please wait..."
    for status in statuses: 
        json.dump(status.user.screen_name,file,sort_keys = True,indent = 4)
        file.write('\n')

    #close the file
    print "Done"
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_screen_names("@RobertDowneyJr") 

