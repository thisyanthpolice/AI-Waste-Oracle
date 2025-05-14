import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import './Grid.css';

function App() {
  const [imagePreview, setImagePreview] = useState(null);
  const [detections, setDetections] = useState([]);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => setImagePreview(reader.result);
      reader.readAsDataURL(file);
    }
  };

  const handleUpload = async () => {
    if (!imagePreview) {
      alert('Please upload an image first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', document.querySelector('input[type="file"]').files[0]);

    try {
      const response = await axios.post('http://localhost:5000/detect', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setDetections(response.data.detections);
    } catch (error) {
      console.error('Error uploading image:', error);
      alert('Failed to detect objects. Please try again.');
    }
  };

  const renderDetections = () => {
    return detections.map((detection, index) => (
      <div key={index} className="detection-item">
        <h2>{detection.item}</h2>
        <p><strong>Material Type:</strong> {detection.material_type}</p>
        <p><strong>Disposal Mechanism:</strong> {detection.guideline}</p>
      </div>
    ));
  };

  return (
    <div className="app">
      <header className="hero">
        <h1>Smart Waste Management System</h1>
        <p>Upload an image to detect waste items and get disposal guidelines.</p>
      </header>
      <main className="main-content">
        <div className="card-container">
          <div className="card upload-card">
            <h2>Upload Image</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload and Detect</button>
          </div>
          <div className="card display-card">
            <h2>Detected Image</h2>
            {imagePreview && (
              <div className="image-wrapper">
                <img src={imagePreview} alt="Uploaded" />
                {detections.length > 0 && <p>{detections[0].item}</p>}
              </div>
            )}
          </div>
        </div>
        <div className="details-panel">
          {detections.length > 0 && renderDetections()}
        </div>
      </main>
    </div>
  );
}

export default App;
