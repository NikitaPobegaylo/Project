import requests
import json

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "9373ea7cd6msh86f898bca984655p13a552jsn5d9a680330f8"
    # "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    # "X-RapidAPI-Key": "a0adcd28ffmsh29f567331ce0cbap143ac2jsn5ffb61a1b960"
}


def get_teams(league):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/teams/league/" + str(league), headers=headers)
    return json.loads(res.content)['api']['teams']


def get_team(id):
    res = requests.get("https://api-football-v1.p.rapidapi.com/v2/teams/team/" + str(id), headers=headers)
    return json.loads(res.content)['api']['teams'][0]
