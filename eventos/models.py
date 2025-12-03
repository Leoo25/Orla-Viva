from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoriaEventos(models.Model):
    class Meta:
        verbose_name = 'Categoria Evento'
        verbose_name_plural = 'Categoria Eventos'
    nome = models.CharField(max_length=100, unique=True)
    cor_pin = models.CharField(max_length=20, default='blue', help_text="Cor do pino (ex:'red','blue')")
    icone_pin = models.CharField(max_length=30, default='info-sign', help_text="Nome do ícone do Folium")
    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    data = models.DateField()
    imagem = models.ImageField(upload_to='fotos_eventos/', null=True,blank=True)
    site_url = models.URLField(max_length=200, blank=True, null=True, help_text="Link do site ou rede social",verbose_name="URL do evento")
    categoria = models.ForeignKey(CategoriaEventos, on_delete=models.SET_NULL, null=True)
    horario = ...
    local = ...
    OPCOES_DESTAQUE = [
        (True, 'Sim'),
        (False, 'Não'),
    ]
    evento_destaque = models.BooleanField(
        choices=OPCOES_DESTAQUE, 
        default=False, 
        verbose_name="Destaque"
    )
    favoritos = models.ManyToManyField(
        User, 
        related_name='eventos_favoritos', 
        blank=True, 
        verbose_name="Favoritado por"
    )

    def __str__(self):
        return self.nome