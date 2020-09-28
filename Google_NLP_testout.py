#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu

import requests
import json
import os
import string
from google.cloud import language
from google.oauth2 import service_account
from google.cloud.language import enums
from google.cloud.language import types

# Build language API client (requires service account key)
client = language.LanguageServiceClient.from_service_account_json('ec601-project-2-5172714cb435.json')

def google_nlp(client, url, invalid_types = ['OTHER'], **data):

    html = extract_text(url, **data)
    
    if not html:
        return None
    
    document = types.Document(
        content=html,
        type=language.enums.Document.Type.HTML )

    features = {'extract_syntax': True,
                'extract_entities': True,
                'extract_document_sentiment': True,
                'extract_entity_sentiment': True,
                'classify_text': False
                }
    
    response = client.annotate_text(document=document, features=features)
    sentiment = response.document_sentiment
    entities = response.entities
    
    response = client.classify_text(document)
    categories = response.categories
        
    def is_type(type):
        return client.enums.Entity.Type(entity.type).name
    
    result = {}
    
    result['sentiment'] = []    
    result['entities'] = []
    result['categories'] = []

    if sentiment:
        result['sentiment'] = [{ 'magnitude': sentiment.magnitude, 'score':sentiment.score }]
        
    for entity in entities:
        if is_type(entity.type) not in invalid_types:
            result['entities'].append({'name': entity.name, 'type': is_type(entity.type), 'salience': entity.salience, 'wikipedia_url': entity.metadata.get('wikipedia_url', '-')  })
            
    for category in categories:
        result['categories'].append({'name':category.name, 'confidence': category.confidence})
        
        
    return result



def extract_text(url, **data):
    
    timeout = data.get('timeout', 50)
    
    results = []
    
    try:
        
        print("Performing the NLP of : {}".format(url))
        response = requests.get(url, timeout=timeout)

        text = response.text
        status = response.status_code

        if status == 200 and len(text) > 0:
            return text
            
        return None
        

    except Exception as e:
        print('Cannot extract text from url: {0}.'.format(url))
        return None

if __name__ == '__main__':
    #pass in the username of the account you want to download
    urls = ["https://www.inverse.com/gaming/last-of-us-2-review",
    "https://www.forbes.com/sites/paultassi/2020/06/22/the-last-of-us-part-2-review-ps4-dig-two-graves/#4cca22803ca9",
    "https://www.polygon.com/2020/6/30/21307200/the-last-of-us-2-controversy-critics-press-naughty-dog-vice-review-leak-sony-ps4-playstation",
    "https://www.polygon.com/reviews/2020/7/8/21316392/last-of-us-2-reviews-spoilers-ellie-joel-abby-ending-revenge"]
    file = open('The-Last-Of-Us-Part-2-NLP.txt', 'a+') 
    for url in urls:
        result = google_nlp(client, url)
        file.write("NLP result of : {}".format(url))
        file.write(json.dumps(result,indent=4))
        file.write('\n')
    #close the file
    print "Done"
    file.close()