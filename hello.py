from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from routes import initialize_routes
from config.environment.development import DevelopConfiguration


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
_my_config = DevelopConfiguration()
app.config['SECRET_KEY'] = _my_config.get_form_secret()

#Initializes the routes
initialize_routes(app)

