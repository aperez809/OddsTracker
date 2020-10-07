from .serializers import *
from rest_framework import generics



# ----------------Game Views-------------------- #
class GameList(generics.ListCreateAPIView):
    """
    View for listing or creating Games.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single Game instance.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameOddsList(generics.ListCreateAPIView):
    """
    View for listing or creating Games and Odds.
    """
    queryset = Game.objects.all()
    serializer_class = GameOddsSerializer

class GameOddsDetail(generics.RetrieveAPIView):
    """
    View for returning a single Game instance with its associated Odds data.
    """
    queryset = Game.objects.all()
    serializer_class = GameOddsSerializer


# ----------------Sport Views-------------------- #
class SportList(generics.ListCreateAPIView):
    """
    View for listing or creating Sports.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single Sport instance.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


# ----------------Region Views-------------------- #
class RegionList(generics.ListCreateAPIView):
    """
    View for listing or creating Regions.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single Region instance.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


# ----------------League Views-------------------- #
class LeagueList(generics.ListCreateAPIView):
    """
    View for listing or creating Leagues.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single League instance.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

# ----------------OddsSources Views-------------------- #
class OddsSourceList(generics.ListCreateAPIView):
    """
    View for listing or creating OddsSources.
    """
    queryset = OddsSource.objects.all()
    serializer_class = OddsSourceSerializer

class OddsSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single OddsSource instance.
    """
    queryset = OddsSource.objects.all()
    serializer_class = OddsSourceSerializer

# ----------------Odds Views-------------------- #
class OddsList(generics.ListCreateAPIView):
    """
    View for listing or creating Odds.
    """
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer

class OddsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for finding, updating, or deleting a single Odds instance.
    """
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer

