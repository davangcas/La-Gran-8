from django.views.generic import TemplateView

class ClubStatsView(TemplateView):
    template_name = "landing/specific/club_stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Estadisticas del club"
        return context