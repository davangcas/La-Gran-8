from django.db import models
from django.contrib.auth.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    status = models.BooleanField(verbose_name="Estado")
    role = models.CharField(verbose_name="Rol", max_length=30)
    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

class Sender(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Emisor"
        verbose_name_plural = "Emisores"

class Receiver(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Receptor"
        verbose_name_plural = "Receptores"

class Message(models.Model):

    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Desarrollo", max_length=300)
    date_sended = models.DateTimeField(verbose_name="Fecha de envío", auto_now_add=True)
    status = models.BooleanField(verbose_name="Mensaje enviado")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

class Notification(models.Model):
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
