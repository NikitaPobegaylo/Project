import pymongo

client = pymongo.MongoClient("mongodb://localhost:27100/")
db = client["cw_db"]
teams = db["teams"]


def insert(_teams):
    return teams.insert_many(_teams).inserted_ids == len(_teams)


def get(id):
    return teams.find_one(id)


def get_all(query):
    return teams.find(query)
