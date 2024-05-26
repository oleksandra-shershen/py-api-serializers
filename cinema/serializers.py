from rest_framework import serializers
from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ['id', 'name', 'rows', 'seats_in_row', 'capacity']