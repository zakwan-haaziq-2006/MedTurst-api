---
title: MedTrust API
emoji: 🏥
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
app_port: 7860
---

# MedTrust Backend API

This is the backend for the MedTrust application, providing medical prediction models for:
- Heart Disease
- Diabetes
- Life Risk
- Brain Tumor (MRI Classification)

## Deployment
This application is configured to run on **Hugging Face Spaces** using the Docker SDK.

### Setup
The `Dockerfile` is set up to:
1. Install dependencies from `requirements.txt`.
2. Run as a non-root user (security requirement).
3. Download models automatically on startup via `model_loader.py`.

## Local Development
```bash
pip install -r requirements.txt
uvicorn api:app --reload
```
