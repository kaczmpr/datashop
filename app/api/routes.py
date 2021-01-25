from flask import jsonify
from app.api import bp
from app.models import Product

# Get All Products
@bp.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify(all_products)
