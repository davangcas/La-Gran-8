from django.db import models
from django.forms import model_to_dict

from apps.administration.models.users import Administrator

class Team(models.Model):
    delegated = models.OneToOneField(Administrator, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Delegado")
    
    name = models.CharField(verbose_name="Nombre", max_length=80)
    played = models.PositiveIntegerField(verbose_name="Partidos Ganados", blank=True, default=0, null=True)
    win = models.PositiveIntegerField(verbose_name="Partidos Ganados", blank=True, default=0, null=True)
    draw = models.PositiveIntegerField(verbose_name="Partidos Empatados", blank=True, default=0, null=True)
    lost = models.PositiveIntegerField(verbose_name="Partidos Perdidos", blank=True, default=0, null=True)
    titles = models.PositiveIntegerField(verbose_name="Títulos conseguidos", blank=True, default=0, null=True)
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    active = models.BooleanField(verbose_name="Habilitado", default=False, blank=True, null=True)
    logo = models.ImageField(verbose_name="Logo", default="teams/default/1.png", upload_to="teams/%y/%m", blank="True", null=True)

    status = models.BooleanField(verbose_name="Estado", blank=True, null=True, default=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

