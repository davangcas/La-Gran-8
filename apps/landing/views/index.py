from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "landing/specific/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "La Gran 8 - Inicio"
        return context