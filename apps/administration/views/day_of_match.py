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
from apps.administration.forms.day_of_match import DayOfMatchForm


class DateOfMatchCreateView(CreateView):
    model = DateOfMatch
    template_name = "administration/specific/fixture/create_data_match.html"
    form_class = DayOfMatchForm
    success_url = ""

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':self.kwargs['pk']})
        return success_url

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                fecha = form.save(commit=False)
                fecha.tournament = Tournament.objects.get(pk=self.kwargs['pk'])
                fecha.save()
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
        context['title'] = "Administradores"
        context['header_page_title'] = "Nueva Fecha de Juego"
        context['active_tournament'] = check_tournament_active()
        return context


class DateOfMatchUpdateView(UpdateView):
    model = DateOfMatch
    template_name = "administration/specific/fixture/create_data_match.html"
    form_class = DayOfMatchForm
    success_url = ""

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        tournament_id = self.get_object().tournament.id
        success_url = reverse_lazy('administration:tournament_detail', kwargs={'pk':tournament_id})
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nueva Fecha"
        context['header_page_title'] = "Nueva Fecha de Juego"
        context['active_tournament'] = check_tournament_active()
        return context


class MatchDayDetailView(DetailView):
    model = DateOfMatch
    template_name = "administration/specific/fixture/detail.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Partidos de la fecha"
        context['header_page_title'] = "Partidos de la Fecha N° " + str(self.get_object().number)
        context['active_tournament'] = check_tournament_active()
        context['partidos'] = self.get_object().matchs.all()
        context['day_match_id'] = self.get_object().id
        context['tournament_id'] = self.get_object().tournament.id
        return context
