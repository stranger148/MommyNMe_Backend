# models.py
# SQLAlchemy models for MommynMe backend: Category, Product, Order.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    delivery_time = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    address = db.Column(db.Text)
    phone = db.Column(db.String(15))
    products = db.Column(db.JSON)  # List of product items and quantity
    status = db.Column(db.String(20), default="pending")  # pending/shipped 