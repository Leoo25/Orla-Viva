from django.shortcuts import redirect, render
import folium
from core.forms import FormUsuario
from eventos.models import Evento
from recomendacoes.models import CategoriaRecomendacao
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from recomendacoes.models import Recomendacao

def cadastrar(request):
    formulario = FormUsuario(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            return redirect('home')
    return render(request, "core/cadastro.html",{'form':formulario})

def loginUsuario(request):
    if request.POST:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else: 
            messages.error(request, "Usuario ou senha incorreto!")
    return render(request, "core/login.html")

def logoutUsuario(request):
    logout(request)
    return redirect('home')

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
@login_required
def meus_favoritos(request):
    eventos_fav = request.user.eventos_favoritos.all()    
    recomendacoes_fav = request.user.recomendacoes_favoritas.all()
    
    context = {
        'eventos': eventos_fav,
        'recomendacoes': recomendacoes_fav
    }
    return render(request, 'core/meus_favoritos.html', context)



