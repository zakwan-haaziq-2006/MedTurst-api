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

# Copy the rest of the application
COPY --chown=user . .

# Ensure models directory is writable (just in case)
RUN chmod 777 /app/models

EXPOSE 7860

# CMD to start the app (HF Spaces uses port 7860 by default)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]

