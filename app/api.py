from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
app.config["DEBUG"] = True

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'snowflake://admin:Datashop1!@uu39760.west-europe.azure/DATASHOP_DB/DEVELOP?warehouse=COMPUTE_WH&role=SYSADMIN'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Product Class/Model
@dataclass
class Product(db.Model):
    id: int
    name: str
    description: str
    price: float
    qty: int

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify(all_products)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
