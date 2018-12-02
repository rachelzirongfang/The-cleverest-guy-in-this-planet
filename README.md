![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/logo1.png)

* Group name: The cleverest guys on this planet (Section 2)
* Members: Jing Wang(jw3690); Zeguan Wu(zw2516); Zirong Fang(zf2204); Ziwei Jiang(zj2246)

## What is it?

* An Intelligent restaurant recommendation based on K-means algorithem: In this project, we will provide visualized restaurant recommendations for our customers who want to choose a restaurant to eat. Here, our recommendations are based on both his preferred distance range and his location. (And We choose Las Vegas city to demonstrate our result.)

## Methodology

* Modules

   - __visualization.py__: Generate a html to show our results on the map, which contains locations of our customer and nearby recommended restaurants. If you click on the recommended restaurant, it will display the restaurant's name and star.

   - __Dinner_Function.py__: First, input customer's location and his preffered distance range radius(defualt=500). Then, assign the customer to the appropriate clusters, which is generated from K-Means method. Finally, return the information of recommended restaurants.

* Functions

   - __DataExtraction.ipynb__: Using Yelp's open dataset(yelp_academic_dataset_business.json): contains business data including location data, attributes, and categories.), we extract useful information including names, addresses, cities, states, geoinfo(latitudes and longitudes), stars and catogories. And then, we extract the business information in Las Vegas city. And finally, we extraxt the information of all the food-related business in Las Vegas and we save the data as yelp_lv_food.json.

   - __clusters_code.ipynb__: In this section, we apply K-Means unsupervised learning algorithm on the restaurant locations in order to classify the restaurants into clusters. First, import the restaurants location information. Then, determine how many clusters should restaurants be classified into. Thrid, classified the restaurants into 13 clusters, output the clusters dictionary and locations of clusters centers. Finally, Visualize the clusters.

   - __what_for_dinner.ipynb (main function for this project)__: The customer needs to enter his (or her) own location, and his (or her) preferred distance range (range radius default 500m). Then, we convert the customer's specific location into precise longgitude and latitude. The main function calls Dinner_Function module, assigns the customer to the appropriate clusters, and returns the recommended restaurants. And main fuction calls visualization module to generate the resulting image (in html format), which contains locations of our customer and nearby recommended restaurants. If you click on the recommended restaurant, it will display the restaurant's name, address and rating star.

## Installation instructions
!pip install folium --upgrade
!pip install shapely --upgrade
!pip install geojsonio -upgrade
!pip install branca --upgrade

## How to Run?

1. Clone this project to your computer.

2. Use Jupyter to open What_for_dinner.ipynb.

3. Type in your location and preffered distance range here:
```python
person_address = input('Input your current address in Las Vegas:')
radius = input('Input your preferred distance range(in meters):')
```
  - For example:
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/input1.png)

4. Run the following code line:
```python
what_for_dinner(person_address,radius=float(radius))
```
5. Get your visualization result in a map:
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/r.png)
Show your location in the map:
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/r1.png)
Show the details of the recommended restaurant:
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/r2.png)


## Test
* Open test.ipynb and run
We use three locations to test whether this project works well. The first two locations are 'Paris Las Vegas' hotel and 'The D Las Vegas' hotel, and we successfully find restaurants around them. We then test the "Nanjing University" in China, because we cannot find restaurants in Las Vegas arond the location , it outputs 'Oops, there is no such restaurant near you :('.
For emxample: test1('Paris Las Vegas')
![logo](https://raw.githubusercontent.com/rachelzirongfang/WhatForDinner/master/img-storage/t1.png)

## Discussion

We faced a problem when choosing restaurants near the customer. Firstly, we try to calculus the distance between the customer and every restaurant then set a constraint. If the distance is smaller than the constraint, then we will select it. However, there are thousands of restaurants in Las Vegas and our customer is not only one person. Assume there are <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{N}" title="\mathbf{N}" /></a> customers using this service and <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{M}" title="\mathbf{M}" /></a> restaurants in New York City, the Big-O of this algorithm is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{O\left&space;(&space;MN&space;\right&space;)}" title="\mathbf{O\left ( MN \right )}" /></a>

As  and  are both quite large, this algorithm is not efficient in solving practical problems.

To optimize this algorithm, we firstly use K-means clustering method to group all the restaurants in to <a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\mathbf{K&space;\left&space;(&space;K\leq&space;M&space;\right&space;)}" title="\mathbf{K \left ( K\leq M \right )}" /></a> clusters. Then calculus the distance between the customer and the centroid of each cluster. Finally, we choose the restaurants in the cluster whose outcome is the smallest as the outcome. At this time, the Big-O is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\bg_white&space;\mathbf{O\left&space;(&space;KN&space;\right&space;)&space;where&space;K\leq&space;M}" title="\mathbf{O\left ( KN \right ) where K\leq M}" /></a>

The efficiency of the algorithms improves a lot.
