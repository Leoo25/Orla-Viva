
from django.contrib import admin
from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'data', 'latitude', 'longitude')
    
    fieldsets = (
        ('Informações Principais', {
            'fields': ('nome', 'descricao', 'data', 'cor', 'imagem')
        }),
        ('Localização (Clique no mapa para definir)', {
            'description': "Use o mapa abaixo para definir a localização. Você pode clicar ou arrastar o marcador.",
            
            'fields': ('latitude', 'longitude') 
        }),
    )
    

    
    class Media:
    
        css = {
            'all': ('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',)
        }

        js = (
            'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
            'admin/js/admin_map.js',
        )