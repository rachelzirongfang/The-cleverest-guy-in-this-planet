
# coding: utf-8

# Part1: Discard those unnecessary data. Extract info about 'name', 'address', 'city', 'state', 'geoinfo', 'stars', 'categories'

# In[1]:


import json

with open('yelp_academic_dataset_business.json','rb') as json_data:
    data = json_data.readlines()
    yelp_data = [json.loads(item) for item in data]
    result = []
    for yelp_dict in yelp_data:
            name = yelp_dict['name']
            address = yelp_dict['address']
            city = yelp_dict['city']
            state = yelp_dict['state']
            latitude = yelp_dict['latitude']
            longitude = yelp_dict['longitude']
            stars = yelp_dict['stars']
            categories = yelp_dict['categories']
            
            temp_dict = {}
            
            yelp = './yelp.json'
            temp_dict['name'] = name
            temp_dict['address'] = address
            temp_dict['city'] = city
            temp_dict['state'] = state
            temp_dict['latitude'] = latitude
            temp_dict['longitude'] = longitude
            temp_dict['stars'] = stars
            temp_dict['categories'] = categories
            result.append(temp_dict)


# Part2: Extract infomation about Las Vegas

# In[9]:


biz_data = result


# In[14]:


biz_lv = []
for biz in biz_data:
    try:
        if biz['city'] == 'Las Vegas':
            biz_lv.append(biz)
    except:
        pass


# Part3: Extract all the food related business in Las Vegas

# In[15]:


#define the vocabulary list for food
voc_list = ['food', 'restaurant', 'bar', 'beer', 'sandwich', 'cafe', 'deli']


# In[16]:


def whether_food(str_):
    for voc in voc_list:
        if str_.find(voc) != -1:
            return 1
        else:
            pass
    return 0


# In[17]:


for i in range(len(biz_lv)):
    try:
        if whether_food(biz_lv[i]['categories'].lower()):
            biz_lv[i]['whether_Food'] = 1
        else:
            biz_lv[i]['whether_Food'] = 0
    except:
        biz_lv[i]['whether_Food'] = 0


# In[19]:


biz_lv_food = []
for biz in biz_lv:
    if biz['whether_Food'] == 1:
        biz_lv_food.append(biz)


# In[20]:


with open('yelp_lv_food.json', 'w') as f:
            json.dump(biz_lv_food, f)


