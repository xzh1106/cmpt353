import pandas as pd
import numpy as np
import sys
import os
import copy
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
from os import listdir
from os.path import isfile, join
from math import cos, asin, sqrt, pi


def get_exif(file):
    image = Image.open(file)
    image.verify
    exif = image.getexif()
    return exif

def get_geotags(lab_exif):
    if not lab_exif:
        raise ValueError("No EXIF data found")
    geotags = {}
    for (i, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if i not in lab_exif:  
                raise ValueError("No EXIF geotags found")

            for (j, val) in GPSTAGS.items():
                if j in lab_exif[i]:
                    geotags[val] = lab_exif[i][j]
    return geotags



def trans_to_decimal(dms, ref): # transform the data into coordinates

    degs = dms[0]
    mins = dms[1] / 60.0
    secs = dms[2] / 3600.0
    if ref in ['S', 'W']:
        degs = -degs
        mins = -mins  # Library for INT_MAX -mins
        secs = -secs
    return round(degs + mins + secs, 3)

def get_coordinates(geotags):
    lat = trans_to_decimal(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = trans_to_decimal(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return [lat,lon]

def output_gpx(points, output_filename):
    """
    Output a GPX file with latitude and longitude from the points DataFrame.
    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)
    
    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)
    
    points.apply(append_trkpt, axis=1,   trkseg=trkseg, doc=doc)
    
    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')
def calculate_distance(lat1,lon1,lat2,lon2):
    p = pi/180     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) *  (1 - cos((lon2 - lon1) * p)) / 2
    
    return 12742 * asin(sqrt(a))
distance_for_points = np.vectorize(calculate_distance)

def total_distance(data):
    total=0
    for i in range(len(data)-1):
        total=total+calculate_distance(data.iloc[i,0],data.iloc[i,1],data.iloc[i+1,0],data.iloc[i+1,1])
    return total

def swap(x,y,data):
    temp=copy.deepcopy(data.iloc[x])
    data.loc[x]=data.iloc[y]
    data.loc[y]=temp


def readexif(filename):
    exif = get_exif(filename)
    tags = get_geotags(exif)
    cod = get_coordinates(tags)
    return cod

positions=[]
for i in range(9):
    filename="inputfile/"+str(i+1)+".jpg"
    temp=readexif(filename)
    positions.append(temp)
# swap(0,1,data)
data= pd.DataFrame (positions, columns = ['lat', 'lon'])
print(data)
df=pd.DataFrame(data.iloc[[0,3,1,3,8,3,6,3,0,5,2,4,7]])
output_gpx(df, 'out.gpx')



class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    def minKey(self, key, mstSet):
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1  
 
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True           
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
 
        self.printMST(parent)
if __name__ == '__main__':
    g = Graph(9)
    g.graph = []
    for i in range (9):              
        temp=[]
        for j in range (9):
                w=calculate_distance(data.iloc[i]['lat'],data.iloc[i]['lon'],data.iloc[j]['lat'],data.iloc[j]['lon'])
                temp.append(w)
        g.graph.append(temp)
   
    g.primMST()

 
 
   
