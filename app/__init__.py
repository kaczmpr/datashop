from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import os


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from app import models