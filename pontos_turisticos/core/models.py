from django.db import models
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)

    def __str__(self) -> str:
        return f'{self.name} - {self.descricao}'

