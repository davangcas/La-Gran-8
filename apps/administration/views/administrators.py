import datetime

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

from apps.administration.models.users import Administrator
from apps.administration.forms.administrator import (
    AdministratorForm, 
    UserFormNew,
    )

class AdministratorListView(ListView):
    model = Administrator
    template_name = "administration/specific/administrator/list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(status=True).filter(role="Administrador")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Administradores"
        context['table_id'] = "admins"
        context['table_title'] = "Administradores"
        context['object_list'] = Administrator.objects.filter(status=True).filter(role="Administrador")
        context['header_page_title'] = "Lista de Administradores"
        return context

class AdministratorCreateView(CreateView):
    template_name = "administration/specific/administrator/create.html"
    model = User
    form_class = UserCreationForm
    second_form_class = AdministratorForm
    thirth_form_class = UserFormNew
    success_url = reverse_lazy('administration:administrators')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.thirth_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            user = form.save(commit=False)
            form3.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.is_superuser = True
            user.date_joined = datetime.datetime.now()
            user.first_name = form3.instance.first_name
            user.last_name = form3.instance.last_name
            user.save()
            administrator = form2.save(commit=False)
            administrator.user = user
            administrator.role = 'Administrador'
            administrator.status = True
            administrator.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors1'] = form.errors
            context['errors2'] = form2.errors
            context['errors3'] = form3.errors
            print(form.errors)
            print(form2.errors)
            print(form3.errors)
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thirth_form_class(self.request.GET)
        context['title'] = "Nuevo administrador"
        context['form_title'] = "Agregar nuevo administrador"
        context['header_page_title'] = "Nuevo Administrador"
        return context

class AdministratorUpdateView(UpdateView):
    model = Administrator
    template_name = "administration/specific/administrator/update.html"
    success_url = reverse_lazy('administration:administrators')
    form_class = UserCreationForm
    second_form_class = AdministratorForm
    thirth_form_class = UserFormNew

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thirth_form_class(self.request.GET)
        context['title'] = "Editar administrador"
        context['form_title'] = "Modificar administrador"
        context['header_page_title'] = "Editar Administrador"
        return context

class AdministratorDeleteView(DeleteView):
    model = Administrator
    template_name = "administration/specific/administrator/delete.html"
    success_url = reverse_lazy('administration:administrators')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        user = User.objects.get(pk=self.object.user.id)
        self.object.delete()
        user.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Administrador"
        context['header_page_title'] = "Eliminar Administrador"
        return context
