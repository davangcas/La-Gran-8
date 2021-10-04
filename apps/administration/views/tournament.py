from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView, DetailView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.tournament import LeagueTable, Scorers, Tournament, League, Cautions, ConfigTournament, GroupAndPlayOff, Group
from apps.administration.forms.tournament import TournamentForm, LeagueForm, ConfigTournamentForm, GroupAndPlayOffForm
from apps.administration.decorators import user_validator
from apps.administration.services import (
    generate_league_table, 
    get_tournament_name, 
    generate_scorers_table, 
    generate_cards_to_players,
    check_or_create_days,
    check_tournament_active,
    generate_fields,
)
from apps.team.models.match import DateOfMatch


class TorunamentCreateView(CreateView):
    model = Tournament
    template_name = "administration/specific/torunament/create.html"
    success_url = reverse_lazy('administration:tournament_new_liga')
    form_class = TournamentForm

    def get_success_url(self):
        torneo = Tournament.objects.last()
        check_or_create_days()
        if torneo.format == "1":
            success_url = reverse_lazy('administration:tournament_new_liga', kwargs={'pk':torneo.id})
        elif torneo.format == "3":
            success_url = reverse_lazy('administration:tournament_new_groups', kwargs={'pk':torneo.id})
        return success_url

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        context['active_tournament'] = check_tournament_active()
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
        context['active_tournament'] = check_tournament_active()
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
        context['active_tournament'] = check_tournament_active()
        return context


class TournamentLigaCreateView(CreateView):
    model = ConfigTournament
    second_model = League
    template_name = "administration/specific/torunament/create_liga.html"
    form_class = ConfigTournamentForm
    second_form_class = LeagueForm
    success_url = reverse_lazy('administration:tournaments')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            try:
                torneo = Tournament.objects.get(pk=self.kwargs['pk'])
                league = form2.save(commit=False)
                config = form.save()
                config.tournament = torneo
                config.save()
                league.status = True
                league.tournament = torneo
                league.save()
                generate_league_table(league.id)
                generate_scorers_table(league.tournament.id)
                generate_cards_to_players(league.tournament.id)
                generate_fields(config.id)
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
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        context['active_tournament'] = check_tournament_active()
        return context


class TournamentGroupAndPlayOffView(CreateView):
    model = ConfigTournament
    second_model = GroupAndPlayOff
    template_name = "administration/specific/torunament/create_group_and_playoff.html"
    form_class = ConfigTournamentForm
    second_form_class = GroupAndPlayOffForm
    success_url = reverse_lazy('administration:tournaments')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            try:
                torneo = Tournament.objects.get(pk=self.kwargs['pk'])
                config = form.save()
                config.tournament = torneo
                config.save()
                group = form2.save()
                group.tournament = torneo
                group.save()
                number_of_goups = group.groups
                for grupo in range(number_of_goups):
                    new_group = Group.objects.create(
                        group_play_off=group,
                        group_name="Grupo " + str(grupo + 1),
                    )
                generate_scorers_table(torneo.id)
                generate_cards_to_players(torneo.id)
                generate_fields(config.id)
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
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        context['active_tournament'] = check_tournament_active()
        return context


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = ""

    def get_template_names(self):
        if self.get_object().format == "1":
            self.template_name = "administration/specific/torunament/details/detail_admin_league.html"
        elif self.get_object().format == "3":
            self.template_name = "administration/specific/torunament/details/detail_admin_groups.html"
        return self.template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_page_title'] = get_tournament_name(self.kwargs['pk'])
        context['title'] = "Torneo" + " " + get_tournament_name(self.kwargs['pk'])
        context['active_tournament'] = check_tournament_active()
        context['tournament_id'] = self.kwargs['pk']
        if self.get_object().format == "1":
            context['formato'] = "Liga"
            context['standings'] = LeagueTable.objects.filter(league=League.objects.filter(tournament=self.get_object()).last()).order_by('position')
            context['scorers'] = Scorers.objects.all().filter(tournament=context['tournament']).order_by('goals').exclude(goals=0)
            context['tournament'] = Tournament.objects.get(pk=self.kwargs['pk'])
            context['league'] = League.objects.filter(tournament=context['tournament']).last()
            context['cards'] = Cautions.objects.all().filter(tournament=context['tournament']).exclude(yellow_cards=0, red_cards=0)
            context['group_matchs'] = DateOfMatch.objects.filter(tournament=context['tournament'])
        elif self.get_object().format == "3":
            context['formato'] = "Grupo y Eliminatoria"
            context['tournament'] = Tournament.objects.get(pk=self.kwargs['pk'])
            context['cards'] = Cautions.objects.all().filter(tournament=context['tournament']).order_by('position')
            context['group_matchs'] = DateOfMatch.objects.filter(tournament=context['tournament'])
            context['groups'] = Group.objects.filter(group_play_off__tournament=context['tournament'])
            context['scorers'] = Scorers.objects.all().filter(tournament=context['tournament']).order_by('goals')
        return context

