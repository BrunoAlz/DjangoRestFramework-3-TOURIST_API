from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")

    def __str__(self):
        return self.usuario.username
