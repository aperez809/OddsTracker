import json
import urllib3
from datetime import datetime
from pprint import pprint

def send_er():
    http = urllib3.PoolManager()
    url = "https://api.the-odds-api.com/v3/odds/?apiKey=2730f79bc3194a9c02969faab3eeea51&sport=upcoming&oddsFormat=american&region=us"
    res = http.request('GET', url)
    fmt_res = json.loads(res.data)
    fmt_res = fmt_res["data"]

    for game in fmt_res:
        cleaned_game_data = clean_data(game, "us")
        pprint(cleaned_game_data)

        res = http.request(
            'POST',
            'https://www.oddstracker.app/api/game-odds',
            body=json.dumps(cleaned_game_data),
            headers={'Content-Type': 'application/json'}
        )
        print(res.data)



def clean_data(game, region):
    sport = game["sport_key"].split("_")[0]
    league = game["sport_nice"]
    team_a = game["teams"][0]
    team_b = game["teams"][1]
    game_time = str(datetime.utcfromtimestamp(game["commence_time"]))
    odds = clean_odds_data(game["sites"])


    return {
        "sport": sport,
        "region": region,
        "league": league,
        "team_a": team_a,
        "team_b": team_b,
        "game_time": game_time,
        "odds": odds
    }

def clean_odds_data(odds_site_list):
    """
    Loop through each site and their listed
    :param odds_site_list: list of sites that have odds for the game
    :return:
    """
    final = []

    for site in odds_site_list:
        source = site["site_nice"]
        time_recorded = str(datetime.utcfromtimestamp(site["last_update"]))
        for mkt_type, val in site["odds"].items():
            market = mkt_type.upper()
            team_a_val = val[0]
            team_b_val = val[1]
            addl_val = val[2] if len(val) == 3 else None

            final.append({
                "source": source,
                "time_recorded": time_recorded,
                "mkt_type": market,
                "team_a_value": team_a_val,
                "team_b_value": team_b_val,
                "addl_value": addl_val,
            })
    return final

send_er()