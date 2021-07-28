from django.db import models
from django.forms import model_to_dict

from apps.team.models.team import Team
from apps.team.models.tournament import Tournament


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    local_team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Equipo local")
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name="Equipo visitante")
    
    goals_local = models.PositiveSmallIntegerField(verbose_name="Goles equipo local")
    goals_away = models.PositiveSmallIntegerField(verbose_name="Goles equipo visitante")
    date_of_match = models.DateTimeField(verbose_name="Fecha del partido")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
    