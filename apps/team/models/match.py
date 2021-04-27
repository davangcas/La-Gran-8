from django.db import models

from apps.team.models.team import Team
from apps.team.models.tournament import Tournament


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    local_team = models.ForeignKey(Team, on_delete=models.PROTECT)
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT)
    goals_local = models.PositiveSmallIntegerField()
    goals_away = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
    