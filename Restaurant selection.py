
# coding: utf-8

# In[1]:


import urllib
from bs4 import BeautifulSoup
import requests


# In[113]:


import json
with open('clusters_final.json','r') as json_data:
    data = json_data.read()
restaurants = json.loads(data)[1:]


# In[114]:


CLIENT_ID = 'MTEIv4L-41Olwx1uNaZ38A'
API_KEY = 'UZj_XiL56l9G-t4tOay6RFbhJ2-oUPhq6yvdcPsNnD1U-AsRa8QkIJ1waJhuaeZGclxAAUzPGZ7xPW8_0FA6oSmg22cebQZYjQ-H3C6LpLnzVSK6qmh-YXQKkOsCXHYx'


# In[115]:


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com' #The API url header
SEARCH_PATH = '/v3/businesses/search' #The path for an API request to find businesses
BUSINESS_PATH = '/v3/businesses/'  # The path to get data for a single business


# In[116]:


def get_restaurants_alias(api_key,name,location):
    import requests
    
    #First we get the access token
    #Set up the search data dictionary
    search_data = {
    'term': name,
    'location': location.replace(' ', '+'),
    'limit': 1
    }
    url = API_HOST + SEARCH_PATH
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    response = requests.request('GET', url, headers=headers, params=search_data).json()
    businesses = response.get('businesses')[0]
    
    res_name = businesses['name']
    res_alias =  businesses['alias']
    
    if res_name.lower() == name.lower():
        return res_alias
    return None


# In[112]:


get_restaurants_alias(API_KEY,'Center Bar',"3400 Las Vegas Blvd S, Las Vegas")


# In[79]:


def get_business_review(api_key,business_id):
    import json
    import requests
    business_path = BUSINESS_PATH + business_id
    url = API_HOST + business_path
    return url

    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }


    response = requests.request('GET', url, headers=headers).json()
    return response
   
    review_text = ''
    for review in response['reviews']:
        review_text += review['text']
    return review_text


# In[80]:


get_business_review(API_KEY,'mon-ami-gabi-las-vegas-2')


# In[120]:


import nltk 
from nltk.corpus import wordnet 
synonyms = [] 
antonyms = [] 
  
for syn in wordnet.synsets('hamburger'):
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
        if l.antonyms(): 
            antonyms.append(l.antonyms()[0].name()) 
  
print(set(synonyms))


# In[125]:


categories = []
for restaurant in restaurants:
    categories.append(restaurant['categories'])
categories


