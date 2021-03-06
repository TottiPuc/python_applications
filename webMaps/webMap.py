#libreria usada para crear mapas web
import folium
import pandas


#objeto map con las coordenadas del punto a graficar 
map = folium.Map(location=[1.205717, -77.285892],zoom_start=9, tiles="Stamen Terrain")

# objeto que permite crear el grupo de puntos o marcadores de volcanes a ser adicionados al mapa 
fgv = folium.FeatureGroup("Volcanes") 
# objeto que permite crear los poligonos y la cantidad de habitantes en el mapa 
fgp = folium.FeatureGroup("Populacion")

#estilar los popups con funciones html

html = """
<h3>Información del volcan</h3>
<a href="https://www.google.com/search?q=%%22{}%%22" target="_blank">{}</a><br>
Height => {} m
"""
#funcion que permite colorear lso marcadores de forma dinamica
def color_change(elevacion):
     if elevacion >= 4000:
          return "red"
     elif 3000 <elevacion < 4000:
          return"orange"
     else:
          return "green"
  


#cargar los datos del dataframe
data = pandas.read_csv("volcanes.txt")
lat = list(data["LAT"])
lon = list(data["LONG"])
ele = list(data["ELEVACION"])
pop = list(data["NOMBRE"])

for lt, ln, ele,name in zip(lat,lon,ele,pop):
     iframe = folium.IFrame(html=html.format(name,name,ele),width=300,height=100)
     fgv.add_child(folium.Marker(location=[lt,ln], popup = folium.Popup(iframe), icon=folium.Icon(color=color_change(ele)))) 

#metodo para agregar poligonos al mapa creado
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))

#se crean las capas al mapa original adicionandolas como hijas
map.add_child(fgv) # capa para volcanes
map.add_child(fgp) # capa para populacion
# se crea el panel de control de las capas
map.add_child(folium.LayerControl())
map.save("Mapa.html")
