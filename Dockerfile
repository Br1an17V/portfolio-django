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

# Run migrations, load data, copy media files to both locations, collect static, then start gunicorn
CMD sh -c "cd portfolio && \
    python manage.py migrate && \
    python manage.py load_initial_data --force && \
    mkdir -p media/profile/2025/10 && \
    cp static/perfil.jpg media/profile/2025/10/perfil.jpg 2>/dev/null || true && \
    python manage.py collectstatic --noinput && \
    mkdir -p staticfiles/profile/2025/10 && \
    cp static/perfil.jpg staticfiles/profile/2025/10/perfil.jpg 2>/dev/null || true && \
    gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000"
