from django.db import models
from django.utils.translation import gettext_lazy as _

class League(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Sport(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Region(models.Model):
    class Meta:
        app_label = 'oddstracker'

    class RegionEnum(models.TextChoices):
        US = 'US', _('us')
        UK = 'UK', _('uk')
        AU = 'AU', _('au')
        EU = 'EU', _('eu')

    id = models.AutoField(primary_key=True)
    name = models.CharField(choices=RegionEnum.choices, max_length=100)

class OddsSource(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Game(models.Model):
    class Meta:
        app_label = 'oddstracker'
    # Represents a sports game to be played

    id = models.AutoField(primary_key=True)
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    game_time = models.DateTimeField(auto_now=False)
    sport = models.ForeignKey(Sport, models.CASCADE)
    region = models.ForeignKey(Region, models.CASCADE)
    league = models.ForeignKey(League, models.CASCADE)


class Odds(models.Model):
    class Meta:
        app_label = 'oddstracker'

    class MktTypeEnum(models.TextChoices):
        H2H = 'H2H', _('h2h')
        SPREAD = 'SPREAD', _('spread')
        TOTALS = 'TOTALS', _('totals')

    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, models.CASCADE)
    time_recorded = models.DateTimeField(auto_now=False)
    source = models.ForeignKey(OddsSource, models.CASCADE)
    mkt_type = models.CharField(choices=MktTypeEnum.choices, max_length=100)
    team_a_value = models.IntegerField
    team_b_value = models.IntegerField
    addl_value = models.IntegerField(blank=True, null=True)