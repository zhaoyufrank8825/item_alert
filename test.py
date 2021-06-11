# from models.item import Item


# URL="https://www.johnlewis.com/2020-apple-ipad-10-2-inch-a12-ipados-wi-fi-32gb/space-grey/p5135266"
# TAG="p"
# QUERY={"class":"price price--large"}

# item = Item(URL, TAG, QUERY)
# item.save_to_mongo()

# items = Item.all()
# print(items)
# print(items[0].load_price())

from models.alert import Alert


alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_reached()

if not alerts:
    print("No alerts, please create an item and an alert to test.")
