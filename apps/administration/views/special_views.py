from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from apps.team.models.team import Team
from apps.team.models.match import DateOfMatch
from apps.team.models.tournament import Tournament, ConfigTournament, DaysOfWeek

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
    torneo = Tournament.objects.filter(status=True).last()
    dias = DaysOfWeek.objects.all()
    print(dias)
    if torneo.format == "1":
        settings = ConfigTournament.objects.filter(tournament=torneo).last()
        print(settings.days.all().first())
    elif torneo.format == "2":
        pass
    elif torneo.format == "3":
        pass
    elif torneo.format == "4":
        pass
    success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':pk})
    return HttpResponseRedirect(success_url)

