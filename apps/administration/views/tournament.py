from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.tournament import Tournament, League
from apps.administration.forms.tournament import TournamentForm, LeagueForm
from apps.administration.decorators import user_validator

class TorunamentCreateView(CreateView):
    model = Tournament
    template_name = "administration/specific/torunament/create.html"
    success_url = reverse_lazy('administration:tournament_new_liga')
    form_class = TournamentForm

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        return context

class TournamentListView(ListView):
    model = Tournament
    template_name = "administration/specific/torunament/list.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Torneos"
        context['table_id'] = "Torneos"
        context['table_title'] = "Torneos"
        context['header_page_title'] = "Lista de Torneos"
        return context

class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = "administration/specific/torunament/delete.html"
    success_url = reverse_lazy('administration:tournaments')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Torneo"
        context['header_page_title'] = "Eliminar Torneo"
        return context

class TournamentLigaCreateView(CreateView):
    model = League
    template_name = "administration/specific/torunament/create_liga.html"
    form_class = LeagueForm
    success_url = reverse_lazy('administration:tournaments')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        return context
