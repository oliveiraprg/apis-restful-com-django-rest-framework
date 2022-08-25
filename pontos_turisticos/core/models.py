from django.db import models


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name} - {self.descricao}'

