#libreria usada para crear mapas web
import folium
import pandas


#objeto map con las coordenadas del punto a graficar 
map = folium.Map(location=[1.205717, -77.285892],zoom_start=9, tiles="Stamen Terrain")

# objeto que permite crear el grupo de puntos o marcadores a ser adicionados al mapa 
fg = folium.FeatureGroup("My map") 

#cargar los datos del dataframe
data = pandas.read_csv("volcanes.txt")
lat = data["LAT"]
lon = data["LONG"]
pop = data["NOMBRE"]

for lt, ln, pp in zip(lat,lon,pop):
     fg.add_child(folium.Marker(location=[lt,ln], popup = pp, icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("Mapa.html")
