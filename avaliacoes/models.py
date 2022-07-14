from django.db import models

from django.contrib.auth.models import User


class Avaliacao(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comentario = models.TextField(null=True, blank=True)
    nota = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("Avaliação")
        verbose_name_plural = ("avaliações")

    def __str__(self):
        return self.usuario.username

