from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.administration.views.index import IndexView, IndexDelegateView
from apps.administration.views.login import LoginFormView
from apps.administration.views.administrators import AdministratorListView, AdministratorCreateView
from apps.administration.views.delegates import DelegateCreateView, DelegateListView
from apps.administration.views.teams import TeamListView

app_name = "administration"

urlpatterns = [
    path('', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='administration:login'), name="logout"),
    path('inicio/', IndexView.as_view(), name="index"),
    path('iniciod/', IndexDelegateView.as_view(), name="indexd"),
    path('admins/', AdministratorListView.as_view(), name="administrators"),
    path('admins/nuevo/', AdministratorCreateView.as_view(), name="administrators_new"),
    path('delegados/', DelegateListView.as_view(), name="delegates"),
    path('delegados/nuevo/', DelegateCreateView.as_view(), name="delegates_new"),
    path('equipos/', TeamListView.as_view(), name="teams"),
]