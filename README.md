# Trashify - Computer Vision-Based Waste smart waste managment system

An AI-powered web application that combines computer vision and generative AI to identify waste items and provide comprehensive disposal guidance.

## Overview

Trashify - Smart Computer Vision-Based Waste Classifier leverages YOLOv8 object detection to identify waste materials from uploaded images, then uses Google Gemini API to generate detailed disposal guidelines, hazard warnings, and safety precautions.

## Key Features

- **Advanced Object Detection**: YOLOv8-based model trained to recognize 35+ waste categories
- **AI-Generated Disposal Guidelines**: Google Gemini API provides dynamic, contextual recommendations
- **Material Classification**: Automatic categorization into Recyclable, Non-Recyclable, and Hazardous
- **Safety Information**: Real-time hazard warnings and handling precautions
- **Visual Detection Results**: Bounding box coordinates for detected items
- **Responsive Web Interface**: Clean, modern UI built with React and Vite

## Technology Stack

### Frontend
- **React 19** - UI component library
- **Vite** - Build tool and development server
- **Axios** - HTTP client for API communication
- **CSS3** - Custom styling

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Ultralytics YOLOv8** - Object detection model
- **OpenCV** - Image processing
- **NumPy** - Numerical computations
- **Google Gemini API** - Generative AI for disposal recommendations

### Machine Learning
- Custom-trained YOLO model
- 60% confidence threshold for detections
- Support for 35+ waste item categories

## How It Works

1. **Image Upload**: User uploads a photo of waste material through the web interface
2. **Object Detection**: YOLOv8 model processes the image and identifies waste items
3. **AI Enhancement**: Detected item names are sent to Google Gemini API
4. **Information Retrieval**: Gemini generates hazard warnings, safety precautions, and disposal methods
5. **Results Display**: Frontend presents detection results with comprehensive disposal guidance

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Google Gemini API key

### Backend Setup

```bash
cd backend
pip install flask flask-cors ultralytics opencv-python numpy google-generativeai
export GOOGLE_API_KEY="your_gemini_api_key_here"
python app.py
```

### Frontend Setup

```bash
npm install
npm run dev
```

## API Endpoints

### GET /health
Health check endpoint to verify backend status and model availability.

### POST /detect
Main detection endpoint for waste classification.

**Request:**
- Content-Type: multipart/form-data
- Body: Image file

**Response:**
```json
{
  "detections": [
    {
      "item": "plastic_bottle",
      "material_type": "Recyclable",
      "guideline": "Rinse and remove the cap...",
      "bbox": [x1, y1, x2, y2]
    }
  ]
}
```

## Supported Waste Categories

**Recyclable Items:**
- Cardboard boxes, Metal cans, Plastic bottles and caps, Glass bottles, Reusable paper

**Non-Recyclable Items:**
- Plastic bags, Styrofoam, Plastic utensils, Snack bags, Straws

**Hazardous Materials:**
- Batteries, Light bulbs, Electronics, Paint cans, Medication, Thermometers

## Use Cases

- Household waste management
- Industrial waste sorting and safety compliance
- Educational tool for waste awareness
- Smart city waste management programs
- Environmental compliance and hazardous material handling
