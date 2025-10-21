FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

# Run Django commands and start server
CMD python portfolio/manage.py migrate && \
    python portfolio/manage.py collectstatic --noinput && \
    gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
