from django.views.generic import TemplateView

class ProximosPartidosView(TemplateView):
    template_name = "landing/specific/proximos_partidos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Proximos Partidos"
        return context