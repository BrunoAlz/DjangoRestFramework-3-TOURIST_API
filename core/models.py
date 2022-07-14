from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from localizacao.models import Localizacao


class PontoTuristico(models.Model):
    
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Ponto Turistico")
        verbose_name_plural = ("Pontos Turisticos")
        ordering = ('id',)

    def __str__(self):
        return self.nome

