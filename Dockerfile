# Use an official Python runtime as a parent image
FROM python:3.5-slim

# Set the working directory to /app
WORKDIR /sample-rest

# Copy the current directory contents into the container at /app
ADD . /sample-rest

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 3601 available to the world outside this container
EXPOSE 3601

# Run service when the container launches
ENTRYPOINT /sample-rest/entry.bash service
