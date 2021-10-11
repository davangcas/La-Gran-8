from django.views.generic import TemplateView

from apps.team.models.tournament import Tournament

class StandigsView(TemplateView):
    template_name = "landing/specific/standigs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Posiciones"
        context['campeonatos'] = Tournament.objects.filter(status=True)
        return context