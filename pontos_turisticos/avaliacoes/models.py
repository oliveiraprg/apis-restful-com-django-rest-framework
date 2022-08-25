from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(decimal_places=2, max_digits=2)
    data = models.DateTimeField(auto_now_add=True)
    aprovada = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.usuario} - {self.nota} - {self.data}'