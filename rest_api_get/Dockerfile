# Use the official Python image as the base image
FROM python:3.8-slim
ENV FLASK_APP rest_api_get/get_api.py
# Set the working directory in the container
WORKDIR /getapi

# Copy the current directory contents into the container at /getapi
COPY rest_api_get/get_api.py /getapi
COPY rest_api_get/cricket_players.json /getapi

# Install Flask and any other dependencies
RUN pip install Flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
