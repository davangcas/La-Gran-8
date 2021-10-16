from django.views.generic.edit import FormView
from apps.team.models.match import Match
from apps.team.models.team import Team
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView
)
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.administration.decorators import user_validator
from apps.team.models.tournament import Group, GroupTable, Tournament
from apps.administration.services import check_tournament_active
from apps.administration.forms.groups import AddTeamToGroupForm


class GroupDetailView(DetailView):
    model = Group
    template_name = "administration/specific/groups/detail.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(self.get_object().group_name)
        context['form_title'] = "Detalles del " + str(self.get_object().group_name)
        context['header_page_title'] = "Detalles del " + str(self.get_object().group_name)
        context['active_tournament'] = check_tournament_active()
        context['standings'] = GroupTable.objects.filter(group_play_off=self.get_object())
        return context


class AssignTeamToGroup(UpdateView):
    template_name = "administration/specific/groups/assign_team_to_group.html"
    form_class = AddTeamToGroupForm
    model = Group

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        teams = self.get_object().group_play_off.tournament.teams.all()
        grupos_cargados = Group.objects.filter(group_play_off=self.get_object().group_play_off)
        grupos_cargados = grupos_cargados.exclude(pk=self.get_object().id)
        for grupo in grupos_cargados:
            if grupo.teams.all():
                for team in grupo.teams.all():
                    teams = teams.exclude(pk=team.id)
        kwargs.update({'teams': teams})
        return kwargs

    def get_success_url(self):
        success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':self.get_object().group_play_off.tournament.id})
        return success_url

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar equipos al " + str(Group.objects.get(pk=self.kwargs['pk']).group_name) 
        context['form_title'] = str(Group.objects.get(pk=self.kwargs['pk']).group_name) 
        context['header_page_title'] = "Agregar equipos al " + str(Group.objects.get(pk=self.kwargs['pk']).group_name) 
        context['active_tournament'] = check_tournament_active()
        return context
