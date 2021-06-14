from flask import Blueprint, render_template, request, redirect, url_for
from models.alert import Alert
from models.store import Store
from models.item import Item

alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
def index():
    alerts = Alert.all()
    return render_template("alerts/index.html", alerts = alerts)

@alert_blueprint.route("/new", methods=['GET', 'POST'])
def new_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']
        name = request.form['name']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag, store.query)
        item.load_price()
        item.save_to_mongo()

        Alert(name, item._id, price_limit).save_to_mongo()
    return render_template("alerts/new_alert.html")

@alert_blueprint.route("/edit/<string:alert_id>", methods=['GET', 'POST'])
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if request.method == 'POST':
        alert.price_limit = float(request.form['price_limit'])
        alert.save_to_mongo()
        return redirect(url_for(".index"))

    return render_template("alerts/edit_alert.html", alert=alert)

@alert_blueprint.route("/remove/<string:alert_id>")
def remove_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    alert.remove_from_mongo()
    return redirect(url_for(".index"))

    