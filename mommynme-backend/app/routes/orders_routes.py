from flask import Blueprint, request, jsonify
from app.models import db, Order

orders_bp = Blueprint('orders_bp', __name__)

@orders_bp.route('/', methods=['POST'])
def place_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')
    payment_mode = data.get('payment_mode')
    products = data.get('products')
    if not all([customer_name, phone, email, address, payment_mode, products]):
        return jsonify({'error': 'Missing required fields'}), 400
    order = Order(
        customer_name=customer_name,
        phone=phone,
        email=email,
        address=address,
        payment_mode=payment_mode,
        products=products,
        status='PENDING'
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully', 'order_id': order.id}), 201

@orders_bp.route('/pending', methods=['GET'])
def get_pending_orders():
    pending_orders = Order.query.filter_by(status='PENDING').all()
    return jsonify([
        {
            'id': o.id,
            'customer_name': o.customer_name,
            'products': o.products,
            'created_at': o.created_at,
            'address': o.address,
            'phone': o.phone,
            'email': o.email
        }
        for o in pending_orders
    ])

@orders_bp.route('/shipped', methods=['GET'])
def get_shipped_orders():
    shipped_orders = Order.query.filter_by(status='SHIPPED').all()
    return jsonify([
        {
            'id': o.id,
            'customer_name': o.customer_name,
            'email': o.email,
            'phone': o.phone,
            'products': o.products,
            'created_at': o.created_at,
            'address': o.address,
            'payment_mode': o.payment_mode
        }
        for o in shipped_orders
    ])

@orders_bp.route('/<int:order_id>/status', methods=['PATCH'])
def update_order_status(order_id):
    data = request.get_json()
    new_status = data.get('status')
    if new_status not in ['PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED']:
        return {'error': 'Invalid status'}, 400
    order = Order.query.get(order_id)
    if not order:
        return {'error': 'Order not found'}, 404
    order.status = new_status
    db.session.commit()
    return {'message': 'Order status updated'} 