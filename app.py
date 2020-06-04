#!/usr/bin/env python3


# https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many


from api.api import get_countries, get_leagues
from pymongo import MongoClient


db = MongoClient(host="localhost", port=27100, username="admin", password="admin", authSource="admin", connect=True).test
# db = MongoClient("mongodb://admin:admin@localhost:27100", authSource="admin").test

print(db.countries.count())


# def xxx():
# 	# countries = get_countries()
# 	# country = countries[0]
# 	# print(countries)
# 	# leagues = get_leagues()
# 	# print(leagues)
# 	# client = MongoClient(host="localhost", port=27100, username="admin", password="admin", authSource="admin", connect=False)
# 	# client.admin.authenticate('admin', 'admin', mechanism="MONGODB-CR")

# 	# print(client)
# 	# print(client['test'])
# 	# print(client['test'].countries)
# 	# print(client['test'].countries.insert_one)
# 	# print(client['test'].command)

# 	# result = client['test'].command("buildinfo")
# 	c = client['test'].countries.find({})
# 	c = list(c)
# 	print(c)

# 	# print(country)
# 	# result = client.test.countries.insert_one(country)
# 	# print(result)
# 	# client.close()


# if __name__ == "__main__":
# 	xxx()



