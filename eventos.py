import folium


eventos = [
    {"nome": "Show na praia", "lat": -24.006, "lon": -46.403},
    {"nome": "Feira gastronômica", "lat": -24.008, "lon": -46.410},
    {"nome": "Café de Negocios, 6/11/2025", "lat": -24.01754383574911, "lon": -46.457684641037694},
    
]

mapa = folium.Map(location=[-24.0058, -46.4028], zoom_start=13)

for e in eventos:
    folium.Marker(
        [e["lat"], e["lon"]],
        popup=e["nome"],
        icon=folium.Icon(color="purple", icon="flag")
    ).add_to(mapa)

mapa.save("eventos_praia_grande.html")
