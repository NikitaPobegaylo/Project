#!/usr/bin/env python3


import unittest
from teams import *


class TestStringMethods(unittest.TestCase):
	def test_teams(self):
		teams = get_teams(leagueId = 1)
		self.assertIsNotNone(teams)

	def test_team(self):
		team = get_team(teamId = 2)
		self.assertIsNotNone(team)


if __name__ == "__main__":
	unittest.main()
