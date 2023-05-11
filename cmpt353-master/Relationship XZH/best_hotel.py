#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium


# In[2]:


data = pd.read_csv('best_hotel_data_cleaning.csv')


# In[3]:


food = data.loc[data['amenity'] == 'food']
parking = data.loc[data['amenity'] == 'parking']
traffic = data.loc[data['amenity'] == 'traffic']
recreation = data.loc[data['amenity'] == 'recreation']
food


# In[4]:


min_lat = data['lat'].min()
max_lat = data['lat'].max()
min_lon = data['lon'].min()
max_lon = data['lon'].max()
BBox = [min_lon,max_lon,min_lat, max_lat]
print(min_lat,max_lat,min_lon,max_lon)


# In[5]:


data_map = folium.Map(location=[49.121383503296705, -122.67246901153845], zoom_start=10)


# In[6]:


for index, row in food.iterrows():
    folium.Circle(
        radius=10,
        location=[row['lat'], row['lon']],
        color='red',
    ).add_to(data_map)


# In[7]:


for index, row in parking.iterrows():
    folium.Circle(
        radius=10,
        location=[row['lat'], row['lon']],
        color='blue',
    ).add_to(data_map)


# In[8]:


for index, row in traffic.iterrows():
    folium.Circle(
        radius=10,
        location=[row['lat'], row['lon']],
        color='green',
    ).add_to(data_map)


# In[9]:


for index, row in recreation.iterrows():
    folium.Circle(
        radius=10,
        location=[row['lat'], row['lon']],
        color='yellow',
    ).add_to(data_map)


# In[10]:


data_map


# In[11]:


air_data = pd.read_csv('listings.csv', parse_dates=['last_review'])
air_data


# In[12]:


air_data_clean = air_data[(air_data['last_review'].dt.year>2020)
                          &(air_data['minimum_nights'] < 3)
                          &(air_data['reviews_per_month']>1)]
air_data_clean


# In[13]:


air_data_map = folium.Map(location=[49.121383503296705, -122.67246901153845], zoom_start=10)


# In[14]:


for index, row in air_data_clean.iterrows():
    folium.Circle(
        radius=10,
        location=[row['latitude'], row['longitude']],
        color='black',
    ).add_to(air_data_map)


# In[15]:


air_data_map


# In[16]:


new_air_data_map = folium.Map(location=[49.121383503296705, -122.67246901153845], zoom_start=10)


# In[17]:


new_air_data_clean = air_data[(air_data['last_review'].dt.year>2020)
                          &(air_data['minimum_nights'] < 3)
                          &(air_data['reviews_per_month']>1)
                          &(air_data['price']>200)]


# In[18]:


new_air_data_clean


# In[19]:


for index, row in new_air_data_clean.iterrows():
    folium.Circle(
        radius=10,
        location=[row['latitude'], row['longitude']],
        color='black',
    ).add_to(new_air_data_map)


# In[20]:


new_air_data_map

