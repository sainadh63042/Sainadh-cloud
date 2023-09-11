# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /mini_calculator_con

# Copy the current directory contents into the container at /app
COPY mini_calculator.py /mini_calculator_con

# Run the Python script when the container launches
ENTRYPOINT ["python", "mini_calculator.py"]
