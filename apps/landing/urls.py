from django.urls import path

from apps.landing.views.index import IndexView
from apps.landing.views.standings import StandigsView
from apps.landing.views.club_stats import ClubStatsView

app_name = "landing"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('posiciones/', StandigsView.as_view(), name="standings"),
    path('estadisticas_del_equipo/', ClubStatsView.as_view(), name="club_stats"),
]