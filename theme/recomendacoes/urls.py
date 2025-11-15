from django.contrib import admin
from django.urls import include, path
from .views import recomendacoes, lista_por_categoria

urlpatterns = [
    path('recomendacoes/',recomendacoes,name='recomendacoes'),
    path('categoria/<int:pk>/',lista_por_categoria, name='lista_recomendacoes_por_categoria'),
]