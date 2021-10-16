from django.contrib import admin

from apps.administration.models.users import *
from apps.administration.models.noticias import *
from apps.administration.models.config import *

admin.site.register(Administrator)
admin.site.register(Noticia)
admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(GeneralConfig)

