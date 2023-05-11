#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys
import pandas as pd
import difflib
import matplotlib.pyplot as plt


# In[2]:


amenities = pd.read_json("amenities-vancouver.json.gz", lines=True)
print(amenities)


# In[3]:


amenities = amenities[amenities['name'].notna()]
print(amenities)


# In[4]:


amenities_types =amenities['amenity'].unique()
print(amenities_types)


# In[11]:


def merge_similar_amentity(df): #merge amenities with similar/same amenity type
    df['amenity'] = df['amenity'].replace(['fast_food'], 'food')
    df['amenity'] = df['amenity'].replace(['food_court'], 'food')
    df['amenity'] = df['amenity'].replace(['restaurant'], 'food')
    df['amenity'] = df['amenity'].replace(['cafe'], 'food')
    df['amenity'] = df['amenity'].replace(['ice_cream'], 'food')
    df['amenity'] = df['amenity'].replace(['bistro'], 'food')
    
    df['amenity'] = df['amenity'].replace(['parking_entrance'], 'parking')
    df['amenity'] = df['amenity'].replace(['bicycle_parking'], 'parking')
    df['amenity'] = df['amenity'].replace(['motorcycle_parking'], 'parking')
    df['amenity'] = df['amenity'].replace(['parking_space'], 'parking')
    
    df['amenity'] = df['amenity'].replace(['pub'], 'recreation')
    df['amenity'] = df['amenity'].replace(['nightclub'], 'recreation')
    df['amenity'] = df['amenity'].replace(['bar'], 'recreation')
    df['amenity'] = df['amenity'].replace(['community_centre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['public_bookcase'], 'recreation')
    df['amenity'] = df['amenity'].replace(['library'], 'recreation')
    df['amenity'] = df['amenity'].replace(['cinema'], 'recreation')
    df['amenity'] = df['amenity'].replace(['theatre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['arts_centre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['fountain'], 'recreation')
    df['amenity'] = df['amenity'].replace(['social_centre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['conference_centre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['marketplace'], 'recreation')
    df['amenity'] = df['amenity'].replace(['spa'], 'recreation')
    df['amenity'] = df['amenity'].replace(['events_venue'], 'recreation')
    df['amenity'] = df['amenity'].replace(['hookah_lounge'], 'recreation')
    df['amenity'] = df['amenity'].replace(['casino'], 'recreation')
    df['amenity'] = df['amenity'].replace(['dance'], 'recreation')
    df['amenity'] = df['amenity'].replace(['Observation Platform'], 'recreation')
    df['amenity'] = df['amenity'].replace(['dive_centre'], 'recreation')
    df['amenity'] = df['amenity'].replace(['toy_library'], 'recreation')
    df['amenity'] = df['amenity'].replace(['leisure'], 'recreation')
    
    df['amenity'] = df['amenity'].replace(['bus_station'], 'traffic')
    df['amenity'] = df['amenity'].replace(['bicycle_rental'], 'traffic')
    df['amenity'] = df['amenity'].replace(['ferry_terminal'], 'traffic')
    df['amenity'] = df['amenity'].replace(['car_rental'], 'traffic')
    df['amenity'] = df['amenity'].replace(['boat_rental'], 'traffic')
    df['amenity'] = df['amenity'].replace(['motorcycle_rental'], 'traffic')
    return df


# In[19]:


amenities = merge_similar_amentity(amenities)
amenities_types =amenities['amenity'].unique()
print(amenities_types)
print(amenities)


# In[17]:


amenities.to_csv('best_hotel_data_cleaning.csv', index = False)


# In[ ]:




