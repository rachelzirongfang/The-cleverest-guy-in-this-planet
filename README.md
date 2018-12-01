![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/logo1.png)

# WhatForDinner
## An intelligent restaurant recommendation based on K-means algorithem

## 1.Description

* Goal: In this project, we will provide recommendations for our customers who want to choose a restaurant to eat. Here, our recommendations are based on both his preferences and his location.

* Data source: We use the open dataset from Yelp(yelp_academic_dataset_business.json). And We choose Las Vegas city to demonstrate our result.

* Process: To come to our final result, we have overall three processes.

  - We first generate a function to screen all the information in the dataset from Yelp and extract the useful information of all the restaurants in the Las Vegas.

  - Second, using the k-means method in machine learning, we will generate his classification visualization of restaurants based on his location and the Yelp academic dataset/Google map dataset. In this visualization, our customers is segmented into regions, where each region is shaded by the predicted rating of the closest restaurant (yellow is 5 stars, blue is 1 star). Specifically, the visualization you will be constructing is a scatter plot in a diagram.

  - In the map above, each dot represents a restaurant. The color of the dot is determined by the restaurant's location. For example, downtown restaurants are colored green. The user that generated this map has a strong preference for Southside restaurants, and so the southern regions are colored yellow.

  - Finally, we come to our finally recommendation based on our customers’ preference and location using the two functions above. We will provide him with a visualization of restaurants, which includes the dot of his location and the dots of locations of our final recommended restaurants.


## 2.Approach

#### （1）Approach to Getting Our Dataset
 
 We get our dataset from Yelp. Yelp provides data in the form of json objects. We will use some build-in function of python’s json module to load these data and set up our restaurant dictionary based on these data. We hope to get name, location and other specific the restaurants in Las Vegas for further processing.

#### （2）Approach to Processing Our Data
The data of restaurants is clustered by k-means method. K-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. So the restaurants on map will be segmented into k clusters by k-means method.

By checking which sector the user is in, we can easily tell restaurants in the shortest distance with the user.

Compared with calculating the distances between the user and every single restaurant in the dataset directly, we just need to tell which cluster our user is in. The computational complexity is much less the former direct method, which can be more than 10,000 for each request. In this case, our model can be much more efficient, especially when the amount of users is large.

#### （3）Approach to Present Our Result
We present our result in a visualized way. The final result that our user get will be a map marked with points which represents restaurants that is selected by the user’s preference in our pre-segmented cluster. An assistive toolbox called mapbox is used.

## 3.Methodology

* 1_DataExtraction.ipynb: Using Yelp's open dataset(yelp_academic_dataset_business.json): contains business data including location data, attributes, and categories.), we extract useful information including names, cities, states, addresses, specific locations(latitudes and longitudes), stars and catogories. And we save the data as yelp.json.

* 2_CityFilter.ipynb: Using yelp.json, we extract the data of businesses in Las Vegas city. And we save the data as yelp_lv_biz.json.

* 3_CategoryFilter.ipynb: Using yelp_lv_biz.json, we extraxt the data of businesses related to food. And we save the data as yelp_lv_food.json.

* 4_clusters.ipynb: In this section, we apply K-Means unsupervised learning algorithm on the restaurant locations in order to classify the restaurants into clusters. First, import the restaurants location information. Then, determine how many clusters should restaurants be classified into. Thrid, classified the restaurants into 13 clusters, output the clusters dictionary and locations of clusters centers.

* search.py: Given the keyword of filtering and original restaurant dataset, output all matching restaurants.

* clusters.py: Given the original restaurant dataset, implement the k-means algorithm, a method for grouping data points into 
clusters by determining their center positions, to classify it into k clusters.

* visualization.py: Given the information of restaurants, draw a scatterplot on the map and add a tag (including restaurant name, business hour, rating and website link) to each scatter point.

* what_for_dinner.py (main function for this project): Given the location and requirements of a customer, find restaurants near him meet the requirements. Visualize the outcome on a map.
Discussion

We faced a problem when choosing restaurants near the customer. Firstly, we try to calculus the distance between the customer and every restaurant then set a constraint. If the distance is smaller than the constraint, then we will select it. However, there are thousands of restaurants in New York City and our customer is not only one person. Assume there are <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{N}" title="\mathbf{N}" /></a> customers using this service and <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{M}" title="\mathbf{M}" /></a> restaurants in New York City, the Big-O of this algorithm is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" title="\mathbf{O\left ( MN \right )}" /></a>

As  and  are both quite large, this algorithm is not efficient in solving practical problems.

To optimize this algorithm, we firstly use K-means clustering method to group all the restaurants in to <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" title="\mathbf{K \left ( K\leq M \right )}" /></a> clusters. Then calculus the distance between the customer and the centroid of each cluster. Finally, we choose the restaurants in the cluster whose outcome is the smallest as the outcome. At this time, the Big-O is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" title="\mathbf{O\left ( KN \right ) where K\leq M}" /></a>

The efficiency of the algorithms improves a lot.
