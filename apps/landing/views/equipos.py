from django.views.generic import TemplateView

from apps.team.models.team import Team

class EquiposView(TemplateView):
    template_name = "landing/specific/equipos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Equipos"
        context['equipos'] = Team.objects.all().order_by('-played', '-win', 'lost', '-goals')
        return context

class EquipoView(TemplateView):
    
    template_name = "landing/specific/equipo_detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Team.objects.get(pk=self.kwargs['pk']).name
        return context