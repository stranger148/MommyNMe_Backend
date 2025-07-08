from flask import Blueprint, request, jsonify
from app.models import db, Category

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    category = Category(name=data['name'], description=data.get('description'))
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created', 'id': category.id}), 201

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([
        {'id': c.id, 'name': c.name, 'description': c.description} for c in categories
    ])

@category_bp.route('/categories/count', methods=['GET'])
def get_category_count():
    count = Category.query.count()
    return jsonify({'count': count})
