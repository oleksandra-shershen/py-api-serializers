from django.urls import path, include
from cinema.views import CinemaHallViewSet, GenreViewSet, ActorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
app_name = "cinema"
