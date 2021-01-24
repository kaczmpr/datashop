from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
