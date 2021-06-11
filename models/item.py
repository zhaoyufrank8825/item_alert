from common.database import Database
import uuid, requests
from bs4 import BeautifulSoup
from typing import Dict


class Item:

    def __init__(self, url: str, tag: str, query: Dict, _id: str = None) -> None:
        self.url = url
        self.tag = tag
        self.query = query
        self._id = _id or uuid.uuid4().hex
        self.collection = "items"
        self.price = None

    def __repr__(self) -> str:
        return f"<Item {self.url}>"

    def load_price(self)  -> float:
        content = requests.get(self.url).content
        element = BeautifulSoup(content, "html.parser").find(self.tag, self.query)
        str_price = element.text.strip()

        # pattern = re.compile(r"(\d+,?\d+\.\d\d)")
        # found_price = pattern.search(str_price).group(1)
        # price = float(found_price.replace(",", ""))

        self.price = float(str_price[1:])
        return self.price

    def json(self) -> Dict:
        return {
            "_id":self._id,
            "url":self.url,
            "tag":self.tag,
            "query":self.query
        }
    
    def save_to_mongo(self):
        Database.insert(self.collection, self.json())

    @classmethod
    def all(cls):
        items = Database.find("items", {})
        return [cls(**item) for item in items] 

    @classmethod
    def get_by_id(cls, id):
        item =  Database.find_one("items", {"_id":id})
        return cls(**item)