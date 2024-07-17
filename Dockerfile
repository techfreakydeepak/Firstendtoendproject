# Use the official Python image from the Docker Hub
FROM python:3.6-slim-buster

# Set the working directory in the container
WORKDIR /service

# Copy the requirements.txt file into the container at /service
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /service
COPY . .

# Specify the command to run on container start
ENTRYPOINT ["python", "app.py"]
