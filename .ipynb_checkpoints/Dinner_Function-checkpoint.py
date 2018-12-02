import json
def dinner(person_site, clusters_coordinates, clusters_data, radius=500):
    
    
    p_lati = person_site[0]
    p_long = person_site[1]
    
    
    """
    Here will be a function to determine whether the person is in Las Vegas
    """
    
    """
    For Las Vegas area, we use 1 degree latitude = 111km and 1 degree longitude = 90km
    """
    d_lati = 0.01801801801/4*radius/500 #0.01801801801/4 is unit degree of latitude for 500 meters
    d_long = 0.02222222222/4*radius/500 #0.02222222222/4 is unit degree of longitude for 500 meters
    
    
    k_num = len(clusters_data)
    k_distance = 100000000
    k_count = 0
    k_count_nd = 0
    k_distance_90=[]
    
    # below calculate 90 percent quantile
    for i in range(len(clusters_data)):
        k_distance_ls = []
        for rstrt in clusters_data[i]:
            k_distance_ls.append((rstrt['latitude'] - clusters_coordinates[i][0])*(rstrt['latitude'] - clusters_coordinates[i][0]) + (rstrt['longitude'] - clusters_coordinates[i][1])*(rstrt['longitude'] - clusters_coordinates[i][1]))
        k_distance_90.append(sorted(k_distance_ls)[int(0.9*len(k_distance_ls))])
    
    # below to get the closest cluster
    for i in range(k_num):
        if (p_lati - clusters_coordinates[i][0])*(p_lati - clusters_coordinates[i][0]) + (p_long - clusters_coordinates[i][1])*(p_long - clusters_coordinates[i][1]) < min(k_distance,k_distance_90[i]):
            k_distance = k_distance_90[i]
            k_count = i
    
    # below to loop over the closest cluster
    rstrt_ls=[[p_lati,p_long]]
    for rstrt in clusters_data[k_count]:
        if abs(p_lati - rstrt['latitude'])<d_lati and abs(p_long - rstrt['longitude'])<d_long:
            if 'stars' in rstrt.keys():
                if rstrt['stars']>=4:
                    rstrt_ls.append(rstrt)
    
    
    if len(rstrt_ls) == 1:
        # below to get the 2nd closest cluster
        k_count_nd = 0
        for i in [elem for elem in range(k_num) if elem != k_count]:
            if (p_lati - clusters_coordinates[i][0])*(p_lati - clusters_coordinates[i][0]) + (p_long - clusters_coordinates[i][1])*(p_long - clusters_coordinates[i][1]) < min(k_distance,k_distance_90[i]):
                k_distance = k_distance_90[i]
                k_count_nd = i
        # try to loop over the 2nd closest cluster
        for rstrt in clusters_data[k_count_nd]:
            if abs(p_lati - rstrt['latitude'])<d_lati and abs(p_long - rstrt['longitude'])<d_long:
                rstrt_ls.append(rstrt)
    
    if len(rstrt_ls) != 1:
        return rstrt_ls
    else:
        return("Oops, we cannot find restaurants for you :(")

