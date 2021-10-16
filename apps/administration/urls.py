from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.administration.views.index import (
    IndexView, 
    IndexDelegateView,
)
from apps.administration.views.login import (
    LoginFormView,
    UpdatePasswordView,
)
from apps.administration.views.administrators import (
    AdministratorListView, 
    AdministratorCreateView,
    AdministratorUpdateView,
    AdministratorDeleteView,
)
from apps.administration.views.delegates import (
    DelegateCreateView, 
    DelegateListView,
    DelegateDeleteView,
    DelegateUpdateView,
)
from apps.administration.views.teams import (
    TeamListView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    TeamDetailView,
    TeamCreateNextView,
)
from apps.administration.views.noticias import (
    NoticiasListView,
    NoticiaCreateView,
    NoticiaDeleteView,
)
from apps.administration.views.player import (
    PlayerListView,
    PlayerCreateView,
    PlayerDeleteView,
    PlayerUpdateView,
    PlayerDelegateListView,
    PlayerDelegateCreateView,
    PlayerDelegateDeleteView,
    PlayerDelegateUpdateView,
)
from apps.administration.views.tournament import (
    TorunamentCreateView,
    TournamentListView,
    TournamentDeleteView,
    TournamentLigaCreateView,
    TournamentGroupAndPlayOffView,
    TournamentDetailView,
)
from apps.administration.views.special_views import (
    activate_team,
    put_match_day_as_played,
    generate_automatic_matchs,
    change_delegate_status,
)
from apps.administration.views.day_of_match import DateOfMatchCreateView, DateOfMatchUpdateView, MatchDayDetailView
from apps.administration.views.match import MatchCreateView, MatchUpdateView, LoadMatchResultView
from apps.administration.views.config import ConfigListView, ConfigupdateView
from apps.administration.views.groups import GroupDetailView, AssignTeamToGroup

app_name = "administration"

urlpatterns = [
    # admin urls
    path('', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='administration:login'), name="logout"),
    path('cambiar_contraseña/', UpdatePasswordView.as_view(), name="change_password"),
    path('inicio/', IndexView.as_view(), name="index"),
    path('config/', ConfigListView.as_view(), name="general_config"),
    path('config/actualizar/<int:pk>/', ConfigupdateView.as_view(), name="general_config_edit"),
    path('admins/', AdministratorListView.as_view(), name="administrators"),
    path('admins/nuevo/', AdministratorCreateView.as_view(), name="administrators_new"),
    path('admins/editar/<int:pk>/', AdministratorUpdateView.as_view(), name="administrators_edit"),
    path('admins/eliminar/<int:pk>/', AdministratorDeleteView.as_view(), name="administrators_delete"),
    path('delegados/', DelegateListView.as_view(), name="delegates"),
    path('delegados/nuevo/', DelegateCreateView.as_view(), name="delegates_new"),
    path('delegados/eliminar/<int:pk>/', DelegateDeleteView.as_view(), name="delegates_delete"),
    path('delegados/editar/<int:pk>/', DelegateUpdateView.as_view(), name="delegates_edit"),
    path('delegados/activar/<int:pk>/', change_delegate_status, name="change_delegate_status"),
    path('equipos/', TeamListView.as_view(), name="teams"),
    path('equipos/nuevo/', TeamCreateView.as_view(), name="teams_new"),
    path('equipos/siguiente/nuevo/<int:pk>/', TeamCreateNextView.as_view(), name="teams_next_new"),
    path('equipos/editar/<int:pk>/', TeamUpdateView.as_view(), name="teams_edit"),
    path('equipo/eliminar/<int:pk>/', TeamDeleteView.as_view(), name="teams_delete"),
    path('equipo/detalle/<int:pk>/', TeamDetailView.as_view(), name="team_detail"),
    path('noticias/', NoticiasListView.as_view(), name="noticias"),
    path('noticias/nueva/', NoticiaCreateView.as_view(), name="noticias_new"),
    path('noticias/eliminar/<int:pk>/', NoticiaDeleteView.as_view(), name="noticias_delete"),
    path('jugadores/', PlayerListView.as_view(), name="players"),
    path('jugadores/nuevo/', PlayerCreateView.as_view(), name="players_new"),
    path('jugadores/eliminar/<int:pk>/', PlayerDeleteView.as_view(), name="players_delete"),
    path('jugadores/editar/<int:pk>/', PlayerUpdateView.as_view(), name="players_edit"),
    path('torneos/', TournamentListView.as_view(), name="tournaments"),
    path('torneo/nuevo/', TorunamentCreateView.as_view(), name="tournament_new"),
    path('torneo/eliminar/<int:pk>/', TournamentDeleteView.as_view(), name="tournament_delete"),
    path('torneo/nuevo/liga/<int:pk>/', TournamentLigaCreateView.as_view(), name="tournament_new_liga"),
    path('torneo/nuevo/grupos/<int:pk>/', TournamentGroupAndPlayOffView.as_view(), name="tournament_new_groups"),
    path('torneo/detalle/<int:pk>/', TournamentDetailView.as_view(), name="tournament_detail"),
    path('torneo/crear_fecha/<int:pk>/', DateOfMatchCreateView.as_view(), name="create_match_day"),
    path('torneo/editar_fecha/<int:pk>/', DateOfMatchUpdateView.as_view(), name="match_day_edit"),
    path('torneo/fecha/detalle/<int:pk>/', MatchDayDetailView.as_view(), name="match_day_detail"),
    path('torneo/crear/partido/<int:pk>/', MatchCreateView.as_view(), name="create_match"),
    path('torneto/moficar/partido/<int:pk>/<int:date_id>/', MatchUpdateView.as_view(), name="update_match"),
    path('torneto/cargar/partido/<int:pk>/<int:date_id>/', LoadMatchResultView.as_view(), name="load_result"),
    path('torneo/grupo/detalle/<int:pk>/', GroupDetailView.as_view(), name="group_detail_tournament"),
    path('torneo/grupo/agregar_equipos/<int:pk>/', AssignTeamToGroup.as_view(), name="assign_team_to_group"),
    # Views whithout a template
    path('equipos/activar/<int:pk>/', activate_team, name="activar_equipo"),
    path('fecha/activar/<int:pk>/', put_match_day_as_played, name="fecha_jugada"),
    path('fechas/generar/automatica/<int:pk>/', generate_automatic_matchs, name="automatic_generate"),
    # delegates urls
    path('inicio/mi_equipo/', IndexDelegateView.as_view(), name="indexd"),
    path('mi_equipo/judadores/', PlayerDelegateListView.as_view(), name="dplayers"),
    path('mi_equipo/jugadores/nuevo/', PlayerDelegateCreateView.as_view(), name="dplayer_new"),
    path('mi_equipo/jugadores/eliminar/<int:pk>/', PlayerDelegateDeleteView.as_view(), name="dplayer_delete"),
    path('mi_equipo/jugadores/editar/<int:pk>/', PlayerDelegateUpdateView.as_view(), name="dplayer_edit"),
]