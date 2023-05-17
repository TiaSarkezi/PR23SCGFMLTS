import pandas as pd
pn2022 = pd.read_csv('data/pn2022.csv', 
                    encoding="unicode_escape",
                    delimiter=";")

coord = []

for stevilka in pn2022['ZaporednaStevilkaPN'].unique():
    df_number = pn2022[pn2022['ZaporednaStevilkaPN'] == stevilka]
    if df_number['GeoKoordinataX'].unique()[0] != 0 and df_number['GeoKoordinataY'].unique()[0] != 0 :
        coord.append((df_number['GeoKoordinataX'].unique()[0], df_number['GeoKoordinataY'].unique()[0]))
        
import pyproj
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:3794", "EPSG:4326")
coordinates_without_duplicates = []

for y, x in coord:
    coordinates_without_duplicates.append(transformer.transform(x, y))
    
import folium
from folium import plugins

m = folium.Map(location=(46, 14.9), tiles="Cartodb dark_matter", zoom_start=8.45)

plugins.HeatMap(coordinates_without_duplicates, radius=5, blur=4).add_to(m)
