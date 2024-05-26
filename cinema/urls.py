from django.urls import path, include
from cinema.views import CinemaHallViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path('', include(router.urls))
]
app_name = "cinema"
