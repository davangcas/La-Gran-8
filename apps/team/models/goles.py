from django.db import models

from apps.team.models.player import Player
from apps.team.models.match import Match


class Scorer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.PositiveSmallIntegerField(verbose_name="Goles", default=1)

    class Meta:
        verbose_name = "Goles de Jugador por Partido"
        verbose_name_plural = "Goles de Jugador por Partido"
