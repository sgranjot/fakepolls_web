from django.urls import path

from . import views

app_name = "fake_elecciones"
urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path("csv/", views.IndexViewCSV.as_view(), name="index"),
    path('create_graphic/', views.CreateGraphic.as_view(), name='create_graphic'),
]