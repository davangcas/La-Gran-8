from django.db import models

class Team(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=80)
    win = models.PositiveIntegerField(verbose_name="Partidos Ganados")
    drawn = models.PositiveIntegerField(verbose_name="Partidos Empatados")
    lost = models.PositiveIntegerField(verbose_name="Partidos Perdidos")
    titles = models.PositiveIntegerField(verbose_name="Títulos conseguidos")
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)

    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"