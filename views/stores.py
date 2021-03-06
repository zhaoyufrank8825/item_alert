from models.user.decorator import require_admin
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from models.store import Store
from models.user import require_admin
import json

store_blueprint = Blueprint("stores", __name__)


@store_blueprint.route("/")
def index():
    stores = Store.all()
    return render_template("stores/index.html", stores = stores)

@store_blueprint.route("/new", methods=['GET', 'POST'])
@require_admin
def new_store():
    if request.method == 'POST':
        url_prefix = request.form['url_pre']
        name = request.form['name']
        tag = request.form['tag']
        query = json.loads(request.form['query'])
        img = request.form['img']
        description = request.form['description']

        Store(url_prefix, name, tag, query, img, description).save_to_mongo()
        return redirect(url_for(".index"))

    return render_template("stores/new_store.html")

@store_blueprint.route("/edit/<string:store_id>", methods=['GET', 'POST'])
@require_admin
def edit_store(store_id):
    store = Store.get_by_id(store_id)
    if request.method == 'POST':
        store.url_prefix = request.form['url_pre']
        store.tag = request.form['tag']
        store.query = json.loads(request.form['query'])
        store.img = request.form['img']
        store.description = request.form['description']

        store.save_to_mongo()
        return redirect(url_for(".index"))
    return render_template("stores/edit_store.html", store=store)

@store_blueprint.route("/remove/<string:store_id>")
@require_admin
def remove_store(store_id):
    store = Store.get_by_id(store_id)
    store.remove_from_mongo()
    return redirect(url_for(".index"))


@store_blueprint.route("/show/<string:store_id>")
def show(store_id):
    store = Store.get_by_id(store_id)
    return render_template("stores/show.html", store=store)
