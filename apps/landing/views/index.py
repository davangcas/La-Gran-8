from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from apps.landing.decorators import data_validation, match_validation
from apps.team.models.match import Match
from apps.team.models.tournament import Scorers, Tournament

class IndexView(TemplateView):
    template_name = "landing/specific/index.html"

    @method_decorator(data_validation)
    @method_decorator(match_validation)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "La Gran 8 - Inicio"
        context['banner_played'] = Match.objects.filter(played=True).order_by('date_of_match', 'hour_of_match')[:3]
        context['banner_unplayed'] = Match.objects.filter(played=False).order_by('date_of_match', 'hour_of_match')[:3]
        context['last_matchs'] = Match.objects.filter(played=True).order_by('date_of_match', 'hour_of_match')[:5]
        context['next_match'] = Match.objects.filter(played=False).order_by('date_of_match', 'hour_of_match').first()
        return context


class ProximamenteView(TemplateView):
    template_name = "landing/specific/proximamente.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Proximamente"
        return context
