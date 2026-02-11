from pydantic import BaseModel, Field,computed_field
from typing import Annotated, Literal

class HeartDiseaseInput(BaseModel):
    age: Annotated[int, Field(ge=0, le=120, description="Age of the patient in years", example=45)]
    sex: Annotated[Literal['F', 'M'], Field(description="Sex of the patient: F (Female), M (Male)", example="M")]
    chest_pain_type: Annotated[Literal['ASY', 'ATA', 'NAP', 'TA'], Field(..., description="Type of chest pain: ASY (asymptomatic), ATA (atypical angina), NAP (non-anginal pain), TA (typical angina)"  )]
    resting_bp: Annotated[int, Field(...,ge=0, le=200,description="Resting blood pressure in mm Hg", example=120)]
    colestrol: Annotated[int, Field(ge=0, le=600)]
    fasting_bs: Annotated[int, Field(ge=0, le=1)]
    resting_ecg: Annotated[Literal['Normal', 'ST', 'LVH'], Field(description="Resting electrocardiogram results: Normal, ST (ST-T wave abnormality), LVH (left ventricular hypertrophy)", example="Normal")]
    max_hr: Annotated[int, Field(ge=0, le=200)]
    ex_ang: Annotated[Literal['Y', 'N'], Field(description="Exercise-induced angina: Y (Yes), N (No)", example="N")]
    old_peak: Annotated[float, Field(ge=0.0, le=10.0,description="Oldpeak: ST depression induced by exercise relative to rest", example=1.5)]
    slope: Annotated[Literal['Flat', 'Up', 'Down'], Field(description="Slope of the ST segment during peak exercise: Flat, Up, Down", example="Up")]


class DiabetesInput(BaseModel):
    gender : Annotated[Literal['Female', 'Male'], Field(description="Gender of the patient: Female, Male", example="Female")]
    age : Annotated[int, Field(ge=0, le=120, description="Age of the patient in years", example=30)]
    hypertension : Annotated[Literal['0', '1'], Field(description="Hypertension status: 0 (No), 1 (Yes)", example="0")]
    heart_disease : Annotated[Literal['0', '1'], Field(description="Heart disease status: 0 (No), 1 (Yes)", example="1")]
    smoking_history : Annotated[Literal['never', 'No Info', 'current', 'former', 'ever', 'not current'], Field(description="Smoking history: never, No Info, current, former, ever, not current", example="current")]
    bmi : Annotated[float, Field(ge=0.0, le=60.0, description="Body Mass Index (BMI) of the patient", example=25.5)]
    HbA1c_level : Annotated[float, Field(ge=0.0, le=15.0, description="HbA1c level of the patient", example=5.5)]
    blood_glucose_level : Annotated[int, Field(ge=0, le=500, description="Blood glucose level of the patient", example=150)]


class LifeRiskInput(BaseModel):
    age: Annotated[int, Field(ge=0, le=120, description="Age of the patient in years", example=30)]
    weight: Annotated[float, Field(ge=0.0, le=500.0, description="Weight of the patient in kg", example=70.5)]
    height : Annotated[float, Field(ge=0.0, le=300.0, description="Height of the patient in cm", example=175.0)]
    exercise : Annotated[Literal['low', 'medium', 'high'], Field(description="Exercise level: low, medium, high", example="medium")]
    sleep : Annotated[float, Field(ge=0.0, le=24.0, description="Average sleeping hours per day", example=7.5)]
    sugar_intake : Annotated[Literal['low', 'medium', 'high'], Field(description="Sugar intake level: low, medium, high", example="low")]
    smoking : Annotated[Literal['yes', 'no'], Field(description="Smoking status:", example="yes")]
    alcohol : Annotated[Literal['yes', 'no'], Field(description="Alcohol consumption status:", example="no")]
    married : Annotated[Literal['yes', 'no'], Field(description="Marital status:", example="yes")]
    profession : Annotated[Literal['student', 'farmer', 'driver', 'doctor', 'artist', 'engineer', 'teacher', 'office_worker'], Field(description="Profession of the patient: student, farmer, driver, doctor, artist, engineer, teacher, office_worker", example="engineer")]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return self.weight / (height_in_meters ** 2)

