from django.urls import path
from .views import PlayerListView, PlayerDetailView

urlpatterns = [
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:player_id>/', PlayerDetailView.as_view(), name='player-detail'),
]