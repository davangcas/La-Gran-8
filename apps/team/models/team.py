from django.db import models
from django.forms import model_to_dict

from apps.administration.models.users import Administrator

class Team(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=80)
    win = models.PositiveIntegerField(verbose_name="Partidos Ganados")
    drawn = models.PositiveIntegerField(verbose_name="Partidos Empatados")
    lost = models.PositiveIntegerField(verbose_name="Partidos Perdidos")
    titles = models.PositiveIntegerField(verbose_name="Títulos conseguidos")
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    active = models.BooleanField(verbose_name="Habilitado", default=True, blank=True, null=True)
    delegated = models.ForeignKey(Administrator, on_delete=models.CASCADE, blank=True, null=True)

    status = models.BooleanField(verbose_name="Estado")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

