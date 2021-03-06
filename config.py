import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/img'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://izzie:Access@localhost/pitch'
    DEBUG = True

class ProdConfig(Config):
        # SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
        # if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        #  SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://izzie:Access@localhost/pitch_test'


config_options = {'development': DevConfig, 'production': ProdConfig,'test':TestConfig}
