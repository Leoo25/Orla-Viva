from django.contrib import admin
from django.urls import include, path
from .views import recomendacoes

urlpatterns = [
    path('recomendacoes/',recomendacoes,name='recomendacoes')
]