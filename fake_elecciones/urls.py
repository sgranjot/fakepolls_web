from django.urls import path

from . import views

app_name = "fake_elecciones"
urlpatterns = [
    path("", views.IndexViewCSV.as_view(), name="index"),
]