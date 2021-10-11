from django.views.generic import TemplateView

from apps.administration.models.noticias import Noticia
from apps.team.models.tournament import Tournament

class NovedadesView(TemplateView):
    template_name = "landing/specific/novedades.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not Noticia.objects.all():
            new = Noticia.objects.create(
                title="Página Web habilitada!",
                body="Les damos la bienvenida a la página oficial de La Gran 8. En este sitio van a ver las novedades, y todo lo relacionado al torneo más apacionante de La Rioja!"
            )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novedades"
        context['novedades'] = Noticia.objects.all().order_by('-id')[:7]
        context['ultima'] = Noticia.objects.last().id
        context['campeonatos'] = Tournament.objects.filter(status=True)
        return context

class NovedadesDetailView(TemplateView):
    template_name = "landing/specific/novedades_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novedades"
        context['novedad'] = Noticia.objects.get(pk=self.kwargs['pk'])
        context['ultimo_id'] = Noticia.objects.last().id
        context['campeonatos'] = Tournament.objects.filter(status=True)
        return context

