#libreria usada para crear mapas web
import folium


#objeto map con las coordenadas del punto a graficar 
map = folium.Map(location=[1.205717, -77.285892],zoom_start=13, tiles="Stamen Terrain")
map.save("Mapa.html")
