import numpy as np 
import pandas as pd
import sys
import matplotlib.pyplot as plt


def main():
    osm_data = pd.read_json(sys.argv[1], lines=True)
    cafe_data=osm_data[osm_data['amenity']=='fast_food']
    cafe_data.to_csv('fastFood_name.csv')

if __name__=='__main__':
    main()