import datetime

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from apps.administration.models.users import Administrator
from apps.team.models.team import Team
from apps.team.models.player import Player

class IndexView(TemplateView):
    template_name = "administration/specific/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.administrator.role == "Delegado":
            return redirect('administration:indexd')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Administración - Inicio"
        context["header_title"] = "Inicio - Administrador"
        context['header_page_title'] = "Bienvenido " + str(self.request.user.first_name) + " " + str(self.request.user.last_name)
        context['numero_delegados'] = Administrator.objects.filter(role="Delegado").count()
        context['equipos_habilitados'] = Team.objects.filter(active=True).count()
        context['jugadores_registrados'] = Player.objects.all().count()
        context['numero_administradores'] = Administrator.objects.filter(role="Administrador").count()
        return context

class IndexDelegateView(TemplateView):
    template_name = "administration/specific/index_delegate.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delegado - Inicio"
        context["header_title"] = "Inicio - Delegado"
        context['header_page_title'] = "Bienvenido " + str(self.request.user.first_name) + " " + str(self.request.user.last_name)
        return context