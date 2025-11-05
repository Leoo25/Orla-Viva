from django.urls import path
from .views import mapa_eventos

urlpatterns = [
    path('mapa/', mapa_eventos, name='mapa_eventos'),
]