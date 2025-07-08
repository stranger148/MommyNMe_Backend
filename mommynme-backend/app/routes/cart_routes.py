from flask import Blueprint, request, jsonify
from app.models import db, Cart

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    product_name = data.get('product_name')
    image1 = data.get('image1')
    description = data.get('description')
    category_id = data.get('category_id')
    quantity = data.get('quantity', 1)

    # Check if product already in cart, increment quantity if so
    cart_item = Cart.query.filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(
            product_id=product_id,
            product_name=product_name,
            image1=image1,
            description=description,
            category_id=category_id,
            quantity=quantity
        )
        db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Added to cart', 'cart_id': cart_item.id}), 201

@cart_bp.route('/', methods=['GET'])
def get_cart():
    cart_items = Cart.query.all()
    return jsonify([
        {
            'id': item.id,
            'product_id': item.product_id,
            'product_name': item.product_name,
            'image1': item.image1,
            'description': item.description,
            'category_id': item.category_id,
            'quantity': item.quantity
        } for item in cart_items
    ])

@cart_bp.route('/<int:cart_id>', methods=['PATCH'])
def update_cart_item(cart_id):
    data = request.get_json()
    quantity = data.get('quantity')
    cart_item = Cart.query.get(cart_id)
    if not cart_item:
        return jsonify({'error': 'Cart item not found'}), 404
    if quantity is not None:
        if quantity <= 0:
            db.session.delete(cart_item)
        else:
            cart_item.quantity = quantity
    db.session.commit()
    return jsonify({'message': 'Cart updated'}) 