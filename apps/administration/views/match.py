from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView, DetailView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.team.models.team import Team

from apps.team.models.tournament import Tournament, LeagueTable, League
from apps.administration.decorators import user_validator
from apps.administration.services import (
    check_tournament_active,
    reposition_league_teams,
)
from apps.team.models.match import DateOfMatch, Match
from apps.administration.forms.match import MatchLeagueForm, MatchLeagueEditForm, MatchLoadResultForm
from apps.team.models.player import Player
from apps.administration.forms.cautions import CautionsForm


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

        if self.object.tournament.format == "1":
            local_team = self.object.local_team
            away_team = self.object.away_team
            local_team_stats = Team.objects.get(pk=local_team.id)
            away_team_stats = Team.objects.get(pk=away_team.id)
            torneo = self.object.tournament
            liga = League.objects.filter(tournament=torneo).last()
            tabla = LeagueTable.objects.filter(league=liga)
            registro_local = tabla.get(team=local_team)
            registro_visitante = tabla.get(team=away_team)

            if self.object.goals_local > self.object.goals_away:
                # Global local
                local_team_stats.played += 1
                local_team_stats.win += 1
                local_team_stats.goals += self.object.goals_local
                local_team_stats.goals_received += self.object.goals_local

                # Match local
                registro_local.points += 3
                registro_local.played += 1
                registro_local.wins += 1
                registro_local.goals += self.object.goals_local
                registro_local.goals_received += self.object.goals_away
                local_diff = self.object.goals_local - self.object.goals_away
                registro_local.dif_goals += local_diff
                
                # Global away
                away_team_stats.played += 1
                away_team_stats.lost += 1
                away_team_stats.goals += self.object.goals_away
                away_team_stats.goals_received += self.object.goals_local

                # Match away
                registro_visitante.played += 1
                registro_visitante.loss += 1
                registro_visitante.goals += self.object.goals_away
                registro_visitante.goals_received += self.object.goals_local
                away_diff = self.object.goals_away - self.object.goals_local
                registro_visitante.dif_goals += away_diff
                
                # Save all
                registro_local.save()
                registro_visitante.save()
                local_team_stats.save()
                away_team_stats.save()
                reposition_league_teams(LeagueTable.objects.filter(league=liga).order_by('-points', '-dif_goals', '-goals'))

            elif self.object.goals_local == self.object.goals_away:
                # Match local
                registro_local.played += 1
                registro_local.draw += 1
                registro_local.goals += self.object.goals_local
                registro_local.goals_received += self.object.goals_away
                registro_local.points += 1

                # Match away
                registro_visitante.played += 1
                registro_visitante.draw += 1
                registro_visitante.goals += self.object.goals_away
                registro_visitante.goals_received += self.object.goals_local
                registro_visitante.points += 1

                # Global local
                local_team_stats.played += 1
                local_team_stats.draw += 1
                local_team_stats.goals += self.object.goals_local
                local_team_stats.goals_received += self.object.goals_away

                # Global away
                away_team_stats.played += 1
                away_team_stats.draw += 1
                away_team_stats.goals += self.object.goals_away
                away_team_stats.goals_received += self.object.goals_local

                # Save all
                registro_local.save()
                registro_visitante.save()
                local_team_stats.save()
                away_team_stats.save()
                reposition_league_teams(LeagueTable.objects.filter(league=liga).order_by('-points', '-dif_goals', '-goals'))
            
            else:
                # Match local
                registro_local.played += 1
                registro_local.loss += 1
                registro_local.goals += self.object.goals_local
                registro_local.goals_received += self.object.goals_away
                local_diff = self.object.goals_local - self.object.goals_away
                registro_local.dif_goals += local_diff

                # Match away
                registro_visitante.played += 1
                registro_visitante.wins += 1
                registro_visitante.goals += self.object.goals_away
                registro_visitante.goals_received += self.object.goals_local
                away_diff = self.object.goals_away - self.object.goals_local
                registro_visitante.dif_goals += away_diff
                registro_visitante.points += 3

                # Global local
                local_team_stats.played += 1
                local_team_stats.lost += 1
                local_team_stats.goals += self.object.goals_local
                local_team_stats.goals_received += self.object.goals_away

                # Global away
                away_team_stats.played += 1
                away_team_stats.win += 1
                away_team_stats.goals += self.object.goals_away
                away_team_stats.goals_received += self.object.goals_local

                # Save all
                registro_local.save()
                registro_visitante.save()
                local_team_stats.save()
                away_team_stats.save()
                reposition_league_teams(LeagueTable.objects.filter(league=liga).order_by('-points', '-dif_goals', '-goals'))
        
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

