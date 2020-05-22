import requests
import json

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "9373ea7cd6msh86f898bca984655p13a552jsn5d9a680330f8"
    # "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    # "X-RapidAPI-Key": "a0adcd28ffmsh29f567331ce0cbap143ac2jsn5ffb61a1b960"
}


def get_leagues():
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/leagues", headers=headers)
    return json.loads(res.content)['api']['leagues']


def get_league(id):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/leagues/league/" + str(id), headers=headers)
    return json.loads(res.content)['api']['leagues'][0]


def get_leagues_season(season):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/leagues/season/" + str(season), headers=headers)
    return json.loads(res.content)['api']['leagues']


def get_league_standings(league_id):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/leagueTable/" + str(league_id), headers=headers)
    return json.loads(res.content)['api']['standings'][0]
