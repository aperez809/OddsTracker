from typing import Dict
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class League(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=100)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

class Sport(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=100)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)


class Region(models.Model):
    class Meta:
        app_label = 'oddstracker'

    class RegionEnum(models.TextChoices):
        US = 'US', _('us')
        UK = 'UK', _('uk')
        AU = 'AU', _('au')
        EU = 'EU', _('eu')

    id: int = models.AutoField(primary_key=True)
    name: RegionEnum = models.CharField(choices=RegionEnum.choices, max_length=100)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self):
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

class OddsSource(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=100)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

class Game(models.Model):
    class Meta:
        app_label = 'oddstracker'
    # Represents a sports game to be played

    id: int = models.AutoField(primary_key=True)
    team_a: str = models.CharField(max_length=100)
    team_b: str = models.CharField(max_length=100)
    game_time: datetime = models.DateTimeField(auto_now=False)
    sport: Sport = models.ForeignKey(Sport, models.CASCADE)
    region: Region = models.ForeignKey(Region, models.CASCADE)
    league: League = models.ForeignKey(League, models.CASCADE)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)


class Odds(models.Model):
    class Meta:
        app_label = 'oddstracker'

    class MktTypeEnum(models.TextChoices):
        H2H = 'H2H', _('h2h')
        H2H_LAY = 'H2H_LAY', _('h2h_lay')
        SPREAD = 'SPREAD', _('spread')
        TOTALS = 'TOTALS', _('totals')

    id: int = models.AutoField(primary_key=True)
    game: Game = models.ForeignKey(Game, related_name="odds", on_delete=models.CASCADE)
    time_recorded: datetime = models.DateTimeField(auto_now=False)
    source: datetime = models.ForeignKey(OddsSource, related_name="source", on_delete=models.CASCADE)
    mkt_type: MktTypeEnum = models.CharField(choices=MktTypeEnum.choices, max_length=100)
    team_a_value: int = models.IntegerField()
    team_b_value: int = models.IntegerField()
    addl_value: int = models.IntegerField(blank=True, null=True)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)
