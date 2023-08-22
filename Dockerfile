# Use Python 3.11.3 as the base image
FROM python:3.11.3

# Install system dependencies, including AWS CLI
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 80 (modify this if your app uses a different port)
EXPOSE 80

# Specify the command to run your application
CMD ["python3", "app.py"]