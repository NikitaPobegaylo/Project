


def insert(_leagues):
    return leagues.insert_many(_leagues).inserted_ids == len(_leagues)


def insert_one(league):
    print(league)
    leagues.insert_one(league)


def get(id):
    return leagues.find_one(id)


def get_all(query):
    return leagues.find(query)

# .sort("field", -1)
# .limit(num)
