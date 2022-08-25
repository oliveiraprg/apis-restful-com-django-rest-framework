from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField
    horario_fun = models.TextField()
    idade_min = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.descricao} - {self.horario_fun}'
