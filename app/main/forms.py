from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Shop
from flask import request


class EditShopForm(FlaskForm):
    id = IntegerField('Shop ID', validators=[DataRequired()])
    owner_id = IntegerField('Owner ID', validators=[DataRequired()])
    city_id = IntegerField('City ID', validators=[DataRequired()])
    address = StringField('Street, number', validators=[DataRequired()])
    lat = FloatField('Latitude')
    long = FloatField('Longtitude')
    submit = SubmitField('Submit')

