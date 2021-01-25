class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'snowflake://admin:Datashop1!@uu39760.west-europe.azure/DATASHOP_DB/DEVELOP?warehouse=COMPUTE_WH&role=SYSADMIN'
    SQLALCHEMY_TRACK_MODIFICATIONS = False