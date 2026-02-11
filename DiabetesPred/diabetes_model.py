import pickle
import pandas as pd
from model_loader import load_model_from_drive


preprocessor = None
model = None

def get_preprocessor():
    global preprocessor
    if preprocessor is None:
        import os
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.pkl")
        preprocessor = pickle.load(open(PREPROCESSOR_PATH, "rb"))
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

