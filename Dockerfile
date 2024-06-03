# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY . /application

ENV PYTHONPATH "${PYTHONPATH}:."

# Install any dependencies needed for your Python service
RUN pip install -r requirements.txt

# Command to run all services
CMD ["python3 app/main.py"]