from django.views.generic import TemplateView

class ContactoView(TemplateView):
    template_name = "landing/specific/contacto.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Contacto"
        return context