from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


# Creating the bootstrap instance
bootstrap = Bootstrap()

def create_app(config_name):
#creating the app instance
    app = Flask(__name__)
#importing the configurations directly to the application instance the one we just created
    app.config.from_object(config_options[config_name])
#completing the intilization
    bootstrap.init_app(app)
#importing the instance from main
    from .main import main as main_blueprint
#then we register the blueprint
    app.register_blueprint(main_blueprint)
#call the function when we create our app
    from .request import configure_request
    configure_request(app)

    return app
