# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from oddstracker.models import Game
import json


class GameTests(APITestCase):
    fixtures = [
        'DBAdmin_TestData.json',
        'Game_TestData.json'
    ]

    # Number of Games in DB before testing
    STARTING_NUM_GAMES = 2

    # URL for getting list of or creating Games
    games_listcreate_url = reverse('games-list')

    # Mock Game data
    game_data = {
        'team_a': 'Washington Football Team',
        'team_b': 'Dallas Cowboys',
        'game_time': '2020-10-05T18:37:00.744747Z',
        'sport': 1,
        'region': 1,
        'league': 1
    }

    def test_create_game(self):
        """
        Ensure we can create a new Game object.
        """
        response = self.client.post(self.games_listcreate_url, data=self.game_data, format='json')
        fmt_res = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), self.STARTING_NUM_GAMES + 1)
        self.assertEqual(Game.objects.get(id=fmt_res['id']).team_a, 'Washington Football Team')

    def test_create_dupe_game(self):
        """
        Ensure we can NOT create a duplicate Game object.
        """
        response_1 = self.client.post(self.games_listcreate_url, data=self.game_data, format='json')
        response_2 = self.client.post(self.games_listcreate_url, data=self.game_data, format='json')

        fmt_res = json.loads(response_1.content)

        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Game.objects.count(), self.STARTING_NUM_GAMES + 1)
        self.assertEqual(Game.objects.get(id=fmt_res['id']).team_a, 'Washington Football Team')

    def test_get_games(self):
        """
        Ensure we can retrieve list of Games
        """
        response = self.client.get(self.games_listcreate_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Game.objects.count(), self.STARTING_NUM_GAMES)

    def test_get_game(self):
        """
        Ensures that we can retrieve a given Game by ID
        """
        create_res = self.client.post(self.games_listcreate_url, data=self.game_data, format='json')
        fmt_create_res = json.loads(create_res.content)

        get_url = reverse('games-detail', args=[fmt_create_res['id']])
        response = self.client.get(get_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {
                             'id': fmt_create_res['id'],
                             'team_a': 'Washington Football Team',
                             'team_b': 'Dallas Cowboys',
                             'game_time': '2020-10-05T18:37:00.744747Z',
                             'sport': 1,
                             'region': 1,
                             'league': 1
                         })

    def test_delete_game(self):
        """
        Ensures that we can properly delete a Game
        #TODO Determine if this should be a hard or soft delete. Current test is hard delete.
        """
        create_res = self.client.post(self.games_listcreate_url, data=self.game_data, format='json')
        fmt_create_res = json.loads(create_res.content)
        self.assertEqual(Game.objects.count(), self.STARTING_NUM_GAMES + 1)

        del_url = reverse('games-detail', args=[fmt_create_res['id']])
        response = self.client.delete(del_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), self.STARTING_NUM_GAMES)


class OddsTests(APITestCase):
    pass


class GameOddsTests(APITestCase):
    fixtures = [
        'DBAdmin_TestData.json',
        'GameOdds_TestData.json'
    ]

    def test_get_game_with_odds(self):
        """
        Ensures a game and its associated odds can be retrieved
        """
        gameodds_retrieve_url = reverse('games-odds-detail', args=[1])
        response = self.client.get(gameodds_retrieve_url, format='json')
        fmt_res = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(fmt_res)
        self.assertEqual(len(fmt_res['odds']), 2)