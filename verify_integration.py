import sys
import os

# Ensure the current directory is in sys.path
sys.path.append(os.getcwd())

print("Starting integration verification...")

try:
    print("Importing Heart Disease Model...")
    from HeartDisease.heart_model import heart_model_predict
    print("Heart Disease Model loaded.")

    print("Importing Diabetes Model...")
    from DiabetesPred.diabetes_model import diabetes_model_predict
    print("Diabetes Model loaded.")

    print("Importing Life Risk Model...")
    from lifeRiskPredictor.life_risk import predict_life_risk_fn
    print("Life Risk Model loaded.")

    print("Importing Brain Tumor Model...")
    from BrainTumer.brain_model import predict_brain_tumor
    print("Brain Tumor Model loaded.")

    print("\nAll modules imported successfully!")

except Exception as e:
    print(f"\nCRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
