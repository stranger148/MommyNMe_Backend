# admin_routes.py
# Admin routes for managing categories, products in MommynMe backend.
from flask import Blueprint, request, jsonify
from ..models import db, Category, Product

admin_bp = Blueprint('admin', __name__)

# POST: Add a new category
@admin_bp.route('/category', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    category = Category()
    category.name = name
    category.description = description
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category added', 'id': category.id}), 201

# POST: Add a new product
@admin_bp.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')
    image1 = data.get('image1')
    image2 = data.get('image2')
    image3 = data.get('image3')
    image4 = data.get('image4')
    if not all([name, price, category_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    product = Product()
    product.name = name
    product.description = description
    product.price = price
    product.category_id = category_id
    product.image1 = image1
    product.image2 = image2
    product.image3 = image3
    product.image4 = image4
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added', 'id': product.id}), 201 