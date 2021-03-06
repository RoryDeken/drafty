"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    CORS(app)
    db.init_app(app)

    with app.app_context():
        from . import auth
        from . import routes
        from . import import_players
        app.register_blueprint(auth.bp)
        db.create_all()
        return app
