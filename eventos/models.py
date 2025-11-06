from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    cor = models.CharField(max_length=20, default="red")
    data = models.DateField()
    imagem = models.ImageField(
        upload_to='fotos_eventos/', 
        null=True,                   
        blank=True                  
    )

    def __str__(self):
        return self.nome