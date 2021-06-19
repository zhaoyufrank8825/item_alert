from models.item import Item


URL="https://www.amazon.com/Apple-iPad-10-2-inch-Wi-Fi-32GB/dp/B08J65DST5/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1623897832&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVWDdFRkJXSk4wVkImZW5jcnlwdGVkSWQ9QTEwNDM5MTUyM1FRUVNKM1UzMEdSJmVuY3J5cHRlZEFkSWQ9QTA0MTU3NzEySFpEQTM1SE1KTDBGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
TAG="span"
QUERY={"id":"price_inside_buybox"}
# <span class="visuallyhidden">$19.99</span>
item = Item(URL, TAG, QUERY)
print(item.load_price())
# item.save_to_mongo()

# items = Item.all()
# print(items)
# print(items[0].load_price())

# from models.alert import Alert


# alerts = Alert.all()

# for alert in alerts:
#     alert.load_item_price()
#     alert.notify_if_reached()

# if not alerts:
#     print("No alerts, please create an item and an alert to test.")

