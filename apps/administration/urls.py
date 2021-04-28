from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.administration.views.index import IndexView
from apps.administration.views.login import LoginFormView
from apps.administration.views.administrators import AdministratorListView, AdministratorCreateView

app_name = "administration"

urlpatterns = [
    path('', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='administration:login'), name="logout"),
    path('inicio/', IndexView.as_view(), name="index"),
    path('admins/', AdministratorListView.as_view(), name="administrators"),
    path('admins/nuevo/', AdministratorCreateView.as_view(), name="administrators_new"),
]