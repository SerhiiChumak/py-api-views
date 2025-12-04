from django.urls import path, include
from cinema.views import MovieViewSet, GenreViewSet, ActorViewSet, CinemaHallViewSet
from rest_framework import routers

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
