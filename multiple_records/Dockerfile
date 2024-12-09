#use the official python image as base image
FROM python:3.8-slim

#set the working directory in the container
WORKDIR /multiple_records

#copy the python file to the working directory
COPY multiple_records.py /multiple_records

#run the python script when the container launches
ENTRYPOINT ["python", "multiple_records.py"]
