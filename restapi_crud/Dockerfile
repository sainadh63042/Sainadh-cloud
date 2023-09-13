# Use the official Python image as the base image
FROM python:3.8-slim
ENV FLASK_APP restapi_crud_operations.py
# Set the working directory in the container
WORKDIR /db_crud

# Copy the current directory contents into the container at /getapi
COPY restapi_crud_operations.py /db_curd
#COPY db_operations.py /db_curd

# Install Flask and any other dependencies
RUN pip install Flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
