from rest_framework import viewsets
from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import CinemaHallSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
