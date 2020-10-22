from logging import log
from .serializers import *
from rest_framework import generics
import json
from pprint import pprint
from rest_framework import status
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)




# ----------------Game Views-------------------- #
class GameList(generics.ListCreateAPIView):
    """
    View for listing or creating Games.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        """
        Returns standard QuerySet unless `upcoming` flag is specified.
        If specified, only returns games happening in the next 7 days.
        """
        qs = super().get_queryset()
        only_upcoming = str(self.request.query_params.get('upcoming')).lower()
        if only_upcoming in ['true', '1']:
            start_date = datetime.today()
            # Captures games taking place today and 7 days from now
            # Hours set to 24 - hour of start_date to capture any missing data from 7th day 
            end_date = start_date + timedelta(days=6, hours=24-start_date.hour)
            return qs.filter(game_time__range=[start_date, end_date])
        return qs

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

    def create(self, request, *args, **kwargs):
        fmt_req = request.data

        # Using throwaway variable because `get_or_create()` returns a 2-tuple
        # where the second value is where or not the object was created
        sport, _ = Sport.objects.get_or_create(name=fmt_req['sport'])
        region, _ = Region.objects.get_or_create(name=fmt_req['region'])
        league, _ = League.objects.get_or_create(name=fmt_req['league'])

        fmt_time = datetime.strptime(fmt_req['game_time'], r"%Y-%m-%d %H:%M:%S")
        fmt_time = timezone.make_aware(fmt_time, timezone.utc)

        game, _ = Game.objects.get_or_create(
            team_a=fmt_req['team_a'],
            team_b=fmt_req['team_b'],
            game_time=fmt_req['game_time'],
            sport=sport,
            region=region,
            league=league
        )
        game.save()

        self.add_odds_to_set(game, fmt_req['odds'])

        return JsonResponse({}, status=201)

    def add_odds_to_set(self, game, odds):
        for elem in odds:
            fmt_time = datetime.strptime(elem['time_recorded'], r"%Y-%m-%d %H:%M:%S")
            fmt_time = timezone.make_aware(fmt_time, timezone.utc)

            source, _ = OddsSource.objects.get_or_create(name=elem['source'])

            odds, _ = Odds.objects.get_or_create(
                game=game,
                team_a_value=elem['team_a_value'],
                team_b_value=elem['team_b_value'],
                addl_value=elem['addl_value'],
                time_recorded=fmt_time,
                source=source,
                mkt_type=elem['mkt_type']
            )

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

