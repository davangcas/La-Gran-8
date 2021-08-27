from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms import model_to_dict

from apps.team.models.team import Team
from apps.team.models.player import Player
from apps.team.choices import TOURNAMENT_FORMATS, MATCH_HOURS

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
    vueltas = models.PositiveSmallIntegerField(verbose_name="Vueltas", default=2)
    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Liga"
        verbose_name_plural = "Ligas"


class LeagueTable(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    position = models.PositiveSmallIntegerField(verbose_name="Posición", blank=True, null=True, default=1)
    played = models.PositiveSmallIntegerField(verbose_name="Partidos jugados", blank=True, null=True, default=0)
    wins = models.PositiveSmallIntegerField(verbose_name="Partidos ganados", blank=True, null=True, default=0)
    loss = models.PositiveSmallIntegerField(verbose_name="Partidos perdidos", blank=True, null=True, default=0)
    draw = models.PositiveSmallIntegerField(verbose_name="Partidos empatados", blank=True, null=True, default=0)
    goals = models.PositiveSmallIntegerField(verbose_name="Goles", blank=True, null=True, default=0)
    goals_received = models.PositiveSmallIntegerField(verbose_name="Goles Recibidos", blank=True, null=True, default=0)
    dif_goals = models.IntegerField(verbose_name="Diferencia de goles", blank=True, null=True, default=0)
    points = models.PositiveSmallIntegerField(verbose_name="Puntos", blank=True, null=True, default=0)

    class Meta:
        verbose_name = "Tabla de Posiciones"
        verbose_name_plural = "Tabla de Posiciones"
        ordering = ['-points']


class PlayOff(models.Model):
    torunament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    away_goal = models.BooleanField(verbose_name="Gol de visitante", default=True)

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Eliminatoria"
        verbose_name_plural = "Eliminatorias"


class Scorers(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True)
    position = models.PositiveSmallIntegerField(verbose_name="Posición", blank=True, null=True, default=1)
    goals = models.PositiveSmallIntegerField(verbose_name="Goles", blank=True, null=True, default=0)
    played = models.PositiveSmallIntegerField(verbose_name="Partidos Jugados", blank=True, null=True, default=0)

    def __str__(self):
        return self.player.name + " - " + self.tournament.name

    class Meta:
        verbose_name = "Tabla de Goleadores"
        verbose_name_plural = "Tabla de Goleadores"


class Cautions(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True)
    position = models.PositiveSmallIntegerField(verbose_name="Posición", blank=True, null=True, default=1)
    played = models.PositiveSmallIntegerField(verbose_name="Partidos Jugados", blank=True, null=True, default=0)
    yellow_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Amarillas", blank=True, null=True, default=0)
    red_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Rojas", blank=True, null=True, default=0)

    def __str__(self):
        return self.player.name + " - " + self.tournament.name

    class Meta:
        verbose_name = "Tabla de Amonestados"
        verbose_name_plural = "Tabla de Amonestados"


class DaysOfWeek(models.Model):
    name = models.CharField(verbose_name="Dia de la semana", max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Día de la semana"
        verbose_name_plural = "Dias de la semana"


class ConfigTournament(models.Model):
    days = models.ManyToManyField(DaysOfWeek, verbose_name="Dias en los que se juegan los partidos")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    hour_init = models.CharField(verbose_name="Horario de comienzo de los partidos", max_length=2, choices=MATCH_HOURS)
    hour_end = models.CharField(verbose_name="Horario de finalización de los partidos", max_length=2, choices=MATCH_HOURS)
    fields = models.PositiveSmallIntegerField(verbose_name="Cantidad de canchas disponibles para jugar", default=1)

    class Meta:
        verbose_name = "Configuración del Torneo"
        verbose_name_plural = "Configuraciones de Torneos"
