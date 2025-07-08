# admin_routes.py
# Admin routes for managing categories, products, and viewing orders in MommynMe backend.
from flask import Blueprint, request, jsonify
from ..models import db, Category, Product, Order

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
    delivery_time = data.get('delivery_time')
    image_url = data.get('image_url')
    category_id = data.get('category_id')
    if not all([name, price, category_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    product = Product()
    product.name = name
    product.description = description
    product.price = price
    product.delivery_time = delivery_time
    product.image_url = image_url
    product.category_id = category_id
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added', 'id': product.id}), 201

# GET: Get all orders
@admin_bp.route('/orders', methods=['GET'])
def get_orders():
    status = request.args.get('status')
    query = Order.query
    if status:
        query = query.filter_by(status=status)
    orders = query.all()
    return jsonify([{
        'id': o.id,
        'customer_name': o.customer_name,
        'address': o.address,
        'phone': o.phone,
        'products': o.products,
        'status': o.status
    } for o in orders]) 