from uuid import uuid4


class InMemoryCollection:
    def __init__(self, collection):
        self._collection = collection

    def insert(self, data):
        key = uuid4()
        self._collection[key] = data
        return key

    def find(self, query):
        pass


class InMemoryDB:
    def __init__(self, URI):
        self._URI = URI
        self._collections = {}

    def get_collection(self, name):
        self._collections.setdefault(name, {})
        return InMemoryCollection(self._collections[name])
