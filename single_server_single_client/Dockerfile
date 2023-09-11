# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /onetoone

# Copy the current directory contents into the container at /app
COPY server.py /onetoone
COPY config_file.json /onetoone

# Define the command to run your application
ENTRYPOINT ["python", "server.py"]
