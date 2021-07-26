from django.db import models
from apps.team.models.team import Team
from django.forms import model_to_dict

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    name = models.Charfield(verbose_name="Nombre y Apellido", max_length=80)
    dni = models.PositiveIntegerField(verbose_name="DNI")
    date_created = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    date_born = models.DateField(verbose_name="Fecha de Nacimiento")
    goals = models.PositiveSmallIntegerField(verbose_name="Goles")
    assists = models.PositiveSmallIntegerField(verbose_name="Asistencias")
    yellow_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Amarillas")
    red_cards = models.PositiveSmallIntegerField(verbose_name="Tarjetas Rojas")
    played = models.PositiveSmallIntegerField(verbose_name="Partidos Jugados")

    status = models.BooleanField(verbose_name="Estado")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

class Goalkeeper(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goal_invict = models.PositiveSmallIntegerField(verbose_name="Valla invictas")
    goals_recibed = models.PositiveSmallIntegerField()
    status = models.BooleanField(verbose_name="Estado")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Arquero"
        verbose_name_plural = "Arqueros"

class Defense(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Defensor"
        verbose_name_plural = "Defensores"

class Middle(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Mediocampista"
        verbose_name_plural = "Mediocampistas"

class Strickers(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta: 
        verbose_name = "Delantero"
        verbose_name_plural = "Delanteros"

