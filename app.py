from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from tensorflow.keras.models import load_model

import numpy as np
from PIL import Image
import io


app = FastAPI(
    title="BrainTumorAI",
    description="AI-powered Brain MRI Tumor Classification using VGG16",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Load trained model
model_vgg = load_model(
    "brain_tumor_vgg16_final.keras"
)

# Class names
class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# Actual model performance
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


@app.get("/", response_class=HTMLResponse)
def home():

    with open(
        "templates/index.html",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model": "VGG16"
    }


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


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    image_data = await file.read()

    # Open uploaded image
    img = Image.open(
        io.BytesIO(image_data)
    ).convert("RGB")

    # Resize
    img = img.resize(
        (224, 224)
    )

    # Convert to NumPy
    img_array = np.array(img)

    # Same preprocessing used during training
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

    predicted_index = int(
        np.argmax(predictions)
    )

    predicted_class = class_names[
        predicted_index
    ]

    confidence = float(
        predictions[predicted_index]
    )

    # User-friendly class name
    display_names = {
        "glioma": "Glioma",
        "meningioma": "Meningioma",
        "notumor": "No Tumor",
        "pituitary": "Pituitary"
    }

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