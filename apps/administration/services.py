from django.contrib.auth.models import User

from apps.team.models.team import Team
from apps.administration.models.users import Administrator
from apps.team.models.player import Player

def check_players_capacity():
    last_player = Player.objects.last()
    team = Team.objects.get(pk=last_player.team.id)
    team_players = Player.objects.filter(team=team)
    print(team_players.count())
    print(team)
    if team_players.count() >= 12:
        team.active = True
        team.save()