from django.views.generic import TemplateView

class StandigsView(TemplateView):
    template_name = "landing/specific/standigs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Posiciones"
        return context