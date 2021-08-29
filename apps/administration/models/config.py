from django.db import models
from django.forms import model_to_dict


class GeneralConfig(models.Model):
    name = models.CharField(verbose_name="Configuración",max_length=60, blank=True, null=True)
    players_requisit = models.PositiveSmallIntegerField(verbose_name="Cantidad de jugadores minima", default=12, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Configuración General"
        verbose_name_plural = "Configuración General"
