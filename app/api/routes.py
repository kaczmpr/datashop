from flask import jsonify, render_template, url_for, request, current_app
from app.api import bp
from app.models import Product, Shop

# Get All Products
@bp.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify(all_products)


@bp.route('/shop', methods=['GET'])
def get_shops():
    all_shops = Shop.query.all()
    return jsonify(all_shops)