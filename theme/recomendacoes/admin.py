from django.contrib import admin
from .models import Recomendacao, CategoriaRecomendacao


@admin.register(Recomendacao)
class RecomendacaoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'descricao', 'latitude', 'longitude','redeSocial_url')
    
    fieldsets = (
        ('Informações Principais', {
            'fields': ('nome', 'descricao', 'telefone','redeSocial_url','categoria','faixa_preco','endereco_texto','avaliacao','imagem',)
        }),
        ('Localização (Clique no mapa para definir)', {
            'description': "Use o mapa abaixo para definir a localização. Você pode clicar ou arrastar o marcador.",
            
            'fields': ('latitude', 'longitude') 
        }),
    )
    class Media:
        html = {
            '\OrlaViva\theme\templates\base.html'
        }
    
        css = {
            'all': ('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',)
        }

        js = (
            'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
            'admin/js/admin_map.js',
        )
@admin.register(CategoriaRecomendacao)
class CategoriaRecomendacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    fieldsets = (('Informações',{
        'fields':('nome','cor_pin','icone_pin','imagem')
    }),)