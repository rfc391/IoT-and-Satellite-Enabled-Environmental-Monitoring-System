
# Minimal Hardened Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY cli.py .
COPY setup.py .

ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s   CMD curl --fail http://localhost:8080 || exit 1

ENTRYPOINT ["python", "cli.py", "--start"]
