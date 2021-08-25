from apps.team.models.team import Team
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.player import Player
from apps.administration.forms.player import PlayerForm, PlayerEditForm, PlayerCreateDelegatedForm
from apps.administration.decorators import user_validator
from apps.administration.services import check_players_capacity


class PlayerCreateView(CreateView):
    model = Player
    template_name = "administration/specific/player/create.html"
    form_class = PlayerForm
    success_url = reverse_lazy('administration:players')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
                check_players_capacity()
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
        context['title'] = "Nuevo Jugador"
        context['form_title'] = "Agregar jugador"
        context['header_page_title'] = "Nuevo Jugador"
        return context

class PlayerListView(ListView):
    model = Player
    template_name = "administration/specific/player/list.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['title'] = "Jugadores"
        context['table_id'] = "jugadores"
        context['table_title'] = "Jugadores"
        context['header_page_title'] = "Lista de Jugadores"
        return context

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "administration/specific/player/delete.html"
    success_url = reverse_lazy('administration:players')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Jugador"
        context['header_page_title'] = "Eliminar Jugador"
        return context

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerEditForm
    template_name = "administration/specific/player/update.html"
    success_url = reverse_lazy('administration:players')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Jugador"
        context['form_title'] = "Modificar Jugador"
        context['header_page_title'] = "Editar Jugador"
        return context

class PlayerDelegateCreateView(CreateView):
    model = Player
    template_name = "administration/specific/player/create_delegate.html"
    form_class = PlayerCreateDelegatedForm
    success_url = reverse_lazy('administration:dplayers')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                team = Team.objects.filter(delegated=request.user.administrator).first()
                player = form.save(commit=False)
                player.team = team
                player.save()
                check_players_capacity()
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
        context['title'] = "Nuevo Jugador"
        context['form_title'] = "Agregar jugador"
        context['header_page_title'] = "Nuevo Jugador"
        return context

class PlayerDelegateListView(ListView):
    model = Player
    template_name = "administration/specific/player/list_delegate.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = Player.objects.filter(team=Team.objects.filter(delegated=self.request.user.administrator).first())
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['title'] = "Jugadores"
        context['table_id'] = "jugadores"
        context['table_title'] = "Jugadores"
        context['header_page_title'] = "Lista de Jugadores"
        return context

class PlayerDelegateDeleteView(DeleteView):
    model = Player
    template_name = "administration/specific/player/delete_delegate.html"
    success_url = reverse_lazy('administration:dplayers')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Jugador"
        context['header_page_title'] = "Eliminar Jugador"
        return context

class PlayerDelegateUpdateView(UpdateView):
    model = Player
    form_class = PlayerEditForm
    template_name = "administration/specific/player/update_delegate.html"
    success_url = reverse_lazy('administration:dplayers')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Jugador"
        context['form_title'] = "Modificar Jugador"
        context['header_page_title'] = "Editar Jugador"
        return context
