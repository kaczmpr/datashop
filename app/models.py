from dataclasses import dataclass
from app import db
import datetime

# Product Class/Model
@dataclass
class Product(db.Model):
    id: int
    name: str
    description: str
    price: float
    qty: int

    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)


# Shop Class/Model
@dataclass
class Shop(db.Model):
    id: int
    owner_id: int
    city_id: int
    address: str
    lat: float
    long: float

    __tablename__ = 'shop'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    address = db.Column(db.String)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    def __init__(self, id, owner_id, city_id, address, lat, long):
        self.id = id
        self.owner_id = owner_id
        self.city_id = city_id
        self.address = address
        self.lat = lat
        self.long = long

    def __repr__(self):
        return '<Shop {id}>'.format(id=self.id)


# Receipt Class/Model
@dataclass
class Receipt(db.Model):
    id: int
    shop_id: int
    datetime: datetime.datetime
    product_id: int
    value: float
    qty: float

    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Float, nullable=False)

    def __init__(self, shop_id, datetime, product_id, value, qty):
        self.shop_id = shop_id
        self.datetime = datetime
        self.product_id = product_id
        self.value = value
        self.qty = qty

    def __repr__(self):
        return '<Receipt {id}>'.format(id=self.id)