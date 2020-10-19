from django.db import models

# Create your models here.

class Mapa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Distancia(models.Model):
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    ponto_1 = models.CharField(max_length=255)
    ponto_2 = models.CharField(max_length=255)
    distancia = models.FloatField(default=0)

    def __str__(self):
        return self.ponto_1+", "+self.ponto_2+", "+str(self.distancia)