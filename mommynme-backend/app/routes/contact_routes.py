from flask import Blueprint, request, jsonify
from app.models import db, Contact

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/', methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not all([name, email, message]):
        return jsonify({'error': 'Missing required fields'}), 400
    contact = Contact(name=name, email=email, message=message)
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Thank you for contacting us!'}), 201

@contact_bp.route('/latest', methods=['GET'])
def get_latest_reviews():
    reviews = Contact.query.order_by(Contact.created_at.desc()).limit(3).all()
    return jsonify([
        {'name': r.name, 'message': r.message}
        for r in reviews
    ]) 