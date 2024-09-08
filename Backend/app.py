from flask import Flask, request, jsonify
from flask_cors import CORS
from model import generate_test_cases
from utils import save_uploaded_images
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.route('/generate_test_cases', methods=['POST'])
def api_generate_test_cases():
    try:
        context = request.form.get('context', '')
        images = request.files.getlist('images')
        
        if not images:
            return jsonify({'error': 'No images uploaded'}), 400
        
        image_paths = save_uploaded_images(images)
        
        logging.info(f"Saved {len(image_paths)} images")
        
        test_cases = generate_test_cases(context, image_paths)
        
        return jsonify({'test_cases': test_cases})
    except Exception as e:
        logging.error(f"Error in api_generate_test_cases: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)