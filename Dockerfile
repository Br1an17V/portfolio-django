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

# Collect static files
RUN python manage.py collectstatic --noinput --settings=portfolio.portfolio.settings

EXPOSE 8000

# Run migrations and start gunicorn
CMD sh -c "python manage.py migrate --settings=portfolio.portfolio.settings && gunicorn wsgi:application --bind 0.0.0.0:8000"
