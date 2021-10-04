from django.shortcuts import redirect

from apps.team.models.tournament import Tournament
from apps.team.models.match import Match

def data_validation(view_function):
    def validation(request, *args, **kwargs):
        if not Tournament.objects.all():
            return redirect('landing:proximamente')
        return view_function(request, *args, **kwargs)
    return validation

def match_validation(view_function):
    def validation(request, *args, **kwargs):
        if not Match.objects.all():
            return redirect('landing:proximamente')
        return view_function(request, *args, **kwargs)
    return validation