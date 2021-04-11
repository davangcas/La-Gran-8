from django.urls import path

from apps.landing.views.index import IndexView

app_name = "landing"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]