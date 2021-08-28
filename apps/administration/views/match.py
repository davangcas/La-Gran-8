from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView, DetailView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.tournament import Tournament
from apps.administration.decorators import user_validator
from apps.administration.services import (
    check_tournament_active,
)
from apps.team.models.match import DateOfMatch, Match
from apps.administration.forms.match import MatchLeagueForm, MatchLeagueEditForm, MatchLoadResultForm
from apps.team.models.player import Player


class MatchCreateView(CreateView):
    model = Match
    template_name = "administration/specific/match/create.html"
    form_class = MatchLeagueForm
    success_url = ""

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        day_match = DateOfMatch.objects.get(pk=self.kwargs['pk'])
        success_url = reverse_lazy('administration:match_day_detail', kwargs={'pk':day_match.id})
        return success_url

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                day_match = DateOfMatch.objects.get(pk=self.kwargs['pk'])
                match = form.save(commit=False)
                match.tournament = day_match.tournament
                match.save()
                day_match.matchs.add(match)
                day_match.save()
                return HttpResponseRedirect(self.get_success_url())
            except Exception as e:
                context = self.get_context_data(**kwargs)
                context['errors'] = e
                return render(request, self.template_name, context)
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors'] = form.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Partido"
        context['form_title'] = "Agregar Partido"
        context['header_page_title'] = "Nuevo Partido"
        context['active_tournament'] = check_tournament_active()
        return context


class MatchUpdateView(UpdateView):
    model = Match
    template_name = "administration/specific/match/update.html"
    form_class = MatchLeagueEditForm
    
    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse_lazy('administration:match_day_detail', kwargs={'pk':self.kwargs['date_id']})
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Partido"
        context['form_title'] = "Modificar Partido"
        context['header_page_title'] = "Modificar Partido"
        context['active_tournament'] = check_tournament_active()
        return context


class LoadMatchResultView(UpdateView):
    model = Match
    template_name = "administration/specific/match/load_result.html"
    form_class = MatchLoadResultForm

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse_lazy('administration:match_day_detail', kwargs={'pk':self.kwargs['date_id']})
        return success_url
    
    def form_valid(self, form):
        form.instance.played = True
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cargar Resultado"
        context['form_title'] = "Cargar Resultado"
        context['header_page_title'] = "Cargar Resultado"
        context['active_tournament'] = check_tournament_active()
        context['jugadores_local'] = Player.objects.filter(team=self.object.local_team)
        context['jugadores_visitantes'] = Player.objects.filter(team=self.object.away_team)
        return context



