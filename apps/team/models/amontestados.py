from django.db import models

from apps.team.models.player import Player
from apps.team.models.match import Match
from apps.team.choices import AMONESTACIONES

class Amonestacion(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Jugador")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)
    type_amonestated = models.CharField(verbose_name="Tipo de amonestación", max_length=1, choices=AMONESTACIONES, default="1")

