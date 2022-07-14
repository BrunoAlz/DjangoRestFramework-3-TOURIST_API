from django.db import models
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)

    class Meta:
        verbose_name = ("Ponto Turistico")
        verbose_name_plural = ("Pontos Turisticos")

    def __str__(self):
        return self.nome

