from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Define flask app
    app = Flask(__name__,instance_relative_config = True)

    # Load configuration from config.py in the instance folder
    app.config.from_object('app.core.conf.ConfigDB')
    app.config.from_pyfile('config.py', silent=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
