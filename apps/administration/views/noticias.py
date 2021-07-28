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

class NoticiasListView(ListView):
    model = Noticia
    template_name = "administration/specific/noticias/list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Noticias"
        context['table_id'] = "noticias"
        context['table_title'] = "Noticias"
        context['header_page_title'] = "Lista de Noticias"
        return context
