from . import views
from django.contrib import admin
from django.urls import include, path
from .views import home, cadastrar

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastro'),
    path('login/', views.loginUsuario, name='login'),
    path('logout', views.logoutUsuario, name='logout'),
    path('favoritos/', views.meus_favoritos, name='meus_favoritos'),
]