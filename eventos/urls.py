from django.urls import path
from . import views

urlpatterns = [
    path('mapa/', views.mapa_eventos, name='mapa_eventos'),
    path('favoritar/<int:evento_id>/', views.toggle_favorito_evento, name='toggle_favorito_evento'),
]