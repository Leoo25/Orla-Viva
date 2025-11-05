from django.shortcuts import render
import folium
from .models import Evento

# Create your views here.
def mapa_eventos(request):
    mapa = folium.Map(location=[-24.0058, -46.4028], zoom_start=13)
    eventos = Evento.objects.all()
    for evento in eventos:
        data_formatada = evento.data.strftime("%d/%m/%Y")
        folium.Marker(
            location=[evento.latitude, evento.longitude],
            popup=f"<b>{evento.nome}</b><br>{evento.descricao}<br>{data_formatada}",
            icon=folium.Icon(color=evento.cor)
        ).add_to(mapa)
    mapa_html = mapa._repr_html_()
    return render(request, 'eventos/mapa_eventos.html', {'mapa': mapa_html})
