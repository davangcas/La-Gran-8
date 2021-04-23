from django.db import models
from apps.team.models.team import Team

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    name = models.Charfield(verbose_name="Nombre y Apellido", max_length=80)
    dni = models.PositiveSmallIntegerField(verbose_name="DNI")
    goals = models.PositiveSmallIntegerField(verbose_name="Goles")
    assists = models.PositiveSmallIntegerField(verbose_name="Asistencias")
    yellow_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Amarillas")
    red_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Rojas")
    played = models.PositiveSmallIntegerField(verbose_name="Partidos Jugados")
    role = models.CharField(verbose_name="Rol", max_length=80)

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
