# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /sample-rest

# Copy the current directory contents into the container at /app
ADD . /sample-rest

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 3601 available to the world outside this container
EXPOSE 3601

# Run service when the container launches
ENTRYPOINT /sample-rest/entry.bash service
