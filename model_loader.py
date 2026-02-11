import os
import gdown
import joblib
from tensorflow.keras.models import load_model as keras_load_model

MODELS = {
    "diabetes": {
        "id": "11iUnppIjNEIClNzqKQDjc4g5rkG32RUf",
        "path": "models/diabetes.pkl",
        "type": "pkl"
    },
    "heart": {
        "id": "1B8_ujjPVgClrmpqTIn-HCsVXTc_tJfbb",
        "path": "models/heart.pkl",
        "type": "pkl"
    },
    "life": {
        "id": "1rwqFqAydkBb_6jBBVhStcdyGmVUSCAsV",
        "path": "models/life.pkl",
        "type": "pkl"
    },
    "brain": {
        "id": "1xb-JBP1YaJTTYUtUvY6ep-SLC_0xknDM",
        "path": "models/brain_model.h5",
        "type": "h5"
    }
}

os.makedirs("models", exist_ok=True)

def load_model_from_drive(name):
    model_info = MODELS[name]
    path = model_info["path"]

    if not os.path.exists(path):
        url = f"https://drive.google.com/uc?id={model_info['id']}"
        print(f"Downloading {name} model from {url}...")

        try:
            # Try plain gdown first with fuzzy extraction (handles some redirect issues)
            gdown.download(url, path, quiet=False, fuzzy=True)
        except Exception as e:
            print(f"Gdown failed: {e}. Retrying with alternative method...")
            # Fallback or retry logic could go here, but fuzzy=True often fixes drive links
            # If it still fails, we might need a direct requests fallback, but let's try this first.
            raise e

    if model_info["type"] == "pkl":
        return joblib.load(path)
    elif model_info["type"] == "h5":
        return keras_load_model(path)
