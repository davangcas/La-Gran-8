from apps.team.models.tournament import Tournament
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from apps.administration.models.users import Administrator
from apps.administration.models.config import GeneralConfig

def user_validator(view_function):

    def validation(request, *args, **kwargs):
        if request.user.administrator.role == "Delegado":
            return redirect('administration:indexd')
        else:
            return view_function(request, *args, **kwargs)

    return validation


def crete_or_not_config(view_function):

    def validation(request, *args, **kwargs):
        config = GeneralConfig.objects.all()
        if not config:
            new_config = GeneralConfig.objects.create(
                name="Cantidad de jugadores minima",
                players_requisit=12,
            )
            new_config.save()
            return view_function(request, *args, **kwargs)
        else:
            return view_function(request, *args, **kwargs)

    return validation


def change_delegate_to_register_players(view_function):
    
    def validation(request, *args, **kwargs):
        torneo = Tournament.objects.filter(status=True)
        if torneo:
            last_tournament = torneo.last()
            if last_tournament.date_finish < datetime.date.today() and request.user.administrator.tournament_sensitive:
                administrator = Administrator.objects.get(user=request.user)
                administrator.active = False
                administrator.save()
            return view_function(request, *args, **kwargs)
        else:
            return view_function(request, *args, **kwargs)

    return validation
