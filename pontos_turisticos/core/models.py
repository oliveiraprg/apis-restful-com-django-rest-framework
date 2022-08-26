from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.descricao}'

