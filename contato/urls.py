from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.contato, name='contato'),
    path('mensagens/', views.lista_mensagens, name='lista_mensagens'),
]
