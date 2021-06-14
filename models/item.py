from models.model import Model
import uuid, requests
from bs4 import BeautifulSoup
from typing import Dict
from dataclasses import dataclass, field


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    price: float = field(default=None)

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
            "query":self.query,
            "price":self.price
        }
    
