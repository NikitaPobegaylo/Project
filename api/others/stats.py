#!/usr/bin/env python3


from config import headers, url as URL
import requests
from datetime import datetime as dt


def get_stats(teamId = 0, leagueId = 0):
  url = "statistics/{leagueId}/{teamId}"
  url = URL(url.format(leagueId = leagueId, teamId = teamId))
  response = requests.get(url, headers=headers)
  response = response.json()
  api = response["api"]
  count = api["results"]
  items = api["statistics"]
  return None if not(count > 0) else items


def get_stats_date(teamId = 0, leagueId = 0, date = None):
  format = '%Y-%m-%d'
  date = '' if not(type(date) == dt.date) else dt.strftime(date, format)
  url = "statistics/{leagueId}/{teamId}/{date}"
  url = URL(url.format(leagueId = leagueId, teamId = teamId, date = date))
  response = requests.get(url, headers=headers)
  response = response.json()
  api = response["api"]
  count = api["results"]
  items = api["statistics"]
  return None if not(count > 0) else items


def get_h2h(team1Id = 0, team2Id = 0):
  url = "fixtures/h2h/{team1Id}/{team2Id}"
  url = URL(url.format(team1Id = team1Id, team2Id = team2Id))
  response = requests.get(url, headers=headers)
  response = response.json()
  api = response["api"]
  count = api["results"]
  items = api["fixtures"]
  return None if not(count > 0) or count != len(items) else items


if __name__ == "__main__":
  # print(get_stats(teamId = 1, leagueId = 1))
  # print(get_stats_date(teamId = 1, leagueId = 1, date = dt.now()))
  # print(get_h2h(team1Id = 1, team2Id = 2))
  pass
