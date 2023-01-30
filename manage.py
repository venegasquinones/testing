#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import folium

# df18.to_excel('results/precipitation_record_and_estimation_final.xlsx', index=False)
df18 = pd.read_excel('precipitation_record_and_estimation_final.xlsx')


# In[2]:


# Create a map object centered on the mean of the coordinates
mean_lat = df18['POINT_Y'].mean()
mean_lon = df18['POINT_X'].mean()
world_map = folium.Map(location=[mean_lat, mean_lon], zoom_start=4)

# Add markers for each location in the DataFrame
for i in range(0, len(df18)):
    if df18.iloc[i]['r2'] >= 0.6:
        color = 'green'
    elif df18.iloc[i]['r2'] < 0.6:
        color = 'red'
    else:
        color = 'black'
    folium.Marker(location=[df18.iloc[i]['POINT_Y'], df18.iloc[i]['POINT_X']],
                  popup=f"{df18.iloc[i]['nombre']} ({df18.iloc[i]['codigo_estacion']}) ({df18.iloc[i]['r2']}) ({df18.iloc[i]['count']})",
                  icon=folium.Icon(color=color)).add_to(world_map)


# Display the map
world_map


# In[ ]:




