from django.forms import ModelForm

from apps.administration.models.noticias import Noticia

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'title',
            'body',
            'image',
        ]