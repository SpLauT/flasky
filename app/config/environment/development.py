from .config import Config, basedir
import os

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'../../../', 'data.sqlite') #consider if this is the most beautiful you can make it :D