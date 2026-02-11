import pickle
import pandas as pd
from model_loader import load_model_from_drive


preprocessor = None
model = None

def get_preprocessor():
    global preprocessor
    if preprocessor is None:
        import os
        from huggingface_hub import hf_hub_download
        local_path = hf_hub_download(
            repo_id="Zakwan2006/medtrust-models",
            filename="preprocessor.pkl",
            local_dir="models",
        )
        preprocessor = pickle.load(open(local_path, "rb"))
    return preprocessor

def get_model():
    global model
    if model is None:
        model = load_model_from_drive('diabetes')
    return model


def diabetes_model_predict(input_data:dict):
    preprocessor = get_preprocessor()
    model = get_model()

    df = pd.DataFrame(input_data, index=[0])
    df_processed = preprocessor.transform(df)
    prediction = model.predict(df_processed)[0]
    probability = model.predict_proba(df_processed)[0][1]
    return prediction, probability

