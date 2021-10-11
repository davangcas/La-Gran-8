from django.views.generic import TemplateView

from apps.team.models.tournament import Tournament

class FixtureView(TemplateView):
    template_name = "landing/specific/fixture.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Fixture"
        context['campeonatos'] = Tournament.objects.filter(status=True)
        return context