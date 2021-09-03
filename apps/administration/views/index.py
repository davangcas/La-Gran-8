import datetime

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from apps.administration.models.users import Administrator
from apps.team.models.team import Team
from apps.team.models.player import Player
from apps.team.models.tournament import Tournament
from apps.administration.decorators import user_validator, change_delegate_to_register_players
from apps.administration.services import check_tournament_active


class IndexView(TemplateView):
    template_name = "administration/specific/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.administrator.role == "Delegado":
            return redirect('administration:indexd')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Administración - Inicio"
        context["header_title"] = "Inicio - Administrador"
        context['header_page_title'] = "Bienvenido " + str(self.request.user.first_name) + " " + str(self.request.user.last_name)
        context['numero_delegados'] = Administrator.objects.filter(role="Delegado").count()
        context['equipos_habilitados'] = Team.objects.filter(active=True).count()
        context['jugadores_registrados'] = Player.objects.all().count()
        context['numero_administradores'] = Administrator.objects.filter(role="Administrador").count()
        context['active_tournament'] = check_tournament_active()
        return context


class IndexDelegateView(TemplateView):
    template_name = "administration/specific/index_delegate.html"

    @method_decorator(login_required)
    @method_decorator(change_delegate_to_register_players)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delegado - Inicio"
        context["header_title"] = "Inicio - Delegado"
        context['header_page_title'] = "Bienvenido " + str(self.request.user.first_name) + " " + str(self.request.user.last_name)
        context['equipo'] = Team.objects.filter(delegated=self.request.user.administrator).first()
        context['jugadores'] = Player.objects.filter(team=Team.objects.filter(delegated=self.request.user.administrator).first())
        context["torneo"] = Tournament.objects.filter(status=True)
        context['active_tournament'] = check_tournament_active()
        return context


