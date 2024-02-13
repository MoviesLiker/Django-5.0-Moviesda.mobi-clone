from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/<int:id>", views.list, name="list"),
    path("movie/<int:id>", views.movie, name="movie"),
    path("video/<int:id>", views.video, name="video"),
    path("download/<int:id>", views.download, name="download"),
]
