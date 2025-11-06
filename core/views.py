from django.shortcuts import render
import folium
from eventos.models import Evento
def home(request):
    m = folium.Map(location=[-24.0058, -46.4028], zoom_start=12) 
    eventos_com_local = Evento.objects.filter(latitude__isnull=False)
    
    for evento in eventos_com_local:
        data_formatada = evento.data.strftime("%d/%m/%Y")
        html_popup = f"<strong>{evento.nome}</strong><br>{evento.descricao}<br>{data_formatada}"
        if evento.imagem:
            url_imagem = evento.imagem.url
            html_popup = f"""
                <div style="width:150px;">
                    <strong>{evento.nome}</strong><br>
                    <img src="{url_imagem}" 
                         alt="Foto do evento" 
                         style="width:100%; height:auto; margin-top:5px; border-radius: 5px;">
                    <hr style="margin: 5px 0;">
                    {evento.descricao}<br>
                    {data_formatada}
                </div>
            """
        popup = folium.Popup(html_popup, max_width=200)
        folium.Marker(
            location=[evento.latitude, evento.longitude],
            popup=popup,
            icon=folium.Icon(color=evento.cor)
        ).add_to(m)
    context = {'mapa': m._repr_html_()}
    return render(request, 'core/home.html', context)
