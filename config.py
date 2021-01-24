import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'snowflake://admin:Datashop1!@uu39760.west-europe.azure/datashop_db/develop/?warehouse=COMPUTE_WH&role=SYSADMIN'
    SQLALCHEMY_TRACK_MODIFICATIONS = False