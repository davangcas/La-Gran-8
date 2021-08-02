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
)

from apps.administration.views.noticias import (
    NoticiasListView,
    NoticiaCreateView,
    NoticiaDeleteView,
)

app_name = "administration"

urlpatterns = [
    path('', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='administration:login'), name="logout"),
    path('cambiar_contraseña/', UpdatePasswordView.as_view(), name="change_password"),
    path('inicio/', IndexView.as_view(), name="index"),
    path('iniciod/', IndexDelegateView.as_view(), name="indexd"),
    path('admins/', AdministratorListView.as_view(), name="administrators"),
    path('admins/nuevo/', AdministratorCreateView.as_view(), name="administrators_new"),
    path('admins/editar/<int:pk>/', AdministratorUpdateView.as_view(), name="administrators_edit"),
    path('admins/eliminar/<int:pk>/', AdministratorDeleteView.as_view(), name="administrators_delete"),
    path('delegados/', DelegateListView.as_view(), name="delegates"),
    path('delegados/nuevo/', DelegateCreateView.as_view(), name="delegates_new"),
    path('delegados/eliminar/<int:pk>/', DelegateDeleteView.as_view(), name="delegates_delete"),
    path('delegados/editar/<int:pk>/', DelegateUpdateView.as_view(), name="delegates_edit"),
    path('equipos/', TeamListView.as_view(), name="teams"),
    path('equipos/nuevo/', TeamCreateView.as_view(), name="teams_new"),
    path('noticias/', NoticiasListView.as_view(), name="noticias"),
    path('noticias/nueva/', NoticiaCreateView.as_view(), name="noticias_new"),
    path('noticias/eliminar/<int:pk>/', NoticiaDeleteView.as_view(), name="noticias_delete")
]