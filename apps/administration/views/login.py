from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

class LoginFormView(LoginView):
    template_name = 'administration/specific/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('administration:index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión - La Gran 8'
        return context

class UpdatePasswordView(FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = "administration/specific/change_password.html"
    success_url = reverse_lazy('administration:login')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data(**kwargs)
            context['errors'] = form.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Contraseña"
        context['form_title'] = "Modificar Contraseña"
        context['header_page_title'] = "Cambiar Contraseña"
        return context
