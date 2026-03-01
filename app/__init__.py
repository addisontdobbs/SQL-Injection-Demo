from flask import Flask
from .init_db import init_db
from .routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-key-change-later"
    app.config["DB_PATH"] = "instance/app.db"

    # Initialize DB + seed users
    init_db(app.config["DB_PATH"])

    # IMPORTANT: register routes
    app.register_blueprint(routes_bp)

    return app
