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

def get_direct_message(ID):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # fetching the direct message  
    direct_message = api.get_direct_message(ID)
    file = open('direct_message.json', 'w')
    print ("Writing tweet objects to JSON please wait...")
    # printing the information 
    file.write("The type is : " + direct_message.type + '\n')
    file.write("The id is : " + direct_message.id + '\n')
    file.write("The created_timestamp is : " + direct_message.created_timestamp + '\n')
  
    # inside message_create 
    file.write("The recipient_id is : " + direct_message.message_create['target']['recipient_id'] + '\n')
    file.write("The sender_id is : " + direct_message.message_create['sender_id'] + '\n')
    file.write("The source_app_id is : " + direct_message.message_create['source_app_id'] + '\n')
    file.write("The text is : " + str(direct_message.message_create['message_data']['text']) + '\n')
    file.write("The entities are : " + str(direct_message.message_create['message_data']['entities']) + '\n')
    file.write("The media attachment is : " + str(direct_message.message_create['message_data']['attachment']) + '\n')

    print ("Done")
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_direct_message("1271013844639313927") 