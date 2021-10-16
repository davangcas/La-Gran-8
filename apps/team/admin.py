from django.contrib import admin

from apps.team.models.match import *
from apps.team.models.player import *
from apps.team.models.team import *
from apps.team.models.tournament import *


admin.site.register(Match)
admin.site.register(DateOfMatch)
admin.site.register(FieldMatch)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(League)
admin.site.register(LeagueTable)
admin.site.register(PlayOff)
admin.site.register(Scorers)
admin.site.register(Cautions)
admin.site.register(DaysOfWeek)
admin.site.register(ConfigTournament)
admin.site.register(GroupAndPlayOff)
admin.site.register(Group)
admin.site.register(GroupTable)

