import os
from werkzeug.utils import secure_filename
from PIL import Image
import logging

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

logging.basicConfig(level=logging.INFO)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_images(images):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    saved_paths = []
    for image in images:
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            
            try:
                with Image.open(image.stream) as img:
                    img = img.convert('RGB')  # Ensure image is in RGB format
                    img.save(path)
                saved_paths.append(path)
                logging.info(f"Saved image: {path}")
            except Exception as e:
                logging.error(f"Error saving image {filename}: {str(e)}")
    
    return saved_paths