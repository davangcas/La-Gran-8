from django.db import models

class Tournament(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=80)
    matchs = models.PositiveIntegerField(verbose_name="Partidos")

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"

class Fixture(models.Model):
    class Meta:
        verbose_name = "Fixture"
        verbose_name_plural = "Fixtures"