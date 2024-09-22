# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the port the Django app will run on
EXPOSE 8000

# Set the default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
