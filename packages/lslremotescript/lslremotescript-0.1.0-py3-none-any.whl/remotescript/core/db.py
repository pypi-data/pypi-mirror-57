from pymongo import MongoClient


class MongoCollection:
    _collection: object

    def __init__(self, collection):
        self._collection = collection

    def insert(self, data):
        assert isinstance(data, dict), f"insert argument should be dict {type(data)} provided"
        return self._collection.insert_one(data).inserted_id


class MongoDB:
    def __init__(self, URI):
        self._URI = URI
        self._client = MongoClient(URI)

    def get_collection(self, name):
        return MongoCollection(self._client[name])

