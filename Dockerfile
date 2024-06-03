# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY . /application

# Install any dependencies needed for your Python service
RUN pip install -r requirements.txt

RUN chmod +x start.sh

# Command to run all services
ENTRYPOINT [ "./start.sh" ]