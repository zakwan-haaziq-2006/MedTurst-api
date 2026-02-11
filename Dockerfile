FROM python:3.10

WORKDIR /app

# Create a non-root user (required for Hugging Face Spaces)
RUN useradd -m -u 1000 user

# Create directory for models and set permissions AS ROOT
RUN mkdir -p /app/models && chown -R user:user /app

USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Copy requirements first to leverage cache
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Download models from HF Hub DURING BUILD (runtime has no network)
RUN python -c "\
from huggingface_hub import hf_hub_download; \
import os; \
os.makedirs('models', exist_ok=True); \
hf_hub_download(repo_id='Zakwan2006/medtrust-models', filename='diabetes.pkl', local_dir='models'); \
hf_hub_download(repo_id='Zakwan2006/medtrust-models', filename='heart.pkl', local_dir='models'); \
hf_hub_download(repo_id='Zakwan2006/medtrust-models', filename='life.pkl', local_dir='models'); \
hf_hub_download(repo_id='Zakwan2006/medtrust-models', filename='brain_model.h5', local_dir='models'); \
hf_hub_download(repo_id='Zakwan2006/medtrust-models', filename='preprocessor.pkl', local_dir='models'); \
print('All models downloaded successfully')"

# Copy the rest of the application
COPY --chown=user . .

EXPOSE 7860

# CMD to start the app (HF Spaces uses port 7860 by default)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]
