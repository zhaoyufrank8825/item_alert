from models.model import Model
from models.item import Item
from dataclasses import dataclass, field
import uuid


@dataclass
class Alert(Model):
    collection: str = field(init=False, default="alerts")
    name: str
    item_id: str
    price_limit: float
    email: str
    img: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex )

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

    def json(self):
        return {
            "item_id": self.item_id,
            "price_limit": self.price_limit,
            "_id": self._id,
            "name": self.name,
            "email": self.email,
            "img": self.img
        }

    def load_item_price(self):
        return self.item.load_price()

    def notify_if_reached(self):
        if self.item.price < self.price_limit:
            print( f"Item {self.item} has reached a price under {self.price_limit}. new price: {self.item.price}.")

