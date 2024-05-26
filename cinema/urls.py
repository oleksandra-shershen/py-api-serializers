from django.urls import path, include
from cinema.views import CinemaHallViewSet, GenreViewSet, ActorViewSet, MovieViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path('', include(router.urls))
]
app_name = "cinema"
