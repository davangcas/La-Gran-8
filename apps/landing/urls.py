from django.urls import path

from apps.landing.views.index import IndexView, ProximamenteView
from apps.landing.views.standings import StandigsView
from apps.landing.views.goleadores import GoleadoresView
from apps.landing.views.fixture import FixtureView
from apps.landing.views.equipos import EquiposView, EquipoView
from apps.landing.views.proximos_partidos import ProximosPartidosView
from apps.landing.views.novedades import NovedadesView, NovedadesDetailView
from apps.landing.views.contacto import ContactoView

app_name = "landing"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('posiciones/', StandigsView.as_view(), name="posiciones"),
    path('goleadores/', GoleadoresView.as_view(), name="goleadores"),
    path('fixture/', FixtureView.as_view(), name="fixture"),
    path('equipos/', EquiposView.as_view(), name="equipos"),
    path('equipo/<int:pk>/', EquipoView.as_view(), name="equipo_detalle"),
    path('proximos_partidos/', ProximosPartidosView.as_view(), name="proximos_partidos"),
    path('novedades/', NovedadesView.as_view(), name="novedades"),
    path('novedades/detalle/<int:pk>/', NovedadesDetailView.as_view(), name="novedades_detail"),
    path('contacto/', ContactoView.as_view(), name="contacto"),
    path('proximamente/', ProximamenteView.as_view(), name="proximamente"),
]