# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to /app
COPY . .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port for Flask app
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
