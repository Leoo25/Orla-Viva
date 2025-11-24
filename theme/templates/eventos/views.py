from django.shortcuts import render
from .models import Evento 

def mapa_eventos(request):
    # 1. BUSCAR DADOS
    # Pega todos os eventos onde 'evento_destaque' é Verdadeiro
    eventos_destaque = Evento.objects.filter(evento_destaque=True).order_by('data')
    
    # 2. PREPARAR O PACOTE
    # A chave 'eventos' deve ser igualzinha ao que usamos no HTML: {% for evento in eventos %}
    context = {
        'eventos': eventos_destaque,
    }
    
    # 3. ENTREGAR PARA A TELA
    return render(request, 'eventos/mapa_eventos.html', context)