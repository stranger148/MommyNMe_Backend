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