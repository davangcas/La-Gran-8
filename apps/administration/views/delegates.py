from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from apps.administration.models.users import Administrator
from apps.administration.forms.administrator import AdministratorForm

class DelegateListView(ListView):
    model = Administrator
    template_name = "administration/specific/administrator/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Administradores"
        return context

class DelegateCreateView(CreateView):
    template_name = "administration/specific/administrator/create.html"
    model = Administrator
    form_class = AdministratorForm
    success_url = reverse_lazy('administration:administrators')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo delegado"
        return context