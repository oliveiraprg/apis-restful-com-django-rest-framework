from django.db import models


class Localizacao(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.cidade} - {self.linha1} {self.linha2}'
