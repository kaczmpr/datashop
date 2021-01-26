from flask import jsonify, render_template, url_for, request, current_app
from app import db
from app.main import bp
from app.models import Product


@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')


@bp.route('/shop', methods=['GET', 'POST'])
def shop():
    return render_template('shop.html', title='Shop')


@bp.route('/product', methods=['GET', 'POST'])
def product():
    return render_template('product.html', title='Product')


@bp.route('/product', methods=['GET', 'POST'])
def receipt():
    return render_template('receipt.html', title='Receipt')