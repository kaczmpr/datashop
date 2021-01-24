from flask import Flask, request, jsonify
from dataclasses import dataclass
from app import db
from app.api import bp


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
@bp.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify(all_products)
