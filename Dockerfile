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

# Set Python path to include portfolio directory
ENV PYTHONPATH=/app/portfolio:$PYTHONPATH

# Create staticfiles directory
RUN mkdir -p portfolio/staticfiles

# Collect static files
RUN cd portfolio && python ../manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "/app/portfolio"]
