#!/usr/bin/env python3


# https://docs.python.org/3.4/library/unittest.html
# https://docs.python.org/3/library/unittest.html
import unittest
from leagues import *


class TestStringMethods(unittest.TestCase):
	def test_leagues(self):
		leagues = get_leagues()
		self.assertIsNotNone(leagues)

	def test_league(self):
		league = get_league(leagueId = 2)
		self.assertIsNotNone(league)

	def test_leagues_season(self):
		leagues = get_leagues_season(season = 2018)
		self.assertIsNotNone(leagues)

	def test_league_standings(self):
		standings = get_league_standings(leagueId = 1)
		self.assertIsNotNone(standings)


if __name__ == "__main__":
	unittest.main()
