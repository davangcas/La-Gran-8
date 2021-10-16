from datetime import date

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

from apps.team.models.team import Team
from apps.team.models.match import DateOfMatch, FieldMatch, Match
from apps.team.models.tournament import Group, GroupAndPlayOff, League, Tournament, ConfigTournament, DaysOfWeek
from apps.administration.services import get_number_of_all_matchs, generate_matchs
from apps.administration.models.users import Administrator

def activate_team(request, pk):
    success_url = reverse_lazy('administration:teams')
    team = Team.objects.get(pk=pk)
    if team.active == True:
        team.active = False
        team.save()
    else:
        team.active = True
        team.save()
    return HttpResponseRedirect(success_url)


def put_match_day_as_played(request, pk):
    fecha = DateOfMatch.objects.get(pk=pk)
    fecha.played = True
    fecha.save()
    success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':fecha.tournament.id})
    return HttpResponseRedirect(success_url)


def generate_automatic_matchs(request, pk):
    torneo = Tournament.objects.get(pk=pk)

    if torneo.format == "1":
        settings = ConfigTournament.objects.filter(tournament=torneo).first()
        fields_match = FieldMatch.objects.filter(tournament=torneo)
        hour_range = int(settings.hour_end) - int(settings.hour_init)
        number_of_matchs_per_day = hour_range * fields_match.count()
        fechas = DateOfMatch.objects.filter(tournament=torneo)

        if fechas:
            print("fechas generadas")
        else:
            all_matchs = get_number_of_all_matchs(torneo)
            matchs_to_play = int(torneo.teams.all().count() / 2)
            league_fechas = all_matchs / matchs_to_play
            for date_match in range(int(league_fechas)):
                new_date_match = DateOfMatch.objects.create(
                    tournament = torneo,
                    number = date_match + 1,
                    day_of_match = torneo.date_init,
                )
            generate_matchs(torneo, matchs_to_play)
    elif torneo.format == "2":
        pass
    elif torneo.format == "3":
        groupconfig = GroupAndPlayOff.objects.filter(tournament=torneo).last()
        groups = Group.objects.filter(group_play_off=groupconfig)
        teams_in_groups = 0
        for group in groups:
            teams_in_groups += group.teams.count()
        teams_in_tournament = torneo.teams.count()
        if teams_in_tournament > teams_in_groups:
            print("Los grupos deben de estar conformados")
            success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':pk})
            return HttpResponseRedirect(success_url)
        else:
            print("Fechas generadas")
        
    elif torneo.format == "4":
        pass
    success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':pk})
    return HttpResponseRedirect(success_url)


def change_delegate_status(request, pk):
    success_url = reverse_lazy('administration:delegates')
    delegate = Administrator.objects.get(pk=pk)
    if delegate.active:
        delegate.active = False
        delegate.tournament_sensitive = True
        delegate.save()
    else:
        delegate.active = True
        delegate.tournament_sensitive = False
        delegate.save()
    return HttpResponseRedirect(success_url)
