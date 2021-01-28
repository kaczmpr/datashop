from flask import jsonify, render_template, url_for, request, current_app, redirect
from app import db
from app.main import bp
from app.models import Product, Shop
from app.main.forms import EditShopForm, EditProductForm


@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')


@bp.route('/shop', methods=['GET', 'POST'])
def shop():
    form = EditShopForm()
    if form.validate_on_submit():
        shop = Shop(owner=form.owner.data, city=form.city.data, segment=form.segment.data, address=form.address.data,
                    lat=form.lat.data, long=form.long.data)
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('shop.html', title='Shop', form=form)


@bp.route('/product', methods=['GET', 'POST'])
def product():
    form = EditProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data, price=form.price.data
                          , qty=form.qty.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('product.html', title='Product', form=form)


@bp.route('/product', methods=['GET', 'POST'])
def receipt():
    return render_template('receipt.html', title='Receipt')