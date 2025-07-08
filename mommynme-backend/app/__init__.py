# __init__.py
# Initializes the Flask app, database, and registers blueprints for MommynMe backend.
from flask import Flask
from flask_cors import CORS
from .models import db
from .routes.category_routes import category_bp
from .routes.product_routes import product_bp
from .routes.cart_routes import cart_bp
from .routes.orders_routes import orders_bp
from .routes.contact_routes import contact_bp
from .routes.featured_update_routes import featured_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)

    # Register only necessary blueprints
    app.register_blueprint(category_bp, url_prefix='/category')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(featured_bp, url_prefix='/featured')

    # Add a root route for welcome message
    @app.route('/')
    def index():
        return '<h2>Welcome to the MommynMe Backend API!</h2>'

    with app.app_context():
        db.create_all()

    return app