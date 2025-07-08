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
    delivery_time = request.form.get('delivery_time')
    category_id = request.form.get('category_id')
    image = request.files.get('image')
    image_url = None
    if image:
        filename = secure_filename(image.filename)
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, filename)
        print('Saving image to:', image_path)
        try:
            image.save(image_path)
            print('Image saved successfully.')
        except Exception as e:
            print('Image save failed:', e)
        image_url = f'/static/uploads/{filename}'
    product = Product(
        name=name,
        description=description,
        price=price,
        delivery_time=delivery_time,
        image_url=image_url,
        category_id=category_id
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'id': product.id, 'image_url': image_url}), 201
