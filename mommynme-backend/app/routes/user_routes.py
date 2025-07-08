# user_routes.py
# User routes for browsing products and placing orders in MommynMe backend.
from flask import Blueprint, request, jsonify
from ..models import db, Product, Order

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
            'delivery_time': p.delivery_time,
            'image_url': p.image_url
        } for p in products
    ])

# POST: Add items to cart (optional, stub)
@user_bp.route('/cart', methods=['POST'])
def add_to_cart():
    # This is a stub. Cart can be managed client-side or expanded here.
    return jsonify({'message': 'Cart endpoint (not implemented server-side)'}), 200

# POST: Place an order
@user_bp.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    address = data.get('address')
    phone = data.get('phone')
    products = data.get('products')
    if not all([customer_name, address, phone, products]):
        return jsonify({'error': 'Missing required fields'}), 400
    order = Order()
    order.customer_name = customer_name
    order.address = address
    order.phone = phone
    order.products = products
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order placed', 'id': order.id}), 201 