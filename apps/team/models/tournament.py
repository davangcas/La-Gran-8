from django.db import models
from django.forms import model_to_dict

from apps.team.models.team import Team

class Tournament(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=80)
    teams = models.PositiveSmallIntegerField(verbose_name="Cantidad de equipos")
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    date_init = models.DateField(verbose_name="Fecha de comienzo", blank=True, null=True)
    date_finish = models.DateField(verbose_name="Fecha de finalización", blank=True, null=True)
    champion = models.ForeignKey(Team, on_delete=models.CASCADE)

    status = models.BooleanField(verbose_name="Estado")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"

class League(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    matchs = models.PositiveSmallIntegerField("Partidos")

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Liga"
        verbose_name_plural = "Ligas"

class PlayOff(models.Model):
    torunament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    initial_round = models.PositiveSmallIntegerField(verbose_name="Rondas")

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Eliminatoria"
        verbose_name_plural = "Eliminatorias"
