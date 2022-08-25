from django.db import models



class Atracao(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField
    horario_fun = models.TextField()
    idade_min = models.IntegerField

    def __str__(self) -> str:
        return f'{self.name} - {self.description}'
