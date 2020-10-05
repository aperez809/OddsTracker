from rest_framework import serializers
from oddstracker.models import *

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name']


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class OddsSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OddsSource
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'team_a', 'team_b', 'game_time', 'sport', 'region', 'league']

class OddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odds
        fields = ['id', 'game', 'time_recorded', 'source', 'mkt_type', 'team_a_value', 'team_b_value', 'addl_value']