from django.db import models
from django.utils.translation import gettext_lazy as _


class League(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

class Sport(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
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

    id = models.AutoField(primary_key=True)
    name = models.CharField(choices=RegionEnum.choices, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

class OddsSource(models.Model):
    class Meta:
        app_label = 'oddstracker'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
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

    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, related_name="odds", on_delete=models.CASCADE)
    time_recorded = models.DateTimeField(auto_now=False)
    source = models.ForeignKey(OddsSource, models.CASCADE)
    mkt_type = models.CharField(choices=MktTypeEnum.choices, max_length=100)
    team_a_value = models.IntegerField()
    team_b_value = models.IntegerField()
    addl_value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        ret = self.__dict__
        ret.pop('_state')
        return str(ret)
