from django.db import models


class Atracao(models.Model):

    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    horario_funcionamento = models.CharField(max_length=250)
    idade_minima = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)

    class Meta:
        verbose_name = ("Atração")
        verbose_name_plural = ("Atrações")

    def __str__(self):
        return self.nome

