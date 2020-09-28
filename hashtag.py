#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu


import tweepy #https://github.com/tweepy/tweepy
import csv
#Twitter API credentials
consumer_key = "************************"
consumer_secret = "***************************************"
access_key = "*****************************************"
access_secret = "*********************************************"

def get_hashtag_tweets(HASHTAG):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    file = open('hashtag.csv', 'a')
    csvWriter = csv.writer(file)
    for tweet in tweepy.Cursor(api.search,q=HASHTAG,count=100, lang="en", since="2020-01-01").items():
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print "Done"
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_hashtag_tweets("#Persona5royal")