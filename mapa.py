import folium


mapa = folium.Map(location=[-24.0058, -46.4028], zoom_start=13)


folium.Marker(
    location=[-24.0058, -46.4028],
    popup="Evento na Praia Grande",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(mapa)



mapa.save("mapa_eventos.html")
