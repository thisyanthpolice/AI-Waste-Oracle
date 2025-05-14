from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
import settings
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent / 'waste-detection'))

app = Flask(__name__)


CORS(app)


model_path = Path(__file__).resolve().parent / 'weights' / 'best.pt'
try:
    model = YOLO(str(model_path))
except FileNotFoundError:
    model = None
    print(f"Error: Model file not found at {model_path}. Ensure 'best.pt' exists in the weights directory.")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'model_loaded': model is not None})

@app.route('/detect', methods=['POST'])
def detect():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    res = model.predict(image, conf=0.6)
    names = model.names

    detections = []
    for result in res:
        for box, cls in zip(result.boxes.xyxy, result.boxes.cls):
            item_name = names[int(cls)]
            guideline = settings.DISPOSAL_GUIDELINES.get(item_name, 'No guideline available.')

            # Determine material type
            if item_name in settings.RECYCLABLE:
                material_type = 'Recyclable'
            elif item_name in settings.NON_RECYCLABLE:
                material_type = 'Non-Recyclable'
            else:
                material_type = 'Hazardous'

            detections.append({
                'item': item_name,
                'material_type': material_type,
                'guideline': guideline,
                'bbox': [int(coord) for coord in box.tolist()]  # Bounding box coordinates
            })

    return jsonify({'detections': detections})

if __name__ == '__main__':
    app.run(debug=True)
