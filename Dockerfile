
# Use the official Python image
FROM python:3.14.0a1-slim

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

# Install gRPC tools
RUN pip install grpcio grpcio-tools

# Add Kafka and RabbitMQ clients
RUN apt-get update && apt-get install -y librdkafka-dev
RUN pip install kafka-python

# Add Redis support
RUN pip install redis

# Add IPFS client
RUN pip install ipfshttpclient

# Add NVIDIA Triton Inference Server client
RUN pip install tritonclient[all]
