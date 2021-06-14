from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from models.store import Store
import json

store_blueprint = Blueprint("stores", __name__)


@store_blueprint.route("/")
def index():
    stores = Store.all()
    return render_template("stores/index.html", stores = stores)

@store_blueprint.route("/new", methods=['GET', 'POST'])
def new_store():
    if request.method == 'POST':
        url_prefix = request.form['url_pre']
        name = request.form['name']
        tag = request.form['tag']
        query = json.loads(request.form['query'])

        Store(url_prefix, name, tag, query).save_to_mongo()
    return render_template("stores/new_store.html")

@store_blueprint.route("/edit/<string:store_id>", methods=['GET', 'POST'])
def edit_store(store_id):
    store = Store.get_by_id(store_id)
    if request.method == 'POST':
        store.url_prefix = request.form['url_pre']
        store.tag = request.form['tag']
        store.query = json.loads(request.form['query'])

        store.save_to_mongo()
        return redirect(url_for(".index"))
    return render_template("stores/edit_store.html", store=store)

@store_blueprint.route("/remove/<string:store_id>")
def remove_store(store_id):
    store = Store.get_by_id(store_id)
    store.remove_from_mongo()
    return redirect(url_for(".index"))

