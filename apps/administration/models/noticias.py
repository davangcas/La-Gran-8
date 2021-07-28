from django.db import models
from django.forms import model_to_dict

class Noticia(models.Model):
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    title = models.CharField(verbose_name="Título", max_length=80)
    body = models.TextField(verbose_name="Cuerpo", max_length=500)
    image = models.ImageField(verbose_name="Imágen", upload_to="noticias/%y/%m/", default="noticias\default\Logo Fondo Gris (1).jpeg", blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
