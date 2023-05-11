
# CMPT353 

OSM Project


## Part 1 Airbnb Choice

- data_cleaning.ipynb

    Required library: 
    
    numpy, pandas, matplotlib.pyplot, folium

    File used: 
    
    amenities-vancouver.json.gz

    Data classification: 
    
    food, traffic, parking, recreation
    
    Output: 
    
    Classified data (amenities-vancouver.json.gz)
- best_hotel.ipynb

    Required library: 
    
    numpy, pandas, matplotlib.pyplot, folium

    File used: 
    
    listings.csv amenities-vancouver.json.gz

    Map: 

    Create map centered at mean latitude and longitude of the data [49.121383503296705, -122.67246901153845].

    amenities-vancouver.json.gz: 

    using folium to located food, transportation, entertainment, shopping mall on base map.

    Airbnb:

    using folium to located Airbnb on base map : one for all Airbnb and one for Airbnb's price higher than 200 

- Operation

    Read from @data_file, Pull the coordinates of each location from the loop and display them in the map.





## Part 2 Restaurant Distribution

- Install the following packages in the computer prompt: 

    pip install folium/osmnx/image/TAGS/GPSTAGS/listdir/isfile/join
- How to run the project:

    In Cluster_TY directory, run python3 restaurant_cluster.py, as expected you will first get a plot, then you will get chain_restaurant_heatmap.html and chain_restaurant_markdown.html Note: you can try different number of clusters by changing the number of cluster in line 95. We used cluster=7 in the report.
## Part 3 Route Planning
- route.py: 

    run python3 route.py, as expected you will get get a gpx output and a tree which demonstrates the best tree graph of the route Note: you can switch any pictures in your input file directory