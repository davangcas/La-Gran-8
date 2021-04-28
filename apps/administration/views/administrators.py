from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from apps.administration.models.users import Administrator
from apps.administration.forms.administrator import AdministratorForm

class AdministratorListView(ListView):
    model = Administrator
    template_name = "administration/specific/administrator/list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Administradores"
        return context

class AdministratorCreateView(CreateView):
    template_name = "administration/specific/administrator/create.html"
    model = User
    form_class = AdministratorForm
    success_url = reverse_lazy('administration:administrators')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo administrador"
        return context