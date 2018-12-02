
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
    m = folium.Map(location=[lat,lon],zoom_start=16)
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



def ResultsVisualization(results):
    
        
    import json
    import folium
    import branca
    
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
        
        col = "#51A8DD"
        color1 = "#005CAF"
        color2 = "#113285"
                
        html = """
                <h4 style="font-family:helvetica;color:%s;font-size:16px">%s</h4>
                <body>
                        
                        <li style="font-family:helvetica;color:%s;font-size:12px">Address: %s
                        <li style="font-family:helvetica;color:%s;font-size:12px">Graded by other costumers as %s Stars.
                </body>
                """%(color1,name,color2,address,color2,stars)

        iframe = branca.element.IFrame(html=html, width=200, height=130)
        popup = folium.Popup(iframe, max_width=500)
        icon=folium.Icon(color='blue')
        folium.Marker(
            location=[lat,lon], 
            popup=popup,
            icon=icon).add_to(m)
            
    return m
            
