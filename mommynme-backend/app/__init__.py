# __init__.py
# Initializes the Flask app, database, and registers blueprints for MommynMe backend.
from flask import Flask
from flask_cors import CORS
from .models import db
from .routes.admin_routes import admin_bp
from .routes.user_routes import user_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)


    # Register blueprints
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp)

    # Add a root route for welcome message
    @app.route('/')
    def index():
        return '<h2>Welcome to the MommynMe Backend API!</h2>'

    with app.app_context():
        db.create_all()

    return app 