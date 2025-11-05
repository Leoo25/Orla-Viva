from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cor = models.CharField(max_length=20, default="red")
    data = models.DateField()

    def __str__(self):
        return self.nome