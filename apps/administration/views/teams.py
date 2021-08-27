from apps.administration.models.users import Administrator
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect

from apps.team.models.team import Team
from apps.administration.forms.team import (
    TeamCreateForm,
    TeamUpdateForm,
    TeamCreateNextForm,
)
from apps.administration.decorators import user_validator
from apps.team.models.player import Player
from apps.administration.services import check_tournament_active


class TeamListView(ListView):
    model = Team
    template_name = "administration/specific/teams/list.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Equipos"
        context['table_id'] = "teams"
        context['table_title'] = "Equipos"
        context['header_page_title'] = "Lista de Equipos"
        context['active_tournament'] = check_tournament_active()
        return context


class TeamCreateView(CreateView):
    model = Team
    template_name = "administration/specific/teams/create.html"
    form_class = TeamCreateForm
    success_url = reverse_lazy('administration:teams')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Equipo"
        context['form_title'] = "Agregar nuevo equipo"
        context['header_page_title'] = "Nuevo Equipo"
        context['active_tournament'] = check_tournament_active()
        return context


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamUpdateForm
    template_name = "administration/specific/teams/update.html"
    success_url = reverse_lazy('administration:teams')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar equipo"
        context['form_title'] = "Modificar equipo"
        context['header_page_title'] = "Modificar Equipo"
        context['active_tournament'] = check_tournament_active()
        return context


class TeamDeleteView(DeleteView):
    model = Team
    template_name = "administration/specific/teams/delete.html"
    success_url = reverse_lazy('administration:teams')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Equipo"
        context['header_page_title'] = "Eliminar Equipo"
        context['active_tournament'] = check_tournament_active()
        return context


class TeamDetailView(TemplateView):
    template_name = "administration/specific/teams/admin/detail.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipo'] = Team.objects.get(pk=self.kwargs['pk'])
        context['jugadores'] = Player.objects.filter(team=Team.objects.get(pk=self.kwargs['pk']))
        context['active_tournament'] = check_tournament_active()
        return context


class TeamCreateNextView(CreateView):
    model = Team
    template_name = "administration/specific/teams/create_next.html"
    form_class = TeamCreateNextForm
    success_url = reverse_lazy('administration:teams')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.delegated = Administrator.objects.get(pk=self.kwargs['pk'])
            team.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors'] = form.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Equipo"
        context['form_title'] = "Agregar nuevo equipo"
        context['header_page_title'] = "Nuevo Equipo"
        context['active_tournament'] = check_tournament_active()
        return context


