FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

# Run migrations and collect static, then start gunicorn
CMD sh -c "cd portfolio && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000"
