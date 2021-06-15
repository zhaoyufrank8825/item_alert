from flask import Blueprint, render_template, request, redirect, url_for, session
from models.alert import Alert
from models.store import Store
from models.item import Item
from models.user import require_login

alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
@require_login
def index():
    alerts = Alert.find_many_by("email", session['email'])
    return render_template("alerts/index.html", alerts = alerts)

@alert_blueprint.route("/new", methods=['GET', 'POST'])
@require_login
def new_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']
        name = request.form['name']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag, store.query)
        item.load_price()
        item.save_to_mongo()

        Alert(name, item._id, price_limit, session['email']).save_to_mongo()
    return render_template("alerts/new_alert.html")

@alert_blueprint.route("/edit/<string:alert_id>", methods=['GET', 'POST'])
@require_login
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if request.method == 'POST':
        alert.price_limit = float(request.form['price_limit'])
        alert.save_to_mongo()
        return redirect(url_for(".index"))

    return render_template("alerts/edit_alert.html", alert=alert)

@alert_blueprint.route("/remove/<string:alert_id>")
@require_login
def remove_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.email == session['email']:
        alert.remove_from_mongo()
    return redirect(url_for(".index"))

    