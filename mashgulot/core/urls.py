from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name='home'),
    path("comp/", views.computers, name='comp'),
    path("games/", views.games, name='games')
]




