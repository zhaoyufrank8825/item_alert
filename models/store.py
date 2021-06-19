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
    img: str
    description: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    
    def json(self):
        return {
            "url_prefix": self.url_prefix,
            "name": self.name,
            "tag": self.tag,
            "query": self.query,
            "_id": self._id,
            "img": self.img,
            "description": self.description
        }

    @classmethod
    def get_by_name(cls, name):
        return cls.find_one_by("name", name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        url_pre = {"$regex": '^{}'.format(url_prefix)}
        print(url_pre, "in get_by_url_prefix", url_prefix)
        return cls.find_one_by("url_prefix", url_pre)

    @classmethod
    def find_by_url(cls, url):
        pattern = re.compile(r"(https?://.*?/)")
        url_pre = pattern.search(url).group(1)
        print(url_pre, "in find_by_url")
        return cls.get_by_url_prefix(url_pre)

    
