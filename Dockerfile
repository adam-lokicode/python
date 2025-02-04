# Use a lightweight Python base image
FROM python:3.8-slim

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel

# Set the working directory
WORKDIR /opt/app

# Copy the application files
COPY . /opt/app

# Verify files exist after COPY
RUN ls -l /opt/app/dronedemo

# Install dependencies
RUN pip install -r requirements.txt

# Run Flask app
CMD ["python", "/opt/app/dronedemo/main.py"]