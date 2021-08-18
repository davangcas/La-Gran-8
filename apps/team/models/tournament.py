from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms import model_to_dict

from apps.team.models.team import Team
from apps.team.choices import TOURNAMENT_FORMATS

class Tournament(models.Model):
    name = models.CharField(verbose_name="Nombre del torneo", max_length=80)
    teams = models.ManyToManyField(Team, related_name="tournament_teams", verbose_name="Equipos del torneo")
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    date_init = models.DateField(verbose_name="Fecha de comienzo", blank=True, null=True)
    date_finish = models.DateField(verbose_name="Fecha de finalización de inscripción", blank=True, null=True)
    champion = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    format = models.CharField(verbose_name="Formato", max_length=1, default="1", blank=True, null=True, choices=TOURNAMENT_FORMATS)

    status = models.BooleanField(verbose_name="Estado", default=True, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.name + " " + str(self.date_created)

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"

class League(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Liga"
        verbose_name_plural = "Ligas"

class TeamLeague(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class PlayOff(models.Model):
    torunament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    initial_round = models.PositiveSmallIntegerField(verbose_name="Rondas")

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Eliminatoria"
        verbose_name_plural = "Eliminatorias"
