
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directories for templates and static files
RUN mkdir -p templates static

# Expose port
EXPOSE 8000

# Set Datadog environment variables (optional)
ENV DD_SERVICE=apm-demo-python
ENV DD_ENV=production
ENV DD_VERSION=1.0.0

# Run the application
CMD ["python", "run.py"]
