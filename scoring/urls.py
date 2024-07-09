from django.urls import path

from . import views

urlpatterns = [
    path(
        "leaderboards/global/",
        views.global_leaderboard,
        name="global-leaderboard",
    ),
    path(
        "leaderboards/project/<int:project_id>/",
        views.project_leaderboard,
        name="project-leaderboard",
    ),
    path(
        "leaderboards/medals/user/<int:user_id>/",
        views.user_medals,
        name="user-medals",
    ),
]
