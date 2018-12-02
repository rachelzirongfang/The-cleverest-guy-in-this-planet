![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/logo1.png)

# WhatForDinner: 
## Intelligent restaurant recommendation based on K-means algorithem
* Group name: The cleverest guys on this planet (Section 2)
* Members: Jing Wang(jw3690); Zeguan Wu(zw2516); Zirong Fang(zf2204); Ziwei Jiang(zj2246)

## Description

* Goal: In this project, we will provide recommendations for our customers who want to choose a restaurant to eat. Here, our recommendations are based on both his preferences and his location.

* Data source: We use the open dataset from Yelp(yelp_academic_dataset_business.json). And We choose Las Vegas city to demonstrate our result.

* Process: To come to our final result, we have overall three processes.

  - We first generate a function to screen all the information in the dataset from Yelp and extract the useful information of all the food-related business in Las Vegas.

  - Second, using the k-means method in machine learning, we determine how many clusters should restaurants be classified into and, classify the restaurants into 13 clusters, output the clusters dictionary and locations of clusters centers and visualize the clusters.

  - Third, show our results on the map. In the map above, the dots represents locations of our customer and nearby recommended restaurants. If you click on recommended restaurant, it will display the restaurant's name and star.

  - Finally, we come to our finally recommendation based on our customers’ preferred distance range and his location using the two functions above. We will provide him with a visualization of restaurants, which includes the dot of his location and the dots of locations of our final recommended restaurants. If you click on the recommended restaurant,  itwill display the restaurant's name, address and rating star.

## Methodology

### Modules

* visualization.py: Generate a html to show our results on the map, which contains locations of our customer and nearby recommended restaurants. If you click on the recommended restaurant, it will display the restaurant's name and star.

Dinner_Function.py: First, input customer's location and his preffered distance range radius(defualt=500). Then, assign the customer to the appropriate clusters, which is generated from K-Means method. Finally, return the information of recommended restaurants.

### Functions

* DataExtraction.ipynb: Using Yelp's open dataset(yelp_academic_dataset_business.json): contains business data including location data, attributes, and categories.), we extract useful information including names, addresses, cities, states, geoinfo(latitudes and longitudes), stars and catogories. And then, we extract the business information in Las Vegas city. And finally, we extraxt the information of all the food-related business in Las Vegas and we save the data as yelp_lv_food.json.

* clusters_code.ipynb: In this section, we apply K-Means unsupervised learning algorithm on the restaurant locations in order to classify the restaurants into clusters. First, import the restaurants location information. Then, determine how many clusters should restaurants be classified into. Thrid, classified the restaurants into 13 clusters, output the clusters dictionary and locations of clusters centers. Finally, Visualize the clusters.

* what_for_dinner.ipynb (main function for this project): The customer needs to enter his (or her) own location, and his (or her) preferred distance range (range radius default 500m). Then, we convert the customer's specific location into precise longgitude and latitude. The main function calls Dinner_Function module, assigns the customer to the appropriate clusters, and returns the recommended restaurants. And main fuction calls visualization module to generate the resulting image (in html format), which contains locations of our customer and nearby recommended restaurants. If you click on the recommended restaurant, it will display the restaurant's name, address and rating star.

## How to Run

1. Clone this project to your computer.

2. Use Jupyter to open what_to_dinner.ipynb.

3. Type in your location here:
```python
person_address = input('Input your current address:')
radius = input('Input your preferred distance range(defualt=500meters):')
```
For example:
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/input.png)

4. Run:
```python
What_for_dinner = (person_site, radius)
```
Get your visualization result in a map.
插入结果图

## Discussion

We faced a problem when choosing restaurants near the customer. Firstly, we try to calculus the distance between the customer and every restaurant then set a constraint. If the distance is smaller than the constraint, then we will select it. However, there are thousands of restaurants in Las Vegas and our customer is not only one person. Assume there are <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{N}" title="\mathbf{N}" /></a> customers using this service and <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{M}" title="\mathbf{M}" /></a> restaurants in New York City, the Big-O of this algorithm is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" title="\mathbf{O\left ( MN \right )}" /></a>

As  and  are both quite large, this algorithm is not efficient in solving practical problems.

To optimize this algorithm, we firstly use K-means clustering method to group all the restaurants in to <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" title="\mathbf{K \left ( K\leq M \right )}" /></a> clusters. Then calculus the distance between the customer and the centroid of each cluster. Finally, we choose the restaurants in the cluster whose outcome is the smallest as the outcome. At this time, the Big-O is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" title="\mathbf{O\left ( KN \right ) where K\leq M}" /></a>

The efficiency of the algorithms improves a lot.
