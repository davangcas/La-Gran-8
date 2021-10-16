import datetime
import pdb

from django.contrib.auth.models import User
from django.views.generic.base import TemplateResponseMixin

from apps.team.models.team import Team
from apps.administration.models.users import Administrator
from apps.team.models.player import Player
from apps.team.models.tournament import (
    Group,
    GroupAndPlayOff,
    Tournament, 
    League, 
    LeagueTable, 
    Scorers, 
    Cautions, 
    DaysOfWeek,
    ConfigTournament,
)
from apps.team.models.match import (
    DateOfMatch,
    FieldMatch,
    Match,
)
from apps.administration.models.config import GeneralConfig

def check_players_capacity():

    last_player = Player.objects.last()
    team = Team.objects.get(pk=last_player.team.id)
    team_players = Player.objects.filter(team=team)

    config = GeneralConfig.objects.first()

    if team_players.count() >= config.players_requisit:
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
        init_positions = 1
        for team in tournament.teams.all():
            league_table = LeagueTable.objects.create()
            league_table.league = league
            league_table.team = team
            league_table.position = init_positions
            league_table.save()
            init_positions += 1

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

    init_position = 1
    for player in players:
        scorers_table = Scorers.objects.create(
            tournament=tournament,
            player=player,
            position=init_position,
        )
        scorers_table.save()
        init_position += 1


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


def check_or_create_days():
    days = DaysOfWeek.objects.all()
    if days:
        pass
    else:
        lunes = DaysOfWeek.objects.create(name="Lunes")
        lunes.save()
        martes = DaysOfWeek.objects.create(name="Martes")
        martes.save()
        miercoles = DaysOfWeek.objects.create(name="Miércoles")
        miercoles.save()
        jueves = DaysOfWeek.objects.create(name="Jueves")
        jueves.save()
        viernes = DaysOfWeek.objects.create(name="Viernes")
        viernes.save()
        sabado = DaysOfWeek.objects.create(name="Sabado")
        sabado.save()
        domingo = DaysOfWeek.objects.create(name="Domingo")
        domingo.save()


def check_tournament_active():
    status = True
    tournaments = Tournament.objects.filter(status=True)
    if tournaments:
        status = True
    else:
        status = False
    return status


def generate_fields(id_config):
    config = ConfigTournament.objects.get(pk=id_config)
    for number in range(config.fields):
        field = FieldMatch.objects.create(
            tournament=config.tournament,
            name="Cancha " + str(number+1),
        )
        field.save()


def create_dorsal(team):
    players = Player.objects.filter(team=team)
    if players.count() > 1:
        id_list = []
        for player in players:
            id_list.append(player.id)
        ultimo_id = id_list[-2]
        ultimo_dorsal_cargado = Player.objects.get(pk=ultimo_id).dorsal
        ultimo_jugador = Player.objects.last()
        ultimo_jugador.dorsal = ultimo_dorsal_cargado + 1
        ultimo_jugador.save()

    else:
        nuevo_dorsal = players.last()
        nuevo_dorsal.dorsal = 1
        nuevo_dorsal.save()


def change_player_dorsal(player):
    dorsal = player.dorsal
    players_same = Player.objects.filter(dorsal=dorsal)
    if players_same.count() == 2:
        other_player = players_same.exclude(pk=player.id).last()
        last_dorsal = Player.objects.filter(team=player.team).order_by('dorsal').last().dorsal
        other_player.dorsal = last_dorsal + 1
        other_player.save()


def get_number_of_all_matchs(torneo):
    teams = torneo.teams.all().count()
    matchs_number = 0

    if torneo.format == "1":
        rounds = League.objects.get(tournament=torneo).vueltas
        for round in range(rounds):
            for team in range(teams):
                matchs_number = matchs_number + (teams - 1) - team

    return matchs_number


def generate_matchs(torneo, partidos_por_fecha):
    if torneo.format == "1":
        teams = torneo.teams.all()
        fields = FieldMatch.objects.filter(tournament=torneo)
        rounds = League.objects.get(tournament=torneo).vueltas
        flag_to_local = True
        fechas = DateOfMatch.objects.filter(tournament=torneo)

        for round in range(rounds):
            flag_to_local = not flag_to_local
            id_team_list = []
            for team in teams:
                id_team_list.append(team.id)
                initial_query = teams.exclude(id__in=id_team_list)
                if initial_query:
                    for local in initial_query:
                        if flag_to_local:
                            new_match = Match.objects.create(
                                tournament=torneo,
                                local_team=team,
                                away_team=local,
                                field=fields.first(),
                                date_of_match=torneo.date_init,
                                hour_of_match="16",
                            )
                            flag_to_local = not flag_to_local
                        else:
                            new_match = Match.objects.create(
                                tournament=torneo,
                                local_team=local,
                                away_team=team,
                                field=fields.first(),
                                date_of_match=torneo.date_init,
                                hour_of_match="16",
                            )
                            flag_to_local = not flag_to_local
        
        matchs = Match.objects.filter(tournament=torneo)
        ids_matchs = []

        for fecha in fechas:
            id_teams = []
            for partido in range(partidos_por_fecha):
                match = matchs.exclude(id__in=ids_matchs)
                match = match.exclude(away_team_id__in=id_teams)
                match = match.exclude(local_team_id__in=id_teams)
                match = match.order_by('?')
                match = match.first()
                if match:
                    ids_matchs.append(match.id)
                    fecha.matchs.add(match)
                    id_teams.append(match.local_team.id)
                    id_teams.append(match.away_team.id)
                else:
                    continue
        
        id_fechas_incompletas = []
        matchs = Match.objects.filter(tournament=torneo)
        unasigned_matchs = matchs.exclude(id__in=ids_matchs)
        dates_of_matchs = DateOfMatch.objects.filter(tournament=torneo)

        for date in dates_of_matchs:
            if date.matchs.all().count() < partidos_por_fecha:
                id_fechas_incompletas.append(date.id)

        fechas_incompletas = dates_of_matchs.filter(id__in=id_fechas_incompletas)

        for fecha in fechas_incompletas:
            equipos = []
            fecha_partidos = fecha.matchs.all()
            partidos_faltantes = partidos_por_fecha - fecha_partidos.count()
            
            for partidos in fecha_partidos:
                equipos.append(partidos.local_team.id)
                equipos.append(partidos.away_team.id)
            
            new_query = unasigned_matchs.exclude(local_team_id__in=equipos)
            second_query = new_query.exclude(away_team_id__in=equipos)
            print(partidos_faltantes, fecha, second_query)
    
    elif torneo.format == "2":
        pass

    elif torneo.format == "3":
        pass

    elif torneo.format == "4":
        pass


def reposition_league_teams(table):
    init_position = 1

    for team in table:
        team.position = init_position
        team.save()
        init_position += 1


def check_groups_conformation(tournament):
    grupos = Group.objects.filter(group_play_off=GroupAndPlayOff.objects.filter(tournament=tournament).last())
    todos_los_equipos = tournament.teams.all().count()
    equipos_asignados = 0
    for grupo in grupos:
        equipos_asignados += grupo.teams.all().count()
    if todos_los_equipos != equipos_asignados:
        return False
    else:
        return True


def agregate_player_to_scorers(player):
    equipo = player.team
    torneos = Tournament.objects.filter(status=True)
    torneos = torneos.filter(teams__id=equipo.id)
    for torneo in torneos:
        nuevo_registro_tarjetas = Cautions.objects.create(
            tournament=torneo,
            player=player,
        )
        tabla_goleadores = Scorers.objects.filter(tournament=torneo).order_by('-position')
        ultima_posicion = tabla_goleadores.first().position
        nuevo_registro_goles = Scorers.objects.create(
            tournament=torneo,
            player=player,
            position=ultima_posicion + 1,
        )

