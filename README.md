# The AI Waste Oracle - Intelligent Waste Management System

This web application, **The Waste Oracle**, provides an intelligent solution for identifying and managing various types of waste. Leveraging the power of Artificial Intelligence, it aims to promote safe and responsible waste disposal practices.

## Key Features:

* **Intelligent Image Recognition:** Users can upload images of waste materials. A trained PyTorch model analyzes these images to identify the type of waste present.
* **AI-Powered Hazard Warnings and Precautions:** Upon identifying an object, the application utilizes the Google Gemini API to fetch relevant hazard warnings, necessary precautions for handling the waste, and recommended disposal mechanisms. This information is dynamically generated based on the identified waste type.
* **User-Friendly Web Interface:** Built with Vite and React, the frontend offers a seamless and intuitive experience for users to upload images and receive immediate information.
* **Robust Backend:** The Flask backend in Python efficiently handles image processing, model inference, and communication with the Gemini API.

## How it Works:

1.  **Image Upload:** The user uploads an image of waste material through the web interface.
2.  **Object Detection:** The uploaded image is sent to the Flask backend. The PyTorch model processes the image to detect and identify the object(s) present.
3.  **AI-Powered Information Retrieval:** The identified waste type is then used as a query for the Google Gemini API.
4.  **Hazard, Precaution, and Disposal Guidance:** Gemini AI returns relevant information regarding potential hazards, necessary safety precautions to take while handling the waste, and recommended disposal methods.
5.  **Information Display:** The Flask backend sends this information back to the React frontend, where it is displayed to the user in a clear and concise manner.

## Technologies Used:

* **Frontend:** Vite, React, HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning Model:** PyTorch (for object detection)
* **AI Integration:** Google Gemini API (for hazard warnings, precautions, and disposal)

## Potential Applications:

* Household waste management
* Industrial waste sorting and safety
* Educational tool for waste awareness
* Environmental safety and compliance


This project demonstrates the potential of combining computer vision and large language models to create intelligent solutions for environmental challenges, promoting safer and more informed waste management practices.
