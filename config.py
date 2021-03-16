import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'snowflake://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'