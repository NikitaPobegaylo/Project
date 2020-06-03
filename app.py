#!/usr/bin/env python3


# https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many


from api.api import get_countries, get_leagues
from pymongo import MongoClient


if __name__ == "__main__":
	# countries = get_countries()
	# country = countries[0]
	# print(countries)
	# leagues = get_leagues()
	# print(leagues)
	client = MongoClient("mongodb://admin:admin@localhost:27100/test?authSource=admin", connect=False)
	print(client)
	print(client['test'])
	# print(client['test'].countries)
	# print(client['test'].countries.insert_one)
	print(client['test'].command)

	# result = client['test'].command("buildinfo")
	result = client.list_database_names()
	print(result)

	# print(country)
	# result = client.test.countries.insert_one(country)
	# print(result)
	# client.close()