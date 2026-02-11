import pickle
import pandas as pd


from model_loader import load_model_from_drive

model = load_model_from_drive('life')

def predict_life_risk_fn(input_data:dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    probability = model.predict_proba(df)
    return prediction[0], probability[0][1]




