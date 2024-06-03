# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies needed for your Python service
RUN pip install -r requirements.txt

# Command to run all services
CMD ["export PYTHONPATH=.", "python3 app/main.py"]