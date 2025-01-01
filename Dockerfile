
# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Command to run the application
CMD ["python", "src/backend/main.py"]
