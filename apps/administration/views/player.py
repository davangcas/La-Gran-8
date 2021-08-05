from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.team.models.player import Player
from apps.administration.forms.player import PlayerForm

class PlayerCreateView(CreateView):
    model = Player
    template_name = "administration/specific/player/create.html"
    form_class = PlayerForm
    success_url = reverse_lazy()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect(self.get_success_url())
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Jugador"
        context['form_title'] = "Agregar jugador"
        context['header_page_title'] = "Nuevo Jugador"
        return context

class PlayerListView(ListView):
    model = Player
    template_name = "administration/specific/player/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['title'] = "Jugadores"
        context['table_id'] = "jugadores"
        context['table_title'] = "Jugadores"
        context['header_page_title'] = "Lista de Jugadores"
        return context

