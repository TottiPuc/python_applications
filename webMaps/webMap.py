#libreria usada para crear mapas web
import folium
import pandas


#objeto map con las coordenadas del punto a graficar 
map = folium.Map(location=[1.205717, -77.285892],zoom_start=9, tiles="Stamen Terrain")

# objeto que permite crear el grupo de puntos o marcadores a ser adicionados al mapa 
fg = folium.FeatureGroup("My map") 

#estilar los popups con funciones html

html = """
<h3>Información del volcan</h3>
<a href="https://www.google.com/search?q=%%22{}%%22" target="_blank">{}</a><br>
Height => {} m
"""

#cargar los datos del dataframe
data = pandas.read_csv("volcanes.txt")
lat = data["LAT"]
lon = data["LONG"]
ele = data["ELEVACION"]
pop = data["NOMBRE"]

for lt, ln, ele,name in zip(lat,lon,ele,pop):
     iframe = folium.IFrame(html=html.format(name,name,ele),width=300,height=100)
     fg.add_child(folium.Marker(location=[lt,ln], popup = folium.Popup(iframe), icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("Mapa.html")
