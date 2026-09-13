
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import os
import io
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


# =========================================================
# APP
# =========================================================

app = FastAPI(
    title="BrainTumorAI",
    description="AI-powered Brain MRI Tumor Classification using VGG16",
    version="1.0.0"
)


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "brain_tumor_vgg16_final.keras"
)

STATIC_DIR = os.path.join(
    BASE_DIR,
    "static"
)

TEMPLATE_DIR = os.path.join(
    BASE_DIR,
    "templates"
)


# =========================================================
# LOAD MODEL
# =========================================================

model_vgg = load_model(MODEL_PATH)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)


# =========================================================
# CLASS NAMES
# =========================================================

class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]


display_names = {
    "glioma": "Glioma",
    "meningioma": "Meningioma",
    "notumor": "No Tumor",
    "pituitary": "Pituitary"
}


# =========================================================
# MODEL INFORMATION
# =========================================================

model_accuracy = "88.06%"

model_metrics = {
    "glioma": {
        "precision": "99%",
        "recall": "63%",
        "f1": "77%"
    },
    "meningioma": {
        "precision": "77%",
        "recall": "90%",
        "f1": "83%"
    },
    "notumor": {
        "precision": "90%",
        "recall": "100%",
        "f1": "95%"
    },
    "pituitary": {
        "precision": "92%",
        "recall": "99%",
        "f1": "96%"
    }
}


# =========================================================
# HOME PAGE
# =========================================================

@app.get("/", response_class=HTMLResponse)
def home():

    index_path = os.path.join(
        TEMPLATE_DIR,
        "index.html"
    )

    with open(
        index_path,
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model": "VGG16"
    }


# =========================================================
# MODEL METRICS
# =========================================================

@app.get("/metrics")
def metrics():

    return {
        "accuracy": model_accuracy,
        "test_images": 1600,
        "classes": 4,
        "model": "VGG16",
        "framework": "TensorFlow / Keras",
        "metrics": model_metrics
    }


# =========================================================
# PREDICTION
# =========================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # Read uploaded image
    image_data = await file.read()

    # Open image
    img = Image.open(
        io.BytesIO(image_data)
    ).convert("RGB")

    # Resize
    img = img.resize(
        (224, 224)
    )

    # Convert to NumPy
    img_array = np.array(img)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Prediction
    predictions = model_vgg.predict(
        img_array,
        verbose=0
    )[0]

    # Get predicted class
    predicted_index = int(
        np.argmax(predictions)
    )

    predicted_class = class_names[
        predicted_index
    ]

    # Confidence
    confidence = float(
        predictions[predicted_index]
    )

    # Response
    return {
        "predicted_class": predicted_class,
        "display_class": display_names[predicted_class],
        "confidence": round(
            confidence * 100,
            2
        ),
        "accuracy": model_accuracy,
        "model": "VGG16"
    }

