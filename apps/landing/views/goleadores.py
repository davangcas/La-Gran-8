from django.views.generic import TemplateView

class GoleadoresView(TemplateView):
    template_name = "landing/specific/goleadores.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Goleadores"
        return context