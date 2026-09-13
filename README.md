# 🧠 Brain Tumor Classification using VGG16

An AI-powered deep learning application that classifies brain MRI images into four categories using **VGG16 Transfer Learning**. The trained model is integrated with **FastAPI** and deployed on **Render** for real-time prediction.

## 🚀 Live Demo

**Live Application:**
https://brain-tumor-vgg16-fastapi.onrender.com

**FastAPI Swagger Documentation:**
https://brain-tumor-vgg16-fastapi.onrender.com/docs

---

## 📌 Project Overview

Brain tumors are abnormal growths of cells in the brain. This project uses a deep learning model based on **VGG16** to classify brain MRI images into four categories.

The application provides an easy-to-use interface where a user can upload an MRI image and receive:

* Predicted tumor category
* Prediction confidence
* Real-time result through a FastAPI backend

> ⚠️ **Disclaimer:** This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis.

---

## 🎯 Objective

The main objectives of this project are:

* Build a brain MRI image classification system.
* Use **VGG16 Transfer Learning** for image classification.
* Classify MRI images into four categories.
* Develop a REST API using **FastAPI**.
* Create a user-friendly web interface.
* Deploy the application on **Render**.
* Return prediction results with confidence scores.

---

## 🧠 Classification Classes

The model classifies MRI images into:

1. **Glioma**
2. **Meningioma**
3. **No Tumor**
4. **Pituitary**

---

## 🏗️ Project Architecture

```text
                Brain MRI Image
                       │
                       ▼
              Image Preprocessing
                       │
                       ▼
                 VGG16 Model
                       │
                       ▼
              Feature Extraction
                       │
                       ▼
              Classification Layer
                       │
                       ▼
             Predicted Tumor Class
                       │
                       ▼
               Confidence Score
                       │
                       ▼
                FastAPI Backend
                       │
                       ▼
                  Web Interface
                       │
                       ▼
                    Render
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras
* VGG16
* Convolutional Neural Network (CNN)
* Transfer Learning

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Deployment & Version Control

* Git
* GitHub
* Git LFS
* Render

---

## 🧠 Model

The project uses **VGG16**, a pretrained convolutional neural network architecture.

Transfer learning was used to leverage pretrained image features and adapt the model for brain MRI classification.

### Model Workflow

```text
Input MRI Image
      ↓
Image Resizing & Preprocessing
      ↓
VGG16 Convolutional Base
      ↓
Feature Extraction
      ↓
Classification Layers
      ↓
4-Class Prediction
```

---

## 📊 Model Performance

The final VGG16 model achieved an **overall test accuracy of 88%** on **1,600 test MRI images**.

### Final VGG16 Classification Report

| Class                | Precision | Recall | F1-Score |  Support |
| -------------------- | --------: | -----: | -------: | -------: |
| Glioma               |      0.99 |   0.63 |     0.77 |      400 |
| Meningioma           |      0.77 |   0.90 |     0.83 |      400 |
| No Tumor             |      0.90 |   1.00 |     0.95 |      400 |
| Pituitary            |      0.92 |   0.99 |     0.96 |      400 |
| **Overall Accuracy** |           |        |  **88%** | **1600** |

### Overall Metrics

| Metric                     |   Score |
| -------------------------- | ------: |
| **Test Accuracy**          | **88%** |
| Macro Average Precision    |    0.89 |
| Macro Average Recall       |    0.88 |
| Macro Average F1-Score     |    0.88 |
| Weighted Average Precision |    0.89 |
| Weighted Average Recall    |    0.88 |
| Weighted Average F1-Score  |    0.88 |
| Test Images                |   1,600 |

The model performs particularly well on the **No Tumor** and **Pituitary** classes. The **Glioma** class has comparatively lower recall, indicating that some glioma images were classified as other categories.

---

## 🔌 FastAPI API

The trained model is served through a **FastAPI REST API**.

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "model": "VGG16"
}
```

### Prediction Endpoint

```http
POST /predict
```

The endpoint accepts an MRI image and returns the predicted class and confidence score.

Example response:

```json
{
  "prediction": "meningioma",
  "confidence": 96.74
}
```

---

## 📖 Swagger API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

**Swagger URL:**

https://brain-tumor-vgg16-fastapi.onrender.com/docs

### How to test the API

1. Open `/docs`.
2. Find `POST /predict`.
3. Click **Try it out**.
4. Upload an MRI image.
5. Click **Execute**.
6. View the prediction and confidence score.

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rkuma9141/brain-tumor-vgg16-fastapi.git
```

### 2. Open the project

```bash
cd brain-tumor-vgg16-fastapi
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run FastAPI

```bash
uvicorn app:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📁 Project Structure

```text
brain-tumor-vgg16-fastapi/
│
├── app.py
├── brain_tumor_vgg16_final.keras
├── requirements.txt
├── .gitattributes
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ☁️ Deployment

The application is deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

The VGG16 `.keras` model is approximately **117 MB**, so **Git LFS** is used to manage the large model file.

---

## 🔄 Application Workflow

```text
1. User uploads MRI image
             ↓
2. FastAPI receives the image
             ↓
3. Image is preprocessed
             ↓
4. VGG16 model performs prediction
             ↓
5. Model generates class probabilities
             ↓
6. Highest probability class is selected
             ↓
7. Prediction + confidence are returned
             ↓
8. Result is displayed to the user
```

---

## 🧪 Example Prediction

Example prediction from the deployed application:

```text
Prediction : Meningioma
Confidence : 96.74%
```

---

## 🔮 Future Improvements

* Improve model performance through further fine-tuning.
* Add **Grad-CAM** for model explainability.
* Add prediction history.
* Add user authentication.
* Improve frontend UI/UX.
* Add model monitoring.
* Add additional MRI datasets.
* Improve handling of difficult tumor classes such as glioma.

---

## 👨‍💻 Author

**Raviranjan Kumar**

B.Tech Computer Science & Engineering

**GitHub:**
https://github.com/rkuma9141

---

## ⚠️ Medical Disclaimer

This application is developed for **educational and research purposes only**.

The predictions generated by this system should **not be considered a medical diagnosis**. Medical decisions should always be made by qualified healthcare professionals.
