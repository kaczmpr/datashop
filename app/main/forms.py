from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, ValidationError, Length
from flask import request


class EditShopForm(FlaskForm):
    owner = StringField('Owner', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    segment = StringField('Segment')
    address = StringField('Street, number', validators=[DataRequired()])
    lat = FloatField('Latitude')
    long = FloatField('Longtitude')
    submit = SubmitField('Submit')


class EditProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    qty = FloatField('Quantity', validators=[DataRequired()])
    subcategory = StringField('Subcategory', validators=[DataRequired()])
    submit = SubmitField('Submit')