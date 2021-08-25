from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView, DetailView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.tournament import LeagueTable, Tournament, League, PlayOff
from apps.administration.forms.tournament import TournamentForm, LeagueForm
from apps.administration.decorators import user_validator
from apps.administration.services import generate_league_table, get_tournament_name

class TorunamentCreateView(CreateView):
    model = Tournament
    template_name = "administration/specific/torunament/create.html"
    success_url = reverse_lazy('administration:tournament_new_liga')
    form_class = TournamentForm

    def get_success_url(self):
        torneo = Tournament.objects.last()
        if torneo.format == "1":
            success_url = reverse_lazy('administration:tournament_new_liga', kwargs={'pk':torneo.id})
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
    
    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                league = form.save(commit=False)
                league.status = True
                league.tournament = Tournament.objects.get(pk=self.kwargs['pk'])
                league.save()
                generate_league_table(league.id)
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
        context['title'] = "Nuevo Torneo"
        context['form_title'] = "Agregar Torneo"
        context['header_page_title'] = "Nuevo Torneo"
        return context


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = ""

    def get_template_names(self):
        if self.get_object().format == "1":
            self.template_name = "administration/specific/torunament/details/detail_admin_league.html"
        return self.template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_page_title'] = get_tournament_name(self.kwargs['pk'])
        context['title'] = "Torneo" + " " + get_tournament_name(self.kwargs['pk'])
        if self.get_object().format == "1":
            context['formato'] = "Liga"
            context['standings'] = LeagueTable.objects.filter(league=League.objects.filter(tournament=self.get_object()).last())
        return context
