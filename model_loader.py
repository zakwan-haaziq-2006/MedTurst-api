import os
import joblib
from huggingface_hub import hf_hub_download

REPO_ID = "Zakwan2006/medtrust-models"

MODELS = {
    "diabetes": {
        "filename": "diabetes.pkl",
        "path": "models/diabetes.pkl",
        "type": "pkl"
    },
    "heart": {
        "filename": "heart.pkl",
        "path": "models/heart.pkl",
        "type": "pkl"
    },
    "life": {
        "filename": "life.pkl",
        "path": "models/life.pkl",
        "type": "pkl"
    },
    "brain": {
        "filename": "brain_model.h5",
        "path": "models/brain_model.h5",
        "type": "h5"
    }
}

os.makedirs("models", exist_ok=True)

def load_model_from_drive(name):
    model_info = MODELS[name]
    path = model_info["path"]

    if not os.path.exists(path):
        print(f"Downloading {name} model from HF Hub ({REPO_ID})...")
        downloaded_path = hf_hub_download(
            repo_id=REPO_ID,
            filename=model_info["filename"],
            local_dir="models",
        )
        print(f"  ✓ {name} model downloaded to {downloaded_path}")

    if model_info["type"] == "pkl":
        return joblib.load(path)
    elif model_info["type"] == "h5":
        from tensorflow.keras.models import load_model as keras_load_model
        return keras_load_model(path)
