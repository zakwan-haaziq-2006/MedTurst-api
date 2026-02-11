from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from schema.schema import HeartDiseaseInput, DiabetesInput, LifeRiskInput

from HeartDisease.heart_model import heart_model_predict
from DiabetesPred.diabetes_model import diabetes_model_predict
from lifeRiskPredictor.life_risk import predict_life_risk_fn
from BrainTumer.brain_model import predict_brain_tumor

from PIL import Image
import io

# -----------------------------
# Create App
# -----------------------------
app = FastAPI()


# -----------------------------
# Health Routes
# -----------------------------
@app.get("/")
def root():
    return {"message": "Medical Model API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# -----------------------------
# Heart Disease
# -----------------------------
@app.post("/predict/heart_disease")
async def predict_heart_disease(user_input: HeartDiseaseInput):

    input_dict = {
        "Age": user_input.age,
        "Sex": user_input.sex,
        "ChestPainType": user_input.chest_pain_type,
        "RestingBP": user_input.resting_bp,
        "Cholesterol": user_input.colestrol,
        "FastingBS": user_input.fasting_bs,
        "RestingECG": user_input.resting_ecg,
        "MaxHR": user_input.max_hr,
        "ExerciseAngina": user_input.ex_ang,
        "Oldpeak": user_input.old_peak,
        "ST_Slope": user_input.slope
    }

    prediction, probability = heart_model_predict(input_dict)

    return JSONResponse(
        content={
            "prediction": int(prediction),
            "probability": float(probability)
        }
    )


# -----------------------------
# Diabetes
# -----------------------------
@app.post("/predict/diabetes")
async def predict_diabetes(user_input: DiabetesInput):

    input_dict = user_input.dict()

    prediction, probability = diabetes_model_predict(input_dict)

    return JSONResponse(
        content={
            "prediction": int(prediction),
            "probability": float(probability)
        }
    )


# -----------------------------
# Life Risk
# -----------------------------
@app.post("/predict/life_risk")
async def predict_life_risk(user_input: LifeRiskInput):

    input_dict = user_input.dict()

    prediction, probability = predict_life_risk_fn(input_dict)

    return JSONResponse(
        content={
            "prediction": prediction,
            "probability": float(probability)
        }
    )


# -----------------------------
# Brain Tumor (Image)
# -----------------------------
@app.post("/predict/brain_tumor")
async def predict_tumor_endpoint(file: UploadFile = File(...)):

    if not file.content_type.startswith("image"):
        return JSONResponse(
            content={"error": "Please upload an image file"},
            status_code=400
        )

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    label, confidence = predict_brain_tumor(image)

    return JSONResponse(
        content={
            "prediction": label,
            "confidence": round(confidence, 4)
        }
    )
