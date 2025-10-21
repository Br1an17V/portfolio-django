web: gunicorn portfolio.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput
