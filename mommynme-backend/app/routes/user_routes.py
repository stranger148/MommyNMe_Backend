# user_routes.py
# User routes for browsing products in MommynMe backend.
from flask import Blueprint, jsonify
from ..models import Product

user_bp = Blueprint('user', __name__)

# GET: Fetch products by category
@user_bp.route('/products/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image1': p.image1,
            'image2': p.image2,
            'image3': p.image3,
            'image4': p.image4
        } for p in products
    ]) 