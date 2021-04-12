from django.db import models

from apps.team.models.team import Team

class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Fecha del encuentro")
    
    class Meta:
        verbose_name = "Encuentro"
        verbose_name_plural = "Encuentros"