from django.views.generic import TemplateView

from apps.administration.models.noticias import Noticia

class NovedadesView(TemplateView):
    template_name = "landing/specific/novedades.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novedades"
        context['novedades'] = Noticia.objects.all().order_by('-id')[:7]
        context['ultima'] = Noticia.objects.last().id
        return context

class NovedadesDetailView(TemplateView):
    template_name = "landing/specific/novedades_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Novedades"
        context['novedad'] = Noticia.objects.get(pk=self.kwargs['pk'])
        context['ultimo_id'] = Noticia.objects.last().id
        return context

