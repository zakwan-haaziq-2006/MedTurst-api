import tensorflow as tf
import numpy as np
from PIL import Image
from keras.models import load_model
from model_loader import load_model_from_drive



# -----------------------------
# Load Model Lazy
# -----------------------------
model = None

def get_model():
    global model
    if model is None:
        try:
            model = load_model_from_drive("brain")
        except Exception as e:
            print(f"Error loading brain tumor model: {e}")
            raise e
    return model


# -----------------------------
# Class Names (CHANGE IF NEEDED)
# -----------------------------
CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]


# -----------------------------
# Prediction Function
# -----------------------------
def predict_brain_tumor(img: Image.Image):

    model = get_model()
    if model is None:
        raise ValueError("Brain tumor model failed to load")

    img = img.convert("RGB")
    img = img.resize((224, 224))

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)

    class_id = int(np.argmax(predictions[0]))
    confidence = float(predictions[0][class_id])

    label = CLASS_NAMES[class_id]

    return label, confidence
