from django.views.generic import TemplateView

from apps.team.models.tournament import Tournament

class ClubStatsView(TemplateView):
    template_name = "landing/specific/club_stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Estadisticas del club"
        context['campeonatos'] = Tournament.objects.filter(status=True)
        return context