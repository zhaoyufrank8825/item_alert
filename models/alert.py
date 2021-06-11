from common.database import Database
from models.item import Item
import uuid


class Alert:
    def __init__(self, item_id, price_limit, _id=None):
        self.item_id = item_id
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self.collection = "alerts"
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            "item_id": self.item_id,
            "price_limit": self.price_limit,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert("alerts", self.json())

    def load_item_price(self):
        return self.item.load_price()

    def notify_if_reached(self):
        if self.item.price < self.price_limit:
            print( f"Item {self.item} has reached a price under {self.price_limit}. new price: {self.item.price}.")

    @classmethod
    def all(cls):
        alerts = Database.find("alerts", {})
        return [ cls(**alert) for alert in alerts]
