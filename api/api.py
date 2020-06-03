#!/usr/bin/env python3


import requests
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from config import headers, url as URL


def get_countries():
	url = "countries"
	url = URL(url)
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["countries"]
	return None if not(count > 0) or count != len(items) else items

def get_leagues():
	url = "leagues"
	url = URL(url)
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["leagues"]
	return None if not(count > 0) or count != len(items) else items

def get_seasons():
	url = "seasons"
	url = URL(url)
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["seasons"]
	return None if not(count > 0) or count != len(items) else items

def get_teams(leagueId = 0):
	url = "teams/league/{leagueId}"
	url = URL(url.format(leagueId = leagueId))
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["teams"]
	return None if not(count > 0) or count != len(items) else items

def get_team(teamId = 0):
	url = "teams/team/{teamId}"
	url = URL(url.format(teamId = teamId))
	response = requests.get(url, headers=headers)
	response = response.json()
	api = response["api"]
	count = api["results"]
	items = api["teams"]
	return None if not(count == 1) or count != len(items) else items[0]



if __name__ == "__main__":
	# print(get_countries())
	# print(get_leagues())
	# print(get_seasons())
	# print(get_teams(leagueId = 2))
	# print(get_team(teamId = 33))
	pass
