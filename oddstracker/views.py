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

class GameOddsDetail(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameOddsSerializer



# ----------------Sport Views-------------------- #
class SportList(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer



# ----------------Region Views-------------------- #
class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer



# ----------------League Views-------------------- #
class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

# ----------------Sources Views-------------------- #
class OddsSourceList(generics.ListCreateAPIView):
    queryset = OddsSource.objects.all()
    serializer_class = OddsSourceSerializer

class OddsSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OddsSource.objects.all()
    serializer_class = OddsSourceSerializer

# ----------------Odds Views-------------------- #
class OddsList(generics.ListCreateAPIView):
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer

class OddsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer

