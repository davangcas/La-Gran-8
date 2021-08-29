from django.views.generic import (
    ListView,
    UpdateView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy

from apps.administration.decorators import user_validator, crete_or_not_config
from apps.administration.services import check_tournament_active
from apps.administration.models.config import GeneralConfig
from apps.administration.forms.config import GeneralConfigForm
from apps.team.models.team import Team
from apps.team.models.player import Player


class ConfigListView(ListView):
    model = GeneralConfig
    template_name = "administration/specific/config/list.html"

    @method_decorator(crete_or_not_config)
    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Configuración General"
        context['table_id'] = "Configuración"
        context['table_title'] = "Configuración"
        context['header_page_title'] = "Elementos a configurar"
        context['active_tournament'] = check_tournament_active()
        return context


class ConfigupdateView(UpdateView):
    model = GeneralConfig
    template_name = "administration/specific/config/update.html"
    form_class = GeneralConfigForm
    success_url = reverse_lazy('administration:general_config')

    @method_decorator(crete_or_not_config)
    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object = form.save()
        teams = Team.objects.all()
        for team in teams:
            players = Player.objects.filter(team=team)
            if players.count() >= self.object.players_requisit:
                team.active = True
                team.save()
            else:
                team.active = False
                team.save()    
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Configuración"
        context['form_title'] = "Modificar"
        context['header_page_title'] = "Editar Configuración"
        context['active_tournament'] = check_tournament_active()
        return context

