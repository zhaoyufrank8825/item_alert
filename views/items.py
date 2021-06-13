from flask import Blueprint, render_template, request
from models.item import Item
import json

item_blueprint = Blueprint("items", __name__)

@item_blueprint.route("/")
def index():
    items = Item.all()
    return render_template("items/index.html", items = items)

@item_blueprint.route("/new", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag = request.form['tag']
        query = json.loads(request.form['query'])

        Item(url, tag, query).save_to_mongo()
    return render_template("items/new_item.html")

    