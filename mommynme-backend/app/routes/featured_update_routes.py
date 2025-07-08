from flask import Blueprint, request, jsonify
from app.models import db, FeaturedUpdate
import os
from werkzeug.utils import secure_filename
from datetime import datetime

featured_bp = Blueprint('featured_bp', __name__)

UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads', 'featured')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@featured_bp.route('/featured-updates', methods=['POST'])
def post_featured_update():
    title = request.form.get('title')
    description = request.form.get('description')
    image = request.files.get('image')
    if not all([title, description, image]) or not allowed_file(image.filename):
        return jsonify({'error': 'Missing or invalid fields'}), 400
    filename = secure_filename(f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{image.filename}")
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    image.save(save_path)
    update = FeaturedUpdate(title=title, description=description, image=filename)
    db.session.add(update)
    db.session.commit()
    return jsonify({'message': 'Featured update posted successfully'}), 201

@featured_bp.route('/featured-updates', methods=['GET'])
def get_featured_updates():
    updates = FeaturedUpdate.query.order_by(FeaturedUpdate.created_at.desc()).all()
    return jsonify([
        {
            'id': u.id,
            'title': u.title,
            'description': u.description,
            'image': u.image,
            'created_at': u.created_at.isoformat()
        }
        for u in updates
    ]) 