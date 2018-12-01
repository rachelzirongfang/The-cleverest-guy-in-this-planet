
# coding: utf-8

# <h2>Library Setup</h2>

# In[4]:


get_ipython().system('pip install shapely --upgrade')
get_ipython().system('pip install geojsonio --upgrade')
get_ipython().system('pip install folium --upgrade')


# <h2>Display Coodinates of our Users</h2>

# In[193]:


def UserCoodinates(lat,lon):
    import folium
    import branca
    m = folium.Map(location=[lat,lon],zoom_start=18)
    html = """
    <h2 style="font-family:helvetica;font-size:16px;color:#7BA23F">You are here</h2>
    <p style="font-family:helvetica;font-size:12px;color:#4D5E39">
    Latitude:%s, Longitude:%s
    </p>
    """%(lat,lon)
    iframe = branca.element.IFrame(html=html, width=200, height=80)
    popup = folium.Popup(iframe, max_width=500)
    icon=folium.Icon(color='green',icon='ok-sign')
    folium.Marker([lat,lon], popup=popup,icon=icon).add_to(m)
    return m


# In[194]:


UserCoodinates(36.22,-115.22)


# <h2>Display the Final Result</h2>

# The restaurants that match your search conditions will be marked red, others will be marked as blue.

# In[205]:


def ResultsVisualization(file_name):
    
    with open(file_name) as fp:
        data = fp.read()
        
    import json
    import folium
    import branca
    
    results = json.loads(data)
    feature_list = []
    feature_collection = {'type':"FeatureCollection","features":feature_list}  
    
    u_lat = results[0][0]
    u_lon = results[0][1]
    m = UserCoodinates(u_lat,u_lon)
    result = results[1:]
    for restaurant in result:
        name = restaurant['name']
        address = restaurant['name']
        lat = restaurant['latitude']
        lon = restaurant['longitude']
        stars = restaurant['stars']
        flag = restaurant['flag']
        url = restaurant['url']
        if flag:
            color = "#EE2746"
            color1 = "#B55D4C"
            color2 = "#64363C"
        else:
            color = "#51A8DD"
            color1 = "#005CAF"
            color2 = "#113285"
                
        html = """
                <h4 style="font-family:helvetica;color:%s;font-size:16px">%s</h4>
                <body>
                        <a href=%s style="font-family:helvetica;color:%s;font-size:12px">%s</a>
                        <li style="font-family:helvetica;color:%s;font-size:12px">Address: %s
                        <li style="font-family:helvetica;color:%s;font-size:12px">Graded by other costumers as %s Stars.
                </body>
                """%(color1,name,url,color2,url,color2,address,color2,stars)

        iframe = branca.element.IFrame(html=html, width=200, height=130)
        popup = folium.Popup(iframe, max_width=500)
        folium.Circle(
            radius=3, 
            location=[lat,lon], 
            popup=popup,
            color=color,
            fill=True, 
            fill_color=color).add_to(m)
            
    return m
            


# In[206]:


ResultsVisualization('clusters_final.json')


