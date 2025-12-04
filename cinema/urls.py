from django.urls import path, include
from cinema.views import MovieViewSet
from rest_framework import routers

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

# movie_list = MovieViewSet.as_view(actions={"get": "list", "post": "create"})
#
# movie_detail = MovieViewSet.as_view(
#     actions={
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy",
#     }
# )
#
# urlpatterns = [
#     path("movies/", movie_list, name="movie-list"),
#     path("movies/<int:pk>/", movie_detail, name="movie-detail"),
# ]
