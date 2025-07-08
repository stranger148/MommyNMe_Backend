from flask import Blueprint, request, jsonify, current_app
from app.models import db, Product
import os
from werkzeug.utils import secure_filename

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    # Accept multipart/form-data
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    category_id = request.form.get('category_id')

    # Check for required fields
    if not name or not price or not category_id:
        return jsonify({'error': 'Missing required fields: name, price, or category_id'}), 400

    # Convert price and category_id to correct types
    try:
        price = float(price)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid price'}), 400
    try:
        category_id = int(category_id)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid category_id'}), 400

    image_fields = ['image1', 'image2', 'image3', 'image4']
    image_paths = []
    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)

    for field in image_fields:
        image = request.files.get(field)
        if image and image.filename:
            filename = secure_filename(image.filename)
            image_path = os.path.join(upload_folder, filename)
            image.save(image_path)
            image_url = f'/static/uploads/{filename}'
            image_paths.append(image_url)
        else:
            image_paths.append(None)

    # Create product using only the fields defined in the Product model
    product = Product(
        name=name,
        description=description,
        price=price,
        category_id=category_id,
        image1=image_paths[0],
        image2=image_paths[1],
        image3=image_paths[2],
        image4=image_paths[3]
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'id': product.id, 'images': image_paths}), 201

@product_bp.route('/products', methods=['GET'])
def get_products():
    category_id = request.args.get('category_id')
    query = Product.query
    if category_id:
        query = query.filter_by(category_id=category_id)
    products = query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image1': p.image1,
            'image2': p.image2,
            'image3': p.image3,
            'image4': p.image4,
            'category_id': p.category_id
        } for p in products
    ])
