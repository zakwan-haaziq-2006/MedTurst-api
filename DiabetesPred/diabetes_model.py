import pickle
import pandas as pd
from model_loader import load_model_from_drive

import os

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.pkl")

preprocessor = pickle.load(open(PREPROCESSOR_PATH, "rb"))
model = load_model_from_drive('diabetes')



def diabetes_model_predict(input_data:dict):
    df = pd.DataFrame(input_data, index=[0])
    df_processed = preprocessor.transform(df)
    prediction = model.predict(df_processed)[0]
    probability = model.predict_proba(df_processed)[0][1]
    return prediction, probability

