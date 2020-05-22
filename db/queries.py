def insert(documents, collection):
    return collection.insert_many(documents).inserted_ids == len(documents)


def insert_one(document, collection):
    collection.insert_one(document)


def get(collection, query):
    return collection.find_one(query)


def get_all(collection, query=None, sort="name"):
    return collection.find(query).sort(sort)
