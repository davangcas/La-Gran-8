import datetime

from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from apps.administration.models.users import Administrator
from apps.administration.forms.administrator import AdministratorForm, UserFormNew
from apps.administration.forms.delegates import DelegateForm, DelegateUserForm
from apps.administration.decorators import user_validator
from apps.team.models.team import Team
from apps.administration.services import check_tournament_active


class DelegateListView(ListView):
    model = Administrator
    template_name = "administration/specific/delegates/list.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delegados"
        context['table_id'] = "delegados"
        context['table_title'] = "Delegados"
        context['object_list'] = Administrator.objects.filter(role="Delegado")
        context['header_page_title'] = "Lista de delegados"
        context['active_tournament'] = check_tournament_active()
        return context


class DelegateCreateView(CreateView):
    template_name = "administration/specific/delegates/create.html"
    model = User
    form_class = UserCreationForm
    second_form_class = AdministratorForm
    thirth_form_class = UserFormNew
    success_url = reverse_lazy('administration:delegates')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        last_delegated = Administrator.objects.filter(role="Delegado").last()
        success_url = reverse_lazy('administration:teams_next_new', kwargs={'pk':last_delegated.id})
        return success_url

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
            administrator.role = 'Delegado'
            administrator.status = True
            administrator.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors1'] = form.errors
            context['errors2'] = form2.errors
            context['errors3'] = form3.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thirth_form_class(self.request.GET)
        context['title'] = "Nuevo delegado"
        context['form_title'] = "Agregar nuevo delegado"
        context['header_page_title'] = "Nuevo Delegado"
        context['active_tournament'] = check_tournament_active()
        return context


class DelegateDeleteView(DeleteView):
    model = Administrator
    template_name = "administration/specific/delegates/delete.html"
    success_url = reverse_lazy('administration:delegates')

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        user = User.objects.get(pk=self.object.user.id)
        self.object.delete()
        user.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Delegado"
        context['header_page_title'] = "Eliminar Delegado"
        context['active_tournament'] = check_tournament_active()
        return context


class DelegateUpdateView(UpdateView):
    model = Administrator
    second_model = User
    template_name = "administration/specific/delegates/update.html"
    success_url = reverse_lazy('administration:delegates')
    form_class = DelegateForm
    second_form_class = DelegateUserForm
    
    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_admin = self.kwargs['pk']
        admin = self.model.objects.get(pk=id_admin)
        usuario = self.second_model.objects.get(pk=admin.user_id)
        form = self.form_class(request.POST, instance=admin)
        form2 = self.second_form_class(request.POST, instance=usuario)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors1'] = form.errors
            context['errors2'] = form2.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        admin = self.model.objects.get(pk=self.kwargs['pk'])
        usuario = self.second_model.objects.get(pk=admin.user_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=usuario)
        context['id'] = self.kwargs['pk']
        context['title'] = "Editar Delegado"
        context['form_title'] = "Modificar Delegado"
        context['header_page_title'] = "Editar Delegado"
        context['active_tournament'] = check_tournament_active()
        return context


