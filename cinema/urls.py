from django.urls import path, include
from cinema.views import CinemaHallViewSet, GenreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
app_name = "cinema"
