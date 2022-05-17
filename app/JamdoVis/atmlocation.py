# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import haversine as hs 
import folium

Atm_user = pd.read_excel('/content/Kingston_location.xlsx')
atm_location = pd.read_excel('/content/ATM_location.xlsx')

Atm_user['coordinates']= list(zip(Atm_user.Lat,Atm_user.Lon))
atm_location['coordinates']= list (zip(atm_location.Lat, atm_location.Lon))

atm_location.tail(16)

def location_from(user,atm):
  dist=hs.haversine(user,atm)
  return round(dist,2)

for _,row in atm_location.iterrows():
  Atm_user[row.ATM]= Atm_user['coordinates'].apply(lambda x: location_from(row.coordinates,x))

m=folium.Map(location=[18.0196,-76.7796], zoom_start=12, tiles='OpenStreetMap')

folium.Circle(
    radius=200,
    location=[18.0196,-76.7796],
    popup="User_1",
    color="purple",
    fill=False,
).add_to(m)

folium.Circle(
    radius=200,
    location=[18.0117,-76.7894],
    popup="User_2",
    color="blue",
    fill=False,
).add_to(m)

folium.Circle(
    radius=200,
    location=[18.0865,-76.7263],
    popup="User_3",
    color="red",
    fill=False,
).add_to(m)

folium.Circle(
    radius=50,
    location=[18.0233,-76.7840],
    popup="User_4",
    color="green",
    fill=False,
).add_to(m)

folium.Circle(
    radius=50,
    location=[18.0030,-76.7898],
    popup="User_5",
    color="brown",
    fill=False,
).add_to(m)

folium.Circle(
    radius=100,
    location=[17.9778,-76.7825],
    popup="User_6",
    color="yellow",
    fill=False,
).add_to(m)





folium.Marker(
    location=[18.006460, -76.789480],
    popup="ATM H - Not Working",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.CircleMarker(
    location=[18.006460, -76.789480],
    radius=10,
    popup="ATM H - Not Working",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.011174,-76.78516  ],
    popup="ATM G - Working",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.CircleMarker(
    location=[18.011174, -76.787516 ],
    radius=10,
    popup="ATM G - Working",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.015451, -76.796075],
    popup="ATM D -  Not Working",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.CircleMarker(
    location=[18.015451, -76.796075 ],
    radius=10,
    popup="ATM D - Not Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.CircleMarker(
    location=[18.016340, -76.747458 ],
    radius=10,
    popup="ATM E -  Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.016340,-76.747458  ],
    popup="ATM E - Working",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.CircleMarker(
    location=[17.966098, -76.802680],
    radius=10,
    popup="ATM A -  Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[17.966098, -76.802680 ],
    popup="ATM A -  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)


folium.CircleMarker(
    location=[18.030864, -76.776356],
    radius=10,
    popup="ATM B -    Not Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.030864, -76.776356],
    popup="ATM B - Not Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)



folium.CircleMarker(
    location=[17.966139, -76.792167],
    radius=10,
    popup="ATM C -     Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[17.966139, -76.792167],
    popup="ATM C -  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)


folium.CircleMarker(
    location=[18.1794021,-76.451757],
    radius=10,
    popup="ATM I -     Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.1794021,-76.451757],
    popup="ATM I -  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)



folium.CircleMarker(
    location=[18.1783536,-76.451051],
    radius=10,
    popup="ATM K -     Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.2351034,-76.6565922],
    popup="ATM K -  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)

folium.CircleMarker(
    location=[18.2351034,-76.6565922],
    radius=10,
    popup="ATM J -   Not  Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.1783536,-76.451051],
    popup="ATM J - Not  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)



folium.CircleMarker(
    location=[18.4019852,-76.9501526],
    radius=10,
    popup="ATM L -   Not  Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.4019852,-76.9501526],
    popup="ATM L - Not  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)




folium.CircleMarker(
    location=[18.2711737,-76.8904369],
    radius=10,
    popup="ATM M -    Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.2711737,-76.8904369],
    popup="ATM M -   Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)



folium.CircleMarker(
    location=[18.40979,-77.1021554],
    radius=10,
    popup="ATM N -  Not   Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.40979,-77.1021554],
    popup="ATM N -  Not  Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)



folium.CircleMarker(
    location=[18.4627142,-77.3354811],
    radius=10,
    popup="ATM O -     Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.4627142,-77.3354811],
    popup="ATM O -    Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)


folium.CircleMarker(
    location=[18.4676119,-77.3052157],
    radius=10,
    popup="ATM P -     Working ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

folium.Marker(
    location=[18.4676119,-77.3052157],
    popup="ATM P -    Working" ,
    icon=folium.Icon(color="green"),
).add_to(m)






























    

m

