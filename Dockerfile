# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip==23.0.1
RUN pip3 install -r requirements.txt

# Copy the entire project
COPY . /app/

# Copy the environment variables file
COPY ./.env /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
