from django.db import models
from django.contrib.auth.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    status = models.BooleanField(verbose_name="Estado")
    role = models.CharField(verbose_name="Rol", max_length=30)
    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

