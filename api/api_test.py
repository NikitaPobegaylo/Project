#!/usr/bin/env python3


# https://docs.python.org/3.4/library/unittest.html
# https://docs.python.org/3/library/unittest.html
import unittest
from api import *


class TestStringMethods(unittest.TestCase):
	def test_countries(self):
		items = get_countries()
		self.assertIsNotNone(items)

	def test_leagues(self):
		items = get_leagues()
		self.assertIsNotNone(items)

	def test_seasons(self):
		items = get_seasons()
		self.assertIsNotNone(items)

	def test_teams(self):
		items = get_teams(leagueId = 1)
		self.assertIsNotNone(items)

	def test_team(self):
		items = get_team(teamId = 2)
		self.assertIsNotNone(items)


if __name__ == "__main__":
	unittest.main()
