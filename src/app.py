#src/app.py

from flask import Flask
from .config import app_config
from .models import db

def create_app(env_name):
    """
    Create App
    """

    #app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    return app