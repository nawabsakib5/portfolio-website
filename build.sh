#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Superuser auto-create — credentials environment থেকে নেবে
python manage.py shell << 'EOF'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created!')
else:
    print('Superuser already exists.')
EOF