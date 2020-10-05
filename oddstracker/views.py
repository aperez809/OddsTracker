from django.shortcuts import render
from oddstracker.models import Game
from .serializers import *
from rest_framework import generics


# ----------------Game Views-------------------- #
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer



# ----------------Sport Views-------------------- #
class SportList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = SportSerializer

class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = SportSerializer



# ----------------Region Views-------------------- #
class RegionList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = RegionSerializer



# ----------------League Views-------------------- #
class LeagueList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = LeagueSerializer


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = LeagueSerializer