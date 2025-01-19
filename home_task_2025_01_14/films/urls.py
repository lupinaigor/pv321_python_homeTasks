from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_list, name='films_list'),
    path('film/<int:id>/', views.film_detail, name='film_detail'),
    path('characters/', views.characters_list, name='characters_list'),
    path('character/<int:id>/', views.character_detail, name='character_detail'),
    path('planets/', views.planets_list, name='planets_list'),
    path('planet/<int:id>/', views.planet_detail, name='planet_detail'),
]