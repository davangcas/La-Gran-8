from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from apps.team.models.team import Team

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
