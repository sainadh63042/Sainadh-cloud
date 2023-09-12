# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /one_to_many

# Copy the server Python scripts into the container at /app
COPY computer.py mobile.py /one_to_many/
COPY config_file.json /one_to_many/

# Expose the ports for both servers
EXPOSE 5001
EXPOSE 5002
