from django.db import models


class Localizacao(models.Model):

    endereco1 = models.CharField(max_length=250)
    endereco2 = models.CharField(max_length=250, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    

    class Meta:
        verbose_name = ("Localização")
        verbose_name_plural = ("Localizações")

    def __str__(self):
        return f'{self.endereco1} - {self.estado}'
