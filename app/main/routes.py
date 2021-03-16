from flask import jsonify, render_template, url_for, request, current_app, redirect, Response
from app import db, create_app
from app.main import bp
from app.models import Product, Shop, Receipt
from app.main.forms import EditShopForm, EditProductForm
import json
from kafka import KafkaConsumer
import ast


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
        product = Product(name=form.name.data, category=form.category.data, price=form.price.data
                          , qty=form.qty.data, subcategory=form.subcategory.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('product.html', title='Product', form=form)


@bp.route('/receipt', methods=['GET', 'POST'])
def receipt():
    return render_template('receipt.html', title='Receipt')


@bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html', title='Dashboards')


@bp.route('/chart-data')
def chart_data():
    consumer = KafkaConsumer('numtest', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                             enable_auto_commit=True, group_id='my-group-flask',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def generate_random_data():
        for message in consumer:
            message = message.value
            data = ast.literal_eval(message)
            receipt = Receipt(data.get('shop_id'), data.get('datetime'), data.get('product_id'), data.get('value'),
                              data.get('qty'))
            json_data = json.dumps({'time': receipt.datetime, 'value': receipt.value, 'shop_id': receipt.shop_id})
            yield f"data:{json_data}\n\n"

    return Response(generate_random_data(), mimetype='text/event-stream')
