from django.views.generic import CreateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.team.models.team import Team

class TeamListView(ListView):
    model = Team
    template_name = "administration/specific/teams/list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Equipos"
        context['table_id'] = "teams"
        context['table_title'] = "Equipos"
        context['header_page_title'] = "Lista de Equipos"
        return context