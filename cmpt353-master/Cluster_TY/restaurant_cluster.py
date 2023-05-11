import numpy as np
import pandas as pd
import sys

import folium
import math
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from math import cos, asin, sqrt, pi
from folium.plugins import HeatMap
from folium import plugins
import osmnx as ox
import networkx as nx

#number of cluster
N=10

#read restaurant data ,cafe data and fastfood data
data=pd.read_csv('..//restaurant_data')
data_cafe=pd.read_csv('./cafe_name.csv')
data_fastfood=pd.read_csv('./fastFood_name.csv')

all_restaurant = data[['lat','lon','name']]
all_cafe=data_cafe[['lat','lon','name']]
all_fastfood=data_fastfood[['lat','lon','name']]


#data without outliers
boundary1=-122.5439258
boundary2=49.2982045
all_restaurant=all_restaurant[all_restaurant['lon']<boundary1]
all_restaurant=all_restaurant[all_restaurant['lat']<boundary2]
all_cafe=all_cafe[all_cafe['lon']<boundary1]
all_cafe=all_cafe[all_cafe['lat']<boundary2]
all_fastfood=all_fastfood[all_fastfood['lon']<boundary1]
all_fastfood=all_fastfood[all_fastfood['lat']<boundary2]


#Find restaurants which has the most number of branches
all_restaurant_count=all_restaurant.groupby('name').size().reset_index(name='obs').sort_values(['obs'], ascending=False)
top_10_chain_restaurant=all_restaurant_count.loc[(all_restaurant_count['obs']>=7)]

#Find cafeteria which has the most number of branches
all_cafe_count=all_cafe.groupby('name').size().reset_index(name='obs').sort_values(['obs'], ascending=False)
top_10_chain_cafe=all_cafe_count.loc[(all_cafe_count['obs']>=8)]

#Find fastFood which has the most number of branches
all_fastfood_count=all_fastfood.groupby('name').size().reset_index(name='obs').sort_values(['obs'], ascending=False)
top_10_chain_fastfood=all_fastfood_count.loc[(all_fastfood_count['obs']>=20)] #actually top 12 because of branch number ties

#Select only top 10 chain-restaurants
all_restaurant=all_restaurant[all_restaurant.name.isin(top_10_chain_restaurant.name)]

#Select only top 10 chain-cafe
all_cafe=all_cafe[all_cafe.name.isin(top_10_chain_cafe.name)]

#Select only top 10(12) chain-fastfood
lis=top_10_chain_fastfood['name']
all_fastfood = all_fastfood[all_fastfood['name'].isin(lis)]

# Show heat map 
data_map = folium.Map(location=[49.284808779798745, -123.12244539679432], zoom_start=10)
location = []
for index, row in all_restaurant.iterrows():
    location.append([row['lat'], row['lon']])
for index, row in all_cafe.iterrows():
    location.append([row['lat'], row['lon']])
for index, row in all_fastfood.iterrows():
    location.append([row['lat'], row['lon']])
data_map.add_child(plugins.HeatMap(location,blur=28))
data_map.save(outfile= "chain_restaurant_heatmap.html")

#Find clusters
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#Putting the training data together
training_data_a=all_restaurant[['lat', 'lon']].values
training_data_b=all_cafe[['lat', 'lon']].values
training_data_c=all_fastfood[['lat', 'lon']].values
training_data=np.concatenate((training_data_a, training_data_b, training_data_c), axis=0)
#Find the number of cluster using "elbow curve method"
Sum_of_squared_distances = []
K = range(1,15)
for num_clusters in K :
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(training_data)
    Sum_of_squared_distances.append(kmeans.inertia_)
plt.plot(K,Sum_of_squared_distances,'bx-')
plt.xlabel('Values of K') 
plt.ylabel('Sum of squared distances/Inertia') 
plt.title('Elbow Method For Optimal k')
plt.show()

#Using number of cluster N=:
kmeans_optimal = KMeans(n_clusters=7)
kmeans_optimal.fit(training_data)
label=kmeans_optimal.fit_predict(training_data)
centers=kmeans_optimal.cluster_centers_
#print(kmeans_optimal.cluster_centers_)


#Marking down the results on the osm map
data_map2 = folium.Map(location=[49.284808779798745, -123.12244539679432], zoom_start=10)
def chooseColor(cluster_num):
    if cluster_num==0:
        return 'red'
    elif cluster_num==1:
        return 'green'
    elif cluster_num==2:
        return 'blue'
    elif cluster_num==3:
        return 'magenta'
    elif cluster_num==4:
        return 'blueviolet'
    elif cluster_num==5:
        return 'black'
    elif cluster_num==6:
        return 'yellow'
    elif cluster_num==7:
        return 'orange'
    elif cluster_num==8:
        return 'aqua'
    elif cluster_num==9:
        return 'lightpink'

for i in range(7):
    XXX=training_data[label == i] 
    for row in XXX:
        folium.Circle(
            radius=80,
            location=[row[0], row[1]],
            color=chooseColor(i),
        ).add_to(data_map2)

for center in centers:
    folium.Circle(
        radius=320,
        location=[center[0], center[1]],
        color='aqua'
    ).add_to(data_map2)

data_map2.save(outfile= "chain_restaurant_markdown.html")
# model = AgglomerativeClustering(n_clusters=5)
# X=all_restaurant[["lat", 'lon']]
# y = model.fit_predict(X)

#Aside: check outliers
#TODO if time permits
from sklearn.neighbors import LocalOutlierFactor
model = LocalOutlierFactor()
y = model.fit_predict(training_data)
