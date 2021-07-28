from django.contrib import admin

from apps.administration.models.users import (
    Administrator, 
    Message,
    )
from apps.team.models.team import (
    Team,
)

# Register your models here.

admin.site.register(Administrator)
admin.site.register(Team)
