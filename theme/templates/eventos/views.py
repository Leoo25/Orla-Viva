from django.shortcuts import render
from .models import Evento 

def mapa_eventos(request):
    # CORREÇÃO: Busca APENAS eventos em destaque e atribui à variável 'eventos' no contexto
    eventos_destaque = Evento.objects.filter(evento_destaque=True).order_by('data')
    
    context = {
        'eventos': eventos_destaque,
        # O mapa não é mais necessário para a lista de cards
    }
    
    # Esta view agora renderiza a lista de cards de eventos
    return render(request, 'eventos/mapa_eventos.html', context)