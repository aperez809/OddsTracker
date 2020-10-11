import json
import urllib3
from datetime import datetime

def send_er():
    http = urllib3.PoolManager()

    fmt_res = """[{"sport_key": "tennis_wta_french_open", "sport_nice": "WTA French Open", "teams": ["Iga Swiatek", "Nadia Podoroska"], "commence_time": 1602162163, "home_team": "Iga Swiatek", "sites": [{"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164972, "odds": {"h2h": [-3333, 1200]}}, {"site_key": "mybookieag", "site_nice": "MyBookie.ag", "last_update": 1602164961, "odds": {"h2h": [-1666, 600]}}, {"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164971, "odds": {"h2h": [-1667, 1450], "h2h_lay": [-1429, 1650]}}], "sites_count": 3}, {"sport_key": "esports_lol", "sport_nice": "League of Legends", "teams": ["G2 Esports", "Suning"], "commence_time": 1602164234, "home_team": "G2 Esports", "sites": [{"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164971, "odds": {"h2h": [135, -182]}}], "sites_count": 1}, {"sport_key": "cricket_ipl", "sport_nice": "IPL", "teams": ["Kings XI Punjab", "Sunrisers Hyderabad"], "commence_time": 1602165600, "home_team": "Sunrisers Hyderabad", "sites": [{"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164986, "odds": {"h2h": [108, -111], "h2h_lay": [110, -110]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164950, "odds": {"h2h": [100, -125]}}, {"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164973, "odds": {"h2h": [110, -137]}}], "sites_count": 3}, {"sport_key": "tennis_wta_french_open", "sport_nice": "WTA French Open", "teams": ["Petra Kvitova", "Sofia Kenin"], "commence_time": 1602169140, "home_team": "Sofia Kenin", "sites": [{"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164972, "odds": {"h2h": [-179, 148]}}, {"site_key": "lowvig", "site_nice": "LowVig.ag", "last_update": 1602164948, "odds": {"h2h": [-181, 161]}}, {"site_key": "betonlineag", "site_nice": "BetOnline.ag", "last_update": 1602164985, "odds": {"h2h": [-182, 161]}}, {"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164971, "odds": {"h2h": [-182, 178], "h2h_lay": [-179, 182]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164978, "odds": {"h2h": [-209, 154]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164961, "odds": {"h2h": [-190, 155]}}, {"site_key": "bookmaker", "site_nice": "Bookmaker", "last_update": 1602164977, "odds": {"h2h": [-185, 150]}}, {"site_key": "intertops", "site_nice": "Intertops", "last_update": 1602164981, "odds": {"h2h": [-189, 145]}}], "sites_count": 8}, {"sport_key": "soccer_finland_veikkausliiga", "sport_nice": "Veikkausliiga - Finland", "teams": ["HIFK", "KuPS Kuopio"], "commence_time": 1602171000, "home_team": "KuPS Kuopio", "sites": [{"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164975, "odds": {"h2h": [575, -238, 340]}}, {"site_key": "draftkings", "site_nice": "DraftKings", "last_update": 1602164968, "odds": {"h2h": [575, -245, 340]}}, {"site_key": "betrivers", "site_nice": "BetRivers", "last_update": 1602164948, "odds": {"h2h": [575, -245, 340]}}, {"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164984, "odds": {"h2h": [780, -222, 390], "h2h_lay": [820, -213, 400]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164975, "odds": {"h2h": [623, -241, 375]}}, {"site_key": "williamhill_us", "site_nice": "William Hill (US)", "last_update": 1602164978, "odds": {"h2h": [600, -225, 340]}}, {"site_key": "betonlineag", "site_nice": "BetOnline.ag", "last_update": 1602164947, "odds": {"h2h": [620, -238, 359]}}], "sites_count": 7}, {"sport_key": "basketball_euroleague", "sport_nice": "Basketball Euroleague", "teams": ["CSKA Moscow", "Maccabi Tel Aviv"], "commence_time": 1602176400, "home_team": "CSKA Moscow", "sites": [{"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164911, "odds": {"h2h": [-263, 210]}}, {"site_key": "lowvig", "site_nice": "LowVig.ag", "last_update": 1602164787, "odds": {"h2h": [-254, 214]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164909, "odds": {"h2h": [-239, 174]}}, {"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164816, "odds": {"h2h": [-250, 215], "h2h_lay": [-213, 250]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164900, "odds": {"h2h": [-260, 210]}}, {"site_key": "intertops", "site_nice": "Intertops", "last_update": 1602164799, "odds": {"h2h": [-278, 190]}}], "sites_count": 6}, {"sport_key": "basketball_euroleague", "sport_nice": "Basketball Euroleague", "teams": ["Anadolu Efes", "Fenerbahçe Beko"], "commence_time": 1602178200, "home_team": "Anadolu Efes", "sites": [{"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164816, "odds": {"h2h": [-156, 136], "h2h_lay": [-135, 158]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164909, "odds": {"h2h": [-175, 131]}}, {"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164911, "odds": {"h2h": [-154, 125]}}, {"site_key": "intertops", "site_nice": "Intertops", "last_update": 1602164799, "odds": {"h2h": [-167, 120]}}], "sites_count": 4}, {"sport_key": "baseball_mlb", "sport_nice": "MLB", "teams": ["Atlanta Braves", "Miami Marlins"], "commence_time": 1602180000, "home_team": "Miami Marlins", "sites": [{"site_key": "williamhill_us", "site_nice": "William Hill (US)", "last_update": 1602164937, "odds": {"h2h": [-135, 125]}}, {"site_key": "lowvig", "site_nice": "LowVig.ag", "last_update": 1602164769, "odds": {"h2h": [-133, 123]}}, {"site_key": "fanduel", "site_nice": "FanDuel", "last_update": 1602164959, "odds": {"h2h": [-130, 114]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164932, "odds": {"h2h": [-140, 120]}}, {"site_key": "betonlineag", "site_nice": "BetOnline.ag", "last_update": 1602164933, "odds": {"h2h": [-135, 124]}}, {"site_key": "betrivers", "site_nice": "BetRivers", "last_update": 1602164965, "odds": {"h2h": [-150, 128]}}, {"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164869, "odds": {"h2h": [-149, 125]}}, {"site_key": "draftkings", "site_nice": "DraftKings", "last_update": 1602164990, "odds": {"h2h": [-150, 128]}}, {"site_key": "betmgm", "site_nice": "BetMGM", "last_update": 1602164772, "odds": {"h2h": [-139, 125]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164797, "odds": {"h2h": [-140, 130]}}, {"site_key": "pointsbetus", "site_nice": "PointsBet (US)", "last_update": 1602164922, "odds": {"h2h": [-140, 120]}}, {"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164978, "odds": {"h2h": [-128, 124], "h2h_lay": [-123, 128]}}, {"site_key": "mybookieag", "site_nice": "MyBookie.ag", "last_update": 1602164809, "odds": {"h2h": [-140, 120]}}], "sites_count": 13}, {"sport_key": "basketball_euroleague", "sport_nice": "Basketball Euroleague", "teams": ["Real Madrid", "Valencia Basket"], "commence_time": 1602183600, "home_team": "Real Madrid", "sites": [{"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164816, "odds": {"h2h": [-323, 275], "h2h_lay": [-278, 350]}}, {"site_key": "gtbets", "site_nice": "GTbets", "last_update": 1602164909, "odds": {"h2h": [-333, 232]}}, {"site_key": "lowvig", "site_nice": "LowVig.ag", "last_update": 1602164787, "odds": {"h2h": [-335, 280]}}, {"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164911, "odds": {"h2h": [-333, 255]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164900, "odds": {"h2h": [-345, 270]}}, {"site_key": "intertops", "site_nice": "Intertops", "last_update": 1602164799, "odds": {"h2h": [-400, 250]}}], "sites_count": 6}, {"sport_key": "soccer_brazil_campeonato", "sport_nice": "Brazil Série A", "teams": ["Atletico Paranaense", "Ceará"], "commence_time": 1602194400, "home_team": "Atletico Paranaense", "sites": [{"site_key": "betfair", "site_nice": "Betfair", "last_update": 1602164597, "odds": {"h2h": [108, 300, 245], "h2h_lay": [112, 330, 255]}}, {"site_key": "betrivers", "site_nice": "BetRivers", "last_update": 1602164799, "odds": {"h2h": [102, 225, 235]}}, {"site_key": "unibet", "site_nice": "Unibet", "last_update": 1602164918, "odds": {"h2h": [102, 225, 235]}}, {"site_key": "bovada", "site_nice": "Bovada", "last_update": 1602164670, "odds": {"h2h": [100, 265, 230]}}, {"site_key": "intertops", "site_nice": "Intertops", "last_update": 1602164840, "odds": {"h2h": [-105, 260, 230]}}], "sites_count": 5}]"""
    fmt_res = json.loads(fmt_res)

    for game in fmt_res:
        cleaned_game_data = clean_data(game, "us")
        res = http.request(
            'POST',
            'http://localhost:8000/api/games',
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