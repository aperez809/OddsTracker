from collections import OrderedDict

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from oddstracker.models import Game
from datetime import datetime
import json

class GameTests(APITestCase):
    sports_data = {'name': 'Football'}
    regions_data = {'name': 'US'}
    leagues_data = {'name': 'NFL'}
    now = '2020-10-05T18:37:00.744747Z'
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

    def setup(self):
        """
        Create mock data in temp db to test requests
        """
        self.client.post(self.sports_url, self.sports_data, format='json')
        self.client.post(self.regions_url, self.regions_data, format='json')
        self.client.post(self.leagues_url, self.leagues_data, format='json')

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