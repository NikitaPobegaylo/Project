#!/usr/bin/env python3


from config import headers, url as URL
import requests


def get_leagues():
	url = "leagues"
	url = URL(url)
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["leagues"]
	return None if not(count > 0) or count != len(items) else items

def get_league(leagueId = 0):
	url = "leagues/league/{leagueId}"
	url = URL(url.format(leagueId = leagueId))
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["leagues"]
	return None if not(count == 1) or count != len(items) else items[0]

def get_leagues_season(season = 0):
	url = "leagues/season/{season}"
	url = URL(url.format(season = season))
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["leagues"]
	return None if not(count > 0) or count != len(items) else items

def get_league_standings(leagueId = 0):
	url = "leagueTable/{leagueId}"
	url = URL(url.format(leagueId = leagueId))
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["standings"]
	return None if not(count > 0) or count != len(items) else items


if __name__ == "__main__":
	# print(get_leagues())
	# print(get_league(leagueId = 2))
	# print(get_leagues_season(season = 2018))
	# print(get_league_standings(leagueId = 1))
	pass
