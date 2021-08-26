from django.contrib.auth.models import User
from django.views.generic.base import TemplateResponseMixin

from apps.team.models.team import Team
from apps.administration.models.users import Administrator
from apps.team.models.player import Player
from apps.team.models.tournament import Tournament, League, LeagueTable, Scorers, Cautions

def check_players_capacity():

    last_player = Player.objects.last()
    team = Team.objects.get(pk=last_player.team.id)
    team_players = Player.objects.filter(team=team)

    if team_players.count() >= 12:
        team.active = True
        team.save()


def get_percentage_of_wins(id_team):
    team = Team.objects.get(pk=id_team)
    wins = team.win
    played = team.played
    percentage = float(wins) / float(played)
    return percentage


def generate_league_table(id_league):
    league = League.objects.get(pk=id_league)
    tournament = Tournament.objects.get(pk=league.tournament.id)
    try:
        for team in tournament.teams.all():
            league_table = LeagueTable.objects.create()
            league_table.league = league
            league_table.team = team
            league_table.position = 1
            league_table.save()

    except Exception as e:
        print(e)


def get_tournament_name(id_tournament):
    torneo = Tournament.objects.get(pk=id_tournament)
    return str(torneo.name)


def list_players_ids(queryset):
    ids = []
    for query in queryset:
        ids.append(query.id)
    return ids


def generate_scorers_table(id_tournament):
    tournament = Tournament.objects.get(pk=id_tournament)
    teams_query = tournament.teams.all()
    players = Player.objects.none()

    for team in teams_query:
        players |= Player.objects.filter(team=team)

    for player in players:
        scorers_table = Scorers.objects.create(
            tournament=tournament,
            player=player,
        )
        scorers_table.save()


def generate_cards_to_players(id_tournament):
    tournament = Tournament.objects.get(pk=id_tournament)
    teams_query = tournament.teams.all()
    players = Player.objects.none()

    for team in teams_query:
        players |= Player.objects.filter(team=team)

    for player in players:
        cautions = Cautions.objects.create(
            tournament=tournament,
            player=player,
        )
        cautions.save()
