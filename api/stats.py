import requests
import json
from datetime import datetime

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "9373ea7cd6msh86f898bca984655p13a552jsn5d9a680330f8"
    # "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    # "X-RapidAPI-Key": "a0adcd28ffmsh29f567331ce0cbap143ac2jsn5ffb61a1b960"
}


def get_stats(team, league):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/statistics/" +
                       str(league) + "/" +
                       str(team), headers=headers)
    return json.loads(res.content)['api']['statistics']


def get_stats_date(team, league, date):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/statistics/" +
                       str(league) + "/" +
                       str(team) + "/" +
                       datetime.strftime(date, '%Y-%m-%d'), headers=headers)
    return json.loads(res.content)['api']['statistics']


def get_h2h(team1, team2):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/fixtures/h2h/" +
                       str(team1) + "/" +
                       str(team2), headers=headers)
    return json.loads(res.content)['api']['fixtures']
