from models.model import Model
from typing import Dict
import uuid, re
from dataclasses import dataclass, field


@dataclass(eq=False)
class Store(Model):
    collection: str = field(init=False, default="stores")
    url_prefix: str
    name: str
    tag: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    
    def json(self):
        return {
            "url_prefix": self.url_prefix,
            "name": self.name,
            "tag": self.tag,
            "query": self.query,
            "_id": self._id
        }

    @classmethod
    def get_by_name(cls, name):
        return cls.find_one_by("name", name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        url_re = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by("url_prefix", url_re)

    @classmethod
    def find_by_url(cls, url):
        pattern = re.compile(r"(https?://.*?/)")
        url_pre = pattern.search(url).group(1)
        return cls.get_by_url_prefix(url_pre)

    
