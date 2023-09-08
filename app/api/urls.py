from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("teams/<str:id>/hitters", views.team_hitters, name="team_hitters"),
    path("teams/<str:id>/pitchers", views.team_pitchers, name="team_pitchers"),
    path("players/hitters/<str:id>", views.player, name="player"),
    path("players/pitchers/<str:id>", views.player_pitcher, name="player_pitcher"),
    path("leaderboards/", views.leaderboard, name="leaderboard",),
    path("players/<str:id>", views.player, name="player"),
]