from django.shortcuts import render
import folium
from .models import Evento, CategoriaEventos

def mapa_eventos(request):
    m = folium.Map(location=[-24.0058, -46.4028], zoom_start=12) 
    eventos_com_local = Evento.objects.select_related('categoria').filter(latitude__isnull=False)
    
    for evento in eventos_com_local:
        data_formatada = evento.data.strftime("%d/%m/%Y")        
        if evento.imagem and evento.site_url:
            url_imagem = evento.imagem.url
            html_popup = f"""
                <div style="width:150px;">
                    <strong>{evento.nome}</strong><br>
                    <img src="{url_imagem}" style="width:100%; height:auto; margin-top:5px; border-radius: 5px;">
                    <hr style="margin: 5px 0;">
                    {evento.descricao}<br>
                    {data_formatada}<br>
                    <a href="{evento.site_url}" target="_blank" style="display:block; text-align:center; background-color: #007bff; color: white; padding: 5px; text-decoration: none; border-radius: 5px; margin-top: 5px;">Saiba Mais</a>
                </div>
            """
        elif evento.imagem:
            url_imagem = evento.imagem.url
            html_popup = f"""<div style="width:150px;"><strong>{evento.nome}</strong><br><img src="{url_imagem}" style="width:100%; height:auto; margin-top:5px; border-radius: 5px;"><hr style="margin: 5px 0;">{evento.descricao}<br>{data_formatada}</div>"""
        elif evento.site_url:
            html_popup = f"""<strong>{evento.nome}</strong><br>{evento.descricao}<br>{data_formatada}<br><a href="{evento.site_url}" target="_blank">Saiba Mais</a>"""
        else:
            html_popup = f"<strong>{evento.nome}</strong><br>{evento.descricao}<br>{data_formatada}"
            
        popup = folium.Popup(html_popup, max_width=200)

        pin_color = 'gray'
        pin_icon = 'info-sign'
        if evento.categoria:
            pin_color = evento.categoria.cor_pin
            pin_icon = evento.categoria.icone_pin
            
        folium.Marker(
            location=[evento.latitude, evento.longitude],
            popup=popup,
            icon=folium.Icon(color=pin_color, icon=pin_icon, prefix='glyphicon')
        ).add_to(m)    
    destaques = Evento.objects.filter(evento_destaque=True).order_by('data')    
    outros_eventos = Evento.objects.filter(evento_destaque=False).order_by('data')
    
    context = {
        'mapa': m._repr_html_(),
        'destaques': destaques,
        'outros_eventos': outros_eventos
    }
    
    return render(request, 'eventos/mapa_eventos.html', context)