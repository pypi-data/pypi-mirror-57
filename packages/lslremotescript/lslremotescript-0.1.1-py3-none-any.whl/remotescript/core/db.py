from pymongo import MongoClient


class MongoCollection:
    _collection: object

    def __init__(self, collection):
        self._collection = collection

    def insert_by_key(self, key, data):
        assert isinstance(data, dict), f"insert argument should be dict {type(data)} provided"
        return self._collection.insert_one({
            'key': key,
            'data': data
        }).inserted_id

    def update_by_key(self, key, data):
        return self._collection.update_one({
            'key': key,
        }, data)

    def find_by_key(self, key):
        return self._collection.find_one({'key': key})


class MongoDB:
    def __init__(self, URI, database):
        self._URI = URI
        self._client = MongoClient(URI)
        self._database = database
        self._db = self._client[self._database]

    def get_collection(self, name):
        return MongoCollection(self._db[name])

