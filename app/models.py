from dataclasses import dataclass
from app import db
from sqlalchemy import Sequence
import datetime

# Product Class/Model
@dataclass
class Product(db.Model):
    id: int
    name: str
    category: str
    price: float
    qty: int
    subcategory: str

    __tablename__ = 'product'
    id = db.Column(db.Integer, Sequence('seq_product'), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    category = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    subcategory = db.Column(db.String(100))

    def __init__(self, name, category, price, qty, subcategory):
        self.name = name
        self.category = category
        self.price = price
        self.qty = qty
        self.subcategory = subcategory

    def __repr__(self):
        return '<Product {id}>'.format(id=self.id)


# Shop Class/Model
@dataclass
class Shop(db.Model):
    id: int
    owner: str
    city: str
    segment: str
    address: str
    lat: float
    long: float

    __tablename__ = 'shop'
    id = db.Column(db.Integer, Sequence('seq_shop'), primary_key=True)
    owner = db.Column(db.String)
    city = db.Column(db.String)
    segment = db.Column(db.String)
    address = db.Column(db.String)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    def __init__(self, owner, city, segment, address, lat, long):
        self.owner = owner
        self.city = city
        self.segment = segment
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
    id = db.Column(db.Integer, Sequence('seq_receipt'), primary_key=True)
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

    def __iter__(self):
        iters = dict((x, y) for x,y in Receipt.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)
        for x, y in iters.items():
            yield x, y
