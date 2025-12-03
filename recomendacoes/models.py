from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoriaRecomendacao(models.Model):
    class Meta:
        verbose_name = 'Categoria Recomendação'
        verbose_name_plural = 'Categoria Recomendações'
    nome = models.CharField(max_length=100, unique=True)
    cor_pin = models.CharField(max_length=20, default='blue', help_text="Cor do pino (ex:'red','blue')")
    icone_pin = models.CharField(max_length=30, default='info-sign', help_text="Nome do ícone do Folium")
    imagem = models.ImageField(
        upload_to='fotos_categorias/', 
        null=True, 
        blank=True, 
        help_text="Imagem de fundo para o card"
    )
    def __str__(self):
        return self.nome

class Recomendacao(models.Model):
    class Meta:
        verbose_name = 'Recomendação'
        verbose_name_plural = 'Recomendações'
    categoria = models.ForeignKey(CategoriaRecomendacao, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='fotos_recomendacoes/', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    endereco_texto = models.CharField(max_length=255, blank=True, help_text="Ex: Av. Castelo Branco, 1234")
    telefone = models.CharField(max_length=20, blank=True)
    redeSocial_url = models.URLField(max_length=200, blank=True, help_text="Link da pagina do ifood ou rede social")
    FAIXA_PRECO_CHOICES = [
        ('$', '$ (Barato)'),
        ('$$', '$$ (Médio)'),
        ('$$$', '$$$ (Caro)'),
    ]
    faixa_preco = models.CharField(max_length=3, choices=FAIXA_PRECO_CHOICES, blank=True, null=True)
    AVALIACOES_CHOICES = [
        ('★','★'),
        ('★★','★★'),
        ('★★★','★★★'),
        ('★★★★','★★★★'),
        ('★★★★★','★★★★★'),
    ]
    avaliacao = models.CharField(max_length=5, choices=AVALIACOES_CHOICES, blank = True, null= True)
    favoritos = models.ManyToManyField(
        User, 
        related_name='recomendacoes_favoritas', 
        blank=True
    )
    

    def __str__(self):
        return self.nome
