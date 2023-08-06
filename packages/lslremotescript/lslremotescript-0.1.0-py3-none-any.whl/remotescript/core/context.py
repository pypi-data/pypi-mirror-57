from .db import MongoDB


class Context:
    def __init__(self, db: MongoDB, namespace: str):
        self._db = db
        self._namespace = namespace

    def get_collection(self, name):
        return self._db.get_collection(f'{self._namespace}_{name}')

