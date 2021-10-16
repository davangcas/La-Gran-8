from django.db import models
from django.forms import model_to_dict

from apps.team.models.team import Team
from apps.team.models.tournament import Tournament
from apps.team.choices import MATCH_HOURS


class FieldMatch(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name="Cancha", max_length=30)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Cancha"
        verbose_name_plural = "Canchas"


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    local_team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Equipo local", related_name="local")
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Equipo visitante", related_name="visitante")
    field = models.ForeignKey(FieldMatch, on_delete=models.CASCADE, verbose_name="Cancha")
    penalties = models.BooleanField(verbose_name="Penales", default=False, null=True, blank=True)
    goals_local = models.PositiveSmallIntegerField(verbose_name="Goles equipo local", blank=True, null=True, default=0)
    goals_away = models.PositiveSmallIntegerField(verbose_name="Goles equipo visitante", blank=True, null=True, default=0)
    date_of_match = models.DateField(verbose_name="Fecha del partido")
    hour_of_match = models.CharField(verbose_name="Hora del partido", max_length=2, choices=MATCH_HOURS, default="16")
    local_penalties = models.PositiveSmallIntegerField(verbose_name="Penales Local", blank=True, null=True, default=0)
    away_penalties = models.PositiveSmallIntegerField(verbose_name="Penales Visitante", blank=True, null=True, default=0)

    played = models.BooleanField(verbose_name="Partido Jugado", blank=True, null=True, default=False)

    def __str__(self):
        return self.local_team.name + " vs " +  self.away_team.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"


class DateOfMatch(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    matchs = models.ManyToManyField(Match, blank=True, null=True)
    number = models.PositiveSmallIntegerField(verbose_name="Número de Fecha", blank=True, null=True)
    day_of_match = models.DateField(verbose_name="Fecha de Juego", blank=True, null=True)

    played = models.BooleanField(verbose_name="Fecha Jugada", default=False, blank=True, null=True)

    def __str__(self):
        return self.tournament.name + " - Fecha N° " + str(self.number) + " - " + str(self.day_of_match)

    class Meta:
        verbose_name = "Fecha"
        verbose_name_plural = "Fechas"

