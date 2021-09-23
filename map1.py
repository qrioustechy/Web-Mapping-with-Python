#Import the necessary packages
import folium
import pandas as pd

data = pd.read_csv("volcanoes.txt")

lat = list(data['LAT'])
lon = list(data["LON"])

#define the base map layer
map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles= "Stamen Terrain")
#[7.420262, 3.878984]

#different tiles available:
    #Stamen(Terrain, Toner, and Watercolor)
    #CartoDB(positron and dark_matter)

#Define a feature group
fg = folium.FeatureGroup(name="My Map")

#Locations
#Coordinates = [[7.429578, 3.908317], [7.496799, 4.078761]]

#Add marker feature to the FG
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup = "I am a Marker", icon=folium.Icon(color='green')))

#Add the fg to the base map layer
map.add_child(fg)

#save the map and name it
map.save("Map1.html")
