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
from apps.administration.forms.player import PlayerForm, PlayerEditForm
from apps.administration.decorators import user_validator


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
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
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
