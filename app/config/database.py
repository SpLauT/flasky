from flask_sqlalchemy import SQLAlchemy
import os

def configure_database(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
    db = SQLAlchemy(app)
    app.config['db'] = db
    
    return db
