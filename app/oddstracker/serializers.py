from rest_framework import serializers
from oddstracker.models import *
from rest_framework.validators import UniqueTogetherValidator


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


class OddsSerializer(serializers.ModelSerializer):
    source = OddsSourceSerializer(many=True, read_only=True)

    class Meta:
        model = Odds
        fields = ['id', 'game', 'time_recorded', 'source', 'mkt_type', 'team_a_value', 'team_b_value', 'addl_value', "source"]

class GameOddsSerializer(serializers.ModelSerializer):
    odds = OddsSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'team_a', 'team_b', 'game_time', 'sport', 'region', 'league', 'odds']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'team_a', 'team_b', 'game_time', 'sport', 'region', 'league']
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=['team_a', 'team_b', 'game_time', 'sport', 'region', 'league']
            )
        ]
