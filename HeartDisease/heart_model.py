import pickle
import pandas as pd
from model_loader import load_model_from_drive



model = None

def get_model():
    global model
    if model is None:
        model = load_model_from_drive('heart')
    return model


def heart_model_predict(heart_input: dict):
    model = get_model()
    input_data = pd.DataFrame([heart_input])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    return prediction, probability
