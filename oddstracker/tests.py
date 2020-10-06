from collections import OrderedDict

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from oddstracker.models import Game
import json
from pprint import pprint


class GameTests(APITestCase):
    sports_data = {'name': 'Football'}
    regions_data = {'name': 'US'}
    leagues_data = {'name': 'NFL'}
    source_data_1 = {'name': 'Caesars'}
    source_data_2 = {'name': 'DraftKings'}
    now = '2020-10-05T18:37:00.744747Z'

    odds_data_1 = {'game':1, 'time_recorded':now, 'source': 1, 'mkt_type':'H2H', 'team_a_value': 150, 'team_b_value': -150}
    odds_data_2 = {'game':1, 'time_recorded':now, 'source': 2, 'mkt_type':'H2H', 'team_a_value': 150, 'team_b_value': -150}

    game_data = {
        'team_a': 'Washington Football Team',
        'team_b': 'Dallas Cowboys',
        'game_time': now,
        'sport': 1,
        'region': 1,
        'league': 1
    }

    sports_url = reverse('sports-list')
    regions_url = reverse('regions-list')
    leagues_url = reverse('leagues-list')
    sources_url = reverse('sources-list')
    odds_url = reverse('odds-list')

    def setup(self):
        """
        Create mock data in temp db to test requests
        """
        self.client.post(self.sports_url, self.sports_data, format='json')
        self.client.post(self.regions_url, self.regions_data, format='json')
        self.client.post(self.leagues_url, self.leagues_data, format='json')
        self.client.post(self.sources_url, self.source_data_1, format='json')
        self.client.post(self.sources_url, self.source_data_2, format='json')


    def test_create_game(self):
        """
        Ensure we can create a new Game object.
        """
        self.setup()
        url = reverse('games-list')
        response = self.client.post(url, data=self.game_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(Game.objects.get().team_a, 'Washington Football Team')

    def test_get_games(self):
        self.setup()
        url = reverse('games-list')
        self.client.post(url, data=self.game_data, format='json')
        self.client.post(url, data=self.game_data, format='json')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Game.objects.count(), 2)

    def test_get_game(self):
        self.setup()
        url = reverse('games-list')
        self.client.post(url, data=self.game_data, format='json')
        response = self.client.get(f'{url}/1', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {
                             'id': 1,
                             'team_a': 'Washington Football Team',
                             'team_b': 'Dallas Cowboys',
                             'game_time': self.now,
                             'sport': 1,
                             'region': 1,
                             'league': 1
                         }
                         )

    def test_get_game_with_odds(self):
        self.setup()
        url = reverse('games-list')
        self.client.post(url, data=self.game_data, format='json')
        self.client.post(self.odds_url, self.odds_data_1, format='json')
        self.client.post(self.odds_url, self.odds_data_2, format='json')
        response = self.client.get(f'{url}/1/odds', format='json')

        formatted_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(formatted_response)
        self.assertEqual(len(formatted_response['odds']), 2)

