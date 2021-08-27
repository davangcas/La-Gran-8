from django.views.generic import (
    CreateView, 
    ListView, 
    DeleteView, 
    UpdateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import (
    render, 
    redirect,
)

from apps.administration.models.noticias import Noticia
from apps.administration.forms.noticias import NoticiaForm
from apps.administration.decorators import user_validator
from apps.administration.services import check_tournament_active


class NoticiasListView(ListView):
    model = Noticia
    template_name = "administration/specific/noticias/list.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Noticias"
        context['table_id'] = "noticias"
        context['table_title'] = "Noticias"
        context['header_page_title'] = "Lista de Noticias"
        context['active_tournament'] = check_tournament_active()
        return context


class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "administration/specific/noticias/create.html"
    success_url = reverse_lazy('administration:noticias')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Noticia"
        context['header_page_title'] = "Nueva Noticia"
        context['form_title'] = "Agregar novedad"
        context['active_tournament'] = check_tournament_active()
        return context


class NoticiaDeleteView(DeleteView):
    model = Noticia
    template_name = "administration/specific/noticias/delete.html"
    success_url = reverse_lazy('administration:noticias')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Noticia"
        context['header_page_title'] = "Eliminar Noticia"
        context['active_tournament'] = check_tournament_active()
        return context


