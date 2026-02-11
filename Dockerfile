FROM python:3.9

WORKDIR /app

# Create a non-root user (required for Hugging Face Spaces)
RUN useradd -m -u 1000 user

# Ensure /app is owned by user so we can write to it
RUN chown user:user /app

USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Copy requirements first to leverage cache
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application
COPY --chown=user . .

# Create directory for models and ensure it's writable
RUN mkdir -p models && chmod 777 models

EXPOSE 7860

# CMD to start the app (HF Spaces uses port 7860 by default)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]

