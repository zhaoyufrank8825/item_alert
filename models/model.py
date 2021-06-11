from abc import ABCMeta, abstractmethod
from common.database import Database


class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, *args, **kwargs) -> None:
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id":self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id":self._id})

    @abstractmethod
    def json(self):
        raise NotImplementedError

    @classmethod
    def get_by_id(cls, id):
        return cls.find_one_by("_id", id)

    @classmethod
    def all(cls):
        elements = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements]

    @classmethod
    def find_one_by(cls, attr, value):
        elem = Database.find_one(cls.collection, {attr: value})
        return cls(**elem)

    @classmethod
    def find_many_by(cls, attr, value):
        elements = Database.find(cls.collection, {attr: value})
        return [cls(**elem) for elem in elements]

  

