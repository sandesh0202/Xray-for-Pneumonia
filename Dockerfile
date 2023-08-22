FROM python:3.8-slim-buster

# Install system dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the PORT environment variable (if your app uses it)
EXPOSE $PORT

# Start your application using Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
