import uuid
from typing import Dict
from models.model import Model


class Store(Model):
    collection = "stores"

    def __init__(self, name: str, url_prefix: str, tag_name: str, query: Dict, _id: str = None):
        super().__init__()
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_id(cls, store_name: str) -> "Store":
        return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_ur_prefix(cls, url_prefix: str) -> "Store":
        url_prefix = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by("url_prefix", url_prefix)
