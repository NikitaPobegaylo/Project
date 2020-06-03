#!/usr/bin/env python3


from config import headers, url as URL
import requests


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
    # print(get_teams(leagueId = 1))
    # print(get_team(teamId = 2))
    pass
