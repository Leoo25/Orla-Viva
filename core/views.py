from django.shortcuts import render
import folium
from eventos.models import Evento
from recomendacoes.models import CategoriaRecomendacao
def home(request):
    m = folium.Map(location=[-24.009197, -46.421477], zoom_start=14) 
    eventos_com_local = Evento.objects.select_related('categoria').filter(latitude__isnull=False)
    
    for evento in eventos_com_local:
        data_formatada = evento.data.strftime("%d/%m/%Y")
        
        if evento.imagem and evento.site_url:
            url_imagem = evento.imagem.url
            html_popup = f"""
                <div style="width:150px;">
                    <strong>{evento.nome}</strong><br>
                    <img src="{url_imagem}" 
                         alt="Foto do evento" 
                         style="width:100%; height:auto; margin-top:5px; border-radius: 5px;">
                    <hr style="margin: 5px 0;">
                    {evento.descricao}<br>
                    {data_formatada}<br>
                    <a href="{evento.site_url}" target="_blank" rel="noopener noreferrer" 
                       style="display:block; text-align:center; background-color: #007bff; color: white; padding: 5px; text-decoration: none; border-radius: 5px; margin-top: 5px;">
                       Saiba Mais
                    </a>
                </div>
            """
        elif evento.imagem:
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
        elif evento.site_url:
            html_popup = f"""
                <strong>{evento.nome}</strong><br>
                {evento.descricao}<br>
                {data_formatada}<br>
                <a href="{evento.site_url}" target="_blank" rel="noopener noreferrer">Saiba Mais</a>
            """
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
            icon=folium.Icon(
                color=pin_color,
                icon=pin_icon,
                prefix='glyphicon' 
            )
        ).add_to(m)
    
    context = {'mapa': m._repr_html_()}
    categorias_recomendacao = CategoriaRecomendacao.objects.all()
    context = {
        'mapa': m._repr_html_(),
        'categorias': categorias_recomendacao
    }
    return render(request, 'core/home.html', context)
