#!/usr/bin/env python3


import unittest
from datetime import datetime as dt
from stats import *


class TestStringMethods(unittest.TestCase):
	def test_stats(self):
		statistics = get_stats(teamId = 1, leagueId = 1)
		self.assertIsNotNone(statistics)

	def test_stats_date(self):
		statistics = get_stats_date(teamId = 1, leagueId = 1, date = dt.now())
		self.assertIsNotNone(statistics)

	def test_h2h(self):
		fixtures = get_h2h(team1Id = 1, team2Id = 2)
		self.assertIsNotNone(fixtures)


if __name__ == "__main__":
	unittest.main()
