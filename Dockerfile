# Use the Python base image
FROM python:3.8-slim-buster

# Install Apache and mod_wsgi
RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi-py3

# Set the working directory in the container
WORKDIR /app

# Copy your Flask app files to the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the Apache configuration file for your app
COPY apache /etc/apache2/sites-available/

# Enable the Apache configuration and modules
RUN a2ensite flask-app.conf && a2enmod wsgi

# Expose port 80 for Apache
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2ctl", "-D", "FOREGROUND"]
